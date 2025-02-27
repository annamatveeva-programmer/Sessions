punctuation = ",.?!"

def find_words(filename):
    '''
    prints the 3 letter words starting with b
    :param filename:
    :return:
    '''
    with open(filename,'r') as f:
        for line in f:
            #Sanitize line
            for p in punctuation:
                line = line.replace(p," ")
            #Break down the line into words
            words = line.split()
            for word in words:
                if len(word) == 3 and word.upper()[0] == "B":
                    print(word)

def get_multiple_6():
    '''
    Returns a multiple of 6 that was entered by the user
    :return: int a number
    '''
    try
        n = input ("Please give me a multiple of 6: ")
        n = int(n) #Convert to integer
        if n % 6 == 0
            return n
        else:
            print("it is not a multiple of 6")
    except ValueError:
        print("you have not entered an integer")

d = {} #Empty dictionary
eng_to_spa = {"one": "uno", "two":"dos","three":"tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "espanol"
print(eng_to_spa)
sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])
eng_to_spa.update({"yes":"si", "no":"no"}) #Update a dictionary with a new dictionary
print(eng_to_spa)
del eng_to_spa["no"] #Remove a key/value from dict
print(eng_to_spa)

# print(eng_to_spa.popitem()) #Not useful since it's hard to know what the last word is
print(eng_to_spa.pop("two")) #Sspecifying the key

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("i dont know that word")

print(eng_to_spa.get("tree", "unknown word"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

for key, value in eng_to_spa.items(): #Simplified a little
    print(f"{value} means {key}")

import requests

link = "https://www.gutenberg.org/cache/epub/84/pg84.txt"

result = requests.get(link)
#print(result.text)
unique_words = {}
punctuation = ";,.'!?-=()"
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace (p," ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word,0) + 1

freq = list(unique_words.values())
freq = sorted(freq, reverse = True)
freq= freq[:10]
print(freq)
print("the most common words in the book")
for f in freq:
    for key, value in unique_words.items():
        if value == f:
            print(key)