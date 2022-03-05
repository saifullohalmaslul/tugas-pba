import xlwt

source = open("../res/sentences.txt", "r", encoding="utf8")
result = open("../res/segmented.txt", "r", encoding="utf8")

good_sentences = source.read()
if not good_sentences.endswith('\n'): good_sentences += '\n'
punkt_sentences = result.read()

if not len(good_sentences) == len(punkt_sentences):
	print("source {0}, result {1}".format(len(good_sentences), len(punkt_sentences)))
	raise Exception("Panjang karakter kedua file berbeda.")

source.close()
result.close()

wb = xlwt.Workbook(encoding="utf8")
ws = wb.add_sheet("Sheet1")
heading = xlwt.XFStyle()
font = xlwt.Font()
font.bold = True
heading.font = font

ws.write(0, 0, label='nomor', style=heading)
ws.write(0, 1, label='kalimat asli', style=heading)
ws.write(0, 2, label='hasil punkt', style=heading)
err_count = 0
stc_start = 0
stc_end = 0
while stc_end != -1:
	stc_end = good_sentences.find('\n', stc_start)
	good_stc = good_sentences[stc_start : stc_end]
	punkt_stc = punkt_sentences[punkt_sentences.rfind('\n', 0, stc_start)+1 : punkt_sentences.find('\n', stc_end-1)]

	if good_stc != punkt_stc:
		err_count += 1
		print('-[{0}]---------------------------------------------'.format(err_count))
		print('\033[92m' + good_stc + '\033[0m')
		print('\033[91m' + punkt_stc + '\033[0m')
		print()
		ws.write(err_count, 0, label=err_count)
		ws.write(err_count, 1, label=good_stc)
		ws.write(err_count, 2, label=punkt_stc) #TODO: buat tanda kesalahan segmentasi
	stc_start = stc_end + 1

stc_count = good_sentences.count('\n')
err_rate = err_count / stc_count * 100
print("Total error {0} dari {1} kalimat ({2}%)".format(err_count, stc_count, err_rate))

cursor = err_count + 1
ws.write(cursor, 0, label='total error', style=heading)
ws.write(cursor, 1, label=err_count)
cursor += 1
ws.write(cursor, 0, label='jumlah kalimat', style=heading)
ws.write(cursor, 1, label=stc_count)
cursor += 1
ws.write(cursor, 0, label='persentase error (%)', style=heading)
ws.write(cursor, 1, label=err_rate)

wb.save('../res/punkt_error.xls')