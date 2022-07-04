from types import NoneType
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import argparse


class WikiWordCounter:
    text = ""
    column_spacing = 25
    url = "https://en.wikipedia.org/wiki/Microsoft"
    section = "History"
    excludeWords = []


    def __init__(self, excludeWords = []):
        if(excludeWords is not None):
            self.excludeWords = excludeWords

        self.__extractText()


    def __extractText(self):
        request = requests.get(self.url)
        soup = BeautifulSoup(request.text, features="html.parser")

        contents = soup.find('div', {"id": "mw-content-text"})
        element_to_parse = contents.find('span', {"id": self.section}).parent.next_sibling

        while(element_to_parse.name != 'h2'):
            if(element_to_parse.name in ('div', 'p', 'h3')):
                toAdd = element_to_parse.getText()
                toAdd = re.sub('(\[[0-9]+\])+', '', toAdd)
                self.text += " " + toAdd

            element_to_parse = element_to_parse.next_sibling

        self.counts = Counter(re.findall('\w+', self.text))

    def topWords(self, topCount:int = 10):
        wordList = self.counts

        if(self.excludeWords is not None):
            for word in list(wordList):
                if word in self.excludeWords:
                    del wordList[word]

        return wordList.most_common(topCount)

    def printTopWords(self, topCount:int = 10):
        top_words = self.topWords(topCount)

        print()
        print(f"Top word count for {self.section} section of {self.url}")
        print("==============================================")
        print(f'{"Word:": <{self.column_spacing}}# of occurrences')
        print("==============================================")
        for word in top_words:
            print(f'{word[0]: <{self.column_spacing}}{word[1]}')


parser = argparse.ArgumentParser(description='Counts the most common words in History section of Microsoft Wiki page.')
parser.add_argument('--top', type=int, help='Specify the number of words to return. default: 10', default=10)
parser.add_argument('--exclude', type=str, nargs='+', help='Words to exclude.')

args = parser.parse_args()

wwc = WikiWordCounter(args.exclude).printTopWords(args.top)