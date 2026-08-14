import streamlit as st

# Configuración de página
st.set_page_config(page_title="Residencia Exclusiva — Dossier Privado", layout="wide")

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

# Inicializar estados de la propiedad y autenticación
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "prop_title" not in st.session_state:
    st.session_state.prop_title = "Ático / Ático Dúplex de Lujo"

if "prop_location" not in st.session_state:
    st.session_state.prop_location = "Valencia, España"

if "prop_desc" not in st.session_state:
    st.session_state.prop_desc = (
        "Exclusiva vivienda completamente reformada con acabados de primera calidad, "
        "diseño minimalista e iluminación natural óptima en todas sus estancias. "
        "Cuenta con una amplia terraza privada, cocina integrada equipada con electrodomésticos "
        "de gama alta, sistema de climatización por aerotermia y domótica integral."
    )

if "prop_price" not in st.session_state:
    st.session_state.prop_price = "485.000 €"

# Inicializar 23 fotos por defecto (pueden ser URLs de imágenes)
if "photos" not in st.session_state:
    default_images = [
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585152220-90363fe7e115?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585152659-32244a19b8ea?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600607687644-c7171b42498f?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600566753086-2f183fb0b462?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600573472592-401b489a3cdc?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600565193358-1a84f331005a?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585152201-f925f68a8607?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600566752431-29ad98270144?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585152202-799d52528741?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80"
    ]
    st.session_state.photos = default_images

# Pantalla de Autenticación con contraseña "danekas"
if not st.session_state.authenticated:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🔐 Acceso Restringido - Dossier Privado")
        password_input = st.text_input("Ingrese la contraseña de acceso:", type="password")
        if st.button("Acceder", use_container_width=True):
            if password_input == "danekas":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta. Utilice: danekas")
    st.stop()

# Menú lateral una vez autenticado
st.sidebar.markdown("### 🧭 Menú de Navegación")
app_mode = st.sidebar.radio("Seleccione la vista:", ["Vista de Cliente (Dossier)", "Panel de Administrador"])

st.sidebar.markdown("---")
if st.sidebar.button("Cerrar Sesión"):
    st.session_state.authenticated = False
    st.rerun()

# ==========================================
# VISTA DE CLIENTE (DOSSIER PRIVADO)
# ==========================================
if app_mode == "Vista de Cliente (Dossier)":
    st.markdown('<span class="tag-private">Dossier Privado</span>', unsafe_allow_html=True)
    st.title(st.session_state.prop_title)
    st.markdown(f"<p style='color: var(--text-muted); font-size: 1.1rem;'>📍 {st.session_state.prop_location}</p>", unsafe_allow_html=True)

    # Galería Principal (Mostramos la foto principal y dos laterales de ejemplo)
    col_main, col_side = st.columns([2, 1])
    with col_main:
        if len(st.session_state.photos) > 0:
            st.image(st.session_state.photos[0], use_container_width=True, caption="Vista Principal")
    with col_side:
        if len(st.session_state.photos) > 1:
            st.image(st.session_state.photos[1], use_container_width=True, caption="Interior")
        if len(st.session_state.photos) > 2:
            st.image(st.session_state.photos[2], use_container_width=True, caption="Terraza")

    st.markdown("---")

    # Apartado de Descripción de la Propiedad
    st.subheader("📝 Descripción del Inmueble")
    st.write(st.session_state.prop_desc)

    st.markdown("---")

    # Galería Completa de las 23 fotos
    st.subheader("📸 Galería Completa (23 Fotografías)")
    gallery_cols = st.columns(3)
    for idx, photo_url in enumerate(st.session_state.photos):
        with gallery_cols[idx % 3]:
            if photo_url.startswith("http"):
                st.image(photo_url, use_container_width=True, caption=f"Foto {idx + 1}")

    st.markdown("---")

    # Detalles clave y precio
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
            <div class="price-amount">{st.session_state.prop_price}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 15px;">Impuestos y gastos no incluidos</div>
            <a href="https://wa.me/34000000000?text=Hola,%20estoy%20interesado%20en%20consultar%20sobre%20el%20Inmueble" class="btn-contact" target="_blank">
                Solicitar Información / Visita
            </a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# PANEL DE ADMINISTRADOR
# ==========================================
elif app_mode == "Panel de Administrador":
    st.title("🛠️ Panel de Administrador")
    st.markdown("Modifique los detalles de la propiedad y gestione las **23 fotografías** del dossier.")
    
    # Doble seguridad visual opcional en panel
    admin_pwd = st.text_input("Confirme contraseña de administrador (danekas):", type="password")
    
    if admin_pwd == "danekas":
        st.success("Acceso al panel de control concedido.")
        
        with st.form("admin_form"):
            st.subheader("Información General")
            st.session_state.prop_title = st.text_input("Título de la Propiedad", value=st.session_state.prop_title)
            st.session_state.prop_location = st.text_input("Ubicación", value=st.session_state.prop_location)
            st.session_state.prop_price = st.text_input("Precio de Venta", value=st.session_state.prop_price)
            
            st.subheader("Descripción del Inmueble")
            st.session_state.prop_desc = st.text_area("Texto descriptivo", value=st.session_state.prop_desc, height=150)
            
            st.subheader("Gestión de las 23 Fotografías (URLs)")
            updated_photos = []
            for i in range(23):
                current_url = st.session_state.photos[i] if i < len(st.session_state.photos) else ""
                new_url = st.text_input(f"URL Foto {i + 1}", value=current_url, key=f"photo_input_{i}")
                updated_photos.append(new_url)
                
            submitted = st.form_submit_button("Guardar Cambios")
            if submitted:
                st.session_state.photos = updated_photos
                st.success("¡Cambios guardados correctamente! Ya puede verlos en la vista de cliente.")
    elif admin_pwd != "":
        st.error("Contraseña incorrecta para el panel de administración.")
