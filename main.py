from utils import student
from utils import teacher



def menu():
    print('***Welcome to our learning system! (e_learning)*** ')

    user_input = input("""
        - Create Account. Enter 'C' to Create account
        - Already have account? then press 'L' to login.
        - Press 'E' to Exit
    """)
    while user_input != 'e':

        if user_input.lower() == 'c':
            account_create()
        elif user_input.lower() == 'l':
            login_data()
        else:
            print('Unknown Command! please try again..')

        user_input = input("""
                - Create Account. Enter 'C' to Create account
                - Already have account? then press 'L' to login.
                - Press 'E' to Exit
            """)


def account_create():
    print('Welcome to our system. Please fill up the information below for opening a account. ')
    choice = input('''
                     ***select the specific one***
                    -press 1 for student
                
                    -press 2 for teacher
                ''')

    while choice != 'q':
        if choice == '1':
            student.account_create_data()
            break
        elif choice == '2':
            teacher.account_create_data()
            break
        else:
            print('Unknown command!. please try again')


def login_data():
    print('Welcome to our system. Please fill up the information below for opening a account. ')
    choice = input('''
                ***select the specific one***
                    -press 1 for student
                    -press 2 for student
                ''')

    while choice != 'q':
        if choice == '1':
            student.login_data()
            break
        elif choice == '2':
            teacher.login_data()
            break
        else:
            print('Unknown command!. please try again')


menu()
