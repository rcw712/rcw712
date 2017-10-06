"""

A module for working with DNA data

Copyright Brian E. Chapman, PhD

"""

def get_kmer_locations(seq,kmer="A"):
    """
    seq: a string containing a sequence
    kmer: a string representing a k-mer of interest
    
    returns: a tuple of starting locations for kmer within seq"""
    index = 0
    locations = []
    while index < len(seq):
        i = seq.find(kmer,index)
        if i == -1:
            break
        else:
            locations.append(i)
            index = i+1
    return tuple(locations)

def get_kmer_locations_recursive(seq, kmer="A", start=0):
    """
    seq: a string containing a sequence
    kmer: a string representing a k-mer of interest
    start: the index to start the search in seq
    
    returns: a list of starting locations for kmer within seq"""
    loc = seq.find(kmer, start)
    if loc != -1:
        return [loc] + get_kmer_locations_recursive(seq, kmer=kmer, start=loc+1)
    else:
        return []

def count_kmers(sequences, kmers=('A',)):
    """
    
    """
    results = {}
    for key,seq in sequences.items():
        counts = {}
        for kmer in kmers:
            if set(kmer.upper()).issubset(set("ACTG")):
                counts[kmer.upper()] = seq.replace("\n","").count(kmer.upper())
        results[key] = counts
    return results
