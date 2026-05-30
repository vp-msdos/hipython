userInput = input("Enter a text: ")

with open("output.txt", "a") as myfile:
    myfile.write("\n"+userInput)

with open("output.txt", "rt") as myfile:
    content = myfile.read()
    print(content)