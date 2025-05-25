# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institute

## Business Understanding
Jaya Jaya Institute merupakan institusi pendidikan tinggi keguruan yang telah beroperasi sejak tahun 2000. Institusi ini dikenal luas karena menerima siswa dari berbagai latar belakang. Jaya Jaya Institute menawarkan lebih dari 10 program studi serta menyediakan pilihan kelas pagi dan malam untuk menyesuaikan kebutuhan para mahasiswanya.


###  Permasalahan Bisnis

Jaya Jaya Institute tengah menghadapi permasalahan bisnis berupa tingginya angka putus studi, di mana banyak siswa tidak menyelesaikan pendidikan mereka. Tingginya dropout rate ini dipengaruhi oleh banyaknya jurusan yang perlu diawasi serta berbagai faktor lainnya. Oleh karena itu, pihak institusi berupaya untuk mengidentifikasi penyebab utama dari permasalahan ini guna mengurangi risiko terjadinya putus studi di masa mendatang.

Proyek ini bertujuan menjawab pertanyaan-pertanyaan berikut:

- Apa saja faktor-faktor yang memengaruhi tingginya angka putus studi di Jaya Jaya Institute?

- Bagaimana cara menyajikan hasil analisis data dropout secara informatif dan interaktif menggunakan dashboard Metabase?

- Bagaimana membangun model machine learning sederhana yang mampu memprediksi kemungkinan dropout siswa dan mengimplementasikannya melalui platform Streamlit?

###  Cakupan Proyek

Untuk menjawab permasalahan di atas, ruang lingkup proyek ini mencakup:

- Mengidentifikasi dan menganalisis faktor-faktor yang memengaruhi tingginya angka putus studi.
- Merancang dan membangun dashboard interaktif menggunakan Metabase untuk menyajikan hasil analisis dan prediksi.
- Mengembangkan model machine learning sederhana untuk melakukan prediksi dan mengimplementasikannya melalui platform Streamlit.


### Persiapan

* **Sumber Data**: Dataset Mahasiswa (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)
*Dataset ini memiliki kolom-kolom seperti Status, Course/Jurusan,Attendance Time/Tipe jurusan, dan berbagai informasi lain mengenai karakteristik mahasiswa.


* **Lingkungan Pengembangan**:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn sqlalchemy python-dotenv psycopg2-binary imbalanced-learn
```

| Library            | Deskripsi                                                       |
| ------------------ | --------------------------------------------------------------- |
| `pandas`           | Mengelola data dalam bentuk tabel (dataframe).                  |
| `numpy`            | Operasi numerik dan array.                                      |
| `matplotlib`       | Visualisasi data dasar.                                         |
| `seaborn`          | Visualisasi statistik yang menarik.                             |
| `scikit-learn`     | Pembuatan dan evaluasi model machine learning.                  |
| `sqlalchemy`       | Koneksi ke database dan ORM (termasuk koneksi ke Metabase).     |
| `python-dotenv`    | Pengelolaan variabel lingkungan dari file `.env`.               |
| `psycopg2-binary`  | Adapter PostgreSQL untuk Python.                                |
| `imbalanced-learn` | Penanganan dataset yang tidak seimbang (misalnya dengan SMOTE). |

---

##  Dashboard Bisnis

![Dashboard](https://github.com/makiatulmsyr17/asets/raw/main/makiatulmsyr17-dashboard.jpg)
Link Akses Dashboard : http://localhost:3000/public/dashboard/de5b61a5-9dbd-4503-aabe-9213f5ec6521 

**Dashboard** dikembangkan menggunakan Metabase dan terhubung ke database PostgreSQL di Supabase.

Dashboard ini menyajikan tampilan interaktif mengenai faktor-faktor penyebab tingginya angka Dropout Mahasiswa.

Dengan menggunakan model khusus, enam visualisasi utama dikembangkan untuk membantu Dosen:

### 1. Tingkat Dropout Mahasiswa

- Total Mahasiswa: 3.630
- Lulus (Graduate): 60,9% (±2.213 mahasiswa)
- Dropout: 39,1% (±1.417 mahasiswa)

Proporsi mahasiswa yang dropout cukup tinggi, yaitu hampir 4 dari 10 mahasiswa tidak menyelesaikan pendidikannya. Ini menunjukkan adanya permasalahan serius yang perlu diinvestigasi lebih dalam.


### 2. Jumlah Scholarship Holder Berdasrkan Mahasiswa Dropout

Grafik menunjukkan bahwa mayoritas mahasiswa dropout bukan penerima beasiswa (Scholarship Holder = 0). Hanya sebagian kecil dari mahasiswa dropout yang menerima beasiswa (Scholarship Holder = 1).

Hal ini menandakan bahwa  beasiswa terbukti membantu mencegah dropout — perbanyak dan arahkan ke yang benar-benar membutuhkan.

### 3.Jumlah Gender Berdasarkan Mahasiswa Dropout
Grafik menunjukkan bahwa jumlah mahasiswa dropout antara gender Perempuan dan laki laki hampir seimbang.


### 4. Jumlah Debtor Berdasarkan Status Dropout
Grafik menunjukkan bahwa mahasiswa yang bukan debitur (kode 0) jauh lebih banyak mengalami dropout dibandingkan yang debitur (kode 1). Artinya, memiliki pinjaman pendidikan (debtor) justru berkorelasi dengan kemungkinan lebih rendah untuk dropout.

### 5. Jumlah Age At Enrollment Berdasarkan Status Dropout
Grafik menunjukkan bahwa dropout paling banyak terjadi pada usia 15–22.5 tahun saat pendaftaran. Semakin bertambah usia saat mendaftar, jumlah dropout semakin menurun drastis.

### 6.Jumlah Admission Grade Berdasarkan Status Dropout
Grafik menunjukkan bahwa mahasiswa dengan nilai masuk (admission grade) 120–140 memiliki jumlah dropout terbanyak. Sementara itu, mahasiswa dengan nilai lebih tinggi (di atas 160) cenderung sangat sedikit yang dropout.

---


## Menjalankan Sistem Machine Learning
Model: Random Forest Classifier
Berikut adalah tampilan dari app yang telah dibuat:

![App Preview](https://raw.githubusercontent.com/makiatulmsyr17/asets/main/Screenshot%202025-05-24%20115556.png)


**Cara Menjalankan Prototype Sistem Machine Learning:**

1. **Akses Halaman Prototype:**
   - Buka tautan yang telah disediakan untuk sistem prediksi dropout mahasiswa.

2. **Isi Formulir Data Mahasiswa:**
   - Masukkan informasi yang diperlukan sesuai dengan kolom yang tersedia:
     - **Status Pernikahan:** Pilih status (Single/Married).
     - **Urutan Pilihan Program Studi:** Masukkan angka antara 1 hingga jumlah program studi yang ada.
     - **Nilai Penerimaan (0-200):** Masukkan nilai keberhasilan penerimaan.
     - **Apakah Mahasiswa Terlantar?:** Pilih “Yes” atau “No”.
     - **Apakah Mahasiswa Memiliki Hutang?:** Pilih “Yes” atau “No”.
     - **Jenis Kelamin:** Pilih antara Male atau Female.
     - **Penerima Beasiswa?:** Pilih “Yes” atau “No”.
     - **Usia Saat Masuk Kuliah:** Masukkan usia mahasiswa.

3. **Lakukan Prediksi:**
   - Setelah semua data diisi, klik tombol **“Make Prediction”** untuk mendapatkan hasil prediksi apakah mahasiswa akan dropout atau lulus.

**Link Akses Prototype:**
- [Student Dropout Prediction](#) *https://student-dropout-prediction2.streamlit.app/*

Silakan mengisi data sesuai dengan kasus yang ingin diprediksi dan tekan tombol untuk melihat hasil prediksinya. Pastikan semua data diisi dengan benar untuk akurasi yang lebih tinggi.


- Jalankan Streamlit
Untuk menjalankan file `app.py` dengan **Streamlit**, ikuti langkah-langkah berikut di terminal (Command Prompt, Anaconda Prompt, atau terminal VS Code):


---
 ### **Aktifkan environment (jika pakai Anaconda/Miniconda)**

Misal environment-nya bernama `streamlit`, maka:

```bash
conda activate streamlit
```

Atau kalau pakai virtualenv:

```bash
source nama_env/bin/activate  # di Linux/Mac
.\nama_env\Scripts\activate   # di Windows
```

---

### **Jalankan Streamlit**

```bash
streamlit run app.py
```

---

### **Akses di Browser**

Setelah dijalankan, akan muncul link seperti:

```
Local URL: http://localhost:8501



```






## **Conclusion**

Berdasarkan data dari 3.630 mahasiswa, tingkat **dropout tergolong tinggi (39,1%)**, yang menunjukkan adanya masalah sistemik yang perlu segera ditindaklanjuti. Beberapa temuan penting meliputi:

1. **Penerima Beasiswa Dropout Lebih Sedikit**
   Beasiswa memiliki peran signifikan dalam mencegah dropout.

2. **Dropout Merata antara Gender**
   Tidak ada perbedaan signifikan antara laki-laki dan perempuan dalam hal dropout.

3. **Mahasiswa Bukan Debitur Lebih Banyak Dropout**
   Mahasiswa dengan pinjaman pendidikan cenderung lebih bertanggung jawab atau termotivasi untuk menyelesaikan studi.

4. **Dropout Banyak Terjadi di Usia Muda (15–22,5 tahun)**
   Mahasiswa yang mendaftar di usia muda lebih rentan untuk dropout, kemungkinan karena ketidaksiapan mental atau akademik.

5. **Dropout Tinggi pada Mahasiswa dengan Nilai Masuk 120–140**
   Menunjukkan bahwa nilai akademik awal berkorelasi dengan keberlangsungan studi.

---

## **Rekomendasi Action Items (Optional)**

 1. **Perluasan dan Penargetan Program Beasiswa**

* Fokuskan pemberian beasiswa pada mahasiswa dengan risiko tinggi dropout (misalnya dari keluarga tidak mampu atau dengan admission grade menengah ke bawah).
* Evaluasi dan perluas skema beasiswa berbasis kebutuhan (need-based scholarship).

2. **Penguatan Dukungan Akademik dan Psikologis**

* Adakan **program pendampingan (mentoring)** khusus bagi mahasiswa baru terutama di usia <23 tahun.
* Sediakan **layanan konseling dan pengembangan keterampilan belajar** sejak awal perkuliahan.

3. **Program Penguatan Mahasiswa dengan Admission Grade Rendah–Menengah**

* Wajibkan mahasiswa dengan nilai masuk 100–140 untuk mengikuti **kelas remedial, bimbingan belajar, atau bootcamp akademik**.
* Lakukan evaluasi berkala terhadap performa akademik mereka.

4. **Studi Lanjutan Terhadap Faktor Non-Akademik**

* Lakukan survei terhadap mahasiswa dropout untuk mengidentifikasi faktor-faktor non-akademik lain seperti motivasi, lingkungan sosial, atau masalah ekonomi.

5. **Pemanfaatan Skema Pinjaman Pendidikan yang Lebih Luas**

* Edukasi dan perluas akses terhadap **skema pinjaman pendidikan (debtor program)** karena terbukti membantu keberlangsungan studi mahasiswa.



# Membuat dan mengaktivkan Virtual Environment

### 1. **Buat Virtual Environment**

```bash
python -m venv env
```

* `env` adalah nama folder virtual environment (boleh diganti).
2. **Aktifkan Virtual Environment**

```bash
.\env\Scripts\activate
```


## Setelah Aktivasi

Setelah aktif, bisa menginstal dependensi seperti:

```bash
pip install -r requirements.txt
```






