the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2 , 'dimes', 3 ,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of tpe:{fruit}")

#alseo we can go throgh mixed lists too
#notice we have to use{} since we don't know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists, fiirst start with an empty one
elements  =[]

# then wuse the range function to do 0 to 5 counts
# cant reach 6 0<=i<6
for i in range(0,6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)
#也可以elements = list(range(0, 6))


#now we can print them out too
for i in elements:
    print(f"Element was:{i}")
    