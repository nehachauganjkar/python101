# If the following words is given as input to the program:
#
# 2 cats and 3 dogs.
#
# Then, the output of the program should be:
#
# ['2', '3']
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
#
# Use re.findall() to find all substring using regex.
#
# Solution:
import re
s = raw_input()
print re.findall("\d+",s)
