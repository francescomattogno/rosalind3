from itertools import product

def rosalind_lexf(letters, num):
	letters = letters.replace(" ", "")
	combinations = ([x for x in product(letters, repeat=num)])
	for i in combinations:
		print(''.join(map(str, i)))


rosalind_lexf('A B C D', 4)

