#loops over names and appends lowercase and spaceless caracters to new usernames list
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

#this loop modifies the original variable usernames
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')

print(usernames)

#looping over the tokens list to determine and count how many of them are XML tags
tokens = ['<greeting>', 'Hello World!', '</greeting>', '</shit>']
count = 0

for token in tokens: 
    if token[0] == '<' and token[-1] == '>':
        count += 1
    
print(count)

#loop for turning a list of strings into html elements
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

for item in items: 
    html_str += "<ul>{}</ul>\n".format(item)
html_str += "<ul>\n"

print(html_str)