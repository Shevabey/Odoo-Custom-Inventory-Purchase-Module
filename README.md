# Odoo Custom Inventory & Purchase Module (`autodidak_purchase`)

Proyek ini merupakan pengembangan modul kustom pada Odoo 14 yang berfokus pada integrasi dan kustomisasi alur bisnis **Inventory** dan **Pembelian (Purchase)**. Modul ini menyertakan model data kustom, logika bisnis dinamis, pengaturan hak akses, serta fungsionalitas ekspor laporan ke format Microsoft Excel (`.xlsx`).

---

## 🚀 Fitur Utama

- **Model Data & Relasi Kustom**: Pembuatan field kustom (`Char`, `Integer`, `Many2one`, `One2many`) yang dipetakan sesuai kebutuhan alur bisnis.
- **Logika Bisnis Dinamis**: Implementasi `computed fields` untuk kalkulasi otomatis serta decorator `@api.onchange` untuk responsivitas form interface.
- **Manajemen Hak Akses Security**: Konfigurasi tingkat keamanan grup pengguna dan kontrol akses model melalui `ir.model.access.csv`.
- **Laporan Kustom Excel (.xlsx)**: Pengolahan dan ekstraksi data dari database Odoo ke laporan spreadsheet interaktif menggunakan library `XlsxWriter` / `report_xlsx`.
- **Pengaturan Modul Terstruktur**: Arsitektur direktori custom addons yang terpisah rapi dari core source Odoo.

---

## 🛠️ Tech Stack & Prerequisites

- **ERP Core**: Odoo 14
- **Programming Language**: Python 3.8+
- **Database**: PostgreSQL 12+
- **Frontend / View**: XML, Odoo QWeb
- **Reporting Library**: `XlsxWriter`, `report_xlsx`

---

## 📥 Panduan Instalasi & Setup

### 1. Clone Repositori

Buka terminal / command prompt, masuk ke direktori ruang kerja kamu, lalu jalankan perintah:

```bash
git clone https://github.com/Shevabey/Odoo-Custom-Inventory-Purchase-Module.git
```

### 2. Persiapan Virtual Environment & Dependency

Pastikan environment Python untuk Odoo sudah aktif, lalu install dependency tambahan untuk pendukung ekspor Excel:

```bash
pip install XlsxWriter
```

### 3. Konfigurasi File `odoo_config.conf`

Buat atau sesuaikan file konfigurasi Odoo kamu (`odoo_config.conf`). Kamu dapat menggunakan template di bawah ini dengan menyesuaikan jalur direktori (`addons_path`), kredensial PostgreSQL (`db_user`, `db_password`), serta direktori log.

```ini
[options]
; Sesuaikan addons_path sesuai lokasi penyimpanan source Odoo dan modul kustom kamu
addons_path = C:\path\to\odoo14\odoo\addons, C:\path\to\odoo14\modul_custom

csv_internal_sep = ,
db_host = localhost
db_maxconn = 512
db_port = 5432
db_user = postgres_user
db_password = postgres_password
db_name = db_odoo

pg_path = C:\Program Files\PostgreSQL\17\bin
logfile = C:\path\to\odoo14\odoo.log

log_db = False
log_db_level = warning
log_handler = :INFO
log_level = info

xmlrpc = True
xmlrpc_interface = 
xmlrpc_port = 8088
longpolling_port = 8088

limit_time_cpu = 3600
limit_time_real = 1200
max_cron_threads = 1
workers = 0
syslog = False
```

---

## ⚙️ Cara Menjalankan & Menginstal Modul

Jalankan perintah berikut pada terminal di dalam direktori utama Odoo kamu untuk memperbarui list modul dan menginstal/memperbarui modul `autodidak_purchase`:

```bash
python odoo-bin -c odoo_config.conf -u autodidak_purchase
```

### Penjelasan Perintah:
- `-c odoo_config.conf`: Menggunakan file konfigurasi Odoo yang telah ditentukan.
- `-u autodidak_purchase`: Melakukan update/install secara langsung pada modul `autodidak_purchase`.

---
