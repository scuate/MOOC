##Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
##Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.
import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    #key: a dummy key, because we just want a set of trimmed nucleotides
    #value: nucleotides
    key = "dummy"
    value = record[1][:-10] ##remove the last 10 chars in nucleotides
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    #key: a dummy key
    #value: trimmed nucleotides
    #output: unique trimmed nucleotides
    nucle_set = set(list_of_values)
    for v in nucle_set:
        mr.emit(v)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
