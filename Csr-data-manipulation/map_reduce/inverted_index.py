##Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.
import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    #key: document id
    #value: document text as a string
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    #key: word
    #value: list of document ids the word occurs in
    id_lst = []
    for v in list_of_values:
        if v not in id_lst:
            id_lst.append(v)
    mr.emit((key,id_lst))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
