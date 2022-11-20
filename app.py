
# def main():
#     dictionary = {
#         'hi': 'heeyyy',
#         'hello': 'hahaha',
#         'okay': 'yessss',
#     }

#     while True:
#         word = input("Enter the word to search: ")
#         if word == "":
#             break
#         if word in dictionary:
#             print(word,":", dictionary[word])
            

# main()


from PyDictionary import PyDictionary

dictionary = PyDictionary

while True:
    print("")
    word = input("Enter the word: ")
    if word == "":
        break
    print(dictionary.meaning(word))


