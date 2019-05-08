import spacy
nlp = spacy.load("en_core_web_sm")



text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""


doc = nlp(text)


filtered_sent=[]

for word in doc:
    if word.is_stop==False:
        filtered_sent.append(word)
print("Filtered Sentence:",filtered_sent)