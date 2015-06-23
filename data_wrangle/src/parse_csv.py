##parse csv file, store all the data in a list
import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"

# csv.reader creates an iterable object, "for" loop calls next() function every time and a list is created for each row
def parse_file(datafile):
    name = ""
    data = []
    counter = 1
    with open(datafile,'rb') as f:
        datareader = csv.reader(f)
        for line in datareader:
            if counter == 1:
                name = line[1]
            elif counter > 2:
                data.append(line)
            counter += 1
    return (name, data)



def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
