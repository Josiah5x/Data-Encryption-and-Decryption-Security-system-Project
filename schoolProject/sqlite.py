import sqlite3


def createDB():
    conn = sqlite3.connect('encryption_decryption_storebase.db')
    print(' created successfully')
    conn.close()


# createDB()


def createTableDB():
    conn = sqlite3.connect('encryption_decryption_storebase.db')
    print(' database open successfully')

    conn.execute('''CREATE TABLE CMP_STAFF2
            KEYNAME           TEXT    NOT NULL,
            KEYVALUE            TEXT    NOT NULL,
            DATE_TIME            CHAR      NOT NULL);''')

    print('table created successfully')


# createTableDB()

def insert():
    conn = sqlite3.connect('staff_registration.db')
    print(' database open successfully')

    idNumber = input('put your id number here: ')
    name = input('Your Username: ')
    password = input('Your password: ')
    admin = input('do you want to choose he/she as admin. YES or NO : ')

    insert_data = "INSERT INTO CMP_STAFF2 (ID, NAME, PASSWORD, ADMIN) VALUES('"+idNumber+"', '" + name + "', '" + password + "', '" + admin + "') "
    conn.execute(insert_data)
    conn.commit()
    print('Record created successfully')
    conn.close()


# insert()


def getResult():

    conn = sqlite3.connect('staff_registration.db')
    print(' database open successfully')
    # confirmed = input('Search: ')
    cursor = conn.execute("SELECT id, name, password, admin FROM CMP_STAFF2")
    for row in cursor:
        # if confirmed == row[3]:

        print(f'Id = {row[0]}')
        namelist = row[1].split()
        for names in namelist:
            print(names)
            print('===========')
        print(f'Password = {row[2]}')
        print(f'Admin = {row[3]} ')
        print('====================')

        # elif confirmed == row[3]:

        #     print(f'Id = {row[0]}')
        #     print(f'Name = {row[1]}')
        #     print(f'Password = {row[2]}')
        #     print(f'Admin = {row[3]} ')

        # else:
        #     pass

    print('operation done successfully')
    conn.close()


getResult()

