import json

name_to_search = input("Enter a name and I will give you his info: ")
found_contact = None 

with open("my_info.json", "r") as file:
    data = json.load(file)

for contact in data["contacts"]:
    if contact["name"] == name_to_search:
        print(f'Your information is {contact}')
        found_contact = contact
        break

if not found_contact:
    age = int(input("Enter new contact age: "))
    data["contacts"].append({
        "name": name_to_search, 
        "age": age
    })


print("stop here")
with open("my_info.json", "w") as file:
    json.dump(data, file)
