# Author: Ryan Lampe
# 6/8/2020
# Advent of Code 2016
# Day 12, Problem 2

# This code is virtually the same as part one, just change initalization of reg c to be 1


# Building part of a "simple processor!" Reminds me of my 230 days :)
import copy


class SimpleProcessor:

    def __init__(self):
        # Build registers
        self.registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
        # Build instruction register
        self.instructions = []

        self.ip = 0

    def input_instructions(self, instructions: list):
        self.instructions = copy.deepcopy(instructions)

    def inc(self, register):
        self.registers[register] += 1

    def dec(self, register):
        self.registers[register] -= 1

    def movi(self, val, register):
        self.registers[register] = val

    def mov(self, source, destination):
        self.registers[destination] = self.registers[source]

    def execute(self):
        instruction = self.instructions[self.ip]
        op = instruction.split(' ')[0]
        op_a = instruction.split(' ')[1]

        if op == 'cpy':
            op_b = instruction.split(' ')[2]

            if op_a.isalpha():
                self.mov(op_a, op_b)
            else:
                self.movi(int(op_a), op_b)
        elif op == 'inc':
            self.inc(op_a)
        elif op == 'dec':
            self.dec(op_a)
        elif op == 'jnz':
            if op_a.isalpha():
                if self.registers[op_a] != 0:
                    op_b = instruction.split(' ')[2]
                    self.ip += int(op_b) - 1 # Because we auto increment each time!
            elif op_a != 0:
                op_b = instruction.split(' ')[2]
                self.ip += int(op_b) - 1
        else:
            print('Unknown instruction: %s' % instruction)

    def run(self):
        while self.ip < len(self.instructions):
            self.execute()
            self.ip += 1

    def display_values(self):
        print(self.registers)


# MAIN
with open('input.txt') as file:
    instructions = file.read().splitlines()
comp = SimpleProcessor()
comp.input_instructions(instructions)
comp.run()
comp.display_values()