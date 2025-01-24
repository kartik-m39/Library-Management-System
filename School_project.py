from datetime import datetime

import numpy as np
import pandas as pd

# Creating a dataframe from respective csv files
Library = pd.read_csv('Library.csv', sep=';')
# Books_issued = pd.read_csv('Issued_books.csv', sep=';')
# Books_issued.drop_duplicates(inplace=True)
# Books_issued.reset_index()



def user():
    user_task = int(input('Enter \n1.To issue a book \n2.To return a book : \n'))
    if user_task == 1:
        #Asking user for the data
        name = input('Enter your Name : ')
        class_ = int(input("Enter your Class : "))
        section = input("Enter your Section : ")
        Roll_no = int(input("Enter your Roll Number : "))
        subject = input('Enter the subject of book you want : ')
        book = input('Enter the book you want : ')
        Books_issued.loc[0, :] = [name, class_, section, Roll_no, subject, book]
        #Books_issued = pd.DataFrame([[name, class_, section, Roll_no, subject, book]],
         #                           columns=['Name', 'Class', 'Section', 'Roll_number', 'Subject', 'Book'])
        Books_issued.to_csv('Issued_books.csv', index=False, header=False, sep=';', mode='a+')
        print('Book successfully issued!')
        #to delete book from library
    elif user_task == 2:
        roll_no = int(input('Enter your Roll Number : '))
        name = input('Enter your name : ')
        # Deleting user's data from database
        Books_issued.drop(index=roll_no)
        print('Book successfully returned by {}'.format(name))
        print(Books_issued)
    else:
        print("Error!")
        user()
    #Books_issued.to_csv('Issued_books.csv', index=False, header=False, sep=';', mode='w')
    num = input('\nTo continue enter 1 and to exit enter exit :\n')
    if num == '1':
        main_func()
    elif str(num) == 'exit':
        print('Exiting the system...')
    else:
        print('Error!')
        main_func()
def lib():
    librarian_task = int(input('Enter \n1.To add a book to the library : \n'
                               '2.To remove a book from the library : \n'))
    if librarian_task == 1:
        pass
    elif librarian_task == 2:
        ind = int(input('Enter book\'s index : '))
        sub = input('Enter book\'s subject : ')
        Library.at[ind, sub] = np.NaN
    num = input('\nTo continue enter 1 and to exit enter exit :\n')
    if num == '1':
        main_func()
    elif num == 'exit':
        print('Exiting the system...')
    else:
        print('Error!')
        main_func()
def main_func():
    task = int(input("Enter \n1.To view books in library \n2.To make changes in library : \n"))
    if task == 1:
        print(Library)
        num = input('\nTo continue press "c" and to exit system type "exit"\nEnter : ')
        if num == 'c':
            main_func()
        elif num == 'exit':
            print('Exiting the system...')
        else:
            print('Error!')
            main_func()
    elif task == 2:
        guest = int(input('Enter 1.User 2.Librarian : \n'))
        if guest == 1:
            user()
        elif guest == 2:
            password = input('Enter password : ')
            if password == '1234':
                lib()
            else:
                print('Error!')
                main_func()
        else:
            print('Error!')
            main_func()
    else:
        print('Error!')
        main_func()
# main_func()
# print(Books_issued)
#Library.to_csv('Library.csv', index=False, sep=';', mode='a')
#Books_issued.to_csv('Issued_books.csv', index=False, header=False,sep=';', mode='a')
a = Library['Fiction']
print(a)
b = input()
for i in a:
    if i == b:
        a.replace(i, np.NaN, inplace=True)
        print('Yes')
        break
    else:
        continue
print(a)
a.dropna(inplace=True)
print(a)

