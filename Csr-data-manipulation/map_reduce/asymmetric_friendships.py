##Generate a list of all non-symmetric friend relationships.
import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    #record: a list of two elements [personA, personB] where personB is personA's friend
    #key:personA
    #value:personB
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    #key: person
    #value: a list of friends of the person
    #output: (friend,person), where tup[0] is a friend of tup[1] but the opposite is not true
    for v in list_of_values:
        if v not in mr.intermediate or key not in mr.intermediate[v]:
            mr.emit((key,v))  ##the friend doesn't have a friend, or the person is not in the friend's friend list
            mr.emit((v,key))




if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
