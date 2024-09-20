#Q1. Write a program which will ask user to enter the marks in percentage and raise the custom exception "InvalidMarksException" if user enters the percentage greater than 100% or less than 0%



class InvalidMarksException(BaseException):
    def __init__(self, message):
        self.message = message

try:
    
    percentage = float(input("Enter your marks in percentage: "))

    if percentage < 0 or percentage > 100:
        raise InvalidMarksException(f"InvalidMarksException:Mark must be from 0 and 100.")
    
except InvalidMarksException as e:
    print(e)

else:
    print(f"You got {percentage} marks!")




























    







    
