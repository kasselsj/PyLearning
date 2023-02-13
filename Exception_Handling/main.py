try:
    my_file = open("mydata2.txt",encoding="utf-8")
except FileNotFoundError as ex:
    print("That file was not found.")
    print(ex.args)
else:
    print("File: ", my_file.read())
    my_file.close()
finally:
    print("finished working with file")