print("Mary had a little lamb.")
#<<<broken 将下面这行中去除“”会怎么样--chu bug 并且format（）中‘不能去除 
#若是要去除format后面的’ 需要在里面加入提前定义好的变量 参考ex6.py中的16行
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")


print("." * 10 + "$" * round(10/2))# what'd that do? 有10个.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. try removing it to see that happens
#<<<broken 下一行中的end=后面加上空格会怎样----没有影响
#<<<broken 下一行中''中加上空格后---出现下面结果----和之前相比cheese后面多了空格
#Cheese Burger
print(end1 + end2 + end3 + end4 + end5 + end6, end =' ' *10 + '8'*10+str(1))
print(end7 + end8 + end9 + end10 + end11 + end12)


