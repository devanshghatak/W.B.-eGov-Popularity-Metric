import tweepy, os, datetime, csv
from tweepy import OAuthHandler

def removeEmo(encoded):
    str=''
    for c in encoded:
        if int(c) > 127:
            str+=' '
        else:
            str+=c
    return str

def getTweets(relPath):
    absPath = os.path.abspath(relPath)

    consumerKey = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    consumerSecret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    accessToken = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    accessSecret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    if os.path.isfile(absPath):
        file = open(absPath,'r')
    else:
        return False

    newPath = os.path.join(os.path.dirname(absPath),str(datetime.date.today()))
    if not os.path.isdir(newPath):
        os.makedirs(newPath)

    auth = OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)
    api = tweepy.API(auth)
    #base = os.path.basename(absPath)
    maxTweets = 2000
    for keyword in file.readlines():
        if keyword == '':
            pass
        else:
            searchedTweets = []
            lastId = -1
            while len(searchedTweets) < maxTweets:
                count = maxTweets - len(searchedTweets)
                try:
                    newTweets = api.search(q=keyword, count=count, max_id=str(lastId - 1), geocode="22.6862,82.7722,2254km")
                    if not newTweets:
                        break
                    for tweets in newTweets:
                        print(tweets.text)
                    searchedTweets.extend(newTweets)
                    lastId = newTweets[-1].id
                except tweepy.TweepError as e:
                    # depending on TweepError.code, one may want to retry or wait
                    # to keep things simple, we will give up on an error
                    break
            keyword = keyword[:-1]
            filename = keyword + "-" + str(datetime.date.today()) + '.csv'
            print ('''***
                    *
                    *
                    *
                    *
                    *
                    *
                    ***''')
            print(keyword)
            print ('''***
                    *
                    *
                    *
                    *
                    *
                    *
                    ***''')
            saved = open(os.path.join(newPath,filename), "a+", newline='')
            writer = csv.writer(saved)
            for result in searchedTweets:
                text = str(result.text)
                encoded = text.encode('utf-8')
                #removed = removeEmo(encoded)
                writer.writerow([encoded])
                #print(str(result.text)+'\n')
                print ('')

            print ('''***
                    *
                    *
                    *
                    *
                    *
                    *
                    ***''')
            print(str(os.path.join(newPath,filename)))
            print ('''***
                    *
                    *
                    *
                    *
                    *
                    *
                    ***''')
            saved.close()

    return True

if __name__ == "__main__":
    bool = getTweets(input("Enter the relative path of file storing keywords: "))

    if not bool:
    	print("Couldn't not write the CSV file")

    else:
    	print("The data is printed")
