from rasa_nlu.model import Interpreter
import json

import speech_recognition as sr
r = sr.Recognizer()
speech = sr.AudioFile('aamir.wav')
with speech as source:
    audio = r.record(source)
text = r.recognize_google(audio)

# text = u"I am calling to claim insurance for my Honda Civic that suffered an accident two days ago when it came in the way of a multi vehical collision."

# This is a call to claim insurance for a [Honda](brand) [Accord](model) from [Karnataka](state). My [Son](relation) was driving his car on the 16th of february this year when he suffered a [front](collision) collision which resulted in [major](severity) loss. We called the [fire](authorities) fighters. It was in the [night](time_of_day). It was a [multi vehical](incident_type) crash.

interpreter = Interpreter.load('models/current/nlu')
result = interpreter.parse(text)
# print(json.dumps(result))

entities = {}

incident_hour = {'morning': 9, 'afternoon': 2, 'evening': 6, 'night': 10}
relative = {'child':'own-child', 'son':'own-child', 'daughter':'own-child', 'husband':'husband', 'wife':'wife', 'relative':'other-relative'}

for entity in result['entities']:
    if entity['confidence'] < 0.35:
        continue
    extractor = entity['extractor']
    if extractor == 'ner_crf':
        key = entity['entity']
        value = entity['value']
        if key == 'time_of_day':
            entities['incident_hour'] = incident_hour[value]
        elif key == 'relation':
            entities[key] = relative[value]
        elif key == 'collision':
            entities[key] = value.capitalize() + ' Collision'

        else:
            entities[key] = value.capitalize()

print(result['entities'])
    