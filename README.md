# Job-App-Tracker
tracks number of applications I've sent out and when their OAs are due and whether there are next steps

# How the program works
The program works in the command line (may add a GUI in the future), it starts by asking if you want to view all entries in the database first then select 2, else if you want to add select 1 and you will be given the option after every entry for another entry

# Running on your local desktop
1. Download Postgres
2. in Postgres Create Database (\c {name of choice})
3. Create the relevant tables such as the companies table and the positions table
4. the commands for the entries within the table are in the sql_cmds.sql file
5. enter relevant information in the main file under db_manager file
6. install dependancies (openpyxl, pandas, psycopg2)

# Contraints
You cannot add a position with the same name for a company more than once (sql_cmds.cmd CONSTRAINT command at the bottom)

# Project Takeaways
Python, Pandas, Postgres, SQL, backend
