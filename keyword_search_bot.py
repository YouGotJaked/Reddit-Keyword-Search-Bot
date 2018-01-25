import praw
import config
import re

keywords = ["ug","microgram","mg","milligram","ml","milliliter"]

def bot_login():
    print "Logging in..."
    
    reddit = praw.Reddit(username = config.username,
                         password = config.password,
                         client_id = config.client_id,
                         client_secret = config.client_secret,
                         user_agent = "Keyword Search Bot")
                         
    print "Logged in as {}".format(reddit.user.me())
    
    return reddit

def run_bot(reddit):
    subreddit = reddit.subreddit("microdosing")
    
    for submission in subreddit.new(limit = 25):
        title = submission.title
        desc = submission.selftext
        foundWord = []
        foundNum = []
        
        print title
        
        #check description for keywords
        for keyword in keywords:
            if re.search(keyword,desc):
                #print '"%s" found in "%s"' % (keyword,title)
                
                loc = re.search(keyword,desc).start()
                
                foundWord.append(loc)
                
                #print '"%s" foundWord at index %s' % (keyword,loc)
                
        findall = re.findall('\d (?i)[um]g',desc)
        if findall:
            print "matched: '%s'" % findall
            print "\n"
    
        if foundWord:
            #print "\nIndeces of keywords: ",foundWord,"\n"

            #check description for numbers
            num_const = '[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
            rx = re.compile(num_const, re.VERBOSE)
            nums = rx.findall(desc)
        
            for index, n in enumerate(nums):
                loc = desc.find(nums[index])
                
                #print '"%s" found at index %s' % (n,loc)
            
                foundNum.append(loc)
            
            #if foundNum:
                #print "\nIndeces of numbers: ",foundNum,"\n"
    
            #if description has numbers check if units follow
            if nums:
                #encode from unicode to ascii
                nums = [n.encode('ascii') for n in nums]
            
                #convert from string to float
                nums = map(float,nums)
                #print nums, "\n"

        #if has_keyword:
        #print "Title: ", title
            #print "Description: ", desc
            

            
            #if description has numbers check if units follow
            #if nums:
                #encode from unicode to ascii
                #nums = [n.encode('ascii') for n in nums]
                
                #for index, n in enumerate(nums):
                    #location of string
                    #loc = desc.find((nums[index]))
                    #length of string
                    #length = len(nums[index])
                
                #print nums[index], "is at index", loc, "with length", length
            
                #convert from string to float
                #nums = map(float,nums)
                #print nums
                #else:
                #print "No numbers here!"

print "\n"


run_bot(bot_login())
