import sqlite3 as sql

# connects to database and creates one if it does not exist
def get_connection():
    return sql.connect('license.db')


# to create table for easy writing and retrieval of database content
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS licenses
                 (license text primary key)''', )
    conn.commit()
    conn.close()


def insert_license(license):
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    license = license.upper()
    try:
        cur.execute("INSERT INTO licenses VALUES (?)", (license,))
        print(f"stored {license} in the database.")
    except sql.IntegrityError:
        print(f"{license} found in database")
    conn.commit()
    conn.close()


def read_license():
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM licenses")
    license = cur.fetchall()
    conn.close()
    return license






def delete_license(license):
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    license = license.upper()
    cur.execute("DELETE FROM licenses WHERE license = ?", (license,))
    conn.commit()
    conn.close()





def validate_license(license):
    if len(license) != 8 and len(license) != 7:
        raise ValueError('License must be either 7 or 8 characters long')
    if not license[0:2].isalpha():
        raise ValueError('License must start with two letter')
    if not license[-2:].isalpha():
        raise ValueError('License must end with two letter')
    if not license[3:-3].isdigit():
        raise ValueError('License must have numbers in between')


def main():
    get_connection()
    while True:
        try:
            license_value = input("Input License numbers to store in database or 'q' to quit").upper()
            if license_value == 'SHOW':
                stored_license = read_license()
                for row in stored_license:
                    print(f"ID:{row[0]}, license: {row[-1]}")

            elif license_value == 'DELETE':
                delete = input("Input license ID to delete").upper()
                delete_license(delete)
                print(f"license {delete} is removed or not found")
            else:
                validate_license(license_value)
                insert_license(license_value)
        except ValueError:
            print("Exiting.")
            break


if __name__ == '__main__':
    main()

