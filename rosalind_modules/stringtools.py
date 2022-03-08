def reverse(seq):
    return seq[::-1]

def complement(seq):
    dct = {
        'A':'T',
        'G':'C',
        'C':'G',
        'T':'A',
        'U':'A'
    }
    
    comp = ''.join([dct[a] for a in seq])
    return comp

def rev_comp(seq):
    rev = reverse(seq)
    rev_comp = complement(rev)
    return rev_comp

def transcribe(dna_seq):
    rna_seq = dna_seq.replace('t','u')
    rna_seq = rna_seq.replace('T','U')
        
    return rna_seq
    
def gc_content(seq):
    count = seq.count('G')+seq.count('C')+seq.count('c')+seq.count('g')
    gc_percent = 100.0*count/len(seq)
    return gc_percent

def FASTA_parser(fasta_infile):
    dct = {}
    with open(fasta_infile,'r') as infile:
        lines = [a.strip('\n') for a in infile.readlines()]
        for line in lines:
            if line.startswith('>'):
                current_id = line[1:]
                dct[current_id] = ''
            else:
                dct[current_id] += line
    return dct

def highest_gc(seqs_dct):
    gcs_dct = {}
    max_gc = 0
    for a in seqs_dct:
        gc = gc_content(seqs_dct[a])
        gcs_dct[a] = gc
        if gc > max_gc:
            max_gc = gc
            max_gc_key = a
    return max_gc_key+'\n'+str(max_gc)
