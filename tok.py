import spacy
from spacy.lang.en import English


nlp = English()

text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""


my_doc = nlp(text)


token_list = []
for token in my_doc:
    token_list.append(token.text)
print(token_list)