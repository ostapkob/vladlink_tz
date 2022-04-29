import json
from rich import print
from print_levels import *
from create_db import *
from db_to_dict import *
from write_to_file import *

with open('categories.json', 'r') as f:
    data = json.load(f)

# print(data)

db = create_db(data)
print(db)
# print('='*40)

print_dict_by_levels(data)
print('~ '*40)

menu = db_to_dict(db, 4)
# print(menu)
print_dict_by_levels(menu)

write_to_file(menu)

test1 = json.dumps(menu, indent=4)
test2 = json.dumps(data, indent=4)