# ⚗️ ChemCompat — Pemeriksa Kompatibilitas Bahan Kimia

Aplikasi web berbasis Streamlit untuk memeriksa **kompatibilitas penyimpanan** antara dua bahan kimia secara aman.

## Fitur Utama

- 🔍 **Cek Kompatibilitas** — Pilih 2 bahan kimia dan lihat apakah aman disimpan bersama
- ❤️ **Favorit** — Simpan bahan kimia yang sering digunakan (tersimpan permanen)
- 🏷️ **Simbol GHS** — Tampil visual lengkap dengan SVG inline (tidak bergantung gambar eksternal)
- ⚠️ **Rekomendasi Penyimpanan** — Saran praktis berdasarkan level bahaya (AMAN / PERHATIAN / BERBAHAYA)
- 📊 **Perbandingan Sifat Fisik** — Titik didih, pH, densitas, dll

## Cara Menjalankan Lokal

### 1. Clone repositori
```bash
git clone https://github.com/USERNAME/chemcompat.git
cd chemcompat
```

### 2. Buat virtual environment (opsional tapi disarankan)
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Install dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi
```bash
streamlit run app.py
```

Buka browser di `http://localhost:8501`

---

## Deploy ke Streamlit Community Cloud

1. Push kode ini ke repositori GitHub Anda
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Klik **"New app"**
4. Pilih repositori dan set **Main file path** ke `app.py`
5. Klik **Deploy**

> **Catatan:** Fitur favorit menggunakan `favorites.json` yang tersimpan di server. Di Streamlit Cloud, file ini akan reset saat app di-restart. Untuk penyimpanan permanen, gunakan `st.session_state` atau integrasi database eksternal.

---

## Struktur File

```
chemcompat/
├── app.py                  # Aplikasi utama Streamlit
├── requirements.txt        # Dependensi Python
├── favorites.json          # Data favorit (auto-dibuat)
├── data/
│   ├── chemicals.py        # Database bahan kimia
│   └── compatibility.py    # Matriks kompatibilitas
└── utils/
    ├── ghs.py              # Render simbol GHS (SVG)
    └── storage.py          # Simpan/load favorit
```

## Menambah Bahan Kimia Baru

Edit `data/chemicals.py` dan tambahkan entri baru:

```python
{
    "id": 13,
    "name": "Nama Bahan",
    "formula": "Formula",
    "cas": "CAS-number",
    "mw": "...", "bp": "...", "mp": "...", "density": "...", "ph": "...",
    "state": "...", "color": "...", "category": "...",
    "ghs": ["GHS02"],          # Kode GHS yang berlaku
    "hazards": [...],
    "ppe": [...],
    "storage": "...",
    "firstaid": "...",
    "storage_group": "FLAMMABLE"  # ACID | BASE | OXIDIZER | FLAMMABLE | SALT | dll
}
```

## Menambah Data Kompatibilitas

Edit `data/compatibility.py`:

```python
"ID_A-ID_B": {
    "level": "BERBAHAYA",       # AMAN | PERHATIAN | BERBAHAYA
    "summary": "Penjelasan singkat...",
    "risks": ["Risiko 1", "Risiko 2"],
    "storage_recommendations": ["Saran 1", "Saran 2"],
    "emergency_note": "Catatan darurat (atau None)"
}
```

---

## Lisensi

MIT License — bebas digunakan dan dimodifikasi.
