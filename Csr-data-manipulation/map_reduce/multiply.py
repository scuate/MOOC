#Assume two matrices A and B(5X5) in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B
import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    #record:  [matrix, i, j, value]
    #key: (x,y) in the result matrix
    #value: for matrixA, (matrixA,j,value); for matrixB, (matrixB,i,value)
    matrix = record[0]
    i = record[1]
    j = record[2]
    val = record[3]
    if matrix=="a":
        for q in range(5):
            key = (i,q)
            value = ("a",j,val)
            mr.emit_intermediate(key,value)
    if matrix=="b":
        for q in range(5):
            key = (q,j)
            value = ("b",i,val)
            mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    #key: result matrix index (i,j)
    #values: a list of necessary multipliers for computing the result (i,j) val
    #output: (i,j,value) in the result matrix
    sum = 0
    for v1 in list_of_values:
        matrix = v1[0]
        row = v1[1]
        val1 = v1[2]
        if matrix=="a":
            for v2 in list_of_values:
                if v2[0]=="b" and row == v2[1]:
                    sum += val1*v2[2]
    mr.emit((key[0],key[1],sum))
                


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
