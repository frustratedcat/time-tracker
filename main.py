import sqlite3

con = sqlite3.connect('time_tracker.db')
cur = con.cursor()

# Create tables and assign appropriate column types
def create_table():
    # Get user inputs
    table_name = input('Enter the table name\n> ')
    table_columns = input('Enter the table columns and types with a single "," between each:\n> ')

    # Create sqlite table
    create_table = f'CREATE TABLE {table_name}({table_columns}) strict'
    cur.execute(create_table)

def main():
    create_table()

if __name__ == '__main__':
    main()
