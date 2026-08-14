import streamlit as st
import json
import os
import base64
import secrets
import string
from PIL import Image
import io
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# CONFIGURACIÓN Y BLOQUEO CSS DE ELEMENTOS NATIVOS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Dossier Inmobiliario Privado",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Ocultamiento estricto y bloqueo absoluto de elementos flotantes, badges y toolbar */
    #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], 
    [data-testid="stDecoration"], [data-testid="stStatusWidget"], .stAppDeployButton {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
        height: 0px !important;
        max-height: 0px !important;
    }
    
    div[class*="viewerBadge"], 
    div[class*="stActionButton"], 
    div[class*="viewerBadge_container"],
    iframe[src*="streamlit"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
        z-index: -999999 !important;
    }
    
    html, body, .stApp {
        background-color: #0f1115;
        color: #f3f4f6;
        max-width: 100vw;
        overflow-x: hidden !important;
    }
    
    .main { 
        background-color: #0f1115; 
        color: #f3f4f6;
        padding-top: 1rem !important;
    }

    h1, h2, h3 { color: #c5a880 !important; }
    
    /* Botones estándar de la aplicación */
    .stButton>button { 
        background-color: #c5a880; 
        color: #0f1115; 
        font-weight: bold; 
        border-radius: 8px; 
        width: 100%;
    }

    /* Unificar colores de métricas (m², hab, baños, precio) para evitar cambios según navegador */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"], [data-testid="stMetricDelta"] {
        color: #f3f4f6 !important;
    }
    [data-testid="stMetricValue"] {
        color: #c5a880 !important;
    }

    /* Forzar estilo del link_button de WhatsApp en color verde corporativo */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        text-align: center !important;
    }
    div.stLinkButton > a:hover {
        background-color: #22bf5b !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

DATA_FILE = "propiedades.json"
WHATSAPP_NUMBER = "34637128212"

# -----------------------------------------------------------------------------
# FUNCIONES AUXILIARES
# -----------------------------------------------------------------------------
def image_to_base64(image_file):
    img = Image.open(image_file)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.thumbnail((1600, 1200))
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG", quality=85)
    return base64.b64encode(buffered.getvalue()).decode()

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Asegurar compatibilidad si propiedades antiguas no tienen "usuarios"
            for prop_id, prop_info in data["propiedades"].items():
                if "portada" not in prop_info:
                    prop_info["portada"] = ""
                if "usuarios" not in prop_info:
                    old_pass = prop_info.get("password_cliente", "Cliente2026")
                    prop_info["usuarios"] = {
                        "cliente_principal": {"password": old_pass, "visitas": 0}
                    }
                    if "password_cliente" in prop_info:
                        del prop_info["password_cliente"]
            return data
            
    return {
        "propiedades": {
            "vivienda-01": {
                "titulo_es": "Ático / Dúplex de Lujo",
                "titulo_en": "Luxury Penthouse / Duplex",
                "ubicacion": "Valencia, España",
                "precio": "485.000 €",
                "superficie": "180 m²",
                "habitaciones": "3",
                "banos": "2",
                "descripcion_es": "Exclusiva vivienda reformada con acabados de primera calidad, diseño minimalista e iluminación natural óptima en todas sus estancias.",
                "descripcion_en": "Exclusive fully renovated property with top-quality finishes, minimalist design, and optimal natural light throughout.",
                "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
                "portada": "",
                "usuarios": {
                    "cliente_principal": {"password": "nala0711", "visitas": 0}
                },
                "imagenes": []
            }
        },
        "admin_password": "Admin2026Password"
    }

def generar_contrasena(longitud=12):
    """Genera una contraseña aleatoria segura para un cliente."""
    caracteres = string.ascii_letters + string.digits
    return "".join(secrets.choice(caracteres) for _ in range(longitud))


def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

db = cargar_datos()

# -----------------------------------------------------------------------------
# COMPONENTE GALERÍA
# -----------------------------------------------------------------------------
def render_galeria(imagenes, is_es=True, height=480):
    imgs_json = json.dumps(imagenes)
    expand_txt = "🔍 Ampliar Foto" if is_es else "🔍 Enlarge Photo"
    close_txt = "✖ Cerrar" if is_es else "✖ Close"
    
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <style>
      * {{ box-sizing: border-box; }}
      html, body {{ 
        margin: 0; padding: 0; width: 100%; height: 100%;
        background-color: #0f1115; font-family: system-ui, -apple-system, sans-serif; 
        color: #f3f4f6; overflow: hidden; touch-action: manipulation; 
      }}
      .gallery-container {{
        position: relative; width: 100%; height: 100vh; max-height: 480px;
        margin: 0 auto; background: #0f1115; border-radius: 10px; overflow: hidden;
        display: flex; align-items: center; justify-content: center; user-select: none;
      }}
      .img-wrapper {{
        width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: #0f1115;
      }}
      .img-wrapper img {{
        max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain;
      }}
      .click-zone {{
        position: absolute; top: 0; height: 100%; width: 30%; cursor: pointer; display: flex; align-items: center; z-index: 5;
      }}
      .click-zone-left {{ left: 0; justify-content: flex-start; padding-left: 10px; }}
      .click-zone-right {{ right: 0; justify-content: flex-end; padding-right: 10px; }}
      .arrow-btn {{
        background: rgba(15, 17, 21, 0.75); color: #c5a880; font-size: 20px; font-weight: bold;
        width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
        border: 1px solid #c5a880; opacity: 0.85;
      }}
      .bottom-bar {{
        position: absolute; bottom: 12px; left: 0; right: 0; display: flex; justify-content: center; align-items: center; gap: 10px; z-index: 6;
      }}
      .counter-badge {{
        background: rgba(15, 17, 21, 0.85); color: #c5a880; padding: 5px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; border: 1px solid #c5a880;
      }}
      .expand-btn {{
        background: rgba(197, 168, 128, 0.95); color: #0f1115; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; border: 1px solid #c5a880; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.4);
      }}
    </style>
    </head>
    <body>
      <div class="gallery-container">
        <div class="img-wrapper">
          <img id="slide" src="" alt="Galería" onclick="openModal()" style="cursor: zoom-in;">
        </div>
        <div class="click-zone click-zone-left" onclick="prevSlide(event)"><div class="arrow-btn">&#10094;</div></div>
        <div class="click-zone click-zone-right" onclick="nextSlide(event)"><div class="arrow-btn">&#10095;</div></div>
        <div class="bottom-bar">
          <div id="badge" class="counter-badge">1/1</div>
          <button class="expand-btn" onclick="openModal()">{expand_txt}</button>
        </div>
      </div>
      <script>
        const photos = {imgs_json};
        let current = 0;
        function getTargetDoc() {{
          try {{ if (window.top && window.top.document && window.top.document.body) return window.top.document; }} catch(e) {{}}
          return document;
        }}
        function render() {{
          if (photos.length === 0) return;
          const src = "data:image/jpeg;base64," + photos[current];
          document.getElementById('slide').src = src;
          const label = (current + 1) + "/" + photos.length;
          document.getElementById('badge').innerText = label;
          const doc = getTargetDoc();
          const modalImg = doc.getElementById('ghs-modal-img');
          const modalBadge = doc.getElementById('ghs-modal-badge');
          if (modalImg) modalImg.src = src;
          if (modalBadge) modalBadge.innerText = label;
        }}
        function nextSlide(e) {{ if(e) e.stopPropagation(); current = (current + 1) % photos.length; render(); }}
        function prevSlide(e) {{ if(e) e.stopPropagation(); current = (current - 1 + photos.length) % photos.length; render(); }}
        function openModal() {{
          if (photos.length === 0) return;
          const doc = getTargetDoc();
          let overlay = doc.getElementById('ghs-mobile-fullscreen-modal');
          if (!overlay) {{
            overlay = doc.createElement('div');
            overlay.id = 'ghs-mobile-fullscreen-modal';
            overlay.style.cssText = 'position: fixed !important; top: 0 !important; left: 0 !important; width: 100vw !important; height: 100vh !important; background-color: #000000 !important; z-index: 2147483647 !important; display: flex !important; align-items: center !important; justify-content: center !important;';
            overlay.innerHTML = `
              <button id="ghs-modal-close" style="position: absolute; top: 20px; right: 20px; background: rgba(197, 168, 128, 0.95); color: #0f1115; border: none; padding: 10px 20px; border-radius: 20px; font-weight: bold; cursor: pointer; z-index: 2147483647;">{close_txt}</button>
              <div id="ghs-modal-prev" style="position: absolute; top: 50%; left: 15px; transform: translateY(-50%); background: rgba(15, 17, 21, 0.85); color: #c5a880; border: 1px solid #c5a880; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 2147483647;">&#10094;</div>
              <img id="ghs-modal-img" src="" style="width: 100vw; height: 100vh; object-fit: contain; background: #000;">
              <div id="ghs-modal-next" style="position: absolute; top: 50%; right: 15px; transform: translateY(-50%); background: rgba(15, 17, 21, 0.85); color: #c5a880; border: 1px solid #c5a880; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 2147483647;">&#10095;</div>
              <div id="ghs-modal-badge" style="position: absolute; bottom: 25px; left: 50%; transform: translateX(-50%); background: rgba(15, 17, 21, 0.85); color: #c5a880; padding: 6px 18px; border-radius: 20px; font-weight: bold; border: 1px solid #c5a880; z-index: 2147483647;">1/1</div>
            `;
            doc.body.appendChild(overlay);
            doc.getElementById('ghs-modal-close').onclick = closeModal;
            doc.getElementById('ghs-modal-prev').onclick = (e) => prevSlide(e);
            doc.getElementById('ghs-modal-next').onclick = (e) => nextSlide(e);
          }}
          overlay.style.display = 'flex';
          render();
        }}
        function closeModal() {{
          const doc = getTargetDoc();
          const overlay = doc.getElementById('ghs-mobile-fullscreen-modal');
          if (overlay) overlay.style.display = 'none';
        }}
        render();
      </script>
    </body>
    </html>
    """
    components.html(html_code, height=height)


# -----------------------------------------------------------------------------
# CONTROL DE SESIÓN
# -----------------------------------------------------------------------------
if "auth_client_user" not in st.session_state:
    st.session_state.auth_client_user = None

# -----------------------------------------------------------------------------
# UNA CONTRASEÑA POR CLIENTE + VIVIENDAS PERMITIDAS
# -----------------------------------------------------------------------------
if "usuarios" not in db or not isinstance(db["usuarios"], dict):
    db["usuarios"] = {}

if "cliente_principal" not in db["usuarios"]:
    db["usuarios"]["cliente_principal"] = {
        "password": "nala0711",
        "propiedades_permitidas": list(db.get("propiedades", {}).keys())
    }
    guardar_datos(db)

for u_name, u_info in db["usuarios"].items():
    if not u_info.get("password"):
        u_info["password"] = "nala0711"
    if "propiedades_permitidas" not in u_info:
        u_info["propiedades_permitidas"] = list(db.get("propiedades", {}).keys())
guardar_datos(db)

# -----------------------------------------------------------------------------
# NAVEGACIÓN
# -----------------------------------------------------------------------------
st.sidebar.title("🚪 Navegación")
modo = st.sidebar.radio(
    "Modo de Acceso",
    ["Vista Cliente", "Panel de Administración (Crear/Editar)"]
)
st.sidebar.markdown("---")

# =============================================================================
# VISTA CLIENTE
# =============================================================================
if modo == "Vista Cliente":
    lang = st.sidebar.selectbox(
        "🌐 Idioma / Language",
        ["Español 🇪🇸", "English 🇬🇧"]
    )
    is_es = "Español" in lang

    # UN SOLO CAMPO DE CONTRASEÑA. NO SELECCIONA VIVIENDA NI USUARIO.
    if not st.session_state.auth_client_user:
        st.markdown("""
        <style>
        .login-wrap {
            min-height:72vh; display:flex; align-items:center;
            justify-content:center; padding:30px 10px;
        }
        .login-box {
            width:min(620px,94vw); padding:48px 42px; text-align:center;
            background:rgba(15,17,21,.96);
            border:1px solid rgba(197,168,128,.55); border-radius:18px;
            box-shadow:0 20px 60px rgba(0,0,0,.45);
        }
        .login-kicker {
            color:#c5a880; font-size:13px; letter-spacing:4px;
            font-weight:700; margin-bottom:20px;
        }
        .login-title { color:#fff !important; font-size:42px; margin:0 0 12px; }
        .login-subtitle { color:#d1d5db; margin-bottom:28px; }
        .login-lock { font-size:42px; margin-bottom:18px; }
        </style>
        <div class="login-wrap"><div class="login-box">
        <div class="login-kicker">DOSSIER INMOBILIARIO PRIVADO</div>
        <div class="login-lock">🔒</div>
        <h1 class="login-title">Acceso privado</h1>
        <div class="login-subtitle">
        Introduce la contraseña que te ha proporcionado tu asesor.
        </div>
        """, unsafe_allow_html=True)

        client_password = st.text_input(
            "Contraseña",
            type="password",
            placeholder="Introduce tu contraseña",
            key="single_client_password"
        )

        if st.button("🔓 ENTRAR AL DOSSIER", use_container_width=True,
                     key="single_client_login"):
            found_user = None
            for u_name, u_info in db["usuarios"].items():
                if client_password == u_info.get("password", ""):
                    found_user = u_name
                    break

            if found_user:
                st.session_state.auth_client_user = found_user
                st.rerun()
            else:
                st.error("Contraseña incorrecta. Acceso denegado.")

        st.markdown("</div></div>", unsafe_allow_html=True)

    else:
        user_name = st.session_state.auth_client_user
        user_info = db["usuarios"].get(user_name, {})

        allowed_ids = [
            p for p in user_info.get("propiedades_permitidas", [])
            if p in db.get("propiedades", {})
        ]

        st.sidebar.success(f"👤 Sesión: {user_name}")

        if st.sidebar.button("🚪 Cerrar sesión", key="client_logout"):
            st.session_state.auth_client_user = None
            st.rerun()

        if not allowed_ids:
            st.warning("No tienes ninguna vivienda asignada. Contacta con tu asesor.")
        else:
            prop_sel = st.sidebar.selectbox(
                "🏠 Vivienda disponible",
                allowed_ids,
                format_func=lambda x: db["propiedades"][x].get("titulo_es", x),
                key="allowed_property_select"
            )
            prop_data = db["propiedades"][prop_sel]
            titulo = prop_data["titulo_es"] if is_es else prop_data["titulo_en"]

            if prop_data.get("portada"):
                cover_src = "data:image/jpeg;base64," + prop_data["portada"]
                cover_img_html = (
                    f'<img class="cover-image" src="{cover_src}" '
                    f'alt="Portada de la vivienda">'
                )
            else:
                cover_img_html = (
                    '<div class="cover-image" '
                    'style="background:linear-gradient(135deg,#252a31,#0f1115);"></div>'
                )

            st.markdown("""
            <style>
            .cover-shell {
                position:relative;width:100%;min-height:48vh;border-radius:18px;
                overflow:hidden;display:flex;align-items:center;
                justify-content:center;margin:0 auto 24px;background:#15171c;
                border:1px solid rgba(197,168,128,.35);
                box-shadow:0 20px 60px rgba(0,0,0,.45);
            }
            .cover-image {
                position:absolute;inset:0;width:100%;height:100%;
                object-fit:cover;filter:brightness(.48);
            }
            .cover-overlay {
                position:absolute;inset:0;
                background:linear-gradient(180deg,rgba(15,17,21,.18) 0%,
                rgba(15,17,21,.52) 55%,rgba(15,17,21,.92) 100%);
            }
            .cover-content {
                position:relative;z-index:2;width:min(900px,90%);
                text-align:center;padding:42px 28px;
            }
            .cover-kicker {
                color:#c5a880;font-size:13px;letter-spacing:4px;
                text-transform:uppercase;font-weight:700;margin-bottom:18px;
            }
            .cover-title {
                color:#fff !important;font-size:clamp(30px,5vw,58px);
                line-height:1.08;margin:0 0 12px;font-weight:700;
            }
            .cover-location {color:#e5e7eb;font-size:17px;}
            </style>
            """, unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="cover-shell">
                    {cover_img_html}
                    <div class="cover-overlay"></div>
                    <div class="cover-content">
                        <div class="cover-kicker">DOSSIER INMOBILIARIO PRIVADO</div>
                        <h1 class="cover-title">{titulo}</h1>
                        <div class="cover-location">📍 {prop_data['ubicacion']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if is_es:
                st.title(prop_data["titulo_es"])
                st.write(prop_data["descripcion_es"])
            else:
                st.title(prop_data["titulo_en"])
                st.write(prop_data["descripcion_en"])

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Superficie" if is_es else "Area", prop_data["superficie"])
            c2.metric("Habitaciones" if is_es else "Bedrooms", prop_data["habitaciones"])
            c3.metric("Baños" if is_es else "Bathrooms", prop_data["banos"])
            c4.metric("Precio" if is_es else "Price", prop_data["precio"])

            if prop_data.get("imagenes"):
                st.markdown("---")
                st.subheader("📸 Galería" if is_es else "📸 Gallery")
                render_galeria(prop_data["imagenes"], is_es=is_es, height=480)

            if prop_data.get("video_url"):
                st.markdown("---")
                st.subheader("🎬 Vídeo" if is_es else "🎬 Video")
                st.video(prop_data["video_url"])

            st.markdown("---")
            st.link_button(
                "💬 Contactar por WhatsApp",
                f"https://wa.me/{WHATSAPP_NUMBER}"
            )

# =============================================================================
# PANEL DE ADMINISTRACIÓN
# =============================================================================
elif modo == "Panel de Administración (Crear/Editar)":
    st.title("🛠️ Panel de Control - Administración")

    admin_pass = st.text_input(
        "Contraseña exclusiva de Administrador:",
        type="password",
        key="admin_login_password"
    )

    if admin_pass == db["admin_password"]:
        st.success("Sesión de administrador activa.")

        tab1, tab2, tab3 = st.tabs([
            "Editar Propiedad",
            "👥 Clientes y Permisos",
            "Crear Nueva Propiedad"
        ])

        with tab1:
            prop_keys = list(db["propiedades"].keys())
            if prop_keys:
                prop_edit = st.selectbox(
                    "Seleccionar Inmueble para Modificar:",
                    prop_keys,
                    key="edit_prop_select"
                )
                p_data = db["propiedades"][prop_edit]

                st.subheader("🖼️ Portada de Acceso del Cliente")
                st.caption("Esta imagen será la portada de esta vivienda.")

                if p_data.get("portada"):
                    st.image(
                        base64.b64decode(p_data["portada"]),
                        caption="Portada actual de esta vivienda",
                        use_container_width=True
                    )

                nueva_portada = st.file_uploader(
                    "Seleccionar / reemplazar portada (JPG, PNG o WEBP)",
                    type=["jpg", "jpeg", "png", "webp"],
                    key=f"cover_upload_{prop_edit}"
                )

                if nueva_portada and st.button(
                    "⭐ Guardar esta imagen como Portada",
                    key=f"save_cover_{prop_edit}"
                ):
                    p_data["portada"] = image_to_base64(nueva_portada)
                    guardar_datos(db)
                    st.success("Portada guardada correctamente.")
                    st.rerun()

                st.markdown("---")
                st.subheader("📸 Gestión de Fotografías")

                if p_data.get("imagenes"):
                    grid_cols = st.columns(4)
                    for i, img_b64 in enumerate(p_data["imagenes"]):
                        col = grid_cols[i % 4]
                        col.image(base64.b64decode(img_b64), use_container_width=True)
                        if i == 0:
                            col.info("⭐ Principal")
                        elif col.button(f"⭐ Fijar como 1ª", key=f"main_{prop_edit}_{i}"):
                            p_data["imagenes"].insert(0, p_data["imagenes"].pop(i))
                            guardar_datos(db)
                            st.rerun()
                        if col.button(f"🗑️ Eliminar #{i+1}", key=f"del_{prop_edit}_{i}"):
                            p_data["imagenes"].pop(i)
                            guardar_datos(db)
                            st.rerun()

                nuevas_fotos = st.file_uploader(
                    "Añadir nuevas imágenes (JPG, PNG, WEBP)",
                    type=["jpg", "jpeg", "png", "webp"],
                    accept_multiple_files=True,
                    key=f"new_photos_{prop_edit}"
                )

                if nuevas_fotos and st.button(
                    "⬆️ Subir e Integrar Fotos",
                    key=f"upload_photos_{prop_edit}"
                ):
                    for f in nuevas_fotos:
                        p_data.setdefault("imagenes", []).append(image_to_base64(f))
                    guardar_datos(db)
                    st.success(f"¡{len(nuevas_fotos)} fotos añadidas correctamente!")
                    st.rerun()

                st.markdown("---")
                with st.form(f"edit_form_{prop_edit}"):
                    st.subheader("📝 Datos del Inmueble")
                    col_a, col_b = st.columns(2)
                    titulo_es = col_a.text_input("Título (ES)", p_data["titulo_es"])
                    titulo_en = col_b.text_input("Título (EN)", p_data["titulo_en"])
                    precio = col_a.text_input("Precio", p_data["precio"])
                    ubicacion = col_b.text_input("Ubicación", p_data["ubicacion"])
                    superficie = col_a.text_input("Superficie", p_data["superficie"])
                    habitaciones = col_a.text_input("Habitaciones", p_data["habitaciones"])
                    banos = col_b.text_input("Baños", p_data["banos"])
                    descripcion_es = st.text_area("Descripción (ES)", p_data["descripcion_es"])
                    descripcion_en = st.text_area("Descripción (EN)", p_data["descripcion_en"])
                    video_url = st.text_input(
                        "URL del Vídeo (YouTube/Vimeo/MP4)",
                        p_data.get("video_url", "")
                    )

                    if st.form_submit_button("💾 Guardar Datos y Textos"):
                        p_data.update({
                            "titulo_es": titulo_es,
                            "titulo_en": titulo_en,
                            "precio": precio,
                            "ubicacion": ubicacion,
                            "superficie": superficie,
                            "habitaciones": habitaciones,
                            "banos": banos,
                            "descripcion_es": descripcion_es,
                            "descripcion_en": descripcion_en,
                            "video_url": video_url
                        })
                        guardar_datos(db)
                        st.success("¡Datos del inmueble guardados!")

        with tab2:
            st.subheader("👥 Clientes, contraseñas y viviendas autorizadas")
            st.info(
                "Cada cliente tiene UNA sola contraseña. "
                "Aquí eliges exactamente qué viviendas puede ver."
            )

            st.subheader("🔐 Generador de Contraseñas")
            col_g1, col_g2 = st.columns([1, 2])
            longitud = col_g1.slider(
                "Longitud", 8, 32, 12, key="admin_generator_length"
            )
            if col_g2.button(
                "🎲 Generar contraseña", key="admin_generator_button"
            ):
                st.session_state.admin_generated_password = generar_contrasena(longitud)

            if "admin_generated_password" in st.session_state:
                st.code(st.session_state.admin_generated_password)

            st.markdown("---")
            st.subheader("Clientes existentes")
            all_properties = list(db["propiedades"].keys())

            for u_name, u_info in list(db["usuarios"].items()):
                with st.expander(f"👤 {u_name}", expanded=True):
                    new_pass = st.text_input(
                        "Contraseña del cliente",
                        value=u_info.get("password", "nala0711"),
                        type="password",
                        key=f"client_pass_{u_name}"
                    )

                    selected_properties = st.multiselect(
                        "🏠 Viviendas que puede ver este cliente",
                        options=all_properties,
                        default=[
                            p for p in u_info.get("propiedades_permitidas", [])
                            if p in all_properties
                        ],
                        format_func=lambda x: db["propiedades"][x].get("titulo_es", x),
                        key=f"client_properties_{u_name}"
                    )

                    col1, col2 = st.columns(2)

                    if col1.button("💾 Guardar cliente", key=f"save_client_{u_name}"):
                        if not new_pass.strip():
                            st.error("La contraseña no puede estar vacía.")
                        else:
                            u_info["password"] = new_pass.strip()
                            u_info["propiedades_permitidas"] = selected_properties
                            guardar_datos(db)
                            st.success(f"Cliente '{u_name}' actualizado.")
                            st.rerun()

                    if col2.button(
                        "🎲 Generar y guardar nueva clave",
                        key=f"generate_save_{u_name}"
                    ):
                        nueva = generar_contrasena()
                        u_info["password"] = nueva
                        u_info["propiedades_permitidas"] = selected_properties
                        guardar_datos(db)
                        st.success(f"Nueva contraseña para '{u_name}': {nueva}")
                        st.rerun()

                    if st.button("🗑️ Eliminar cliente", key=f"delete_client_{u_name}"):
                        if len(db["usuarios"]) > 1:
                            del db["usuarios"][u_name]
                            guardar_datos(db)
                            st.rerun()
                        else:
                            st.warning("Debe existir al menos un cliente.")

            st.markdown("---")
            st.subheader("➕ Crear nuevo cliente")

            new_client_name = st.text_input("Nombre del cliente", key="new_client_name")
            new_client_password = st.text_input(
                "Contraseña del cliente",
                value="nala0711",
                type="password",
                key="new_client_password"
            )
            new_client_properties = st.multiselect(
                "🏠 Viviendas que podrá ver",
                options=all_properties,
                format_func=lambda x: db["propiedades"][x].get("titulo_es", x),
                key="new_client_properties"
            )

            if st.button("➕ Crear cliente", key="create_client"):
                if not new_client_name.strip():
                    st.warning("Introduce un nombre para el cliente.")
                elif new_client_name in db["usuarios"]:
                    st.error("Ese cliente ya existe.")
                elif not new_client_password.strip():
                    st.error("La contraseña no puede estar vacía.")
                else:
                    db["usuarios"][new_client_name] = {
                        "password": new_client_password.strip(),
                        "propiedades_permitidas": new_client_properties
                    }
                    guardar_datos(db)
                    st.success(f"Cliente '{new_client_name}' creado correctamente.")
                    st.rerun()

        with tab3:
            st.subheader("Añadir Nueva Propiedad al Portafolio")
            new_id = st.text_input(
                "Identificador único (ej: piso-gran-via, atico-patacona)",
                key="new_property_id"
            )

            if st.button("Crear Inmueble", key="create_property"):
                if new_id and new_id not in db["propiedades"]:
                    db["propiedades"][new_id] = {
                        "titulo_es": "Nueva Propiedad",
                        "titulo_en": "New Property",
                        "ubicacion": "Valencia, España",
                        "precio": "0 €",
                        "superficie": "0 m²",
                        "habitaciones": "0",
                        "banos": "0",
                        "descripcion_es": "Descripción...",
                        "descripcion_en": "Description...",
                        "video_url": "",
                        "portada": "",
                        "usuarios": {},
                        "imagenes": []
                    }
                    guardar_datos(db)
                    st.success(f"Propiedad '{new_id}' creada correctamente.")
                    st.rerun()
                elif new_id in db["propiedades"]:
                    st.error("Ese identificador ya existe.")

    elif admin_pass != "":
        st.error("Clave de administrador incorrecta. Acceso denegado.")
