formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four")) #<<<出现错误，format 多了个e  foramte
print(formatter.format(True, False ,False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem", #<<<出现错误，“，”忘记打了
    "Or a song about fear"
))
#不能连着套用 2 个 format
# print("i am good {} {}".format('man'*2).format(False))
# format后面（）内可以直接写数字或变量，当要打出字符得加‘’
