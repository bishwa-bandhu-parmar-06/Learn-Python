# 6. Write a python function which converts inches to cms. 


def inches_to_cms(inches):
    cms = inches * 2.54
    return cms

inches = float(input("Enter the value in inches: "))
cms = inches_to_cms(inches)
print(f"{inches} inches is equal to {cms} centimeters.")