import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestión Inventario Ganadero", page_icon="🐄", layout="wide")

# Inicialización del inventario en session_state si no existe
if 'inventario' not in st.session_state:
    datos = [
        {'NroAnimal': 'Criadero-92-4 Care Queso', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 1741666.67, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1508-280-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2562000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1666-246-2(LOLA)', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2577000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1674-145-1(Normando)', 'Sexo': 'Macho', 'Cat_Ingreso': 'MC', 'Cat_Venta': 'MC', 'Finca': 'Garcitas', 'Costo_Unitario': 1409400.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1749-139-1 Negro Peludo', 'Sexo': 'Macho', 'Cat_Ingreso': 'MC', 'Cat_Venta': 'MC', 'Finca': 'Garcitas', 'Costo_Unitario': 1728000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1755-319-3', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2969333.33, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1761-62-11', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2754904.76, 'Estado': 'En Tránsito', 'PesoSalida': 487, 'Subasta': '1985', 'Lote': '82', 'ValorVenta': 0},
        {'NroAnimal': '1769-73-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VG', 'Cat_Venta': 'VG', 'Finca': 'Garcitas', 'Costo_Unitario': 2441800.00, 'Estado': 'En Tránsito', 'PesoSalida': 467, 'Subasta': '1985', 'Lote': '82', 'ValorVenta': 0},
        {'NroAnimal': '1797-214-2', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2547600.00, 'Estado': 'Vendido', 'PesoSalida': 477, 'Subasta': '1985', 'Lote': '88', 'ValorVenta': 3300000.00},
        {'NroAnimal': '1839-137-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 3228800.00, 'Estado': 'Vendido', 'PesoSalida': 505, 'Subasta': '1985', 'Lote': '88', 'ValorVenta': 3475800.00},
        {'NroAnimal': '1851-167-6', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VC', 'Cat_Venta': 'VC', 'Finca': 'Garcitas', 'Costo_Unitario': 2713828.57, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1853-115-3', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2413600.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1867-60-9', 'Sexo': 'Macho', 'Cat_Ingreso': 'ML', 'Cat_Venta': 'ML', 'Finca': 'Garcitas', 'Costo_Unitario': 1388621.86, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0}
    ]
    st.session_state.inventario = pd.DataFrame(datos)

# Manejo de Autenticación / Login
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
            
    st.info("💡 Credenciales disponibles:
- **Finca:** Usuario: `Garcitas` | Clave: `Garcitas`
- **Báscula:** Usuario: `Bascula` | Clave: `Bascula`
- **Oficina:** Usuario: `Comercial` | Clave: `Comercial`")

# ----------------- APLICACIÓN AUTENTICADA -----------------
else:
    st.sidebar.title(f"👤 {st.session_state.username}")
    st.sidebar.caption(f"Rol: {st.session_state.user_role}")
    if st.sidebar.button("Cerrar Sesión"):
        logout()
        
    df = st.session_state.inventario

    # ROL 1: VAQUERO FINCA (GARCITAS) - SIN VALORES DE DINERO
    if st.session_state.username == 'Garcitas':
        st.title("📱 Módulo Finca Garcitas (Vaquero)")
        st.caption("Gestión simplificada: Selección de reses para transporte y asignación de peso de salida.")
        
        # Filtro por Sexo
        sexo = st.radio("1. Seleccione Sexo de las Reses:", ["HEMBRAS (🐄)", "MACHOS (🐂)"], horizontal=True)
        sexo_val = "Hembra" if "HEMBRAS" in sexo else "Macho"
        
        # Filtrar solo animales activos de ese sexo
        df_finca = df[(df["Estado"] == "Activo") & (df["Sexo"] == sexo_val)].copy()
        
        st.write(f"### Reses Activas Disponibles en Finca ({len(df_finca)})")
        
        if len(df_finca) == 0:
            st.info("No hay reses activas disponibles para el sexo seleccionado.")
        else:
            # MOSTRAR TABLA LIMPIA SIN VALORES MONETARIOS
            st.dataframe(
                df_finca[["NroAnimal", "Sexo", "Cat_Ingreso", "Finca", "Estado"]],
                use_container_width=True
            )
            
            st.markdown("---")
            st.subheader("🚚 Seleccionar Animales a Transportar y Asignar Peso")
            
            with st.form("form_despacho"):
                reses_seleccionadas = st.multiselect(
                    "Seleccione los números de arete/consecutivos que suben al camión:",
                    options=df_finca["NroAnimal"].tolist()
                )
                
                pesos_dict = {}
                if reses_seleccionadas:
                    st.write("#### Ingrese el Peso de Salida (Kg) para cada res seleccionada:")
                    for res in reses_seleccionadas:
                        pesos_dict[res] = st.number_input(
                            f"Peso de salida para {res} (Kg):",
                            min_value=50, max_value=1000, value=450, step=1
                        )
                
                btn_despachar = st.form_submit_button("🚚 DESPACHAR A TRÁNSITO")
                
                if btn_despachar:
                    if not reses_seleccionadas:
                        st.warning("Debe seleccionar al menos una res para despachar.")
                    else:
                        for res in reses_seleccionadas:
                            idx = df[df["NroAnimal"] == res].index
                            df.loc[idx, "Estado"] = "En Tránsito"
                            df.loc[idx, "PesoSalida"] = pesos_dict[res]
                        
                        st.session_state.inventario = df
                        st.success(f"¡Se despacharon {len(reses_seleccionadas)} reses al estado EN TRÁNSITO exitosamente!")
                        st.rerun()

    # ROL 2: VAQUERO BÁSCULA (BASCULA)
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
                
                cat_nueva = st.selectbox("Reclasificar Categoría de Venta:", ["VG", "NG", "NF", "MC", "ML", "VC", "VP"])
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
                        
                        st.session_state.inventario = df
                        st.success(f"¡Lote {lote_num} (Subasta {subasta_num}) asignado a {len(reses_lote)} reses!")
                        st.rerun()

    # ROL 3: COMERCIAL Y CONTABILIDAD
    elif st.session_state.username == 'Comercial':
        st.title("📊 Tablero Comercial y Conciliación Contable")
        st.caption("Visión completa de inventarios, costos, facturación y punto de equilibrio.")
        
        activos = len(df[df["Estado"] == "Activo"])
        transito = len(df[df["Estado"] == "En Tránsito"])
        vendidos = len(df[df["Estado"] == "Vendido"])
        val_inv = df[df["Estado"] == "Activo"]["Costo_Unitario"].sum()
        val_ventas = df[df["Estado"] == "Vendido"]["ValorVenta"].sum()
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Cabezas Activas Finca", f"{activos}")
        col2.metric("Cabezas En Tránsito", f"{transito}")
        col3.metric("Valor Invertido Activo", f"${val_inv:,.2f}")
        col4.metric("Ventas Totales Facturadas", f"${val_ventas:,.2f}")
        
        st.markdown("---")
        st.subheader("📋 Inventario General Completo")
        st.dataframe(df, use_container_width=True)
