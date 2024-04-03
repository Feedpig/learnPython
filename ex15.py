from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's you file {filename}\n>>>")
print(f"{txt.read()}\n>>>")


txt.close()

# with open(filename,'r') as Txt:
#     print(Txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()

txt =  open(filename)
