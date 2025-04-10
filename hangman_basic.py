import random

# List of words
hangman_words = [
    "apple", "tiger", "chair", "house", "plant",
    "bread", "phone", "water", "cloud", "smile",
    "jungle", "window", "bottle", "rocket", "camera",
    "flower", "monkey", "desert", "planet", "pencil",
    "oxygen", "cryptic", "zephyr", "awkward", "rhythm",
    "iceberg", "galaxy", "python", "tsunami", "voyage"
]


# selecting random word
# ran = random.randint(0,len(hangman_words))
# word = hangman_words[ran]
word = random.choice(hangman_words)
# print(word)

#Welcoming the user
print("Welcome to Hangamn \n ")

#Printinf underscores for input
o ="_ "
final = ""
for i in range(len(word)):
    final += o
print(final)
# print(len(final))

# Converting ste into list
word1 = list(word)
# print(word1)

#Creating a Final value to compre with
compared_with = ""
for i in word1:
    compared_with += str(i)+" "

# Diagram to display of Hangman when wrong answer is Entered
output = [
"""   -------------------
            |           |
            o           |
                        |
                        |
                        |
                      __|__
""",
"""   -------------------
            |           |
            o           |
            |           |
                        |
                        |
                        __|__
""",
"""   -------------------
            |           |
            o           |
            |\          |
                        |
                        |
                      __|__
""",
"""   -------------------
            |           |
            o           |
           /|\          |
                        |
                        |
                      __|__
""",
"""   -------------------
            |           |
            o           |
           /|\          |
             \          |
                        |
                      __|__
""",
"""   -------------------
            |           |
            o           |
           /|\          |
           / \          |
                        |
                      __|__
"""
]

#define number of chances
chance = 6
# Staritng the loop
coun = 0


while coun < chance: 
    #Taking input
    choice = input("\n Enter The Guess : ").upper()

    # # Comparing if element entered in list
    if choice in word1:

        #FIND INDEX
        index = int(word1.index(choice))

        #EDIT HR VALUE AT INDEX TO NULL TO PREVENT CONSIDERING SAME VALUE , if not wanted
        word1[index] = " "

        # Configure it to the index of final including spaces 
        if index != 0:
            index *= 2
        
        #convert Str to list for replace value at particular position
        final1 = list(final)
        final1[index] = choice

        # Again construct the string
        final = ""
        for i in final1:
            final += i

        print("\n Letter PRESENT")
        print(final)
        # print(f"{final} == {compared_with}")
        if final == compared_with:
            print("🎉 SUCCESS! You completed the word.")
            break
    else:
            print("\n NOT PRESENT")
            print(f"\t {output[coun]}")
            if coun + 1 < chance :
                print(final)
            coun += 1
if coun == chance :
    print("💀 LIFE OVER")
    print(f"The word was: {word}")
else:
    print("🎉 YOU WON THE HANGMAN GAME!")
         
