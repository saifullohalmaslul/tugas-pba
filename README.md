# Tugas 2 Pemrosesan Bahasan Alami

## What's this
2a adalah program yang akan melakukan proses segmentasi kalimat, dan juga membuat sebuah file excel yang akan memberitahu pengguna tentang total kesalahan segmentasi.
2b adalah program yang akan melakukan *stemming*, sebuah proses dimana kata pada setiap line akan dideteksi dan dirubah menjadi kata dasar (jika kata tersebut belum dasar).

## How to use
### 2a
Pada folder src, jalankan `seg_punkt.py` terlebih dahulu, ini akan membuat file baru yang berisi hasil segmentasi kalimat otomatis. Input file bisa dirubah dengan mengedit *source code*. Lalu jalankan `count_error.py` untuk membuat file excel yang berisi jumlah error. Kedua file output ini akan disimpan pada folder res.
#### Dependency
- NLTK
- xlwt
`pip install NLTK xlwt`

### 2b
Pada folder src, akan terdapat dua file. Dua file ini bisa dijalankan pada urutan manapun. Sebelum menjalankan program, siapkan sebuah file text yang akan dibaca. Lalu jalankan

`python <nama_program> <direktori_text_file>`

Untuk mempermudah, masukan file text dalam folder yang sama.

 `stemming.py` akan menjalanakan proses stemming tanpa menggunakan proses multiprocessing, sementara `multiprocess-stemming.py` akan menjalankannya dengan multiprocessing.

#### Dependency
- Sastrawi
`pip install Sastrawi`
