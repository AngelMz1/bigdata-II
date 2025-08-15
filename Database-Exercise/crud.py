'''
create a sccrcipt to crud actions
'''

#imports
import os
from database import con, cur


#functions
def create_user():
    os.system('clear')
    fname = input('enter your firtname: ')
    lname = input('enter your lastname: ')
    ide_numb = input('enter your id number: ')
    email = input('enter your email: ')
    new_data = f'''
        INSERT INTO users (firstname,lastname, ide_number, email)
        VALUES ('{fname}', '{lname}', '{ide_numb}', '{email}');'''

    con.execute(new_data)
    con.commit()
    print(':::User has been created successfuly :::')

def list_users():
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
    print(data)

def update_users():
    os.system('clear')
    updater = input('enter id number to modify: ')
    fname = input('enter your firtname: ')
    lname = input('enter your lastname: ')
    ide_numb = input('enter your id number: ')
    email = input('enter your email: ')
    update_user = f'''
        UPDATE users 
        SET ide_number = {}'''
