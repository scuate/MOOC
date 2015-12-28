##Describe a MapReduce algorithm to count the number of friends for each person.
import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    #record: a list of two elements [personA, personB] where personB is personA's friend
    #key:personA
    #value:1
    key = record[0]
    value = 1
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    #key: person
    #value: a list of "one"s
    #output: (person, friend_count)
    total = 0
    for v in list_of_values:
        total += 1
    mr.emit((key,total))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
