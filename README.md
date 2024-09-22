## Nama Kelompok  
Muhammad Hafiz Dicky Putra (L0123096)  
Nadzira Rifqi Amin Rinawan (L0123104)  

### Apa itu 20 Solver?
20 Solver adalah program yang dirancang untuk menemukan semua kemungkinan kombinasi operasi matematika yang dapat menghasilkan nilai 20. Program ini menggunakan empat angka yang dimasukkan oleh pengguna, serta berbagai kombinasi dari empat operasi aritmatika dasar (penjumlahan +, pengurangan -, perkalian *, pembagian /), dan juga tanda kurung () untuk menentukan urutan operasi. Program ini menguji setiap kombinasi yang memungkinkan di antara angka-angka dan operasi tersebut.
  
### Penjelasan Singkat tentang Program
#### Memasukkan Input
Pengguna memasukkan input dari form di halaman web 'index.html' yang nanti akan diambil oleh 'brute_20solver.py'
#### Mencari Kombinasi
Program mengambil angka-angka yang dimasukkan dan membuat semua permutasi dari angka-angka tersebut. Permutasi ini adalah semua kemungkinan urutan dari empat angka yang berbeda.  
  
Program juga menghasilkan kombinasi operasi dengan mencoba berbagai kombinasi dari empat operasi matematika (+, -, *, /). Untuk setiap kombinasi, program menghasilkan tiga operator yang ditempatkan di antara angka-angka.
#### Menggunakan Template Operasi
Di dalam program, sudah disiapkan segala kemungkinan ekspresi yang bisa dibentuk dari kelima operasi tersebut dengan menyisipkan tanda kurung (). Contohnya seperti :  
  
"{a} {op1} {b} {op2} {c} {op3} {d}"  
"({a} {op1} {b}) {op2} ({c} {op3} {d})"  
"(({a} {op1} {b}) {op2} {c}) {op3} {d}",  
"({a} {op1} ({b} {op2} {c})) {op3} {d}",  
"{a} {op1} (({b} {op2} {c}) {op3} {d})",  
"{a} {op1} ({b} {op2} ({c} {op3} {d}))"  

#### Menghitung Operasi
Program menggunakan eval() untuk mengevaluasi ekspresi matematika yang dihasilkan dari kombinasi angka, operator, dan template.Setiap ekspresi diuji apakah menghasilkan nilai 20.  
Jika hasilnya adalah 20, ekspresi tersebut dianggap sebagai solusi dan disimpan dalam kumpulan solusi unik (unique_solutions).

#### Menampilkan Hasil
Setelah semua kombinasi angka dan operasi diuji, hasil berupa daftar solusi yang valid dikirim ke template 'result.html'.
  
### Contoh Pengujian
Jika pengguna memasukkan angka 5, 5, 5, 1, program akan memeriksa semua kombinasi dari angka-angka ini dengan operasi +, -, *, /, serta urutan operasi menggunakan tanda kurung. Misalnya, salah satu ekspresi yang dihasilkan adalah:  
  
__|(5-1)*5-5 = 20|__

  
### Link Pengumpulan
link deploy : https://20solver.pythonanywhere.com/  
link video : 
