import math

def request_number():
    while True:
        input_str = input("How many birthdays shal I generate? ")
        if input_str.isnumeric() and int(input_str)<=100 and int(input_str)>0:
            return int(input_str)        
        else:
            print("Invalid input. Please choose a number between 1-100.")

# Use the function to request a number from the user
#number = request_number()

# Print the number outside of the function
print(request_number()())


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]