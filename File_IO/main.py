import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random Text.\nHere's some more text.\nMore text.")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)