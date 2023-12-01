import itertools

def rosalind_perm(input):
	nums = ''
	for i in range(1,input+1):
		nums += str(i)
	combinations = ([x for x in itertools.permutations(leads)])
	print(len(combinations))
	for i in combinations:
		print(' '.join(map(str, i)))


rosalind_perm(6)