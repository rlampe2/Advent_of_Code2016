# Author: Ryan Lampe
# 5/17/2020
# Advent of Code 2016
# Day 5, Problem 1

import hashlib

# Testing examples given in instructions to check hashing algorithm is the same
# print(hashlib.md5(b"abc3231929").hexdigest()) # Should start as 000001
# print(hashlib.md5(b"abc5017308").hexdigest()) # Should start as 000008

realPasswordLength = 8
currentLength = 0
currentPassword = ""
i = 0

with open('input.txt') as file:
    doorId = file.readline()  # No newline, because file doesn't have newline to second line

while realPasswordLength > currentLength:
    testWord = doorId + str(i)
    testHash = hashlib.md5(testWord.encode()).hexdigest()
    i += 1
    good = True
    for c in testHash[0:5]:
        if c != "0":
            good = False
            break
    if good:
        print(testHash[5])
        currentPassword = currentPassword + testHash[5]
        currentLength += 1
print("The password is: %s" % currentPassword)



