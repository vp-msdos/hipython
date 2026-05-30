file_handler = open("practice.txt","rt")
print(file_handler.read())
file_handler.close()
"""
file_handler1 = open("test.txt","xt")
file_handler1.write("This is test file")
file_handler1.close()
"""

file_handler2 = open("practice.txt","wt")
file_handler2.write("This is waste file")
file_handler2.close()

file_handler3 = open("practice.txt","rt")
list1 = file_handler3.readlines()
for line in list1:
    print(line)

