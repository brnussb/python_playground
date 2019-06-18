"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

unqtexts = list(set(texts))
print(unqtexts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

## print (calls)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
