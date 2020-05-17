# Author: Ryan Lampe
# 5/14/2020
# Advent of Code 2016
# Day 4, Problem 1

# Likely a regex would be easier...


from collections import Counter
import re
import string

validIDs = []

with open('input.txt', 'r') as file:
    roomList = file.readlines()

for room in roomList:
    # find index of rightmost occurence of [ and ] to get slice indices
    order = room[room.rfind("[") + 1: room.rfind("]")]
    checkSum = room[room.rfind("-") + 1: room.rfind("[")]
    # Add spaces
    roomName = re.sub("-", " ", room[:room.rfind("-")])

    # Decrypt room name:
    shiftDistance = int(checkSum)
    # Need to stay in ascii range:
    alph = list(string.ascii_lowercase)
    roomLetters = list(roomName)
    decrypted = ""

    for c in roomLetters:
        if c != ' ':
            newIndex = (alph.index(c) + shiftDistance) % len(alph)
            c = alph[newIndex]
        decrypted = decrypted + c
    # Uncomment to print out all the
    # print("%s - %s (%s)" % (decrypted, checkSum, roomName) )
    # Find string that has North in it
    if "north" in decrypted:
        print("%s - %s (%s)" % (decrypted, checkSum, roomName) )