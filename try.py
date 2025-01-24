import pandas as pd
import datetime
import numpy as np
def main():
    do = input("\n1.To view books in library \n2.To make changes in library\nEnter : ")
    if int(do) == 1:
        print(Library)
    elif int(do) == 2:
        guest = input("\n1.User 2.Librarian\nEnter : ")
        if int(guest) == 1:
            task = input('\n1.Issue book 2.Return book\nEnter : ')
            if int(task) == 1:
                issue_book()
            elif int(task) == 2:
                return_book()
            else:
                print('Error!')
                main()
            Lib = pd.DataFrame({"Physics": Physics,
                                "Chemistry": Chemistry,
                                "Mathematics": Mathematics,
                                "Literature": Literature,
                                "Biography": Biography,
                                "Fiction": Fiction})
            Lib.to_csv('Library.csv', index=False, sep=';', mode='w')
        elif int(guest) == 2:
            password = input('\nEnter password : ')
            if password == '1234':
                task = input('\n1.Add book to library 2.Remove book from library\nEnter : ')
                if int(task) == 1:
                    add_book()
                elif int(task) == 2:
                    remove_book()
                else:
                    print('Error!')
                    main()
            else:
                print('Wrong password')
                main()
        else:
            print('Error!')
            main()
    else:
        print('Error!')
        main()
def issue_book():
    name = input('\nEnter your name : ')
    class_ = int(input('Enter your class : '))
    section = input('Enter your section : ')
    adm_no = int(input('Enter your admission number : '))
    sub = input('\nEnter the subject of the book to be issued : ')
    book = input('Enter the book to be issued : ')
    if sub == 'Physics':
        for item in Physics:
            if item == book:
                Physics.replace(item, 'None', inplace=True)
                ibooks = pd.DataFrame([[name, class_, section, adm_no, book, datetime.datetime.now()]],
                                      columns=['Name', 'Class', 'Section', 'Admission_number', 'Book', 'Date_time'])
                new = pd.concat([ibooks_main, ibooks], ignore_index=True)
                new.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully issued.')
                break
            elif book != item:
                continue
            else:
                print('Book is already issued.')
    elif sub == 'Chemistry':
        for item in Chemistry:
            if item == book:
                Chemistry.replace(item, 'None', inplace=True)
                ibooks = pd.DataFrame([[name, class_, section, adm_no, book, datetime.datetime.now()]],
                                      columns=['Name', 'Class', 'Section', 'Admission_number', 'Book', 'Date_time'])
                new = pd.concat([ibooks_main, ibooks], ignore_index=True)
                new.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully issued.')
                break
            elif book != item:
                continue
            else:
                print('Book is already issued.')
    elif sub == 'Mathematics':
        for item in Mathematics:
            if item == book:
                Mathematics.replace(item, 'None', inplace=True)
                ibooks = pd.DataFrame([[name, class_, section, adm_no, book, datetime.datetime.now()]],
                                      columns=['Name', 'Class', 'Section', 'Admission_number', 'Book', 'Date_time'])
                new = pd.concat([ibooks_main, ibooks], ignore_index=True)
                new.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully issued.')
                break
            elif book != item:
                continue
            else:
                print('Book is already issued.')
    elif sub == 'Literature':
        for item in Literature:
            if item == book:
                Literature.replace(item, 'None', inplace=True)
                ibooks = pd.DataFrame([[name, class_, section, adm_no, book, datetime.datetime.now()]],
                                      columns=['Name', 'Class', 'Section', 'Admission_number', 'Book', 'Date_time'])
                new = pd.concat([ibooks_main, ibooks], ignore_index=True)
                new.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully issued.')
                break
            elif book != item:
                continue
            else:
                print('Book is already issued.')
    elif sub == 'Biography':
        for item in Biography:
            if item == book:
                Biography.replace(item, 'None', inplace=True)
                ibooks = pd.DataFrame([[name, class_, section, adm_no, book, datetime.datetime.now()]],
                                      columns=['Name', 'Class', 'Section', 'Admission_number', 'Book', 'Date_time'])
                new = pd.concat([ibooks_main, ibooks], ignore_index=True)
                new.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully issued.')
                break
            elif book != item:
                continue
            else:
                print('Book is already issued.')
    elif sub == 'Fiction':
        for item in Fiction:
            if item == book:
                Fiction.replace(item, 'None', inplace=True)
                ibooks = pd.DataFrame([[name, class_, section, adm_no, book, datetime.datetime.now()]],
                                      columns=['Name', 'Class', 'Section', 'Admission_number', 'Book', 'Date_time'])
                new = pd.concat([ibooks_main, ibooks], ignore_index=True)
                new.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully issued.')
                break
            elif book != item:
                continue
            else:
                print('Book is already issued.')
    else:
        print('Error')
        main()
def return_book():
    adm_no = int(input('\nEnter your admission number : '))
    sub = input('Enter the subject of the book to be returned : ')
    book = input('Enter the book to be returned : ')
    if sub == 'Physics':
        for item in Physics:
            if item == 'None':
                Physics.replace('None', book, inplace=True)
                ibooks = pd.read_csv('Issued_books.csv', sep=';')
                ibooks.drop(ibooks[ibooks.Admission_number == adm_no].index, inplace=True)
                ibooks.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully returned.')
                break
            elif item != 'None':
                continue
            else:
                print('Book already present in the library.')
    elif sub == 'Chemistry':
        for item in Chemistry:
            if item == 'None':
                Chemistry.replace('None', book, inplace=True)
                ibooks = pd.read_csv('Issued_books.csv', sep=';')
                ibooks.drop(ibooks[ibooks.Admission_number == adm_no].index, inplace=True)
                ibooks.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully returned.')
                break
            elif item != 'None':
                continue
            else:
                print('Book already present in the library.')
    elif sub == 'Mathematics':
        for item in Mathematics:
            if item == 'None':
                Mathematics.replace('None', book, inplace=True)
                ibooks = pd.read_csv('Issued_books.csv', sep=';')
                ibooks.drop(ibooks[ibooks.Admission_number == adm_no].index, inplace=True)
                ibooks.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully returned.')
                break
            elif item != 'None':
                continue
            else:
                print('Book already present in the library.')
    elif sub == 'Literature':
        for item in Literature:
            if item == 'None':
                Literature.replace('None', book, inplace=True)
                ibooks = pd.read_csv('Issued_books.csv', sep=';')
                ibooks.drop(ibooks[ibooks.Admission_number == adm_no].index, inplace=True)
                ibooks.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully returned.')
                break
            elif item != 'None':
                continue
            else:
                print('Book already present in the library.')
    elif sub == 'Biography':
        for item in Biography:
            if item == 'None':
                Biography.replace('None', book, inplace=True)
                ibooks = pd.read_csv('Issued_books.csv', sep=';')
                ibooks.drop(ibooks[ibooks.Admission_number == adm_no].index, inplace=True)
                ibooks.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully returned.')
                break
            elif item != 'None':
                continue
            else:
                print('Book already present in the library.')
    elif sub == 'Fiction':
        for item in Fiction:
            if item == 'None':
                Fiction.replace('None', book, inplace=True)
                ibooks = pd.read_csv('Issued_books.csv', sep=';')
                ibooks.drop(ibooks[ibooks.Admission_number == adm_no].index, inplace=True)
                ibooks.to_csv('Issued_books.csv', index=False, sep=';', mode='w')
                print('Book successfully returned.')
                break
            elif item != 'None':
                continue
            else:
                print('Book already present in the library.')
    else:
        print('Error')
        main()
def add_book():
    sub = input('\nEnter the subject of the book to be added : ')
    book = input('Enter the book to be added : ')
    if sub == 'Physics':
        df1 = pd.DataFrame([[book, 'None', 'None', 'None', 'None', 'None']],
                      columns=["Physics", 'Chemistry', 'Mathematics', 'Literature', 'Biography', 'Fiction'])
        dft = pd.concat([Library, df1], ignore_index=True)
        dft.to_csv('Library.csv', index=False, sep=';', mode='w')
        print('Book successfully added to library.')
    elif sub == 'Chemistry':
        df2 = pd.DataFrame([['None', book, 'None', 'None', 'None', 'None']],
                      columns=["Physics", 'Chemistry', 'Mathematics', 'Literature', 'Biography', 'Fiction'])
        dft = pd.concat([Library, df2], ignore_index=True)
        dft.to_csv('Library.csv', index=False, sep=';', mode='w')
        print('Book successfully added to library.')
    elif sub == 'Mathematics':
        df3 = pd.DataFrame([['None', 'None', book, 'None', 'None', 'None']],
                      columns=["Physics", 'Chemistry', 'Mathematics', 'Literature', 'Biography', 'Fiction'])
        dft = pd.concat([Library, df3], ignore_index=True)
        dft.to_csv('Library.csv', index=False, sep=';', mode='w')
        print('Book successfully added to library.')
    elif sub == 'Literature':
        df4 = pd.DataFrame([['None', 'None', 'None', book, 'None', 'None']],
                      columns=["Physics", 'Chemistry', 'Mathematics', 'Literature', 'Biography', 'Fiction'])
        dft = pd.concat([Library, df4], ignore_index=True)
        dft.to_csv('Library.csv', index=False, sep=';', mode='w')
        print('Book successfully added to library.')
    elif sub == 'Biography':
        df5 = pd.DataFrame([['None', 'None', 'None', 'None', book, 'None']],
                      columns=["Physics", 'Chemistry', 'Mathematics', 'Literature', 'Biography', 'Fiction'])
        dft = pd.concat([Library, df5], ignore_index=True)
        dft.to_csv('Library.csv', index=False, sep=';', mode='w')
        print('Book successfully added to library.')
    elif sub == 'Fiction':
        df6 = pd.DataFrame([['None', 'None', 'None', 'None', 'None', book]],
                      columns=["Physics", 'Chemistry', 'Mathematics', 'Literature', 'Biography', 'Fiction'])
        dft = pd.concat([Library, df6], ignore_index=True)
        dft.to_csv('Library.csv', index=False, sep=';', mode='w')
        print('Book successfully added to library.')
    else:
        print('Error!')
        main()
def remove_book():
    sub = input('\nEnter the subject of the book to be removed : ')
    book = input('Enter the book to be removed : ')
    if sub == 'Physics':
        for cols in Physics:
            if cols == book:
                Physics.replace(cols, 'None', inplace=True)
                print('Book removed from the library.')
            elif book != cols:
                continue
            else:
                print("No such book present in the library")
    elif sub == 'Chemistry':
        for cols in Chemistry:
            if cols == book:
                Chemistry.replace(cols, 'None', inplace=True)
                print('Book removed from the library.')
            elif book != cols:
                continue
            else:
                print("No such book present in the library")
    elif sub == 'Mathematics':
        for cols in Mathematics:
            if cols == book:
                Mathematics.replace(cols, 'None', inplace=True)
                print('Book removed from the library.')
            elif book != cols:
                continue
            else:
                print("No such book present in the library")
    elif sub == 'Literature':
        for cols in Literature:
            if cols == book:
                Literature.replace(cols, 'None', inplace=True)
                print('Book removed from the library.')
            elif book != cols:
                continue
            else:
                print("No such book present in the library")
    elif sub == 'Biography':
        for cols in Biography:
            if cols == book:
                Biography.replace(cols, 'None', inplace=True)
                print('Book removed from the library.')
            elif book != cols:
                continue
            else:
                print("No such book present in the library")
    elif sub == 'Fiction':
        for cols in Fiction:
            print(cols)
            if cols == book:
                Fiction.replace(cols, 'None', inplace=True)
                print('Book removed from the library.')
            elif book != cols:
                continue
            else:
                print("No such book present in the library")
    else:
        print('Error!')
        main()
    Lib = pd.DataFrame({"Physics": Physics,
                        "Chemistry": Chemistry,
                        "Mathematics": Mathematics,
                        "Literature": Literature,
                        "Biography": Biography,
                        "Fiction": Fiction})
    Lib.to_csv('Library.csv', index=False, sep=';', mode='w')
def repeat():
    num = input('\nTo continue press "c" and to exit system type "exit"\nEnter : ')
    if num == 'c':
        main()
    elif num == 'exit':
        print('Exiting the system...')
        exit()
    else:
        print('Error!')
        main()
    repeat()

while True:
    print('\n      "WELCOME TO LIBRARY MANAGEMENT SYSTEM"      \n')
    print('Instructions :-\n1.For every wrong input the system runs again.\n'
          '2.There are only single copies of books in the library.\n'
          '3.Only one book can be issued, returned, added and removed from the library at a time.\n'
          '4.Avoid entering wrong inputs as it may cause errors.')
    Library = pd.read_csv('Library.csv', sep=';', na_values='None')
    Library.dropna(how='all', inplace=True)
    ibooks_main = pd.DataFrame(columns=['Name', 'Class', 'Section', 'Admission_number', 'Book', 'Date_time'])
    Physics = pd.Series(Library['Physics'])
    Chemistry = pd.Series(Library['Chemistry'])
    Mathematics = pd.Series(Library['Mathematics'])
    Literature = pd.Series(Library['Literature'])
    Biography = pd.Series(Library['Biography'])
    Fiction = pd.Series(Library['Fiction'])
    main()
    repeat()
