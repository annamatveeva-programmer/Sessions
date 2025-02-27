s1 = "banana"
s2 = 'banana'
print(s1,s2)
s1 = 'And John said: "How are you". The person replied: "I\'m smart?"' #Use \ to use bpth ' and "
print(s1)
s1 = "I can print \" and another \""
print(s1)
#Indexing, starts from 0
s = "0123456789"
print(s[1], s[7], s[9])
print(s[-1], s[-3], s[-9])
print(len(s)) #Size of the string
print(f"the lenght is {len(s)}")
s = "hello"
print(help(s.capitalize()))
print(s.capitalize())
print("HELLO".casefold()) #Same as .lower() method
print("hello".center(50))
print("hello".center(50, "."))
print("I see a little dove".count("e")) #How many times do I see "e"
print("bananananana".count("ana"))
x = "I do not count nor compare"
print(f"there are: {x.count("o")} 'o's inside {x}") #Number of "o"s in the sentence
print("helloooo695656pool".find("l",10)) #Find "l" starting from position 10
#Find positions that a string appear
s = "bob guesss home meet bob so they can take bob some where"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1: #if they dont find the letter is  -1
        break
    print("found bob in position", start)
    pos = start + 1
#Filler, fill between each element of the list
items = ["cat", "rat", "mouse", "house"]
print("+another+".join(items))
print("I LIKE to go HiKing".lower().upper())
print("I like to go skiing".title())
#Replace, replace item with item inside the string
print("I like to go skiing".replace("i","l").replace("e", "3"))
print("I like to go skiing".split())