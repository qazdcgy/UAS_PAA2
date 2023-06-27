# UAS PAA2
##  Analisis Algoritma Bubble Sort dan Insertion Sort
#### Bubble Sort

Worst Case
Worst case terjadi ketika daftar yang diurutkan dalam urutan terbalik. Pada kasus ini, Bubble Sort harus melalui seluruh perulangan dan melakukan pertukaran pada setiap langkahnya. Jadi, jumlah perbandingan dan pertukaran yang dilakukan adalah maksimum.

##### Kompleksitas Worst Case:

- Perbandingan: `O(n^2)`
- Pertukaran: `O(n^2)`

Best Case
Best case terjadi ketika daftar sudah terurut dengan benar. Pada kasus ini, Bubble Sort akan melalui seluruh perulangan, tetapi tidak akan melakukan pertukaran karena daftar sudah terurut. Meskipun demikian, algoritma ini tidak memiliki optimasi khusus untuk mengenali keadaan terurut dan menghentikan prosesnya.

##### Kompleksitas Best Case:

- Perbandingan: `O(n)`
- Pertukaran: `O(1)`

Average Case
Rata-rata kasus terjadi ketika elemen-elemen dalam daftar memiliki urutan acak. Pada kasus ini, Bubble Sort harus melalui beberapa perulangan dan melakukan pertukaran untuk memastikan seluruh daftar terurut.

##### Kompleksitas Average Case:

- Perbandingan: `O(n^2)`
- Pertukaran: `O(n^2)`

#### Insertion Sort


Worst Case
Worst case terjadi ketika daftar yang diurutkan dalam urutan terbalik. Pada kasus ini, Insertion Sort harus memindahkan setiap elemen ke posisi yang benar dalam bagian terurut. Jadi, setiap iterasi akan melibatkan perbandingan dan pergeseran elemen.

##### Kompleksitas Worst Case:

- Perbandingan: `O(n^2)`
- Pergeseran: `O(n^2)`

Best Case
Best case terjadi ketika daftar sudah terurut dengan benar. Pada kasus ini, Insertion Sort hanya perlu membandingkan setiap elemen dengan elemen sebelumnya dan tidak perlu melakukan pergeseran.

##### Kompleksitas Best Case:

- Perbandingan: `O(n)`
- Pergeseran: `O(1)`

Average Case
Rata-rata kasus terjadi ketika elemen-elemen dalam daftar memiliki urutan acak. Pada kasus ini, Insertion Sort harus memindahkan beberapa elemen untuk menyisipkannya ke posisi yang benar dalam bagian terurut.

##### Kompleksitas Average Case:

- Perbandingan: `O(n^2)`
- Pergeseran: `O(n^2)`

## Analisis Algoritma TSP dan Dijkstra
#### TSP (Travelling Salesman Problem)

Worst Case
Worst case dalam TSP terjadi ketika setiap simpul terhubung langsung dengan semua simpul lainnya. Pada kasus ini, TSP harus mengunjungi setiap simpul tepat sekali sebelum kembali ke simpul awal. Solusi TSP ini memiliki kompleksitas eksponensial, sehingga waktu eksekusi akan meningkat secara signifikan dengan jumlah simpul yang bertambah.

##### Kompleksitas Worst Case:

- Waktu: `O(n!)`
- Ruang: `O(n)`

Best Case
Best case dalam TSP terjadi ketika graf memiliki sedikit simpul atau jika simpul-simpulnya terisolasi sehingga tidak ada koneksi langsung antara simpul-simpul tersebut. Dalam kasus ini, TSP tidak perlu melakukan perjalanan jauh dan solusi terbaiknya adalah mengunjungi setiap simpul secara berurutan. Namun, TSP masih memiliki kompleksitas waktu yang eksponensial, meskipun lebih sedikit dibandingkan dengan worst case.

##### Kompleksitas Best Case:

- Waktu: `O(n!)`
- Ruang: `O(n)`

Average Case
Rata-rata kasus dalam TSP terjadi ketika simpul-simpul dalam graf terhubung secara acak. Dalam kasus ini, TSP harus memeriksa berbagai kemungkinan perjalanan dan memilih jalur terpendek. Solusi TSP ini memiliki kompleksitas waktu yang eksponensial, sehingga waktu eksekusi akan meningkat secara signifikan dengan jumlah simpul yang bertambah.

##### Kompleksitas Average Case:

- Waktu: `O(n!)`
- Ruang: `O(n)`

#### Dijkstra

Worst Case
Worst case dalam Dijkstra terjadi ketika semua simpul terhubung langsung dengan simpul awal dan memiliki bobot yang berbeda. Pada kasus ini, Dijkstra harus memperbarui estimasi jarak terpendek pada setiap iterasi untuk semua simpul, termasuk simpul yang telah dikunjungi sebelumnya. Waktu eksekusi Dijkstra dalam worst case akan meningkat secara linier dengan jumlah simpul dalam graf.

#### Kompleksitas Worst Case:

- Waktu: `O(|V|^2 + |E|)`
- Ruang: `O(|V|)`

Best Case
Best case dalam Dijkstra terjadi ketika semua simpul terhubung langsung dengan simpul awal dan memiliki bobot yang sama. Dalam kasus ini, Dijkstra hanya perlu memeriksa setiap simpul sekali dan memperbarui estimasi jarak terpendek jika ditemukan jalur yang lebih pendek. Waktu eksekusi Dijkstra dalam best case akan meningkat secara linier dengan jumlah simpul dalam graf.

##### Kompleksitas Best Case:

- Waktu: `O(|V|^2 + |E|)`
- Ruang: `O(|V|)`

Average Case
Rata-rata kasus dalam Dijkstra terjadi ketika bobot-bobot pada simpul dan tepi dalam graf berbobot memiliki distribusi acak. Dalam kasus ini, Dijkstra harus memeriksa setiap simpul dan memperbarui estimasi jarak terpendek sesuai dengan kondisi yang ditemui. Waktu eksekusi Dijkstra dalam average case akan meningkat secara linier dengan jumlah simpul dalam graf.

##### Kompleksitas Average Case:

- Waktu: `O(|V|^2 + |E|)`
- Ruang: `O(|V|)

##### **Developer Info**
File README.md di GitHub ini dikembangkan oleh:

- Nama: Wahyudi. Z
- NIM: F55121078
- Email: newbie2345@gmail.com

Jika Anda memiliki pertanyaan atau masukan terkait file ini, silakan hubungi developer melalui email yang tertera di atas.
