#Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n可以转行
#”空格“后面加变量《《《  ，逗号不能忘记
print("Here are the days: ", days)
print("Here are the months: sss", months)  #months的变量跟在 前面”“最后一个字符
print("Here are the months: {}".format(months)) #这里面的点 参考下面注释

#<<<注意下面2行代码， format前面一个是点一个是逗号，逗号的话 只能在{}再加snow，而点的话{}里面为snow
print("Here are the months {}.",format('snow'))   
print("Its fleece was white as {}.".format('snow'))


#三个”“” 和“”“ 一起也可以打印字符串
print("""
There's something going on here,
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

