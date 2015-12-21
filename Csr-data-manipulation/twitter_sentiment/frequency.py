##compute the term frequency of the live stream data (the json data harvested from twitter)
##term_freq=occurences of the term in all tweets/occurences of all terms in all tweets
##print out (term,freq) pairs

from sys import argv
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))



def getTermDict(tweet_file):
    tweetf = open(tweet_file)
    total = 0
    termDict = {}
    for line in tweetf:
        line = line.rstrip()
        tweet = json.loads(line)
        if 'text' in tweet:
            content = tweet['text'].split()
            for w in content:
                total += 1
                if w not in termDict:
                    termDict[w] = 1
                else:
                    termDict[w] += 1

    return termDict, total

def cmptFreq(termDict,total):
    for key,val in termDict.iteritems():
        freq = float(val)/total
        try:
            print key,freq
        except UnicodeEncodeError:
            print key.encode('utf-8'),freq
 

def main():
    tweet_file = argv[1]
#    hw()
#    lines(sent_file)
#    lines(tweet_file)
    termDict,total = getTermDict(tweet_file)
    cmptFreq(termDict,total)

if __name__ == '__main__':
    main()
    
