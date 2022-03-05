from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import sys
import time

file = open(sys.argv[1], "r", encoding='utf8')
sentence = file.read()
file.close()

ts = time.perf_counter()
factory = StemmerFactory()
stemmer = factory.create_stemmer()
output = stemmer.stem(sentence)
te = time.perf_counter()
print(f"Finished in {te - ts:0.4f} seconds")

out = open(sys.argv[1], "w", encoding='utf8')
out.write(output)
out.close()