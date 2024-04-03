from sys import argv
# def Shushu(a1,a2,a3):
#     print(f"{a1}+{a2}+{a3}={format(int(a1)+int(a2)+int(a3))}")

# print("first one")
# script,arg_a1, arg_a2,arg_a3 = argv
# Shushu(arg_a1, arg_a2,arg_a3)

# print("secend one")
# a_1 = input("输入 a1:")
# a_2 = input("shuru a2:")
# a_3 = input("shuru a3:")
# Shushu(a_1,a_2,a_3)


def printf(*args):
    for i,arg in enumerate(args):
        print(arg)
        if i == len(args)-1: 
            #i start from 0 , when the numembers of args are 4 ,0 -3
            print()
# data1 = input("first:")
# data2 = input("second:")
# printf(data1,data2)    

Data_acount = int(input("entering the number of data:"))
data = []
for i in range(Data_acount):
    data.append(input(f"Please input {i+1} data:"))
printf(*data)


