# Author: Ryan Lampe
# 5/14/2020
# Advent of Code 2016
# Day 7, Problem 1

import re

# Parse the ip and return a list of all the hypernets


def parse_hypernets(ipString):
    nets = []
    results = re.finditer(r'\[.*?\]', ipString)
    for item in results:
        nets.append(item.group(0)[1:-1]) # Trim off brackets
    return nets

# Determine if a string has a 4 character reflection


def reflection(string):
    reflect = False
    for i in range(len(string) - 3):
        #if string[i: i + 4] == string[i + 3: i - 1: -1] and string[i] != string[i + 1]:  # reverse substring
        if string[i] == string[i + 3] and string [i + 1] == string[i + 2] and string[i] != string[i + 1]:
                reflect = True
    return reflect

# Return a list of each chunk of strings that are outside of the brackets


def parse_rip(string):
    rip = []
    startInc = 0
    endExcl = -1
    for i in range(len(string)):
        if string[i] == '[':
            endExcl = i
            rip.append(string[startInc: endExcl])
        if string[i] == ']':
            if i < len(string) - 1:
                if string[i + 1] != '[':
                    startInc = i + 1
    return rip

def tls_ip(string):
    validHNet = True
    validABBA = False
    hypernets = parse_hypernets(ip)
    for net in hypernets:
        if reflection(net):
            validHNet = False
            break
    if validHNet: # Proceed to check for ABBA
        rips = parse_rip(ip)
        for rip in rips:
            if reflection(rip):
                validABBA = True

    if validHNet and validABBA:
        return True
    return False



with open('input.txt', 'r') as file:
    ips = file.read().splitlines()

numTLS = 0

for ip in ips:
    validHNet = True
    validABBA = False
    hypernets = parse_hypernets(ip)
    for net in hypernets:
        if reflection(net):
            validHNet = False
            break
    if validHNet: # Proceed to check for ABBA
        rips = parse_rip(ip)
        for rip in rips:
            if reflection(rip):
                validABBA = True

    if validHNet and validABBA:
        numTLS += 1
print("The number of valid TLS ips is : %d" % numTLS)



#NOt 65
#NOT 74
# Method testing:
# test = "abba[mnop]qrst[hello]asdf[abba]asdf[asfacca][hell][elle]"
#
# inBrack = parse_hypernets(test)
#
# print (inBrack)
#
# for brack in inBrack:
#     if reflection(brack):
#         print (brack)

test = "abba[asdf]acd[]affaasdf[asdf]aaaa[aaaa]"
outBrack = parse_rip(test)
print(outBrack)

for o in outBrack:
    if reflection(o):
        print (o)

