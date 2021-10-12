# Read the file and get the DNA string
file = open('cds_seq.txt', 'r')
dna = file.read()

f = open("rna.txt", "w")
rna = ""

# Generate the RNA string
for i in dna:
    # Replace all occurrences of T with U
    if i == "T":
        rna += "U"
    else:
        rna += i


f.write(rna)

# RNA codon table
print           'UUU : F, CUU : L, AUU : I, GUU : V,'
print            'UUC : F, CUC : L, AUC : I, GUC : V,'
print            'UUA : L, CUA : L, AUA : I, GUA : V,'
print            'UUG : L, CUG : L, AUG : M, GUG : V,'
print            'UCU : S, CCU : P, ACU : T, GCU : A,'
print            'UCC : S, CCC : P, ACC : T, GCC : A,'
print            'UCA : S, CCA : P, ACA : T, GCA : A,'
print           'UCG : S, CCG : P, ACG : T, GCG : A,'
print            'UAU : Y, CAU : H, AAU : N, GAU : D,'
print            'UAC : Y, CAC : H, AAC : N, GAC : D,'
print            'UAA : TER, CAA : Q, AAA : K, GAA : E,'
print            'UAG : TER, CAG : Q, AAG : K, GAG : E,'
print            'UGU : C, CGU : R, AGU : S, GGU : G,'
print            'UGC : C, CGC : R, AGC : S, GGC : G,'
print            'UGA : TER, CGA : R, AGA : R, GGA : G,'
print           'UGG : W, CGG : R, AGG : R, GGG : G '
print "------------------------------------------------------------------------------------------------------------------------------------"
    

#counting occurance of each codon
codons = (rna[n:n+3] for n in xrange(0,len(rna),3))

dict_codons = {}

for codon in codons:
    if dict_codons.has_key(codon):
        dict_codons[codon] += 1
    else:
        dict_codons[codon] = 1

#print dict_codons

#(occurance of each codon/total number of codon)*1000
total = 0  
for i in dict_codons:  
     total = total + dict_codons[i]  
for j in dict_codons:  
    dict_codons[j] = (float)(dict_codons[j])/total  

dict_codons.update((x, y*1000) for x, y in dict_codons.items())
print "Codon usage table for Saccharomyces cerevisiae"
print "------------------------------------------------------------------------------------------------------------------------------------"

print dict_codons
#for sorting
#for key in sorted(dict_codons):
   # print("%s: %s" % (key, dict_codons[key]))

print ""
  





