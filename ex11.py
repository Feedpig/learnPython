#结尾没有end时 是直接换行输入结果，加入end后 结尾对应添加符号
print("How old are you?")
#将input的字符形式用int（）转化为整数 
age = int(input())
print("How tall are you?", end='>>>')
height = int(input())
print("How much do you weight?", end=' \n')
weight = int(input())
#可以直接对这些变量进行数学运算
print(f"So, you're {age} old, {height} tall and {weight} heavy {weight+height+age}.")