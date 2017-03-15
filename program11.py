# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

s = raw_input()
numbers = [num for num in s.split(',')]
val = []

for num in numbers:
    intp = int(num,2)
    if not intp%5:
        val.append(num)
print ','.join(val)
