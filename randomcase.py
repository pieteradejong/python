"""
- option first letter of each word capitalized
- parameter x in [0,1] is pribability capitalized
- 
"""

def random_case(s):
    res = []
    for i, c in enumerate(s):
        _ = c.upper() if i % 2 != 0 else c.lower()
        res.append(_)
    return ''.join(res)

print(random_case('myRanDOMcasE'))

