import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestión Inventario Ganadero", page_icon="🐄", layout="wide")

# ----------------- BASE DE DATOS INICIAL CON MÁS ANIMALES REPRESENTATIVOS -----------------
if 'inventario' not in st.session_state:
    datos = [
        # MACHOS - MACHO CEBA (MC)
        {'NroAnimal': '1674-145-1(Normando)', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO CEBA', 'Cat_Venta': 'MACHO CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1409400.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1749-139-1 Negro Peludo', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO CEBA', 'Cat_Venta': 'MACHO CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1728000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1912-232-1 (tigre)', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO CEBA', 'Cat_Venta': 'MACHO CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1850000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': 'MADRINERO', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO CEBA', 'Cat_Venta': 'MACHO CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1900000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1964-124-9', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO CEBA', 'Cat_Venta': 'MACHO CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1780000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1964-124-10', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO CEBA', 'Cat_Venta': 'MACHO CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1780000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        
        # MACHOS - MACHO LEVANTE (ML)
        {'NroAnimal': '1867-60-9', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO LEVANTE', 'Cat_Venta': 'MACHO LEVANTE', 'Finca': 'Garcitas', 'Costo_Unitario': 1388621.86, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1878-165-1', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO LEVANTE', 'Cat_Venta': 'MACHO LEVANTE', 'Finca': 'Garcitas', 'Costo_Unitario': 1420000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1897-174-10', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO LEVANTE', 'Cat_Venta': 'MACHO LEVANTE', 'Finca': 'Garcitas', 'Costo_Unitario': 1390000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1904-7-1', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO LEVANTE', 'Cat_Venta': 'MACHO LEVANTE', 'Finca': 'Garcitas', 'Costo_Unitario': 1450000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},

        # MACHOS - CRIA MACHO (CM)
        {'NroAnimal': 'CM (662-0)', 'Sexo': 'Macho', 'Cat_Ingreso': 'CRIA MACHO', 'Cat_Venta': 'CRIA MACHO', 'Finca': 'Garcitas', 'Costo_Unitario': 800000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': 'CM(LOLA)', 'Sexo': 'Macho', 'Cat_Ingreso': 'CRIA MACHO', 'Cat_Venta': 'CRIA MACHO', 'Finca': 'Garcitas', 'Costo_Unitario': 850000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': 'CM(1885-29-2)', 'Sexo': 'Macho', 'Cat_Ingreso': 'CRIA MACHO', 'Cat_Venta': 'CRIA MACHO', 'Finca': 'Garcitas', 'Costo_Unitario': 820000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},

        # MACHOS - MACHO GORDO / BUFALO
        {'NroAnimal': '1955-217-1', 'Sexo': 'Macho', 'Cat_Ingreso': 'MACHO GORDO', 'Cat_Venta': 'MACHO GORDO', 'Finca': 'Garcitas', 'Costo_Unitario': 2400000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1972-14-1', 'Sexo': 'Macho', 'Cat_Ingreso': 'BUFALO', 'Cat_Venta': 'BUFALO', 'Finca': 'Garcitas', 'Costo_Unitario': 2100000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},

        # HEMBRAS - VACA PARIDA (VP)
        {'NroAnimal': 'Criadero-92-4 Care Queso', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 1741666.67, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1508-280-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2562000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1666-246-2(LOLA)', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2577000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1755-319-3', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2969333.33, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1761-62-11', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2754904.76, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1797-214-2', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2547600.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1839-137-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 3228800.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1853-115-3', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2413600.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1853-115-7', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2413600.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1870-13-4', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2565537.50, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1871-93-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2890335.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1872-7-5', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA PARIDA', 'Cat_Venta': 'VACA PARIDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2587308.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},

        # HEMBRAS - VACA GORDA (VG)
        {'NroAnimal': '1769-73-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA GORDA', 'Cat_Venta': 'VACA GORDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2441800.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1893-302-5', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA GORDA', 'Cat_Venta': 'VACA GORDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2480000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1924-253-2', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA GORDA', 'Cat_Venta': 'VACA GORDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2510000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1925-340-7', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA GORDA', 'Cat_Venta': 'VACA GORDA', 'Finca': 'Garcitas', 'Costo_Unitario': 2530000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},

        # HEMBRAS - VACA CEBA (VC)
        {'NroAnimal': '1851-167-6', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA CEBA', 'Cat_Venta': 'VACA CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 2713828.57, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1870-13-6 Colanta', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA CEBA', 'Cat_Venta': 'VACA CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 2565537.50, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1885-29-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VACA CEBA', 'Cat_Venta': 'VACA CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 2600000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},

        # HEMBRAS - CRIA HEMBRA (CH)
        {'NroAnimal': 'CH(Criadero-Girolanda)', 'Sexo': 'Hembra', 'Cat_Ingreso': 'CRIA HEMBRA', 'Cat_Venta': 'CRIA HEMBRA', 'Finca': 'Garcitas', 'Costo_Unitario': 850000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': 'CH(Criadero-92-4)', 'Sexo': 'Hembra', 'Cat_Ingreso': 'CRIA HEMBRA', 'Cat_Venta': 'CRIA HEMBRA', 'Finca': 'Garcitas', 'Costo_Unitario': 880000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': 'CH(1876-69-11)', 'Sexo': 'Hembra', 'Cat_Ingreso': 'CRIA HEMBRA', 'Cat_Venta': 'CRIA HEMBRA', 'Finca': 'Garcitas', 'Costo_Unitario': 820000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},

        # HEMBRAS - HEMBRA LEVANTE (HL) / NOVILLA CEBA (NC)
        {'NroAnimal': '1882-54-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'HEMBRA LEVANTE', 'Cat_Venta': 'HEMBRA LEVANTE', 'Finca': 'Garcitas', 'Costo_Unitario': 1350000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1882-54-7', 'Sexo': 'Hembra', 'Cat_Ingreso': 'HEMBRA LEVANTE', 'Cat_Venta': 'HEMBRA LEVANTE', 'Finca': 'Garcitas', 'Costo_Unitario': 1360000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1918-332-3', 'Sexo': 'Hembra', 'Cat_Ingreso': 'NOVILLA CEBA', 'Cat_Venta': 'NOVILLA CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1850000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1922-166-2 (VACA NEGRA)', 'Sexo': 'Hembra', 'Cat_Ingreso': 'NOVILLA CEBA', 'Cat_Venta': 'NOVILLA CEBA', 'Finca': 'Garcitas', 'Costo_Unitario': 1880000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0}
    ]
    st.session_state.inventario = pd.DataFrame(datos)

# ----------------- MANEJO DE AUTENTICACIÓN / LOGIN -----------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = ''
    st.session_state.username = ''

def login(usuario, password):
    usuarios_validos = {
        'Garcitas': ('Garcitas', 'Vaquero Finca'),
        'Bascula': ('Bascula', 'Vaquero Báscula/Corrales'),
        'Comercial': ('Comercial', 'Comercial & Contabilidad')
    }
    
    if usuario in usuarios_validos and password == usuarios_validos[usuario][0]:
        st.session_state.logged_in = True
        st.session_state.username = usuario
        st.session_state.user_role = usuarios_validos[usuario][1]
        st.success(f"Bienvenido {usuario} ({usuarios_validos[usuario][1]})")
        st.rerun()
    else:
        st.error("Usuario o contraseña incorrectos.")

def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = ''
    st.session_state.username = ''
    st.rerun()

# ----------------- PANTALLA DE LOGIN -----------------
if not st.session_state.logged_in:
    st.title("🐄 Sistema de Inventario Ganadero Bovino")
    st.subheader("Acceso al Sistema")
    
    with st.form("login_form"):
        usuario = st.text_input("Usuario", placeholder="Ej: Garcitas, Bascula, Comercial")
        password = st.text_input("Contraseña", type="password")
        submit_button = st.form_submit_button("Ingresar")
        
        if submit_button:
            login(usuario.strip(), password.strip())
            
    st.info("""💡 **Credenciales disponibles:**
- **Finca:** Usuario: `Garcitas` | Clave: `Garcitas`
- **Báscula:** Usuario: `Bascula` | Clave: `Bascula`
- **Oficina:** Usuario: `Comercial` | Clave: `Comercial`""")

# ----------------- APLICACIÓN AUTENTICADA -----------------
else:
    df = st.session_state.inventario
    
    # CALCULOS DE METRICAS CABECERA (FINCA GARCITAS)
    df_activos_garcitas = df[(df["Finca"] == "Garcitas") & (df["Estado"] == "Activo")]
    df_transito = df[df["Estado"] == "En Tránsito"]
    total_animales = len(df_activos_garcitas)
    total_hembras = len(df_activos_garcitas[df_activos_garcitas["Sexo"] == "Hembra"])
    total_machos = len(df_activos_garcitas[df_activos_garcitas["Sexo"] == "Macho"])
    total_transito = len(df_transito)

    # ENCABEZADO Y HEADER CON METRICAS SUPERIOR DERECHA
    head_col1, head_col2 = st.columns([2, 3])
    with head_col1:
        st.title("🐄 Inventario Ganadero")
        st.caption(f"Usuario: **{st.session_state.username}** | Rol: {st.session_state.user_role}")
    with head_col2:
        # METRICAS EN LA PARTE SUPERIOR DERECHA (INCLUYE CONTADOR EN TRÁNSITO)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total en Finca", f"{total_animales}")
        m2.metric("Hembras (🐄)", f"{total_hembras}")
        m3.metric("Machos (🐂)", f"{total_machos}")
        m4.metric("En Tránsito (🚚)", f"{total_transito}")

    st.markdown("---")

    # ----------------- ROL 1: VAQUERO FINCA (GARCITAS) -----------------
    if st.session_state.username == 'Garcitas':
        
        opcion_finca = st.radio(
            "Elija una opción:",
            ["📋 Ver animales por categoría", "🚚 Transportar animales"],
            horizontal=True
        )

        # OPCIÓN 1: VER ANIMALES POR CATEGORÍA (RESUMEN MATRIZ)
        if opcion_finca == "📋 Ver animales por categoría":
            st.subheader("📋 RESUMEN DE INVENTARIO ACTIVO POR FINCA Y CATEGORÍA")
            st.markdown("### FINCA: Garcitas")

            # Separar por Sexo
            machos_df = df_activos_garcitas[df_activos_garcitas["Sexo"] == "Macho"]
            hembras_df = df_activos_garcitas[df_activos_garcitas["Sexo"] == "Hembra"]

            # Obtener categorías únicas de cada sexo presentes o estándar
            cats_machos = sorted(machos_df["Cat_Ingreso"].unique().tolist())
            cats_hembras = sorted(hembras_df["Cat_Ingreso"].unique().tolist())

            col_m, col_h = st.columns(2)

            with col_m:
                st.markdown("#### 🐂 MACHOS")
                if len(machos_df) == 0:
                    st.info("No hay machos activos.")
                else:
                    # Crear columnas para cada categoría de machos
                    cols_cat_m = st.columns(max(len(cats_machos), 1))
                    for idx, cat in enumerate(cats_machos):
                        sub_df = machos_df[machos_df["Cat_Ingreso"] == cat]
                        with cols_cat_m[idx]:
                            st.markdown(f"**{cat}** ({len(sub_df)})")
                            for animal in sub_df["NroAnimal"].tolist():
                                st.code(animal, language=None)

            with col_h:
                st.markdown("#### 🐄 HEMBRAS")
                if len(hembras_df) == 0:
                    st.info("No hay hembras activas.")
                else:
                    # Crear columnas para cada categoría de hembras
                    cols_cat_h = st.columns(max(len(cats_hembras), 1))
                    for idx, cat in enumerate(cats_hembras):
                        sub_df = hembras_df[hembras_df["Cat_Ingreso"] == cat]
                        with cols_cat_h[idx]:
                            st.markdown(f"**{cat}** ({len(sub_df)})")
                            for animal in sub_df["NroAnimal"].tolist():
                                st.code(animal, language=None)

            st.markdown("---")
            # TABLA MATRIZ EN FORMATO HOJA DE RESUMEN
            st.subheader("📊 Tabla Matriz de Resumen")
            
            # Construir dict para DataFrame de Resumen
            max_len = 0
            listas_cat = {}
            
            # Unir todas las categorías
            for cat in cats_machos + cats_hembras:
                sub = df_activos_garcitas[df_activos_garcitas["Cat_Ingreso"] == cat]["NroAnimal"].tolist()
                listas_cat[cat] = sub
                if len(sub) > max_len:
                    max_len = len(sub)
            
            # Normalizar longitudes para formar una tabla limpia
            matrix_data = {}
            for cat, lista in listas_cat.items():
                pad = lista + [""] * (max_len - len(lista))
                matrix_data[f"{cat} ({len(lista)})"] = pad
                
            df_matriz = pd.DataFrame(matrix_data)
            st.dataframe(df_matriz, use_container_width=True)

        # OPCIÓN 2: TRANSPORTAR ANIMALES
        elif opcion_finca == "🚚 Transportar animales":
            st.subheader("🚚 Seleccionar Animales a Transportar y Asignar Peso de Salida")
            
            sexo = st.radio("Seleccione Sexo para filtrar:", ["HEMBRAS (🐄)", "MACHOS (🐂)"], horizontal=True)
            sexo_val = "Hembra" if "HEMBRAS" in sexo else "Macho"
            
            df_finca_filtro = df_activos_garcitas[df_activos_garcitas["Sexo"] == sexo_val]
            
            st.write(f"### Reses Disponibles ({len(df_finca_filtro)})")
            st.dataframe(df_finca_filtro[["NroAnimal", "Sexo", "Cat_Ingreso", "Finca"]], use_container_width=True)
            
            # MULTISELECT FUERA DEL FORMULARIO PARA DETECCIÓN EN TIEMPO REAL
            reses_seleccionadas = st.multiselect(
                "Seleccione los números de arete/consecutivos que suben al camión:",
                options=df_finca_filtro["NroAnimal"].tolist()
            )
            
            if reses_seleccionadas:
                with st.form("form_despacho_transporte"):
                    st.write("#### Ingrese el Peso de Salida (Kg) para cada res seleccionada:")
                    pesos_dict = {}
                    for res in reses_seleccionadas:
                        pesos_dict[res] = st.number_input(
                            f"Peso de salida para {res} (Kg):",
                            min_value=50, max_value=1000, value=450, step=1,
                            key=f"peso_{res}"
                        )
                    
                    btn_despachar = st.form_submit_button("🚚 CONFIRMAR Y DESPACHAR A TRÁNSITO")
                    
                    if btn_despachar:
                        for res in reses_seleccionadas:
                            idx = df[df["NroAnimal"] == res].index
                            df.loc[idx, "Estado"] = "En Tránsito"
                            df.loc[idx, "PesoSalida"] = pesos_dict[res]
                        
                        st.session_state.inventario = df
                        st.success(f"¡Se despacharon {len(reses_seleccionadas)} reses al estado EN TRÁNSITO exitosamente!")
                        st.rerun()
            else:
                st.info("👆 Seleccione una o más reses en el cuadro superior para ingresar sus pesos de salida.")

    # ----------------- ROL 2: VAQUERO BASCULA -----------------
    elif st.session_state.username == 'Bascula':
        st.title("🚛 Módulo Corrales y Báscula de Subasta")
        st.caption("Reclasificación de categoría comercial y asignación de Lote y Pesaje Colectivo.")
        
        df_trans = df[df["Estado"] == "En Tránsito"].copy()
        st.write(f"### Reses En Tránsito ({len(df_trans)})")
        
        if len(df_trans) == 0:
            st.info("No hay reses en tránsito pendientes por lotear.")
        else:
            st.dataframe(df_trans[["NroAnimal", "Sexo", "Cat_Ingreso", "Cat_Venta", "PesoSalida", "Finca"]], use_container_width=True)
            
            st.markdown("---")
            st.subheader("📦 Armar Lote y Registrar Pesaje Colectivo")
            
            with st.form("form_loteo"):
                subasta_num = st.text_input("Número de Subasta:", value="1985")
                lote_num = st.text_input("Número de Lote:", value="82")
                
                reses_lote = st.multiselect(
                    "Seleccione las reses que componen este lote:",
                    options=df_trans["NroAnimal"].tolist()
                )
                
                cat_nueva = st.selectbox("Reclasificar Categoría de Venta:", ["VACA GORDA", "NOVILLO GORDO", "NOVILLA CEBA", "MACHO CEBA", "MACHO LEVANTE", "VACA CEBA", "VACA PARIDA"])
                peso_colectivo = st.number_input("Peso Colectivo Total del Lote en Báscula (Kg):", min_value=0, value=950, step=5)
                
                btn_guardar_lote = st.form_submit_button("💾 ASIGNAR LOTE Y PESO COLECTIVO")
                
                if btn_guardar_lote:
                    if not reses_lote:
                        st.warning("Seleccione al menos una res para armar el lote.")
                    else:
                        peso_prom = peso_colectivo / len(reses_lote) if len(reses_lote) > 0 else 0
                        for res in reses_lote:
                            idx = df[df["NroAnimal"] == res].index
                            df.loc[idx, "Subasta"] = subasta_num
                            df.loc[idx, "Lote"] = lote_num
                            df.loc[idx, "Cat_Venta"] = cat_nueva
                            df.loc[idx, "PesoSalida"] = peso_prom
                            df.loc[idx, "Estado"] = "Loteado"
                        
                        st.session_state.inventario = df
                        st.success(f"¡Lote {lote_num} (Subasta {subasta_num}) asignado a {len(reses_lote)} reses!")
                        st.rerun()

    # ----------------- ROL 3: COMERCIAL Y CONTABILIDAD -----------------
    elif st.session_state.username == 'Comercial':
        st.title("📊 Tablero Comercial y Conciliación Contable")
        st.caption("Visión completa de inventarios, costos, facturación y punto de equilibrio.")
        
        activos = len(df[df["Estado"] == "Activo"])
        transito = len(df[df["Estado"] == "En Tránsito"])
        loteados = len(df[df["Estado"] == "Loteado"])
        vendidos = len(df[df["Estado"] == "Vendido"])
        val_inv = df[df["Estado"] == "Activo"]["Costo_Unitario"].sum()
        val_ventas = df[df["Estado"] == "Vendido"]["ValorVenta"].sum()
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Cabezas Activas Finca", f"{activos}")
        col2.metric("Cabezas En Tránsito", f"{transito}")
        col3.metric("Cabezas Loteadas", f"{loteados}")
        col4.metric("Valor Invertido Activo", f"${val_inv:,.2f}")
        
        st.markdown("---")
        st.subheader("📋 Inventario General Completo")
        st.dataframe(df, use_container_width=True)

    st.sidebar.markdown("---")
    if st.sidebar.button("Cerrar Sesión"):
        logout()
