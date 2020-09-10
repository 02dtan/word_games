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
chars=input("input your characters in ALL CAPS: ")
charsList=sorted(list(chars))
final=[]
with open("scrabble.txt", 'r') as f:
    for line in f:
        line=line.strip()
        if sorted(list(line)) == charsList:
            final.append(line)
print(final)

#3: The game of ghost is played by taking turns with
#   a partner to add a letter to an increasingly long
#   word. The first person to make a valid scrabble word
#   of length 3 or more loses. Must continuously be valid word.
#3a:Write a bot to play ghost against you.
