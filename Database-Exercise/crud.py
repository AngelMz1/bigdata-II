'''
create a sccrcipt to crud actions
'''

#imports
import os
from database import con, cur
import sqlite3
from tabulate import tabulate


#functions
def create_user():
    os.system('clear')
    fname = input('enter your firstname: ')
    lname = input('enter your lastname: ')
    ide_numb = input('enter your id number: ')
    email = input('enter your email: ')
    new_data = f'''
        INSERT INTO users (firstname,lastname, ide_number, email)
        VALUES ('{fname}', '{lname}', '{ide_numb}', '{email}');'''

    try:
        con.execute(new_data)
        con.commit()
        print(':::User has been created successfuly :::')
    except sqlite3.Error as e:
        print(f'::: An error has ocurred ::: {e}') 
        con.rollback()
    input('press enter to continue...')

def list_users():
    os.system('clear')
    user_data_query = '''
        SELECT
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'active' else 'inactive' end as status
            FROM 
            users'''
    cur.execute(user_data_query)
    data = cur.fetchall()
    headers = ['id', 'firstname', 'lastname', 'ide_number', 'email', 'status']
    print(tabulate(data, headers=headers, tablefmt='grid'))
    input('press enter to continue...')

def list_active_users():
    os.system('clear')
    user_data_query = '''
        SELECT
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'active' else 'inactive' end as status
            FROM 
            users
            WHERE status = 1'''

    cur.execute(user_data_query)
    data = cur.fetchall()
    headers = ['id', 'firstname', 'lastname', 'ide_number', 'email', 'status']
    print(tabulate(data, headers=headers, tablefmt='grid'))
    input('press enter to continue...')

def list_inactive_users():
    os.system('clear')
    user_data_query = '''
        SELECT
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'active' else 'inactive' end as status
            FROM 
            users
            WHERE status = 0'''

    cur.execute(user_data_query)
    data = cur.fetchall()
    headers = ['id', 'firstname', 'lastname', 'ide_number', 'email', 'status']
    print(tabulate(data, headers=headers, tablefmt='grid'))
    input('press enter to continue...')

def update_users():
    os.system('clear')
    updater = input('enter id number to modify: ')
    miniQuery = f'''
        SELECT
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'active' else 'inactive' end as status
            FROM
            users
            WHERE ide_number = {updater}'''
    cur.execute(miniQuery)
    data = cur.fetchall()
    headers = ['id', 'firstname', 'lastname', 'ide_number', 'email', 'status']
    print(tabulate(data, headers=headers, tablefmt='grid'))
    fname = input('enter firtname: ')
    lname = input('enter lastname: ')
    ide_numb = input('enter id number: ')
    email = input('enter email: ')
    status = input('1: active, 0: inactive \nenter status: ')
    update_user = f'''
        UPDATE users 
        SET ide_number = {ide_numb},
            firstname = '{fname}',
            lastname = '{lname}',
            email = '{email}',
            status = {status}
        WHERE ide_number = {updater}
        '''
    cur.execute(update_user)
    con.commit()
    print('::: user has been updated successfully :::')
    input('press enter to continue...')

def delete_user():
    os.system('clear')
    deleter = input('enter id number to delete: ')
    delete_user = f'''
        DELETE FROM users
        WHERE ide_number = {deleter}
        '''
    cur.execute(delete_user)
    con.commit()
    print('::: user has been deleted successfully :::')
    input('press enter to continue...')

def search_user():
    os.system('clear')
    searcher = input('enter id number to search: ')
    search_user = f'''
        SELECT
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'active' else 'inactive' end as status
            FROM
            users
            WHERE ide_number = {searcher}'''
    cur.execute(search_user)
    data = cur.fetchall()
    headers = ['id', 'firstname', 'lastname', 'ide_number', 'email', 'status']
    print(tabulate(data, headers=headers, tablefmt='grid'))
    input('press enter to continue...')

#main screen
main_screen = '''
::: Users DB :::
    Main Menu
    [1]. create new user
    [2]. list all users
    [3]. list active users
    [4]. list inactive users
    [5]. update user  ---> all data with ide_number
    [6]. Delete user  ---> with ide_number
    [7]. search user  ---> with ide_number
    [8]. exit
    '''
def valid_option():
    while True:
        os.system('clear')
        print(main_screen)

        try:
            option = int(input('enter an option: '))
        except ValueError:
            print('::: enter a valid number :::')
            input('press enter to continue...')
            continue

        if option == 8:
            print('::: see you soon :::')
            break
        elif option >= 1 or option <=7:
            if option == 1:
                create_user()
            elif option == 2:
                list_users()    
            elif option == 3:
                list_active_users()
            elif option == 4:
                list_inactive_users()
            elif option == 5:
                update_users()
            elif option == 6:
                delete_user()
            elif option == 7:
                search_user()
        else:
            print('::: enter a valid option :::')
            input('press enter to continue...')
            continue

valid_option()