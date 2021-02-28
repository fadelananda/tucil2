# Tugas Kecil 2 IF-2211 Strategi Algoritma

## Penjelasan Singkat Algoritma yang Diimplementasikan
Program yang dibuat akan menyelesaikan salah satu permasalahan pengambilan mata kuliah dengan menggunakan algoritma Topological Sort. Algoritma yang dipakai yaitu membuat list of simpul utama, simpul yang bersesuaian, dan derajat dari setiap simpul. Algoritma topological sort akan diimplementasi selama jumlah elemen pada list utama belum kosong. Algoritma topological sort memiliki mekanisme mencari semua simpul yang berderajat nol kemudian memasukkannya ke dalam list solusi. Kemudian list solusi ini akan digunakan untuk menghapus list simpul utama dan simpul yang bersesuaian. Kemudian list jumlah derajat masuk akan disesuaikan dengan list simpul yang bersesuaian. List solusi ini kemudian akan ditampilkan ke layar dan loop while akan diulangi lagi sampai jumlah elemen list simpul utama sama dengan nol.

## Requirement Program
- Python 3.8.2

## Cara Menggunakan Program
1. Buatlah sebuah test case dalam bentuk file .txt yang berisi daftar mata kuliah beserta prasyaratnya
2. Masukkan test case tersebut ke dalam folder test yang ada
3. Masuklah ke dalam folder bin atau src kemudian buka terminal yang anda pakai (disarankan menggunakan terminal linux atau ubuntu)
4. Ketikkan perintah 'python3 13519146.py' atau jika tidak bisa 'py 13519146.py'
5. Masukkan nama file .txt yang ada buat (misal 'graph1.txt') kemudian klik enter
6. Tunggu hingga selesai melakukan eksekusi

## Author
Fadel Ananda D. / 13519146