from sys import argv

script, user_name = argv
#下面变量为之后input内的提示词
promt = '>>> '

print(f"Hi {user_name}, i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"Do you like me {user_name}")
likes = input(promt)

print(f"Where do you live {user_name}")
lives = input(promt)

print("What kind of computer do you have?")
computer = input(promt)

print(f"""
Alringt, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer. Nice.
""")


