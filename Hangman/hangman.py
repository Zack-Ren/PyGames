import random

lives = 0
usedChars = []
ans = []
allowedChars = 'abcdefghijklmnopqrstuvwxyz'

#Read words into an array
text = open('Dic.txt')
temp = text.read()
wordlist = temp.split()
text.close()

# User inputted word
def getWord():
    x = random.randint(0,len(wordlist))

    word = wordlist[x].replace('\'','')
    lives = len(word) - 1

    return word, lives

# Create blank list for correct letters guessed
def initAns(word):
    for i in range(len(word)):
        ans.append('_')
    return ans

# Get users guess, check if letter has been used before
def getChr():
    user = input('Guess a letter\n')
    while(len(user) != 1 or user not in allowedChars):
        user = input('Invalid input, try again\n')
    usedChars.append(user)
    while(len(usedChars)) != len(set(usedChars)):
        del usedChars[-1]
        user = input('You already used that letter, try again\n')
        usedChars.append(user)

# Check if users guess is in the word, else reduce a life
def checkLetter(lives):
    if usedChars[-1] not in word:
        lives -= 1
        print('You have', lives, 'lives left!')

    for i in range(len(word)):
        if (usedChars[-1] == word[i]):
            ans[i] = usedChars[-1]
    print(ans)
    return lives

def checkWin(word, ans):
	for i in range (len(ans)):
		if ans[i] != word[i]:
			return False
	return True

word,lives = getWord()
ans = initAns(word)
print('Your word is', len(ans), 'letters long')

while (lives > 0):
    # Getting user guess, making sure no dupes
    getChr()
    print(usedChars)
    lives = checkLetter(lives)

    if (checkWin(word, ans)):
        print('You win!')
        quit()
    
print("The word was '",word,"'")