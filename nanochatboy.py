from collections import namedtuple
from random import choice
from sklearn import svm
import spacy

Rule = namedtuple('Rule', 'questions answers')

class NanoChatbot:
    def __init__(self, language='pt'):
        if language == 'pt':
            self.nlp = spacy.load("pt_core_news_lg")
        elif language == 'en':
            self.nlp = spacy.load("en_core_web_lg")
        else:
            raise ValueError("Language not supported.")
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
                train_x.append(question)
                train_y.append(index)

        docs = [self.nlp(text) for text in train_x]
        train_x_word_vectors = [x.vector for x in docs]
        
        self.svm = svm.SVC(kernel='linear')
        self.svm.fit(train_x_word_vectors, train_y)

    def respond(self, text):
        index = self.svm.predict([self.nlp(text).vector])[0]
        if len(self.answers[index]) == 1:
            return self.answers[index][0]
        return choice(self.answers[index])