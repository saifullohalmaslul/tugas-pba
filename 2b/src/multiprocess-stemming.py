from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from multiprocessing import Pool

if __name__ == '__main__':
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()

	sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
	words = sentence.split()

	with Pool(5) as pool:
		output = pool.map(stemmer.stem, words)

	output = ' '.join(output)

	print(output)
	# ekonomi indonesia sedang dalam tumbuh yang bangga

	print(stemmer.stem('Mereka meniru-nirukannya'))
	# mereka tiru