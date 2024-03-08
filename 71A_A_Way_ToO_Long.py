n = int(input())

wordList = []

for i in range(n):
    word = input()
    wordList.append(word)
    
# print(len(wordList))
print(wordList)

# word = wordList[0]
# print(word)

# tempWord = word[0]+str(len(word)-2)+word[-1]
# print(tempWord)

# # for word in wordList:
# #     print(word)
    
# i = wordList.index(word)
# wordList.insert(i, tempWord)

for word in wordList:
    if len(word)< 10:
        continue
    else:
        tempWord = word[0]+str(len(word)-2)+word[-1]
        i = wordList.index(word)
        wordList.insert(i,tempWord)

print(wordList)

# for word in wordList:
#     print(word)
#     if len(word) > 10:        
#         print("inside if")
#         tempWord = word[0]+str(len(word)-2)+word[-1]
#         index = wordList.index(word)
#         wordList.insert(index, tempWord)

# print(wordList)
