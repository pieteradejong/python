# source:
# https://twitter.com/CodingComputing/status/1632623417471176704


a_dict = {}
a_string = "BANANA"
a_range = range ( len ( a_string ) )
for char, a_dict[char] in zip(a_string, a_range):
	pass

assert(a_dict['B'] == 0)
assert(a_dict['A'] == 5)
assert(a_dict['N'] == 4)
