# Todo List Application - Flask

Aplikasi Todo List sederhana yang dibangun menggunakan Flask dan MySQL. Aplikasi ini memungkinkan pengguna untuk membuat, membaca, memperbarui, dan menghapus task (tugas) dengan mudah.

## 📋 Deskripsi

Project ini adalah aplikasi web Todo List yang dibuat untuk memudahkan pengguna dalam mengelola tugas-tugas mereka. Aplikasi ini memiliki fitur CRUD (Create, Read, Update, Delete) lengkap untuk mengelola task dengan status (Pending atau Complete).

## ✨ Fitur-Fitur

### 1. **Menampilkan Semua Data Task (Index)**
   - Menampilkan daftar semua task yang ada dalam database
   - Menampilkan informasi: nomor urut, nama task, dan status task
   - Menyediakan tombol untuk menambah task baru, edit, dan delete
   - **Dikembangkan oleh: Khansa**

### 2. **Membuat Task Baru (Create)**
   - Form untuk menambahkan task baru
   - Input nama task
   - Pilihan status task (Pending/Complete)
   - **Dikembangkan oleh: Maya**

### 3. **Mengedit Task (Edit)**
   - Form untuk mengubah data task yang sudah ada
   - Dapat mengubah nama task dan status
   - Menggunakan ID task untuk mengidentifikasi task yang akan diedit
   - **Dikembangkan oleh: Kemal**

### 4. **Menghapus Task (Delete)**
   - Fitur untuk menghapus task dari database
   - Menggunakan ID task untuk mengidentifikasi task yang akan dihapus
   - **Dikembangkan oleh: Ardel**

### 5. **Frontend/UI**
   - Desain antarmuka yang user-friendly
   - Styling dengan CSS untuk pengalaman pengguna yang lebih baik
   - Layout responsif dengan navbar
   - **Dikembangkan oleh: Elang**

## 👥 Anggota Tim

| Nama | Kontribusi |
|------|------------|
| **Elang** | Frontend/UI Design |
| **Kemal** | Fitur Edit Task |
| **Ardel** | Fitur Delete Task |
| **Khansa** | Fitur Menampilkan Semua Data (Index) |
| **Maya** | Fitur Create Task |

## 🛠️ Teknologi yang Digunakan

- **Flask** - Web framework untuk Python
- **MySQL** - Database management system
- **Flask-MySQLdb** - Extension Flask untuk koneksi MySQL
- **Jinja2** - Template engine untuk Flask
- **HTML/CSS** - Untuk frontend

## 📦 Dependencies

Proyek ini menggunakan beberapa package Python yang tercantum dalam `requirements.txt`:

- Flask==3.1.2
- Flask-MySQLdb==2.0.0
- mysqlclient==2.2.7
- Jinja2==3.1.6
- Werkzeug==3.1.4

## 🚀 Instalasi dan Setup

### Prasyarat
- Python 3.x
- MySQL Server
- pip (Python package manager)

### Langkah-langkah

1. **Clone repository atau download project**
   ```bash
   cd project-uts-s1
   ```

2. **Buat virtual environment (opsional tapi disarankan)**
   ```bash
   python -m venv venv
   ```

3. **Aktifkan virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup Database MySQL**
   - Buat database baru dengan nama `db_todo_list`
   - Pastikan MySQL server sudah berjalan
   - Update konfigurasi database di `app.py` jika diperlukan:
     ```python
     app.config['MYSQL_HOST'] = "localhost"
     app.config['MYSQL_USER'] = "root"
     app.config['MYSQL_PASSWORD'] = ""  # Sesuaikan dengan password MySQL Anda
     app.config['MYSQL_DB'] = "db_todo_list"
     ```

6. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

7. **Buka browser dan akses**
   ```
   http://localhost:5000
   ```

## 📁 Struktur Project

```
project-uts-s1/
│
├── app.py                 # File utama aplikasi Flask
├── requirements.txt       # Daftar dependencies
├── README.md             # Dokumentasi project
│
├── templates/            # Folder template HTML
│   ├── index.html        # Halaman utama (menampilkan semua task)
│   ├── create.html       # Halaman form create task
│   ├── edit.html         # Halaman form edit task
│   └── layouts/
│       └── index.html    # Layout base untuk semua halaman
│
└── static/               # Folder untuk file statis (CSS, JS, images)
    └── style.css         # File stylesheet CSS
```

## 🔌 Endpoint/Routes

- `GET /` - Menampilkan semua task (Index page)
- `GET/POST /create` - Halaman dan form untuk membuat task baru
- `GET/POST /edit/<id>` - Halaman dan form untuk mengedit task berdasarkan ID
- `GET/POST /delete/<id>` - Endpoint untuk menghapus task berdasarkan ID

## 📝 Catatan

- Pastikan MySQL server sudah berjalan sebelum menjalankan aplikasi
- Sesuaikan konfigurasi database di `app.py` sesuai dengan setup MySQL Anda
- Disarankan untuk menggunakan virtual environment untuk menghindari konflik dependencies

---

**Project ini dibuat untuk keperluan UTS Pemrograman Dasar**

