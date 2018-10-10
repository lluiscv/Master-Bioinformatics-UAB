#ASSIGNMENT 2

def sum_odds(a,b):
    count = 0
    for x in range(a,b+1):
        if x % 2 != 0:
            count += x
    return count

print sum_odds(4,15)
print range(4,15+1)

#ASSIGNMENT 3

def count_bases(s):
	A,C,T,G = 0,0,0,0
	for x in s:
		if x == 'A':
			A += 1
		elif x == 'C':
			C += 1
		elif x == 'T':
			T += 1
		elif x == 'G':
			G += 1
	return 'There are %d Adenines, %d Cytosines, %d Thymines and %d Guanines' %(A,C,T,G)

#ASSIGNMENT 4

def translate(t):
	u = ''
	for i in t:
		if i == 'T':
			u += 'U'
		else:
			u += i   
	return u


#ASSIGNMENT 5

	"""
	First function to calculate the percent of G and C given a DNA sequence
	as a string, with an error of 0.001.
	"""


def GC_percent(sequence):
    GC = 0
    for i in sequence:
        if i in ['G','C']:
            GC += 1
    return format(((GC * 100) / len(sequence)), '.3f')


	"""
	This second function gets the names of .txt files containing
	the FASTA formated sequences, and returns the name of the one
	having the highest GC content, followed by this percentage, as 
	calculated by the previous function.
	"""


def higher_GC(*strings):
    headers = []
    seqs = []
    for i in strings:
        with open(i) as fasta:
            m = list(fasta)
            seq = ''
            for s in m:
                if s.startswith('>'):
                    headers.append(s[1:-1])
                else:
                    seq += s
        seqs.append(''.join(seq.split()))
    d = dict(zip(seqs, headers))
    contents = []
    for x in list(d.keys()):
        contents.append(GC_percent(x))

    return headers[contents.index(max(contents))] + ' ' + max(contents)