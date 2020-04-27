import os
from email.parser import Parser

# Open Email
file_to_open = "C:\\Users\\maxfr\\Desktop\\2020-Enron-Journal\\maildir\\lay-k\\all_documents\\1_"
with open(file_to_open, "r") as file:
    data = file.read()

email = Parser().parsestr(data)

print("\nTo: " , email["to"])
print("\nFrom: " , email["from"])

print("\n Subject: " , email["subject"])
print("\n\n Body: " , email.get_payload())