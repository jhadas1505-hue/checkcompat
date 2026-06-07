CHEMICALS = [
    {
        "id": 1, "name": "Asam Sulfat", "formula": "H₂SO₄", "cas": "7664-93-9",
        "mw": "98.08 g/mol", "bp": "337°C", "mp": "-10°C", "density": "1.84 g/cm³", "ph": "<1",
        "state": "Cair", "color": "Tidak berwarna", "category": "Asam Kuat",
        "ghs": ["GHS05", "GHS08"],
        "hazards": [
            {"type": "danger", "text": "Korosif kuat — menyebabkan luka bakar parah pada kulit dan mata"},
            {"type": "danger", "text": "Berbahaya jika tertelan atau terhirup"},
            {"type": "warning", "text": "Reaksi eksotermik kuat dengan air"},
        ],
        "ppe": ["Kacamata pelindung", "Sarung tangan nitril", "Jas lab", "Pelindung wajah"],
        "storage": "Simpan di tempat dingin, kering, terventilasi. Jauhkan dari bahan organik dan logam.",
        "firstaid": "Jika terkena kulit: bilas dengan air mengalir min. 20 menit. Segera cari pertolongan medis.",
        "storage_group": "ACID"
    },
    {
        "id": 2, "name": "Natrium Klorida", "formula": "NaCl", "cas": "7647-14-5",
        "mw": "58.44 g/mol", "bp": "1413°C", "mp": "801°C", "density": "2.17 g/cm³", "ph": "~7",
        "state": "Padat (kristal)", "color": "Putih", "category": "Garam",
        "ghs": [],
        "hazards": [
            {"type": "info", "text": "Tidak diklasifikasikan berbahaya dalam penggunaan normal"},
        ],
        "ppe": ["Sarung tangan (opsional)", "Kacamata pelindung jika bubuk"],
        "storage": "Simpan di tempat kering, jauhkan dari kelembaban.",
        "firstaid": "Jika terkena mata: bilas dengan air. Tidak memerlukan penanganan khusus.",
        "storage_group": "SALT"
    },
    {
        "id": 3, "name": "Natrium Hidroksida", "formula": "NaOH", "cas": "1310-73-2",
        "mw": "40.00 g/mol", "bp": "1388°C", "mp": "318°C", "density": "2.13 g/cm³", "ph": ">13",
        "state": "Padat / Larutan", "color": "Putih / Tidak berwarna", "category": "Basa Kuat",
        "ghs": ["GHS05", "GHS07"],
        "hazards": [
            {"type": "danger", "text": "Korosif kuat — menyebabkan luka bakar parah"},
            {"type": "warning", "text": "Higroskopis — menyerap kelembaban dari udara"},
        ],
        "ppe": ["Kacamata pelindung", "Sarung tangan karet", "Jas lab", "Pelindung wajah"],
        "storage": "Simpan tertutup rapat di tempat kering. Jauhkan dari asam.",
        "firstaid": "Jika terkena kulit/mata: bilas dengan air mengalir min. 20 menit.",
        "storage_group": "BASE"
    },
    {
        "id": 4, "name": "Etanol", "formula": "C₂H₅OH", "cas": "64-17-5",
        "mw": "46.07 g/mol", "bp": "78.4°C", "mp": "-114.1°C", "density": "0.789 g/cm³", "ph": "~7",
        "state": "Cair", "color": "Tidak berwarna", "category": "Pelarut Organik",
        "ghs": ["GHS02", "GHS07"],
        "hazards": [
            {"type": "danger", "text": "Mudah terbakar — titik nyala 13°C"},
            {"type": "warning", "text": "Menyebabkan iritasi mata"},
        ],
        "ppe": ["Sarung tangan nitril", "Kacamata pelindung", "Tidak boleh ada api terbuka"],
        "storage": "Simpan di tempat dingin, terventilasi, jauh dari nyala api dan panas.",
        "firstaid": "Jika terhirup: pindahkan ke udara segar.",
        "storage_group": "FLAMMABLE"
    },
    {
        "id": 5, "name": "Asam Klorida", "formula": "HCl", "cas": "7647-01-0",
        "mw": "36.46 g/mol", "bp": "-85°C (gas)", "mp": "-114°C (gas)", "density": "1.19 g/cm³", "ph": "<1",
        "state": "Gas / Larutan", "color": "Tidak berwarna", "category": "Asam Kuat",
        "ghs": ["GHS05", "GHS07"],
        "hazards": [
            {"type": "danger", "text": "Korosif — menyebabkan luka bakar pada kulit dan mata"},
            {"type": "danger", "text": "Uap berbahaya jika terhirup"},
        ],
        "ppe": ["Kacamata pelindung", "Sarung tangan PVC", "Jas lab", "Lemari asam"],
        "storage": "Simpan di lemari asam yang terventilasi. Jauhkan dari basa, oksidator, dan logam.",
        "firstaid": "Jika terhirup: pindahkan ke udara segar. Jika terkena kulit: bilas 15 menit.",
        "storage_group": "ACID"
    },
    {
        "id": 6, "name": "Aseton", "formula": "C₃H₆O", "cas": "67-64-1",
        "mw": "58.08 g/mol", "bp": "56°C", "mp": "-95°C", "density": "0.784 g/cm³", "ph": "~7",
        "state": "Cair", "color": "Tidak berwarna", "category": "Pelarut Organik",
        "ghs": ["GHS02", "GHS07"],
        "hazards": [
            {"type": "danger", "text": "Sangat mudah terbakar — titik nyala -20°C"},
            {"type": "warning", "text": "Menyebabkan iritasi mata dan saluran pernapasan"},
        ],
        "ppe": ["Sarung tangan nitril", "Kacamata pelindung", "Tidak ada nyala api"],
        "storage": "Simpan di tempat dingin, terventilasi, dalam wadah tertutup rapat.",
        "firstaid": "Jika terhirup: pindahkan ke udara segar. Jika terkena mata: bilas dengan air.",
        "storage_group": "FLAMMABLE"
    },
    {
        "id": 7, "name": "Ammonia", "formula": "NH₃", "cas": "7664-41-7",
        "mw": "17.03 g/mol", "bp": "-33°C", "mp": "-77.7°C", "density": "0.73 g/L", "ph": ">11",
        "state": "Gas / Larutan", "color": "Tidak berwarna", "category": "Gas / Basa",
        "ghs": ["GHS02", "GHS06", "GHS05", "GHS09"],
        "hazards": [
            {"type": "danger", "text": "Gas beracun — berbahaya jika terhirup"},
            {"type": "danger", "text": "Menyebabkan luka bakar parah pada kulit dan mata"},
        ],
        "ppe": ["Masker gas", "Kacamata pelindung", "Sarung tangan karet", "Lemari asam"],
        "storage": "Simpan dalam wadah bertekanan di tempat dingin dan terventilasi. Jauhkan dari asam.",
        "firstaid": "Jika terhirup: pindahkan segera ke udara segar, beri oksigen. Hubungi 119.",
        "storage_group": "BASE"
    },
    {
        "id": 8, "name": "Metanol", "formula": "CH₃OH", "cas": "67-56-1",
        "mw": "32.04 g/mol", "bp": "64.7°C", "mp": "-97.6°C", "density": "0.791 g/cm³", "ph": "~7",
        "state": "Cair", "color": "Tidak berwarna", "category": "Pelarut Organik",
        "ghs": ["GHS02", "GHS06", "GHS08"],
        "hazards": [
            {"type": "danger", "text": "Beracun — dapat menyebabkan kebutaan atau kematian jika tertelan"},
            {"type": "danger", "text": "Mudah terbakar — titik nyala 11°C"},
        ],
        "ppe": ["Kacamata pelindung", "Sarung tangan nitril tebal", "Jas lab", "Lemari asam"],
        "storage": "Simpan di tempat dingin, terventilasi, jauh dari panas dan api.",
        "firstaid": "DARURAT — Jika tertelan: SEGERA hubungi 119.",
        "storage_group": "FLAMMABLE"
    },
    {
        "id": 9, "name": "Hidrogen Peroksida", "formula": "H₂O₂", "cas": "7722-84-1",
        "mw": "34.01 g/mol", "bp": "150°C", "mp": "-0.43°C", "density": "1.45 g/cm³", "ph": "~4-5",
        "state": "Cair", "color": "Tidak berwarna", "category": "Oksidator",
        "ghs": ["GHS03", "GHS05", "GHS07"],
        "hazards": [
            {"type": "danger", "text": "Oksidator kuat — dapat menyebabkan kebakaran saat kontak dengan bahan organik"},
            {"type": "danger", "text": "Korosif pada konsentrasi tinggi"},
        ],
        "ppe": ["Kacamata pelindung", "Sarung tangan nitril", "Jas lab"],
        "storage": "Simpan di tempat dingin, gelap, terventilasi. Jauhkan dari logam dan debu.",
        "firstaid": "Jika terkena kulit/mata: bilas dengan banyak air.",
        "storage_group": "OXIDIZER"
    },
    {
        "id": 10, "name": "Benzena", "formula": "C₆H₆", "cas": "71-43-2",
        "mw": "78.11 g/mol", "bp": "80.1°C", "mp": "5.5°C", "density": "0.876 g/cm³", "ph": "~7",
        "state": "Cair", "color": "Tidak berwarna", "category": "Hidrokarbon Aromatik",
        "ghs": ["GHS02", "GHS08", "GHS06"],
        "hazards": [
            {"type": "danger", "text": "Karsinogen — menyebabkan leukemia pada paparan jangka panjang"},
            {"type": "danger", "text": "Sangat mudah terbakar — titik nyala -11°C"},
        ],
        "ppe": ["Sarung tangan khusus", "Kacamata pelindung", "Jas lab", "Lemari asam wajib"],
        "storage": "Simpan dalam wadah tertutup rapat di lemari asap. Hindari paparan seminimal mungkin.",
        "firstaid": "DARURAT — jika terhirup berlebihan atau tertelan: SEGERA hubungi 119.",
        "storage_group": "FLAMMABLE"
    },
    {
        "id": 11, "name": "Kalium Permanganat", "formula": "KMnO₄", "cas": "7722-64-7",
        "mw": "158.03 g/mol", "bp": "240°C (dekomposisi)", "mp": "N/A", "density": "2.70 g/cm³", "ph": "~7-8",
        "state": "Padat (kristal)", "color": "Ungu kemerahan", "category": "Oksidator",
        "ghs": ["GHS03", "GHS05", "GHS07", "GHS09"],
        "hazards": [
            {"type": "danger", "text": "Oksidator kuat — dapat menyebabkan kebakaran atau ledakan"},
            {"type": "danger", "text": "Berbahaya bagi lingkungan perairan"},
        ],
        "ppe": ["Kacamata pelindung", "Sarung tangan nitril", "Jas lab"],
        "storage": "Simpan terpisah dari bahan organik, reduktor, dan asam.",
        "firstaid": "Jika terkena kulit: bilas dengan air. Jika terkena mata: bilas min. 15 menit.",
        "storage_group": "OXIDIZER"
    },
    {
        "id": 12, "name": "Asam Nitrat", "formula": "HNO₃", "cas": "7697-37-2",
        "mw": "63.01 g/mol", "bp": "83°C", "mp": "-42°C", "density": "1.51 g/cm³", "ph": "<1",
        "state": "Cair", "color": "Tidak berwarna / kekuningan", "category": "Asam Kuat / Oksidator",
        "ghs": ["GHS03", "GHS05", "GHS07"],
        "hazards": [
            {"type": "danger", "text": "Korosif kuat dan oksidator — sangat berbahaya"},
            {"type": "danger", "text": "Bereaksi hebat dengan logam menghasilkan gas NO₂ beracun"},
        ],
        "ppe": ["Kacamata pelindung", "Sarung tangan PVC", "Jas lab", "Pelindung wajah", "Lemari asam"],
        "storage": "Simpan terpisah dari bahan organik, basa, dan logam. Ventilasi sangat diperlukan.",
        "firstaid": "Jika terkena kulit: bilas min. 20 menit. Gas NO₂ terhirup: segera cari bantuan medis.",
        "storage_group": "ACID_OXIDIZER"
    },
]
