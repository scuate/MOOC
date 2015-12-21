##compute the ten most frequent hashtags from the live stream data

from sys import argv
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def getHtFreq(argv):
    tweetf = open(argv[1])
    htDict = {}
    for line in tweetf:
        line = line.rstrip()
        tweet = json.loads(line)
        if 'entities' in tweet:
            ht_lst = tweet['entities']['hashtags']
            if len(ht_lst) > 0:
                for ht in ht_lst:
                    ht_txt = ht['text']
                    if ht_txt not in htDict:
                        htDict[ht_txt] = 1
                    else:
                        htDict[ht_txt] += 1
    return htDict


def printTopTen(htDict):
    i = 0
    for k in sorted(htDict,key=htDict.get):
        if i == 10:
            break
        try:
            print k, htDict[k]
        except UnicodeEncodeError:
            print k.encode('utf-8'), htDict[k]
        i += 1



def main():

#    lines(sent_file)
#    lines(tweet_file)
    htDict = getHtFreq(argv)
    printTopTen(htDict)
    
if __name__ == '__main__':
    main()
