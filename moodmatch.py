import requests
import json
import re


class MoodMatch:

    def __init__(self, options=None):
        if options is None:
            options = {}

        self.options = options
        self.accuracy = 0
        #increase accuracy to inc base num of matches in opinions
        if 'accuracy' in self.options:
            self.accuracy = self.options['accuracy']
        self.api_key = self.options['api_key']

    def match(self, mood, opinions):
        mood = self.clean_word(mood)
        resp = self.get_synonyms(mood)

        resp_types = ('adjective', 'noun', 'verb')
        mood_syns = []

        for t in resp_types:
            if t in resp:
                if 'syn' in resp[t]:
                    mood_syns.extend(resp[t]['syn'])
                if 'sim' in resp[t]:
                    mood_syns.extend(resp[t]['sim'])
        mood_syns.extend([mood])

        #words to array, remove whitespace tabs, newlines
        opinion_words = opinions.split()
        match_count = 0
        #look for our search mood within content opinions
        for word in opinion_words:
            word = self.clean_word(word)
            if word in mood_syns:
                match_count += 1

        #if found, our content likely matches our mood
        if match_count > self.accuracy:
            return True
        else:
            return False

    def get_synonyms(self, word):
        word = word.lower()
        url = 'http://words.bighugelabs.com/api/2/{0}/{1}/json'.format(self.api_key, word)
        r = requests.get(url)
        return json.loads(r.text)

    def clean_word(self, word):
        matches = re.findall(r'\w+', word)
        if matches:
            return ''.join(matches).lower()
        else:
            return word