print("Welcome To BMI Calculator.")

height = float(input("Enter your height in Meter : "))
weight = float(input("Enter Your Weight in Kg : "))

bmi = round(weight / (height ** 2))
# bmi = weight / (height ** 2)
# print(bmi)

if bmi < 18.5:
    print(f"Your Bmi is {bmi}, You are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your Bmi is {bmi}, You Have Normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your Bmi is {bmi}, You are overweight")
elif bmi > 30 and bmi < 35:
    print(f"Your Bmi is {bmi}, You are obese")
elif bmi > 35:
    print(f"Your Bmi is {bmi}, You are clinically obese")
else:
    print("Something Went Wrong")