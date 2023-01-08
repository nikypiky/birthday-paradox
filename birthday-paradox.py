import math
def request_nmbr():
    nmbr_of_birthdays = input('How many birthdays shal I generate? ')
    try:
        nmbr_of_birthdays = int(nmbr_of_birthdays)
    except:
        print('Plese choose a number')
        request_nmbr()
        print()
    print(nmbr_of_birthdays)
    
request_nmbr()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]