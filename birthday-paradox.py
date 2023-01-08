import math
import random

def request_number():
    while True:
        input_str = input("How many birthdays shal I generate? ")
        if input_str.isnumeric() and int(input_str)<=100 and int(input_str)>0:
            return int(input_str)        
        else:
            print("Invalid input. Please choose a number between 1-100.")

# Use the function to request a number from the user
number = request_number()

# Print the number outside of the function
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#dates = {'January' : 31, 'February' : 28, 'March' : 31, 'April' : 30, 'May' : 31, 'June' : 30, 'July' : 31, 'August' : 31, 'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}
#for n in number:
index_dates = random.randint(0, 11)
print(index_dates)
print(months[index_dates])
print(days[index_dates])



