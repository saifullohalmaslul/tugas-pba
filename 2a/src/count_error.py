from xlwt import Workbook, Worksheet

source = open("../res/sentences.txt", "r")
result = open("../res/segmented.txt", "r")

good_sentences = source.read()
punkt_sentences = result.read()

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
for char in good_sentences:
	stc_end += 1
	if char == '\n':
		good_stc = good_sentences[stc_start:stc_end]
		punkt_stc = punkt_sentences[stc_start:stc_end]
		if good_stc != punkt_stc:
			err_count += 1
			ws.write(err_count, 0, label=err_count)
			ws.write(err_count, 1, label=good_stc.rstrip())
			ws.write(err_count, 2, label=punkt_stc.rstrip())
		stc_start = stc_end

wb.save('../res/punkt_error.xls')