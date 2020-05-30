# Author: Ryan Lampe
# 5/29/2020
# Advent of Code 2016
# Day 9, Problem 1

# The language given online between repeating once and not repeating at all is unintuitive. Be careful!
# Since there are no forms of (nx0) with n in Z, we don't have to worry about deleting sequences


# Method to return a string with a substring inserted into it at a given index
def insert_substring(string, substring, index_to_place_before):
    # FTD Error handling for index out of bounds...?
    return string[:index_to_place_before] + substring + string[index_to_place_before:]

# Tests:
#compressed = 'A(2x2)BCD(2x2)EFG'
#compressed = 'X(8x2)(3x3)ABCY'
#compressed = '(6x1)(1x3)A'


with open('input.txt', 'r') as file:
    # Read in the file as one string, removing all newlines
    compressed = file.read().replace('\n', '').replace('\r', '').replace(' ', '')
# Cursor positions
instr_start = 0
instr_end = 0
m = 0
end_of_comp = False
while not end_of_comp:  # Uncertain if this handles edge cases with compressions at the very end of a file


    # Find the next instruction
    while compressed[instr_start] != '(':
        instr_start += 1
        if instr_start == len(compressed):
            end_of_comp = True
            break
    while compressed[instr_end] != ')' and not end_of_comp:
        instr_end += 1
    if end_of_comp:
        break
    instruction = compressed[instr_start + 1:instr_end]
    substr_len = instruction.split('x')[0]
    substr_len = int(substr_len)
    num_repeats = int(instruction.split('x')[1])
    substr = compressed[instr_end + 1: instr_end + 1 + substr_len]  # exclusive of ending

    # Trim the instruction off of the string
    print(compressed)
    compressed = compressed[:instr_start] + compressed[instr_end + 1:]
    print(compressed)
    insertion_location = instr_start + substr_len
    m = 1
    # Repeatedly insert the substring into the current version of the compressed string
    while m < num_repeats:
        compressed = insert_substring(compressed, substr, insertion_location)
        insertion_location += substr_len
        m += 1

    # Start looking for the next instruction after the substring we've added
    instr_start = insertion_location
    instr_end = instr_start

    if instr_start == len(compressed):
        end_of_comp = True

print("The number of chars in uncompressed is to %d" % len(compressed))
print(compressed)