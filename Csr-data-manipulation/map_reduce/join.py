##given records from two tables--Orders and LineItem, join them by order_id
import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    #record: a list of strings representing a tuple in the database (LineItem and Orders mixed together--list[0] indicates which table the record's from) 
    #key: order_id
    #value: the records from both tables
    key = record[1] ##list[1] is the order_id
    value = record ##the entire record
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    #key: order_id
    #list_of_values: all the records where the order id is the same
    #output: a list of joined records from table Orders and LineItem
    for v1 in list_of_values:
        if v1[0] == "order":
            for v2 in list_of_values:
                if v2[0] == "line_item":
                    result = v1+v2
                    mr.emit(result)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
