from os import error
from xlwt import Workbook

source = open("../res/sentences.txt", "r")
result = open("../res/segmented.txt", "r")

good_sentences = source.read()
if not good_sentences.endswith('\n'): good_sentences += '\n'
punkt_sentences = result.read()

if not len(good_sentences) == len(punkt_sentences):
	raise Exception("Panjang karakter kedua file berbeda.")

source.close()
result.close()

wb = Workbook(encoding="utf8")
ws = wb.add_sheet("Sheet1")
ws.write(0, 0, label='nomor')
ws.write(0, 1, label='kalimat asli')
ws.write(0, 2, label='hasil punkt')
err_count = 0
stc_start = 0
stc_end = 0
while stc_end != -1:
	stc_end = good_sentences.find('\n', stc_start)
	good_stc = good_sentences[max(0, stc_start-1) : stc_end+1]
	punkt_stc = punkt_sentences[max(0, stc_start-1) : stc_end+1]
	if good_stc != punkt_stc:
		punkt_stc = punkt_sentences[punkt_sentences.rfind('\n', 0, stc_start)+1 : punkt_sentences.find('\n', stc_end)+1]

		err_count += 1
		print('- {0} ---------------------------------------------'.format(err_count))
		print('\033[92m' + good_stc + '\033[0m')
		print('\033[91m' + punkt_stc + '\033[0m')
		ws.write(err_count, 0, label=err_count)
		ws.write(err_count, 1, label=good_stc.rstrip())
		ws.write(err_count, 2, label=punkt_stc.rstrip()) #TODO: buat tanda kesalahan segmentasi
	stc_start = stc_end + 1

print("Total error {0} dari {1} kalimat".format(err_count, good_sentences.count('\n')))

wb.save('../res/punkt_error.xls')