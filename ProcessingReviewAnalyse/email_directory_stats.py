import os
from collections import Counter
from email.parser import Parser

# Directory of Kevin Lays family folder
rootdir = "C:\\Users\\maxfr\\Desktop\\2020-Enron-Journal\\maildir\\lay-k\\family"

def email_analyse(inputfile, to_email_list, from_email_list):
    # Read in the file and parse the data to data variable
    with open(inputfile, "r") as f:
        data = f.read()

    # Parses in email data
    email = Parser().parsestr(data)

    # If the to email list is multiple emails then this splits it up and saves in an object
    if email["to"]:
        email_to = email["to"]
        email_to = email_to.replace("\n", "")
        email_to = email_to.replace("\t", "")
        email_to = email_to.replace(" ", "")
        
        email_to = email_to.split(",")	

    # Saves the from and to emails in a list
    for email_to_1 in email_to:
        to_email_list.append(email_to_1)
    from_email_list.append(email["from"])


# Post Function Work
to_email_list = []
from_email_list = []

# OS Walk through folder and for each filename, build to the list
for directory, subdirectory, filenames in os.walk(rootdir):
    for filename in filenames:
        email_analyse(os.path.join(directory, filename), to_email_list, from_email_list)

# Print out the email lists
print(to_email_list)
print("\n")
print(from_email_list)

# Print out the most common to and from emails
print("\nTo email addresses: \n")
print(Counter(to_email_list).most_common(10))
print("\nFrom email addresses: \n")
print(Counter(from_email_list).most_common(10))