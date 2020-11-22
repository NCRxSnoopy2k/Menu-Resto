from json import load

file_path = "mytxt/menu.json"
mode = "r"

with open(file_path, mode) as file:
	tickets = load(file)

clean_names = []

for menu in menus:
	clean_names.append(menu.strip())
print(clean_names)
