from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from multiprocessing import Pool, cpu_count
import sys
import time

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stemming(batch):
	
	# stemmer.cache = cache
	print("starting process..")
	ts = time.perf_counter()
	result = stemmer.stem(batch)
	te = time.perf_counter()
	print(f"process finished in {te - ts:0.4f} seconds")
	return result

if __name__ == '__main__':
	n_process = cpu_count()

	file = open(sys.argv[1], "r", encoding='utf8')
	sentence = file.read()
	file.close()

	ts = time.perf_counter()
	batches = []
	start = 0
	for i in range(n_process):
		end = start + int(len(sentence)/n_process)
		end = sentence.find(' ', end)
		if end == -1: end = len(sentence) + 1
		batches.append(sentence[start:end])
		start = end

	# factory = StemmerFactory()
	# stemmer = factory.create_stemmer()
	with Pool(n_process) as pool:
		output = pool.map(stemming, batches)

	output = ' '.join(output)

	te = time.perf_counter()
	print(f"Finished in {te - ts:0.4f} seconds")

	out = open("../res/out.txt", "w", encoding='utf8')
	out.write(output)
	out.close()