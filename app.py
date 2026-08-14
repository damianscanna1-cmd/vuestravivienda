import streamlit as st
from PIL import Image

# Configuración de página
st.set_page_config(page_title="Dossier Privado de Propiedades", layout="wide")

# Estilos CSS personalizados (Modo Oscuro Elegante / Lujo)
st.markdown("""
<style>
    :root {
        --bg-color: #0f1115;
        --card-bg: #181b22;
        --accent-color: #c5a880;
        --text-main: #f3f4f6;
        --text-muted: #9ca3af;
        --border-color: #272b35;
    }
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-main);
    }
    .tag-private {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: var(--accent-color);
        border: 1px solid var(--accent-color);
        padding: 4px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 15px;
    }
    .price-card {
        background-color: var(--card-bg);
        border: 1px solid var(--accent-color);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
    }
    .price-amount {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-main);
        margin-bottom: 10px;
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
        text-align: center;
        margin-top: 15px;
    }
    .btn-contact:hover { background-color: #d8b98f; }
    h1, h2, h3 { color: var(--text-main); }
</style>
""", unsafe_allow_html=True)

# Inicializar almacenamiento de propiedades en session_state
if "properties" not in st.session_state:
    st.session_state.properties = [
        {
            "id": 1,
            "title": "Ático / Ático Dúplex de Lujo",
            "location": "Valencia, España",
            "desc": "Exclusiva vivienda completamente reformada con acabados de primera calidad, diseño minimalista e iluminación natural óptima en todas sus estancias.",
            "price": "485.000 €",
            "youtube_url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "client_password": "nala0711",
            "views": 0,
            "photos": []
        }
    ]

if "auth_role" not in st.session_state:
    st.session_state.auth_role = None  # Puede ser "admin" o "client"
if "current_property_id" not in st.session_state:
    st.session_state.current_property_id = None

# Función auxiliar para convertir enlaces comunes de YouTube a formato embed
def format_youtube_embed(url):
    if "embed/" in url:
        return url
    if "watch?v=" in url:
        video_id = url.split("watch?v=")[1].split("&")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    return url

# ==========================================
# PANTALLA DE ACCESO (LOGIN)
# ==========================================
if st.session_state.auth_role is None:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🔐 Acceso al Dossier Privado")
        st.write("Ingrese su contraseña de cliente o la contraseña de administrador (`nala0711`).")
        entered_password = st.text_input("Contraseña de acceso:", type="password")
        
        if st.button("Ingresar", use_container_width=True):
            if entered_password == "nala0711":
                st.session_state.auth_role = "admin"
                st.rerun()
            else:
                # Comprobar si la contraseña coincide con alguna propiedad de cliente
                matched_prop = None
                for prop in st.session_state.properties:
                    if prop["client_password"] == entered_password:
                        matched_prop = prop
                        break
                
                if matched_prop:
                    st.session_state.auth_role = "client"
                    st.session_state.current_property_id = matched_prop["id"]
                    matched_prop["views"] += 1  # Incrementa el contador de visitas
                    st.rerun()
                else:
                    st.error("Contraseña incorrecta. Verifique sus datos.")
    st.stop()

# ==========================================
# PANEL DE ADMINISTRADOR
# ==========================================
if st.session_state.auth_role == "admin":
    st.sidebar.markdown("### 🛠️ Menú Administrador")
    admin_menu = st.sidebar.radio("Opciones", ["Crear Propiedad", "Gestionar / Ver Propiedades", "Estadísticas de Visitas"])
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.auth_role = None
        st.rerun()

    if admin_menu == "Crear Propiedad":
        st.title("➕ Crear Nueva Propiedad")
        with st.form("create_property_form"):
            new_title = st.text_input("Título de la Propiedad")
            new_location = st.text_input("Ubicación")
            new_price = st.text_input("Precio de Venta (ej: 550.000 €)")
            new_desc = st.text_area("Descripción detallada del inmueble")
            new_youtube = st.text_input("URL del vídeo de YouTube")
            new_client_pwd = st.text_input("Contraseña de acceso para los clientes de esta propiedad", value="nala0711")
            
            st.write("📷 **Subir Fotografías desde el Ordenador** (Máximo 23 fotos)")
            uploaded_files = st.file_uploader("Seleccionar imágenes", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
            
            submit_btn = st.form_submit_button("Guardar y Crear Propiedad")
            if submit_btn:
                if not new_title:
                    st.error("El título de la propiedad es obligatorio.")
                else:
                    new_id = len(st.session_state.properties) + 1
                    photos_list = []
                    if uploaded_files:
                        for file in uploaded_files[:23]:
                            img = Image.open(file)
                            photos_list.append(img)
                            
                    st.session_state.properties.append({
                        "id": new_id,
                        "title": new_title,
                        "location": new_location,
                        "desc": new_desc,
                        "price": new_price,
                        "youtube_url": new_youtube,
                        "client_password": new_client_pwd,
                        "views": 0,
                        "photos": photos_list
                    })
                    st.success(f"¡Propiedad '{new_title}' creada con éxito!")

    elif admin_menu == "Gestionar / Ver Propiedades":
        st.title("📋 Gestión de Propiedades Existentes")
        for i, prop in enumerate(st.session_state.properties):
            with st.expander(f"Propiedad #{prop['id']}: {prop['title']} (Contraseña: {prop['client_password']})"):
                with st.form(f"edit_form_{prop['id']}"):
                    e_title = st.text_input("Título", value=prop["title"], key=f"et_{i}")
                    e_location = st.text_input("Ubicación", value=prop["location"], key=f"el_{i}")
                    e_price = st.text_input("Precio", value=prop["price"], key=f"ep_{i}")
                    e_desc = st.text_area("Descripción", value=prop["desc"], key=f"ed_{i}")
                    e_youtube = st.text_input("URL YouTube", value=prop["youtube_url"], key=f"ey_{i}")
                    e_pwd = st.text_input("Contraseña de Cliente", value=prop["client_password"], key=f"epwd_{i}")
                    
                    st.write(f"Fotos actuales: {len(prop['photos'])}. Puede subir nuevas para actualizar:")
                    e_files = st.file_uploader("Subir nuevas fotos (máx 23)", type=["png", "jpg", "jpeg"], accept_multiple_files=True, key=f"ef_{i}")
                    
                    save_changes = st.form_submit_button("Actualizar Propiedad")
                    if save_changes:
                        prop["title"] = e_title
                        prop["location"] = e_location
                        prop["price"] = e_price
                        prop["desc"] = e_desc
                        prop["youtube_url"] = e_youtube
                        prop["client_password"] = e_pwd
                        if e_files:
                            prop["photos"] = [Image.open(f) for f in e_files[:23]]
                        st.success("¡Propiedad actualizada correctamente!")

    elif admin_menu == "Estadísticas de Visitas":
        st.title("📊 Contador de Visitas por Propiedad")
        for prop in st.session_state.properties:
            st.markdown(f"""
            <div style="background-color: var(--card-bg); padding: 20px; border-radius: 12px; border: 1px solid var(--border-color); margin-bottom: 15px;">
                <h3>🏠 {prop['title']}</h3>
                <p><b>Ubicación:</b> {prop['location']}</p>
                <p><b>Contraseña asignada:</b> <code>{prop['client_password']}</code></p>
                <p style="color: var(--accent-color); font-size: 1.3rem; margin-top: 10px;">👁️ <b>Visitas registradas:</b> {prop['views']}</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# VISTA DE CLIENTE (DOSSIER PRIVADO)
# ==========================================
elif st.session_state.auth_role == "client":
    prop = next((p for p in st.session_state.properties if p["id"] == st.session_state.current_property_id), None)
    
    if not prop:
        st.error("No se encontró la propiedad asociada.")
        if st.button("Volver"):
            st.session_state.auth_role = None
            st.rerun()
    else:
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state.auth_role = None
            st.session_state.current_property_id = None
            st.rerun()

        st.markdown('<span class="tag-private">Dossier Privado</span>', unsafe_allow_html=True)
        st.title(prop["title"])
        st.markdown(f"<p style='color: var(--text-muted); font-size: 1.1rem;'>📍 {prop['location']}</p>", unsafe_allow_html=True)

        # Galería principal (Muestra las primeras fotos o ejemplos si no hay suficientes)
        col_main, col_side = st.columns([2, 1])
        with col_main:
            if len(prop["photos"]) > 0:
                st.image(prop["photos"][0], use_container_width=True, caption="Vista Principal")
            else:
                st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80", use_container_width=True, caption="Vista Principal")
        with col_side:
            if len(prop["photos"]) > 1:
                st.image(prop["photos"][1], use_container_width=True, caption="Interior")
            else:
                st.image("https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Interior")
            if len(prop["photos"]) > 2:
                st.image(prop["photos"][2], use_container_width=True, caption="Terraza")
            else:
                st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Terraza")

        st.markdown("---")

        # Apartado de Video de YouTube de la propiedad
        if prop["youtube_url"]:
            st.subheader("🎥 Recorrido en Vídeo")
            embed_url = format_youtube_embed(prop["youtube_url"])
            st.markdown(f"""
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 16px; background-color: var(--card-bg); border: 1px solid var(--border-color);">
                <iframe src="{embed_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen></iframe>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")

        # Apartado de Descripción detallada
        st.subheader("📝 Descripción del Inmueble")
        st.write(prop["desc"])

        st.markdown("---")

        # Galería Completa (Soporta hasta 23 fotos subidas)
        st.subheader(f"📸 Galería Completa ({len(prop['photos'])} Fotografías)")
        if len(prop["photos"]) > 0:
            gallery_cols = st.columns(3)
            for idx, photo in enumerate(prop["photos"]):
                with gallery_cols[idx % 3]:
                    st.image(photo, use_container_width=True, caption=f"Foto {idx + 1}")
        else:
            st.info("No hay fotografías adicionales cargadas en este dossier.")

        st.markdown("---")

        # Especificaciones y Precio
        col_details, col_price = st.columns([2, 1])

        with col_details:
            st.subheader("⚙️ Especificaciones Técnicas")
            st.markdown("""
            * **Superficie:** 180 m²
            * **Habitaciones:** 3
            * **Baños:** 2
            * **Eficiencia Energética:** A+
            * **Estado:** Reformado a estrenar
            * **Planta:** 5ª Exterior con ascensor
            * **Orientación:** Sur / Sureste
            """)

        with col_price:
            st.markdown(f"""
            <div class="price-card">
                <div style="font-size: 0.9rem; color: var(--text-muted); text-transform: uppercase;">Precio de Venta</div>
                <div class="price-amount">{prop['price']}</div>
                <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 15px;">Impuestos y gastos no incluidos</div>
                <a href="https://wa.me/34000000000?text=Hola,%20estoy%20interesado%20en%20consultar%20sobre%20esta%20propiedad" class="btn-contact" target="_blank">
                    Solicitar Información / Visita
                </a>
            </div>
            """, unsafe_allow_html=True)
