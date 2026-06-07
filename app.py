import streamlit as st
import json
from data.chemicals import CHEMICALS
from data.compatibility import COMPATIBILITY_MATRIX
from utils.ghs import render_ghs_badge
from utils.storage import load_favorites, save_favorites

st.set_page_config(
    page_title="ChemCompat — Pemeriksa Kompatibilitas Bahan Kimia",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #085041 0%, #0F6E56 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }
    .compat-safe {
        background: #E1F5EE;
        border-left: 4px solid #0F6E56;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin: 0.5rem 0;
        color: #085041;
    }
    .compat-warning {
        background: #FAEEDA;
        border-left: 4px solid #BA7517;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin: 0.5rem 0;
        color: #412402;
    }
    .compat-danger {
        background: #FCEBEB;
        border-left: 4px solid #A32D2D;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin: 0.5rem 0;
        color: #501313;
    }
    .ghs-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin: 0.5rem 0;
    }
    .ghs-badge {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        background: #f5f5f0;
        border-radius: 10px;
        padding: 8px 12px;
        min-width: 80px;
        font-size: 11px;
        color: #444;
        text-align: center;
    }
    .chem-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }
    .fav-item {
        background: #f9f9f7;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }
    .result-matrix {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e0e0e0;
        margin-top: 1rem;
    }
    .stButton button {
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

if "favorites" not in st.session_state:
    st.session_state.favorites = load_favorites()

if "page" not in st.session_state:
    st.session_state.page = "Cek Kompatibilitas"

st.markdown("""
<div class="main-header">
    <h1 style="margin:0;font-size:22px">⚗️ ChemCompat</h1>
    <p style="margin:4px 0 0;opacity:0.85;font-size:14px">Pemeriksa Kompatibilitas Penyimpanan Bahan Kimia</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔍 Cek Kompatibilitas", "❤️ Favorit", "📖 Panduan GHS"])

with tab1:
    st.subheader("Pilih Dua Bahan Kimia")

    col1, col2 = st.columns(2)
    chem_names = [c["name"] for c in CHEMICALS]

    with col1:
        st.markdown("**Bahan Kimia Pertama**")
        selected_a = st.selectbox("Pilih bahan kimia A", chem_names, key="chem_a", label_visibility="collapsed")
        chem_a = next(c for c in CHEMICALS if c["name"] == selected_a)

        st.markdown(f"**{chem_a['name']}** `{chem_a['formula']}`")
        st.caption(f"CAS: {chem_a['cas']}  ·  {chem_a['category']}")

        ghs_html = '<div class="ghs-container">'
        for g in chem_a.get("ghs", []):
            ghs_html += render_ghs_badge(g)
        ghs_html += "</div>"
        if chem_a.get("ghs"):
            st.markdown(ghs_html, unsafe_allow_html=True)
        else:
            st.caption("Tidak ada simbol GHS")

        if st.button("❤️ Simpan ke Favorit", key="fav_a"):
            entry = {"id": chem_a["id"], "name": chem_a["name"], "formula": chem_a["formula"], "cas": chem_a["cas"], "category": chem_a["category"]}
            if not any(f["id"] == chem_a["id"] for f in st.session_state.favorites):
                st.session_state.favorites.append(entry)
                save_favorites(st.session_state.favorites)
                st.success(f"{chem_a['name']} disimpan ke favorit!")
            else:
                st.info("Sudah ada di favorit.")

    with col2:
        st.markdown("**Bahan Kimia Kedua**")
        other_names = [n for n in chem_names if n != selected_a]
        selected_b = st.selectbox("Pilih bahan kimia B", other_names, key="chem_b", label_visibility="collapsed")
        chem_b = next(c for c in CHEMICALS if c["name"] == selected_b)

        st.markdown(f"**{chem_b['name']}** `{chem_b['formula']}`")
        st.caption(f"CAS: {chem_b['cas']}  ·  {chem_b['category']}")

        ghs_html = '<div class="ghs-container">'
        for g in chem_b.get("ghs", []):
            ghs_html += render_ghs_badge(g)
        ghs_html += "</div>"
        if chem_b.get("ghs"):
            st.markdown(ghs_html, unsafe_allow_html=True)
        else:
            st.caption("Tidak ada simbol GHS")

        if st.button("❤️ Simpan ke Favorit", key="fav_b"):
            entry = {"id": chem_b["id"], "name": chem_b["name"], "formula": chem_b["formula"], "cas": chem_b["cas"], "category": chem_b["category"]}
            if not any(f["id"] == chem_b["id"] for f in st.session_state.favorites):
                st.session_state.favorites.append(entry)
                save_favorites(st.session_state.favorites)
                st.success(f"{chem_b['name']} disimpan ke favorit!")
            else:
                st.info("Sudah ada di favorit.")

    st.divider()
    st.subheader(f"Hasil Kompatibilitas: {chem_a['name']} + {chem_b['name']}")

    key_ab = f"{chem_a['id']}-{chem_b['id']}"
    key_ba = f"{chem_b['id']}-{chem_a['id']}"
    compat = COMPATIBILITY_MATRIX.get(key_ab) or COMPATIBILITY_MATRIX.get(key_ba)

    if compat:
        level = compat["level"]
        if level == "AMAN":
            css_class = "compat-safe"
            icon = "✅"
        elif level == "PERHATIAN":
            css_class = "compat-warning"
            icon = "⚠️"
        else:
            css_class = "compat-danger"
            icon = "🚫"

        st.markdown(f"""
        <div class="{css_class}">
            <strong>{icon} {level}</strong><br>
            {compat['summary']}
        </div>
        """, unsafe_allow_html=True)

        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.markdown("**Risiko Utama**")
            for r in compat.get("risks", []):
                st.markdown(f"- {r}")
        with col_r2:
            st.markdown("**Rekomendasi Penyimpanan**")
            for r in compat.get("storage_recommendations", []):
                st.markdown(f"- {r}")

        if compat.get("emergency_note"):
            st.warning(f"🚨 **Darurat:** {compat['emergency_note']}")
    else:
        st.info("Data kompatibilitas untuk kombinasi ini belum tersedia. Asumsikan perlu dipisahkan dan konsultasikan dengan MSDS masing-masing bahan.")

    st.divider()
    st.subheader("Perbandingan Sifat Fisik")
    pcol1, pcol2, pcol3 = st.columns(3)
    props = [("Berat Molekul", "mw"), ("Titik Didih", "bp"), ("Titik Leleh", "mp"),
             ("Densitas", "density"), ("pH", "ph"), ("Wujud", "state")]
    for i, (label, key) in enumerate(props):
        with [pcol1, pcol2, pcol3][i % 3]:
            st.metric(label, f"{chem_a.get(key,'—')} / {chem_b.get(key,'—')}")

with tab2:
    st.subheader(f"Bahan Kimia Tersimpan ({len(st.session_state.favorites)})")

    if not st.session_state.favorites:
        st.info("Belum ada bahan kimia favorit. Cari bahan kimia dan klik 'Simpan ke Favorit'.")
    else:
        for i, fav in enumerate(st.session_state.favorites):
            col_f1, col_f2 = st.columns([4, 1])
            with col_f1:
                st.markdown(f"""
                <div class="fav-item">
                    ⚗️ <strong>{fav['name']}</strong> <code>{fav['formula']}</code><br>
                    <small style="color:#666">CAS: {fav['cas']} · {fav['category']}</small>
                </div>
                """, unsafe_allow_html=True)
            with col_f2:
                if st.button("🗑️ Hapus", key=f"del_fav_{i}"):
                    st.session_state.favorites.pop(i)
                    save_favorites(st.session_state.favorites)
                    st.rerun()

        if st.button("🗑️ Hapus Semua Favorit"):
            st.session_state.favorites = []
            save_favorites([])
            st.rerun()

with tab3:
    st.subheader("Panduan Simbol GHS")
    st.caption("GHS (Globally Harmonized System) adalah sistem internasional untuk klasifikasi dan pelabelan bahan kimia berbahaya.")

    ghs_info = [
        ("GHS01", "Eksplosif", "Bahan eksplosif atau self-reactive, bereaksi mudah meledak"),
        ("GHS02", "Mudah Terbakar", "Cairan, gas, padatan mudah terbakar atau pirofori"),
        ("GHS03", "Oksidator", "Bahan pengoksidasi, dapat menyebabkan/memperkuat kebakaran"),
        ("GHS04", "Gas Bertekanan", "Gas dalam tabung bertekanan, dapat meledak jika dipanaskan"),
        ("GHS05", "Korosif", "Merusak jaringan kulit, mata, dan dapat mengkorosi logam"),
        ("GHS06", "Beracun Akut", "Beracun jika tertelan, terhirup, atau kontak dengan kulit"),
        ("GHS07", "Berbahaya", "Bahaya kesehatan ringan-sedang, iritasi, sensitisasi"),
        ("GHS08", "Bahaya Kesehatan Serius", "Karsinogen, mutagen, toksik reproduksi, kerusakan organ"),
        ("GHS09", "Bahaya Lingkungan", "Berbahaya bagi ekosistem perairan dan lingkungan"),
    ]

    cols = st.columns(3)
    for i, (code, label, desc) in enumerate(ghs_info):
        with cols[i % 3]:
            badge_html = render_ghs_badge(code)
            st.markdown(f"""
            <div style="background:#f9f9f7;border:1px solid #e0e0e0;border-radius:10px;padding:12px;margin-bottom:10px;display:flex;align-items:flex-start;gap:10px">
                {badge_html}
                <div>
                    <strong style="font-size:13px">{code}</strong><br>
                    <span style="font-size:12px;color:#0F6E56;font-weight:500">{label}</span><br>
                    <span style="font-size:11px;color:#666;line-height:1.4">{desc}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
