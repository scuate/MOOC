##derive the sentiment score for terms that don't exist in the given sentiment word dict
##use the sentiment word dict to derive the sentiment score for a tweet, then assign a point to the term in this tweet (0 if neutral, 1 if positive, -1 if negative)
##score = aggregated points/num of tweets the term appears in

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
    newTermSent = {}
    for line in tweetf:
        newTerms = []
        line = line.rstrip()
        tweet = json.loads(line)
        score = 0
        if 'text' in tweet:
            content = tweet['text'].split()
            for w in content:
                if w in sentDict:
                    score += sentDict[w]
                else:
                    newTerms.append(w)
        
        if score == 0:    ##if the tweet is neutral(by computing sentiment words)
            binScore = 0  ##the point for the term is zero
        else:      ##if the tweet is positive, the term gets pt 1; negative,pt-1
            binScore = score/int(abs(score))
        
        for t in newTerms:
            if t not in newTermSent:
                newTermSent[t] = [binScore,1]
            else:
                newTermSent[t][0] += binScore  ##the value of the dict is a two-item list, item 0 being the aggregated pts for the term, item 1 the num of tweets it's in
                newTermSent[t][1] += 1

    return newTermSent

def getNewScore(newDict):
    for key in newDict:
        binScore, count = newDict[key]
        score = float(binScore)/count  ##the score for the term is the aggregated pts over all tweets divided by the num of tweets it appears in
        try:
            print key,score
        except UnicodeEncodeError:
            print key.encode('utf-8'),score
 

def main():
    sent_file = open(argv[1])
    tweet_file = open(argv[2])
#    hw()
#    lines(sent_file)
#    lines(tweet_file)
    sentDict = getSentDict(argv)
    newTermDict = getSentScore(sentDict,argv)
    getNewScore(newTermDict)

if __name__ == '__main__':
    main()
    
