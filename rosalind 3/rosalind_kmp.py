def rosalind_kmp(sequence):
    length = len(sequence)
    fl = [0] * length

    j = 0
    for i in range(1, length):
        while j > 0 and s[i] != s[j]:
            j = fl[j - 1]
        if sequence[i] == sequence[j]:
            j += 1
        fl[i] = j

    return fl

dnasequence = """#input the file content here"""
lines = dnasequence.split('\n')[1:]
dna = ''.join(lines)
result = rosalind_kmp(dna)
print(' '.join(map(str, result)))