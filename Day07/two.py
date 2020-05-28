# Author: Ryan Lampe
# 5/14/2020
# Advent of Code 2016
# Day 7, Problem 2
#
# IP Format: [hypernet]supernet
# in any recurance and order


import re

# Parse the ip and return a list of all the hypernets


def parse_hypernets(ipString):
    hypers = []
    results = re.finditer(r'\[.*?\]', ipString)
    for item in results:
        hypers.append(item.group(0)[1:-1]) # Trim off brackets
    return hypers

# Parse the ip and return a list of all supernets


def parse_supernets(string):
    supers = []
    #Remove HNets
    string = re.sub("[\(\[].*?[\)\]]", ',', string)
    supers = string.split(',')
    return supers

# Get a set of abas from supers

def get_abas(supers):
    abas = set()
    for super in supers:
        for i in range(len(super) - 2):
            if super[i] == super[i + 2] and super[i] != super[i + 1]:
                abas.add(super[i:i+3])
    return abas


# Get a set of BABS from hypers (The code would be the same as get_abas)


def get_babs(hypers):
    return get_abas(hypers)



#Convert a list of babs to abas

def babs_to_abas(babs):
    abas = set()
    for bab in babs:
        aba = bab[1] + bab[0] + bab[1]
        abas.add(aba)
    return abas


def is_ssl(ip):
    hypers = parse_hypernets(ip)
    supers = parse_supernets(ip)

    babs = get_babs(hypers)
    actual_abas = get_abas(supers)

    test_abas = babs_to_abas(babs)

    intersect = test_abas.intersection(actual_abas)

    if len(intersect) == 0:
        return False
    return True


# Main


with open('input.txt', 'r') as file:
    ips = file.read().splitlines()

numSSL = 0

for ip in ips:
    if is_ssl(ip):
        numSSL += 1
print("The number of valid SSL ips is : %d" % numSSL)
