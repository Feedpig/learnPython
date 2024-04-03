types_of_people = 10
x= f"There are {types_of_people} types of people."

binary = "binary"
do_not ="don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said :{x}")
#可以直接写：print(f"i also said: '{y})
print(f"I also said: {f'{y}'}")

# bad_boy = print(f"i'm bad boy{do_not}")
# print(bad_boy.format(do_not))

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
#这个format后面的（变量--任意定义的变量）就是将这个变量放于16行的{}中 
print(joke_evaluation.format(do_not))
print(f"sdfsf {do_not}")
#print(f"i like this{format(do_not)}")
w = "This is the left side of..."
e = "a string with a right side."
#这行代码也可以写成print（f“{w+e}”）
print(w+e)
print(f"{w+e}")
#当不知道这行代码是什么意思的时候就print
