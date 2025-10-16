# marks = {
#     "Alice" : 100,
#     "Harry" : 57,
#     "Bob" : 9,
#     "mac" : 24,
#     "list" : [1,2,3],
#     0: "Jemi"
# }

# # print(marks.items())
# # print(marks.keys())
# # print(marks.values())

# # marks.update({"Harry": 100, "renuka": 45})
# # print(marks)

# print(marks.get("Harry4"))  #retrun none
# print(marks["Harry4"]) #return error

# Create dictionary
person = {'name': 'Alice', 'age': 25}

# Get value
print(person.get('name'))             # Alice
print(person.get('gender', 'N/A'))    # N/A

# Add or update
person['city'] = 'Delhi'

# pop
print(person.pop('age'))              # 25

# popitem
print(person.popitem())               # ('city', 'Delhi')

# setdefault
person.setdefault('gender', 'Female')  # Adds gender: Female if not present

# keys, values, items
print(person.keys())   # dict_keys(['name', 'gender'])
print(person.values()) # dict_values(['Alice', 'Female'])
print(person.items())  # dict_items([('name', 'Alice'), ('gender', 'Female')])

# update
person.update({'age': 30, 'city': 'Mumbai'})
print(person)  # {'name': 'Alice', 'gender': 'Female', 'age': 30, 'city': 'Mumbai'}

# copy
copy_dict = person.copy()

# clear
person.clear()
print(person)  # {}
