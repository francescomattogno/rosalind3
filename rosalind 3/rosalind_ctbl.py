
import re

def parse_newick(t): 
    return sorted(re.sub('[^0-9a-zA-Z_]+', ' ', t).strip().split(' '))
    

def char_table(c):
    
    characterstab = []
    
    
    taxa = parse_newick(c)
    taxa_dict = {i:taxa.index(i) for i in taxa}
    
    
    level = 0
    position = []
    subtrees = []
    
   
    for i in range(len(t)):
        if c[i] == '(':
            level += 1
            position.append(i)
        elif c[i] == ')':
            sub = c[position[-1]+1:i]
            del position[-1]

            while len(subtrees) < level:
                subtrees.append([])
                
            subtrees[level-1].append(sub)
            level -= 1
    
   
    for i in range(1, len(subtrees)):
        for j in subtrees[i]:
            characterstab.append([0 for i in range(len(taxa_dict))])
            
            for k in parse_newick(j):
                characterstab[-1][taxa_dict[k]] = 1
    
   
    return characterstab
    
    
def rosalind_ctbl():
    with open('rosalind_ctbl.txt', 'r') as infile:
        tree = infile.read().strip()
    
    result = char_table(tree)
    
    with open('output/rosalind_ctbl_out.txt', 'w') as outfile:
        outfile.write('\n'.join([''.join(map(str, result[i])) for i in range(len(result))]))


if __name__ == '__main__':
    rosalind_ctbl()