from collections import namedtuple
from random import choice
from sklearn import svm
import spacy

Rule = namedtuple('Rule', 'questions answers')

class NanoChatbot:
    def __init__(self, language='pt'):
        languages = {'pt': 'pt_core_news_lg', 'en': 'en_core_web_lg'}
        self.nlp = spacy.load(languages[language])
        self.answers = []
        self.svm = None
    
    def train(self, train_data):
        self.__train_svm(train_data)
        self.answers = [rule.answers for rule in train_data]

    def __train_svm(self, train_data):
        train_x = []
        train_y = []
        for index, rule in enumerate(train_data):
            for question in rule.questions:
                train_x.append(self.nlp(question).vector)
                train_y.append(index)
        
        self.svm = svm.SVC(kernel='linear')
        self.svm.fit(train_x, train_y)

    def respond(self, text):
        index = self.svm.predict([self.nlp(text).vector])[0]
        if len(self.answers[index]) == 1:
            return self.answers[index][0]
        return choice(self.answers[index])