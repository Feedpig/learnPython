ten_thing = "Apples oranges Crows Telephone Light Sugar"

print("Wait there are not 10 thing in that list. Let's fix chat.")

stuff = ten_thing.split(' ')
more_stuff = ["Day","Night","Song",
              "Frisbee","Corn","Banana","Girl","Boy"]

# while len(stuff) != 10 :
#     next_one = more_stuff.pop()
#     print("Adding: ",next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now.")

#extract item in reversed from more_stuuf
for item in reversed(more_stuff):
    if len(stuff) >=10:
        print(more_stuff)
        break
    print("Adding: ",item)
    stuff.append(item)
    print(f"There are {len(stuff)} items now.")
print("There we go:",stuff)

print("Let's do some thing with stuff")
#first stuff
print(stuff[1])
#last stuff
print(stuff[-1])
#last stuff and withdrow it
print(stuff.pop())
#add ' ' in during each stuff
print(' '.join(stuff))
#[3,) 左开右闭
print('#'.join(stuff[3:5]))

