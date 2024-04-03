from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")
a = input("filename?")
b= open(a)
print("Opening the file...")
target = open(filename,'w')

print("Truncating the file Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")


#下面这行代码是将所有的文字用一个输出
target.write(f">>>\n{line1} \n{line2} \n{line3}")
"""
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
print("And finally, we close it.")
target.close()

with open(a,'w') as txt:
    print("now i'm going to erase ")
    txt.truncate()

    print("Now I'm going to ask you for three lines.")
    line1 = input("line 1: ")
    line2 = input("line 2: ")
    txt.write(f">>>\n{line1} \n{line2} \n{line3}")