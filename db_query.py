#!/usr/bin/python

import glob
import os
import sqlite3

print('Files with .sqlite3 extension in current dir:')
print(*glob.glob('*.sqlite3'), sep='\n')
file_names_db = [os.path.splitext(val)[0] for val in glob.glob('*.sqlite3')]
chosen_db = input(f'Choose from: {file_names_db} -> type one: ')

if chosen_db in file_names_db:
    chosen_db = chosen_db+'.sqlite3'
else:
    print('Choose valid option, please')
    exit()

con = sqlite3.connect(chosen_db)
cur = con.cursor()
cur.execute('''
SELECT name
FROM sqlite_schema
WHERE type='table';
''')

print(f'Available tables in {chosen_db} are: ')
for result in cur:
    print('-', *result)


chosen_table = input('Select table to show: ')
print(f'In table "{chosen_table}" rows are:')

cur.execute(f'''
SELECT *
FROM {chosen_table};
''')
for result in cur:
    print(*result)

con.close()
