
import streamlit as st

st.set_page_config(page_title="Residencia Exclusiva", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0f1115; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.components.v1.html("
<!DOCTYPE html>
<html lang=\"es\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Residencia Exclusiva — Dossier Privado</title>
  <link href=\"https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
  <style>
    :root {
      --bg-color: #0f1115;
      --card-bg: #181b22;
      --accent-color: #c5a880;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --border-color: #272b35;
      --font-family: 'Plus Jakarta Sans', sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background-color: var(--bg-color); color: var(--text-main); font-family: var(--font-family); padding: 20px; }
    .container { max-width: 1100px; margin: 0 auto; }
    .top-bar { display: flex; justify-content: space-between; align-items: center; padding-bottom: 20px; }
    .tag-private { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: var(--accent-color); border: 1px solid var(--accent-color); padding: 4px 12px; border-radius: 20px; }
    h1 { font-size: 2.5rem; margin-top: 10px; }
    .location { color: var(--text-muted); font-size: 1.1rem; margin-bottom: 25px; }
    .hero-gallery { display: grid; grid-template-columns: 2fr 1fr; gap: 15px; margin-bottom: 40px; }
    .hero-gallery img { width: 100%; height: 100%; object-fit: cover; border-radius: 12px; }
    .video-wrapper { position: relative; padding-bottom: 56.25%; height: 0; border-radius: 16px; overflow: hidden; border: 1px solid var(--border-color); }
    .video-wrapper iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
    .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 40px; }
    .feature-card { background-color: var(--card-bg); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; text-align: center; }
    .feature-value { font-size: 1.8rem; font-weight: 700; color: var(--accent-color); }
    .feature-label { font-size: 0.85rem; color: var(--text-muted); text-transform: uppercase; }
    .price-card { background-color: var(--card-bg); border: 1px solid var(--accent-color); padding: 30px; border-radius: 16px; text-align: center; }
    .price-amount { font-size: 2.2rem; font-weight: 700; margin-bottom: 10px; }
    .btn-contact { display: block; width: 100%; background-color: var(--accent-color); color: #0f1115; text-decoration: none; font-weight: 600; padding: 14px 0; border-radius: 8px; }
  </style>
</head>
<body>
  <div class=\"container\">
    <div class=\"top-bar\">
      <span class=\"tag-private\">Dossier Privado</span>
    </div>
    <h1>Ático / Ático Dúplex de Lujo</h1>
    <p class=\"location\">Valencia, España</p>
    <section class=\"hero-gallery\">
      <img src=\"https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80\" alt=\"Salón\">
      <div style=\"display:grid; gap:15px;\">
        <img src=\"https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80\" alt=\"Interior\">
        <img src=\"https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80\" alt=\"Terraza\">
      </div>
    </section>
    <section class=\"video-wrapper\">
      <iframe src=\"https://www.youtube.com/embed/dQw4w9WgXcQ\" allowfullscreen></iframe>
    </section>
    <section class=\"features-grid\" style=\"margin-top:40px;\">
      <div class=\"feature-card\"><div class=\"feature-value\">180 m²</div><div class=\"feature-label\">Superficie</div></div>
      <div class=\"feature-card\"><div class=\"feature-value\">3</div><div class=\"feature-label\">Habitaciones</div></div>
      <div class=\"feature-card\"><div class=\"feature-value\">2</div><div class=\"feature-label\">Baños</div></div>
    </section>
    <div class=\"price-card\">
      <div class=\"price-amount\">485.000 €</div>
      <a href=\"https://wa.me/34000000000\" class=\"btn-contact\">Solicitar Información</a>
    </div>
  </div>
</body>
</html>
", height=2500, scrolling=True)
