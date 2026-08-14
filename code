from flask import Flask, render_template_string

app = Flask(__name__)

# Código HTML de la página integrado
HTML_CODE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>Residencia Exclusiva — Dossier Privado</title>
  
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

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

    body {
      background-color: var(--bg-color);
      color: var(--text-main);
      font-family: var(--font-family);
      line-height: 1.6;
      padding-bottom: 60px;
    }

    .container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 20px;
    }

    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 0;
    }

    .tag-private {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: var(--accent-color);
      border: 1px solid var(--accent-color);
      padding: 4px 12px;
      border-radius: 20px;
    }

    .lang-selector {
      display: flex;
      gap: 12px;
      align-items: center;
    }

    .flag-btn {
      background: none;
      border: 2px solid transparent;
      cursor: pointer;
      padding: 4px;
      border-radius: 8px;
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      opacity: 0.5;
    }

    .flag-btn.active {
      opacity: 1;
      border-color: var(--accent-color);
      background-color: var(--card-bg);
    }

    .flag-btn:hover { opacity: 1; }

    .flag-btn img {
      width: 28px;
      height: 20px;
      border-radius: 3px;
      object-fit: cover;
      display: block;
    }

    header { margin-bottom: 25px; }

    h1 {
      font-size: 2.5rem;
      font-weight: 600;
      letter-spacing: -0.5px;
      margin-top: 10px;
      margin-bottom: 5px;
    }

    .location {
      color: var(--text-muted);
      font-size: 1.1rem;
    }

    .hero-gallery {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 15px;
      margin-bottom: 40px;
      border-radius: 16px;
      overflow: hidden;
    }

    .hero-gallery img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }

    .hero-gallery .main-img { height: 480px; }
    .hero-gallery .side-imgs {
      display: grid;
      grid-template-rows: 1fr 1fr;
      gap: 15px;
    }

    .img-wrapper {
      overflow: hidden;
      background-color: var(--card-bg);
    }

    .img-wrapper:hover img { transform: scale(1.03); }

    .video-section { margin-bottom: 40px; }

    .video-section h2, .description-box h2 {
      font-size: 1.4rem;
      margin-bottom: 15px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 10px;
    }

    .video-wrapper {
      position: relative;
      padding-bottom: 56.25%;
      height: 0;
      overflow: hidden;
      border-radius: 16px;
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
    }

    .video-wrapper iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }

    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
      margin-bottom: 40px;
    }

    .feature-card {
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
      padding: 20px;
      border-radius: 12px;
      text-align: center;
    }

    .feature-value {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--accent-color);
    }

    .feature-label {
      font-size: 0.85rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .details-section {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 40px;
    }

    .description-box p {
      color: var(--text-muted);
      margin-bottom: 15px;
    }

    .specs-list { list-style: none; }
    .specs-list li {
      display: flex;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid var(--border-color);
      font-size: 0.95rem;
    }

    .specs-list span:first-child { color: var(--text-muted); }

    .price-card {
      background-color: var(--card-bg);
      border: 1px solid var(--accent-color);
      padding: 30px;
      border-radius: 16px;
      text-align: center;
      position: sticky;
      top: 20px;
    }

    .price-title {
      font-size: 0.9rem;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-bottom: 5px;
    }

    .price-amount {
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 10px;
    }

    .price-note {
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-bottom: 20px;
    }

    .btn-contact {
      display: block;
      width: 100%;
      background-color: var(--accent-color);
      color: #0f1115;
      text-decoration: none;
      font-weight: 600;
      padding: 14px 0;
      border-radius: 8px;
      transition: background-color 0.3s ease;
    }

    .btn-contact:hover { background-color: #d8b98f; }

    @media (max-width: 768px) {
      .hero-gallery { grid-template-columns: 1fr; }
      .hero-gallery .main-img { height: 300px; }
      .hero-gallery .side-imgs { grid-template-columns: 1fr 1fr; }
      .details-section { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <div class="container">
    <div class="top-bar">
      <span class="tag-private" data-es="Dossier Privado" data-en="Private Dossier">Dossier Privado</span>
      <div class="lang-selector">
        <button class="flag-btn active" id="btn-es" onclick="changeLanguage('es')" title="Español" aria-label="Cambiar a Español">
          <img src="https://flagcdn.com/w40/es.png" alt="Bandera de España">
        </button>
        <button class="flag-btn" id="btn-en" onclick="changeLanguage('en')" title="English" aria-label="Switch to English">
          <img src="https://flagcdn.com/w40/gb.png" alt="United Kingdom Flag">
        </button>
      </div>
    </div>

    <header>
      <h1 data-es="Ático / Ático Dúplex de Lujo" data-en="Luxury Penthouse / Duplex">Ático / Ático Dúplex de Lujo</h1>
      <p class="location">Valencia, España</p>
    </header>

    <section class="hero-gallery">
      <div class="img-wrapper main-img">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80" alt="Salón minimalista" loading="lazy">
      </div>
      <div class="side-imgs">
        <div class="img-wrapper">
          <img src="https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80" alt="Interior moderno" loading="lazy">
        </div>
        <div class="img-wrapper">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80" alt="Terraza privada" loading="lazy">
        </div>
      </div>
    </section>

    <section class="video-section">
      <h2 data-es="Recorrido en Vídeo" data-en="Video Tour">Recorrido en Vídeo</h2>
      <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ?rel=0&modestbranding=1" title="Video Tour" allowfullscreen></iframe>
      </div>
    </section>

    <section class="features-grid">
      <div class="feature-card">
        <div class="feature-value">180 m²</div>
        <div class="feature-label" data-es="Superficie" data-en="Surface Area">Superficie</div>
      </div>
      <div class="feature-card">
        <div class="feature-value">3</div>
        <div class="feature-label" data-es="Habitaciones" data-en="Bedrooms">Habitaciones</div>
      </div>
      <div class="feature-card">
        <div class="feature-value">2</div>
        <div class="feature-label" data-es="Baños" data-en="Bathrooms">Baños</div>
      </div>
      <div class="feature-card">
        <div class="feature-value">A+</div>
        <div class="feature-label" data-es="Eficiencia Energética" data-en="Energy Rating">Eficiencia Energética</div>
      </div>
    </section>

    <div class="details-section">
      <div class="description-box">
        <h2 data-es="Descripción del Inmueble" data-en="Property Description">Descripción del Inmueble</h2>
        <p data-es="Exclusiva vivienda completamente reformada..." data-en="Exclusive fully renovated property...">Exclusiva vivienda completamente reformada con acabados de primera calidad, diseño minimalista e iluminación natural óptima en todas sus estancias.</p>
        <p data-es="Cuenta con una amplia terraza privada..." data-en="Features a spacious private terrace...">Cuenta con una amplia terraza privada, cocina integrada equipada con electrodomésticos de gama alta, sistema de climatización por aerotermia y domótica integral.</p>
        
        <h2 style="margin-top: 30px;" data-es="Especificaciones Técnicas" data-en="Technical Specifications">Especificaciones Técnicas</h2>
        <ul class="specs-list">
          <li><span data-es="Tipo de Propiedad" data-en="Property Type">Tipo de Propiedad</span> <strong data-es="Ático" data-en="Penthouse">Ático</strong></li>
          <li><span data-es="Estado" data-en="Condition">Estado</span> <strong data-es="Reformado a estrenar" data-en="Brand new renovation">Reformado a estrenar</strong></li>
          <li><span data-es="Planta" data-en="Floor">Planta</span> <strong data-es="5ª Exterior con ascensor" data-en="5th Floor Exterior with elevator">5ª Exterior con ascensor</strong></li>
          <li><span data-es="Orientación" data-en="Orientation">Orientación</span> <strong data-es="Sur / Sureste" data-en="South / Southeast">Sur / Sureste</strong></li>
          <li><span data-es="Calefacción / Clima" data-en="Heating / Cooling">Calefacción / Clima</span> <strong data-es="Aerotermia por conductos" data-en="Ducted Aerothermal">Aerotermia por conductos</strong></li>
          <li><span data-es="Garaje" data-en="Garage">Garaje</span> <strong data-es="Incluido (1 plaza)" data-en="Included (1 space)">Incluido (1 plaza)</strong></li>
        </ul>
      </div>

      <div>
        <div class="price-card">
          <div class="price-title" data-es="Precio de Venta" data-en="Asking Price">Precio de Venta</div>
          <div class="price-amount">485.000 €</div>
          <div class="price-note" data-es="Impuestos y gastos no incluidos" data-en="Taxes and fees not included">Impuestos y gastos no incluidos</div>
          <a href="https://wa.me/34000000000?text=Hola" class="btn-contact" target="_blank" data-es="Solicitar Información / Visita" data-en="Request Information / Viewing">
            Solicitar Información / Visita
          </a>
        </div>
      </div>
    </div>
  </div>

  <script>
    function changeLanguage(lang) {
      const elements = document.querySelectorAll('[data-es][data-en]');
      elements.forEach(el => {
        el.textContent = el.getAttribute(`data-${lang}`);
      });
      document.documentElement.lang = lang;
      document.getElementById('btn-es').classList.toggle('active', lang === 'es');
      document.getElementById('btn-en').classList.toggle('active', lang === 'en');
      localStorage.setItem('preferred_lang', lang);
    }

    window.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('preferred_lang');
      const userBrowserLang = navigator.language || navigator.userLanguage;
      if (savedLang) {
        changeLanguage(savedLang);
      } else if (userBrowserLang.startsWith('en')) {
        changeLanguage('en');
      } else {
        changeLanguage('es');
      }
    });
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
