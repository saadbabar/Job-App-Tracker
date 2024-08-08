from db_manager import DBManager
from job_app import Job_Applications
from dotenv import load_dotenv
import os
def main():
    db_manager = DBManager(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    app = Job_Applications(db_manager)

    while True:
        print("\nMenu:")
        print("1. Add a new job application")
        print("2. View and export all applications to Excel")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            app.add_application()
        elif choice == '2':
            app.export_to_excel()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    db_manager.close()

if __name__ == "__main__":
    main()
