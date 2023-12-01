from Bio import SeqIO

def rosalind_revp(s):
    for i in range(len(s)):
        for l in range(4, 13):
            if i + l > len(s):
                continue

            s1 = s[i:i+l]
            s2 = s1.reverse_complement()

            if s1.seq == s2.seq:
                print("%s %s" % (i + 1, l))
                
with open("rosalind_revp.txt", "r") as f:
    input_seq = next(SeqIO.parse(f, "fasta"))
rosalind_revp(input_seq)