from nltk import text
import nltk.tokenize.punkt

file = open("../res/sentences.txt", "r", encoding='utf8')
text = file.read()
text = text.replace("\n", " ")
file.close()

tokenizer = nltk.data.load('../res/indo.pickle')
segmented = tokenizer.tokenize(text)

out = open("../res/segmented.txt", "w", encoding='utf8')
for sentence in segmented:
	out.write(sentence + "\n")

out.close()
