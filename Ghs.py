GHS_INFO = {
    "GHS01": {"label": "Eksplosif", "color": "#E24B4A"},
    "GHS02": {"label": "Mudah Terbakar", "color": "#EF9F27"},
    "GHS03": {"label": "Oksidator", "color": "#EF9F27"},
    "GHS04": {"label": "Gas Bertekanan", "color": "#378ADD"},
    "GHS05": {"label": "Korosif", "color": "#E24B4A"},
    "GHS06": {"label": "Beracun Akut", "color": "#639922"},
    "GHS07": {"label": "Berbahaya", "color": "#EF9F27"},
    "GHS08": {"label": "Bahaya Kesehatan", "color": "#E24B4A"},
    "GHS09": {"label": "Bahaya Lingkungan", "color": "#1D9E75"},
}

GHS_SVG_PATHS = {
    "GHS01": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#E24B4A" stroke-width="1.5"/><path d="M11 10h2v5h-2zm0 6h2v2h-2z" fill="#E24B4A"/>',
    "GHS02": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#EF9F27" stroke-width="1.5"/><path d="M12 5c0 0-5 3.5-5 8.5a5 5 0 0010 0C17 8.5 12 5 12 5z" fill="#EF9F27"/><path d="M12 8c0 0-2.5 2-2.5 5a2.5 2.5 0 005 0C14.5 10 12 8 12 8z" fill="white"/>',
    "GHS03": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#EF9F27" stroke-width="1.5"/><circle cx="12" cy="13" r="4" fill="#EF9F27"/><path d="M12 9v8M8 13h8" stroke="white" stroke-width="1.5"/>',
    "GHS04": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#378ADD" stroke-width="1.5"/><ellipse cx="12" cy="14" rx="4" ry="5.5" fill="#378ADD"/><rect x="10.5" y="6" width="3" height="2.5" rx="1" fill="#378ADD"/>',
    "GHS05": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#E24B4A" stroke-width="1.5"/><path d="M8 7h4v7c0 2-4 4-4 4V7z" fill="#E24B4A" opacity="0.8"/><path d="M16 7h-4v7c0 2 4 4 4 4V7z" fill="#E24B4A"/>',
    "GHS06": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#639922" stroke-width="1.5"/><circle cx="12" cy="13" r="5" fill="#2c2c2c"/><circle cx="10" cy="11.5" r="1" fill="white"/><circle cx="14" cy="11.5" r="1" fill="white"/><path d="M10 15.5s1-1.5 2-1.5 2 1.5 2 1.5" stroke="white" stroke-width="1" fill="none"/>',
    "GHS07": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#EF9F27" stroke-width="1.5"/><path d="M12 7l-0.8 5h1.6L12 7z" fill="#EF9F27" stroke="#EF9F27" stroke-width="0.5"/><circle cx="12" cy="15.5" r="1.2" fill="#EF9F27"/>',
    "GHS08": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#E24B4A" stroke-width="1.5"/><path d="M12 6c-3 0-5.5 2-5.5 5.5v1l1.5 4h8l1.5-4v-1C17.5 8 15 6 12 6z" fill="#E24B4A" opacity="0.85"/><path d="M11 10h2v4h-2z M12 10V8" stroke="white" stroke-width="1.2" fill="none"/>',
    "GHS09": '<polygon points="12,2 22,20 2,20" fill="white" stroke="#1D9E75" stroke-width="1.5"/><path d="M12 6C9 6 7 9.5 7 13c0 2 1 4 3 4.5" stroke="#1D9E75" stroke-width="1.5" fill="none"/><path d="M12 6c3 0 5 3.5 5 7 0 2-1 4-3 4.5" stroke="#1D9E75" stroke-width="1.5" fill="none"/><circle cx="12" cy="18.5" r="1" fill="#1D9E75"/>',
}


def render_ghs_badge(code: str) -> str:
    info = GHS_INFO.get(code, {"label": code, "color": "#888"})
    svg_inner = GHS_SVG_PATHS.get(code, "")
    svg = f'''<svg width="52" height="52" viewBox="0 0 24 22" xmlns="http://www.w3.org/2000/svg">
        {svg_inner}
    </svg>'''
    return f'''<div class="ghs-badge">
        {svg}
        <span style="font-size:10px;color:#555;text-align:center;line-height:1.3">{code}<br>{info["label"]}</span>
    </div>'''
