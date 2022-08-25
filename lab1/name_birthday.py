from datetime import date

# Creates a dictionary containing the months in text and numerical
months = {1: 'JANUARY', 2: 'FEBRUARY', 3: 'MARCH', 4: 'APRIL', 5: 'MAY', 6: 'JUNE', 7: 'JULY', 8: 'AUGUST', 9: 'SEPTEMBER', 10: 'OCTOBER', 11: 'NOVEMBER', 12: 'DECEMBER' }

# defines the main function where all the action is called upon/established.
def main():
    date_today = date.today()
    user_name = get_name()
    birthday_month = get_birthday_month()
    print('Hello, '+ user_name)
    birthday_month_check(birthday_month, date_today)
    print(len(user_name))

# get_name function will request the user to enter a name and check to ensure at least one character was entered.
def get_name ():
    name = input('Please enter your name: ')
    while not name:
        print('Please enter at least one character')
        name = input('Please enter your name: ')
    return name
    
# get_brithday_month asks the user to enter a birthday month, and checks the character. potential todo - add a check to make sure its a valid month.   
def get_birthday_month ():
    birthday_month = input('Please enter your birthday month: ')
    while not birthday_month:
        print('Please enter at least one character')
        birthday_month = input('Please enter your birthday month: ')
    return birthday_month

# takes the month, and date then checks to see if the month entered and the current month match, if so it will display a message saying happy birthday month.    
def birthday_month_check(month, date):
    date_month = date.month
    date_conversion = months[date_month]
    if month.upper() == date_conversion:
        print('Happy Birthday month!')

main()



