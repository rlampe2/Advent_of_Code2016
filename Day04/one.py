# Author: Ryan Lampe
# 5/14/2020
# Advent of Code 2016
# Day 4, Problem 1

# Likely a regex would be eaiser...


from collections import Counter
import re

validIDs = []

with open('input.txt', 'r') as file:
    roomList = file.readlines()

for room in roomList:
    # find index of rightmost occurence of [ and ] to get slice indices
    order = room[room.rfind("[") + 1: room.rfind("]")]
    checkSum = room[room.rfind("-") + 1: room.rfind("[")]
    # Remove dashes from room name ("chars to remove", "replace with", string to do it on)
    roomName = re.sub("-", "", room[:room.rfind("-")])

    # Get frequency of chars:
    # 5 Most common chars in order
    # This doesn't break ties lexicographically
    # freq = Counter(roomName).most_common(5) # can't pull just five, b/c the order isn't lexicographical
    freq = Counter(roomName).most_common()
    # Resort in order of count, with ties settled lexicographically (from stack overflow! sort by freq then alph in py)
    freq = sorted(freq, key=lambda item: (-item[1], item[0]))

    # Check to see if the checksum is valid
    match = True
    for o, c in zip(order, freq):
        if o != c[0]:

            match = False
    if match:
        validIDs.append(checkSum)


sum = 0
for id in validIDs:
    sum += int(id)

print(sum)
