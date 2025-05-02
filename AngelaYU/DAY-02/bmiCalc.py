height = input("Enter Your Height in M : ")
# print(type(height))
weight = input("Enter Your Weight in KG : ")
# print(type(weight))

# converting string  value into float
person_height = float(height)

# converting string value into int
person_weight = int(weight)

# body_Mass_index = person_weight / (person_height * person_height)

# OR

body_Mass_index = person_weight / person_height ** 2 

# converting float value into int 
integer_Value = int(body_Mass_index)

print(integer_Value)