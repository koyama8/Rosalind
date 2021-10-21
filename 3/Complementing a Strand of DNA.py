DNA = {'A':'T','C':'G','T':'A','G':'C'}

def Complementing(seq):
    return ''.join(DNA[n] for n in seq)[::-1]

print(Complementing("GTCA"))