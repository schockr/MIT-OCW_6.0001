# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re
import collections
collections.Callable = collections.abc.Callable

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """
        Initializes a NewsStory object        

        guid (string): globally unique identifier
        title (string): the title of the news story
        description (string): a description of the news story
        link (string): a link to more content
        pubdate (datetime): published datetime of news story

        A NewsStory object has five attributes:
            self.guid (string, determined by input guid)
            self.title (string, determined by input title)
            self.description (string, determined by input description)
            self.link (string, determined by input link)
            self.pubdate (datetime, determined by input pubdate)

        Returns
        -------
        None.

        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
        
    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid

    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title

    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description

    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link
    
    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate   
    
    def set_guid(self, guid):
        self.guid = guid
        
    def set_title(self, title):
        self.title = title
    
    def set_description(self, description):
        self.description = description
    
    def set_link(self, link):
        self.link = link
        
    def set_pubdate(self, pubdate):
        self.pubdate = pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def get_phrase(self):
        return self.phrase
    # def evaluate(self, story):
    #     if self.phrase in story.get_title():
    #         return True
    #     elif self.phrase in story.get_description():
    #         return True
    #     else:
    #         return False
        

    #@abstractmethod
    def is_phrase_in(self, story):
        phrase = self.get_phrase().lower()
        story = story.lower()
        
        punc = re.compile("[!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']{1,}")
        
        # remove all punctuation
        newstory = punc.sub(' ', story).split()
        
        # initialize empty list to store indices of matched words
        matched_index_list = []
        
        for word in phrase.split():
            if word not in newstory:
                return False
            else:
                #  iterate each word and iterator of each item in the passed argument
                for index, text in enumerate(newstory):
                    if word == text:
                        #  get the index of the matched word in text
                        matched_index_list.append(index)
        #  get the difference between succeeding and preceeding indices
        matched_index_value = [matched_index_list[i + 1] - matched_index_list[i]
                       for i in range(len(matched_index_list) - 1)]        
        
        # Ensure words are consecutive in pharse
        for value in matched_index_value:
            if value != 1:
                return False
            
        return True
        
#         matches = re.finditer(punc,story)
#         for m in matches:
#             print(m.start())
#             print(m.end()-1)
#             print(len(story)-1)
#             print(story)
#             # if m.start()-1 == ' '
#            # or m.end()+1 == ' '
#            # then we can just find and replace with nothing
#            # else we need to replace the match group with a space
#            # but, if m.start() - 1 <=0 then we don't check and automatically replace with nothing
#            # if m.end() >= len(story) then we don't check and automatically replace with nothing
           
#             if m.start()-1<=0 or m.end() >= len(story):
#                 newstory = re.sub(m.group(),'',newstory)#re.sub(punc,'',newstory)
#             elif story[m.start()-1]==' ' or story[m.end()+1]==' ':
#                 newstory = re.sub(m.group(),'',newstory)#re.sub(punc,'',newstory)
#             else:
#                 newstory = re.sub(m.group(),' ',newstory)#re.sub(punc,' ',story)
#                 # if m.start() and m.end()-1 not in [0,len(story)-1]:
          
               
#             #     if story[m.start()-1] ==' ' or story[m.end()-1]==' ':
#             #         story = re.sub(punc,'',story)
#             #         print(story)
#             #     else:
#             #         story = re.sub(punc,' ',story)
#             # else:
#             #     story = re.sub(punc,' ',story)
#             print(m)
# #        story = re.sub(punc,'', story)
#         print(newstory)
#         # for i in string.punctuation:
#         #     story = story.replace(i,' ')
#         story = newstory.lower().strip()
#        # story = story.translate(str.maketrans('','',string.punctuation))
        
#         #print(story)
#         if phrase.strip() in story:
#             print(phrase,'|',story,True)
#             return True
#         print(phrase,'|',story,False)
#         return False
        
# Problem 3
class TitleTrigger(PhraseTrigger):
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

    

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        self.time = datetime.strptime(time,"%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))
    
    def get_time(self):
        return self.time
        
# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self,story):
        return self.time > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

class AfterTrigger(TimeTrigger):
    def evaluate(self,story):
        return self.time < story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T
        
    def get_T(self):
        return self.T
    
    def evaluate(self,story):
        return not self.T.evaluate(story)
# Problem 8
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
        
    def get_T1(self):
        return self.T1
    
    def get_T2(self):
        return self.T2
    
    def evaluate(self,story):
        if (self.T1.evaluate(story)==True and self.T2.evaluate(story)==True):
            return True
        return False

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
        
    def get_T1(self):
        return self.T1
    
    def get_T2(self):
        return self.T2
    
    def evaluate(self,story):
        if (self.T1.evaluate(story)==True or self.T2.evaluate(story)==True):
            return True
        return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []
    
    # search through each story and execute triggers. If trigger returns true then 
    # add story to filtered story list
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                filtered_stories.append(story)
                break
            
    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    trigger_lines = []
    for item in lines:
        trigger_lines.append(tuple(item.split(',')))
        
    # keys from triggers.txt file
    trigger_keys = ['TITLE','DESCRIPTION','AFTER','BEFORE','AND','OR','NOT','ADD']
    
    trigger_dict = {}
    for trig in trigger_lines:
        for key in trigger_keys:
            if key==trig[1]:
                trigger_dict[trig[0]] = []
                for i in range(len(trig)-1):
                    trigger_dict[trig[0]].append(tup[i+1])
            elif key == trig[0]:
                trigger_dict[trig[0]] = []
                for i in range(len(trig)-1):
                    trigger_dict[trig[0]].append(trig[i+1])
    
    trigger_list = []
    trig_dict = {}
    
    for key,val in trigger_dict.items():

        if "TITLE" in val:
            obj = TitleTrigger(val[1])
            trig_dict.setdefault(key, obj)

        elif "DESCRIPTION" in val:
            obj = DescriptionTrigger(val[1])
            trig_dict.setdefault(key, obj)

        elif "Before" in val:
            obj = BeforeTrigger(val[1])
            trig_dict.setdefault(key, obj)

        elif "AFTER" in val:
            obj = AfterTrigger(val[1])
            trig_dict.setdefault(key, obj)

        elif "AND" in val:
            obj = AndTrigger(val[1], val[2])
            trig_dict.setdefault(key, obj)

        elif "OR" in val:
            obj = OrTrigger(val[1], val[2])
            trig_dict.setdefault(key, obj)

        elif key == "NOT":
            obj = NotTrigger(val[1])
            trig_dict.setdefault(key, obj)

        #  add specified triggers to the list
        elif key == "ADD":
            for item in val:
                for obj_key, obj in trig_dict.items():
                    if item == obj_key:
                        trigger_list.append(obj)

    return trigger_list


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("trump")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

