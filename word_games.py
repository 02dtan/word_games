"""
    with open("scrabble.txt", 'r') as f:
    count = 0
    for line in f:
        if count > 5:
            break
        print(line)
        count += 1
"""

#1: Compute scrabble tile score of given string input

#2: Compute all "valid scrabble" words that you could make
#   with all char from an input string. Returns list of
#   valid words; if no words, returns empty list
"""
chars=input("input your characters in ALL CAPS: ")
charsList=sorted(list(chars))
final=[]
with open("scrabble.txt", 'r') as f:
    for line in f:
        line=line.strip()
        if sorted(list(line)) == charsList:
            final.append(line)
print(final)
"""

#3: The game of ghost is played by taking turns with
#   a partner to add a letter to an increasingly long
#   word. The first person to make a valid scrabble word
#   of length 3 or more loses. Must continuously be valid word.
#3a:Write a bot to play ghost against you.

#This program is currently nonfunctional - something is not working in the block at line 48
#Will split into functions in free time but am hungry
word=""
with open("scrabble.txt", 'r') as g:
    flip = 1
    while flip == 1:
        flip=0
        char=input("input a character in ALL CAPS: ")
        word=word+char
        for line in g:
            temp=""
            line=line.strip()
            if line==word:
                print("you made the word "+line+", so you lost")
                break
            for charac in line:
                temp=temp+charac
                if temp==word:
                    flip = 1
                    break
    print(word + " is no longer a valid word, so you lost")
