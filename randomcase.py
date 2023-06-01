from random import random

"""
- option first letter of each word capitalized
- parameter x in [0,1] is probability capitalized
- 
"""

def randomize_case(strToRandomize: str=None) -> str:
    res = []
    for _, char in enumerate(strToRandomize):
        replChar = char if random() > .5 else char.swapcase()
        res.append(replChar)
    return ''.join(res)

print(randomize_case('myrandomcase'))


