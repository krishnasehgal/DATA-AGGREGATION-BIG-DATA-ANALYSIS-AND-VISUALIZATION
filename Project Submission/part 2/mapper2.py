#!/usr/bin/env python
"""mapper2.py"""

import sys
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

for line in sys.stdin:
    line = re.sub(r'http\S+', '', line)
    # replace 't  by t
    line = re.sub(r"'t",'t',line)
    line = re.sub(r"[.]",'',line)
    #remove puntuation
    line = re.sub(r'[^\w\s]',' ',line)

    stopwords = ['about', 'all', 'along', 'also', 'an', 'any', 'and', 'are', 'around', 'after', 'according', 'another',
                'already', 'because', 'been', 'being', 'but', 'become', 'can', 'could', 'called',
                'during', 'do', 'dont', 'does', 'doesn', 'did', 'didnt', 'etc', 'for', 'from', 'far',
                'get', 'going', 'had', 'has', 'have', 'he', 'her', 'here', 'him', 'his', 'how',
                'into', 'isnt', 'its', 'just', 'let', 'like', 'may', 'more', 'must', 'most', 
                'not', 'now', 'new', 'next', 'one', 'other', 'our', 'out', 'over', 'own', 'put', 'right',
                'say', 'said', 'should', 'she', 'since', 'some', 'still', 'such', 
                'take', 'that', 'than', 'the', 'their', 'them', 'then', 'there', 'these',
                'they', 'this', 'those', 'through', 'time', 'told', 'thing', 
                'use' ,'until', 'via', 'very', 'under',
                'was', 'way', 'were', 'what', 'which', 'when', 'where', 'who', 'why', 'will', 'with', 'would', 'wouldnt', 
                'yes', 'you', 'your', 'file', 'files','pdf', 'bedroom', 'replied',  'ago', 'home', 'report', 'doc', 'day',
                'com', 'comment', 'comments', 'reply', 'people', 'says', 'ceo', 'glass', 'ideas', 'year', 'years', 'fri',
                'furniture', 'smartphone','media', 'email', 'manual', 'short', 'description','bed', 'service', 'guide', 
                'repair', 'book', 'edit', 'free', 'money', 'top', 'share', 'thu', 'video', 'only', 'read', 'post', 'local',
                'iphones', 'many']
    # split the line into words
    words = line.split()

    for k in range(len(words) - 1):
        #stemming
        #l = ps.stem(words[k])
        l = words[k]
        l = l.lower()
        if l not in stopwords and len(l)>2 and  not (l.isdigit()):
            for j in words[k+1:]:
                r = j.lower()
                #r = ps.stem(r)
                if r in stopwords or l == r or len(r)<=2 or r.isdigit():
                    continue
                key = l+"-"+r
                print "%s\t%s" % (key,1)


