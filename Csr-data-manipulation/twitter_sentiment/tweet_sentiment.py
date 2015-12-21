##derive the tweet sentiment with a sentiment word dictionary
##a sentiment score is aggregated by the scores of sentiment words in a tweet
##print out the score in order for each tweet

from sys import argv
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def getSentDict(argv):
    sent_f = open(argv[1])
    sentDict = {}
    for line in sent_f:
        term, score = line.split('\t')
        sentDict[term] = int(score)
    return sentDict

def getSentScore(sentDict,argv):
    tweetf = open(argv[2])
    for line in tweetf:
        line = line.rstrip()
        tweet = json.loads(line)
        score = 0
        if 'text' in tweet:
            content = tweet['text'].split()
            for w in content:
                if w in sentDict:
                    score += sentDict[w]
        print score
            
            # try:
            #     print content
            # except UnicodeEncodeError:
            #     print content.encode('utf-8')

def main():
    sent_file = open(argv[1])
    tweet_file = open(argv[2])
#    lines(sent_file)
#    lines(tweet_file)
    sentDict = getSentDict(argv)
    getSentScore(sentDict,argv)
    
if __name__ == '__main__':
    main()
