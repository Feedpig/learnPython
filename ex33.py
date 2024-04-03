import numpy as np
i = 0
numbers = []
#需要手动i+1
while i <6 :
    print(f"At the top i is {i}")
    numbers.append(i)

    i+=1
    print("Numbers now:", numbers)
    print(f"At the bottom i is{i}")

print("The numbers: ")

for num in numbers:
    print(num)
numbers1 =[]
#for 不需要手动+1, 步长2 只能为整数
for a in range(0,6,2):
    numbers1.append(a)
    print(f"a = {a}")
print(numbers1)
#利用numpy 步长可以为小数
number2 =[]
for i in np.arange(0,6,1.5):
    print(f"i= {i}")