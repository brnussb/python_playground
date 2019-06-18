"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

firsttext = texts[0]
incoming_number, answering_number, time = firsttext[0], firsttext[1], firsttext[2]

print ("First record of texts, {} texts {} at time {}.".format(incoming_number, answering_number, time))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

lastcall = calls[-1]
incoming_number, answering_number, time, during = lastcall[0], lastcall[1], lastcall[2], lastcall[3]

print("Last record of calls, {} calls {} at time {}, lasting {} seconds.".format(incoming_number, answering_number, time, during))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
