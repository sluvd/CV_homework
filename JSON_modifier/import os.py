import os
import re
import json
os.listdir('D:\l')
files = [f for f in os.listdir('.') if re.match(r'[0-9]+.*\.json', f)]
files.sort()
len(files)
print(files)
c = 89;
my_counter = 0
for i in files:
    my_counter += 1;
    c += 1
    a = f"{c}"
    with open(i, 'r') as file:
        print(i)
        json_data = json.load(file)
        json_data['imagePath'] = f"1 ({a}).jpg"
        output_filename = f'{i}'# + '_output.json'
    with open(output_filename, 'w') as file:
        json.dump(json_data, file, indent=2)
print(my_counter)