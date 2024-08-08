import pandas as pd
from db_manager import DBManager

class Job_Applications:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager
        self.cur = db_manager.cur
    def add_application(self):
        while True:

            company_name = input("Enter company name: ")
            position_name = input("Enter the positon applied for: ")
            date_applied = input("Enter date applied (YYYY-MM-DD): ")
            assessment_due_date = input("Enter the assessment due date (YYYY-MM-DD, optional): ")

            assessment_due_date = assessment_due_date if assessment_due_date else None

            self.cur.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
            company = self.cur.fetchone()

            if company is None:
                #if company = DNE, add it to the companies table
                self.cur.execute("INSERT INTO companies (name) VALUES (%s) RETURNING id", (company_name,))
                company_id = self.cur.fetchone()
            else:
                company_id = company[0]

            #check if company alr exists
            self.cur.execute(
                "SELECT id FROM positions WHERE company_id = %s AND position_name = %s",
                (company_id, position_name)
            )

            existing_position = self.cur.fetchone()

            if existing_position is not None:
                print(f"The positoon '{position_name}' at '{company_name}' already exists.")
                return
            
            #Insert position
            self.cur.execute(
                "INSERT INTO positions (company_id, position_name, application_date, assessment_due_date) VALUES (%s, %s, %s, %s)",
                (company_id, position_name, date_applied, assessment_due_date)
            )

            self.conn.commit()
            print(f"Application for '{position_name}' at '{company_name}' added successfully.")

            more = input("Do you want to add more applications? (yes/no): ")
            if more.lower() != "yes":
                break

    def get_applications(self):
        self.cur.execute("""
            SELECT companies.name, positions.position_name, positions.application_date, positions.assessment_due_date
            FROM positions
            JOIN companies ON positions.company_id = companies.id
        """)
        rows = self.cur.fetchall()
        df = pd.DataFrame(rows, columns=["Company", "Position", "Application Date", "Assessment Due Date"])
        return df
    
    def export_to_excel(self, filename='job_applications.xlsx'):
        df = self.get_applications()
        df.to_excel(filename, index=False)
        print(f"Data exported to {filename}")