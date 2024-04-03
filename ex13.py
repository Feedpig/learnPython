from sys import argv
#read the WYSS section for how to run this
#input of the argv are char tpye not int ,if want to cal need to be transfered
script, first, second, third= argv

print("<<< argv=", repr(argv))
#运行时得添加python ex13.py 1 2 3 其中三个数字就是变量 可以是字符
#input是在运行脚本过程中需要用户输入的，argv是在用户执行命令时输入
print("The script is called: ", script)
print("Your first variable is:", int(first)+len(second))  #这样的结果只是 12 此时变量还只是字符 int(first)+int(second) 变成这样就可以进行数学计算了
print("Your second variable is:", second)
print("Your third variable is:", third)


