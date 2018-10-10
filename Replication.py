def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq 


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def SkewArray(Genome):
    skew = [0]
    n = len(Genome)
    for i in range(n):
        if Genome[i] == "G":
            skew.append(skew[i] + 1)
        elif Genome[i] == "C":
            skew.append(skew[i] - 1)
        else:
            skew.append(skew[i])
    return skew


def HammingDistance(p, q):
    if len(p) == len(q):
        count = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                count += 1
        return count
    else:
        return "Strings are not the same length"


def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            positions.append(i)
    return positions


def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            count += 1
    return count

#Text = sequence
#k = length of the pattern
#d = number of missmatches
#v = minimum number of repetitions of the pattern, with d smismatches

def MissmatchPattern(Text, k, d, v):
    freq = {}
    n = len(Text)
    best = {}
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if HammingDistance(Text[i:i+k], Pattern) <= d:
                freq[Pattern] += 1
    for i in freq:
        if freq[i] >= v:
            best[i] = v
    return best