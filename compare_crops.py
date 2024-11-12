import json

# python compare_crops.py

with open("new_crops.json", "r") as file:
    new_crops = json.load(file)

with open("old_crops.json", "r") as file:
    old_crops = json.load(file)

# Map crops by name to their IDs for both stages
new_name_to_id = {crop["name"]: crop["id"] for crop in new_crops}
old_name_to_id = {crop["name"]: crop["id"] for crop in old_crops}

# Identify name matches with different IDs
name_discrepancies = {
    name: (new_name_to_id[name], old_name_to_id[name])
    for name in new_name_to_id.keys() & old_name_to_id.keys()
    if new_name_to_id[name] != old_name_to_id[name]
}

# Identify names that are unique to each stage
names_only_in_new_crops = set(new_name_to_id.keys()) - set(old_name_to_id.keys())
names_only_in_old_crops = set(old_name_to_id.keys()) - set(new_name_to_id.keys())

# Output results
print("Name discrepancies with different IDs:", name_discrepancies)
print("Names only in new crops:", names_only_in_new_crops)
print("Names only in old crops:", names_only_in_old_crops)
