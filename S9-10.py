import random
sum = 0
for i in range(10):
    sum += random.randint(1,100)
print(sum)
def greet():
    """
    Simple function that just print hello
    :return: None
    """
    print("Hello!")

def greet2(name):
    """
    Simple function that greets a person
    :param name: Name of the person
    :return: None
    """
    print(f"Hello, {name}")

greet2("Anna")

def special_op(a=1,b=1): #a=1 and b=1 is defining the implicit values (1,1)
    '''
    Special op is 10*a+b
    :param a: first number
    :param b: second number
    :return: value, 10*a+b
    '''
    return 10*a+b

print(special_op(10,2))
print(special_op(2,10))
result = special_op(8,9)
print(f"the special op for 8 and 9 is: {result}")
print(special_op(b=8, a=9))
print(special_op()) #Runs with the implicit values
print(special_op(a=9))

def bond_greet(name):
    print(f"The name is: {name}")

def bondise_name(first_name="James", last_name="Bond"):
    return f"{last_name}, {first_name}, {last_name}"

print(bondise_name("John", "Doe"))
bond_greet(bondise_name("John", "Doe"))
bond_greet(bondise_name())

#Virtual diary
with open("diary.txt", "a") as fp:
    while True:
        text = input("How do you feel today? (type q to quit): ")
        if text == "q":
            break
        fp.write(f"{text}\n")

fp = open("text.txt", "r") #"r" (to read) is by default, so not really needed
print(fp.read()) #Print the entire content of the file
fp.close()
#Same thing with context manager
with open("text.txt", "r") as f:
    print(f.read())
# Read from the same file, line by line
print("read the file line by line")
line_number = 1
with open("text.txt", "r") as fp:
    for line in fp: #Iterate over the file line by line
        print(f'{line_number}: {line}', end="") #Ask print not to add a new line with the end = ""
        #print(line.rstrip())
        line_number +=1
print("done printing")