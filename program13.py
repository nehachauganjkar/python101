# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

sentence = raw_input()
d = {"DIGITS": 0 , "LETTERS": 0}
for c in sentence:
    if c.isdigit():
        d["DIGITS"] += 1;
    if c.isalpha():
        d["LETTERS"] += 1;
    else:
     pass;
print "LETTERS", d["DIGITS"]
print "DIGITS", d["LETTERS"]
