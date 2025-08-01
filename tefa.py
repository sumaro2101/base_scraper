import re
name, password = re.search(r'(.{1,}:.{1,}@)', 'ds:ds@138.128.91.65:8100').group().strip('@').split(':')
print(name, password)
