
with open('test1.txt','w') as file:
    file.write("print(1+2)")

with open('test1.txt','r') as file:
    code = file.read()

exec(code)
