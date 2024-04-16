import json

ages = []

# oldest_contact = None 

with open("my_info.json", "r") as file:
    data = json.load(file)

all_contacts = data["contacts"]

for contact in all_contacts:
    ages.append(contact["age"])

ages = [contact["age"] for contact in all_contacts]



analytics = {
    "max_age": max(ages),
    "min_age": min(ages),
    "avg_age": sum(ages) / len(ages) 
}

print(f"The analytics are {analytics}")
