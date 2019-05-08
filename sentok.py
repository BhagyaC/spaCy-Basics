import spacy
from spacy.lang.en import English
nlp= English()


text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""

sbd = nlp.create_pipe('sentencizer')
nlp.add_pipe(sbd)

my_doc = nlp(text)

# Create list of word tokens
sent_list = []
for sent in my_doc.sents:
    sent_list.append(sent.text)
print(sent_list)