import streamlit as st
import pandas as pd

st.set_page_config(page_title='Gestión Inventario Ganadero', page_icon='🐄', layout='wide')

st.title('🐄 Aplicación Móvil y de Escritorio: Inventario Ganadero Bovino')
st.caption('Sistema de Triple Rol: Campo (Vaquero Finca), Corrales (Subasta) y Contabilidad Comercial')

if 'inventario' not in st.session_state:
    datos = [
        {'NroAnimal': 'Criadero-92-4 Care Queso', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 1741666.67, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1508-280-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2562000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1666-246-2(LOLA)', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2577000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1674-145-1(Normando)', 'Sexo': 'Macho', 'Cat_Ingreso': 'MC', 'Cat_Venta': 'MC', 'Finca': 'Garcitas', 'Costo_Unitario': 1409400.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1749-139-1 Negro Peludo', 'Sexo': 'Macho', 'Cat_Ingreso': 'MC', 'Cat_Venta': 'MC', 'Finca': 'Garcitas', 'Costo_Unitario': 1728000.00, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1755-319-3', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2969333.33, 'Estado': 'Activo', 'PesoSalida': 0, 'Subasta': '', 'Lote': '', 'ValorVenta': 0},
        {'NroAnimal': '1761-62-11', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2754904.76, 'Estado': 'Vendido', 'PesoSalida': 487, 'Subasta': '1985', 'Lote': '82', 'ValorVenta': 3100000.00},
        {'NroAnimal': '1769-73-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VG', 'Cat_Venta': 'VG', 'Finca': 'Garcitas', 'Costo_Unitario': 2441800.00, 'Estado': 'Vendido', 'PesoSalida': 467, 'Subasta': '1985', 'Lote': '82', 'ValorVenta': 3387200.00},
        {'NroAnimal': '1797-214-2', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 2547600.00, 'Estado': 'Vendido', 'PesoSalida': 477, 'Subasta': '1985', 'Lote': '88', 'ValorVenta': 3300000.00},
        {'NroAnimal': '1839-137-1', 'Sexo': 'Hembra', 'Cat_Ingreso': 'VP', 'Cat_Venta': 'VP', 'Finca': 'Garcitas', 'Costo_Unitario': 3228800.00, 'Estado': 'Vendido', 'PesoSalida': 505, 'Subasta': '1985', 'Lote': '88', 'ValorVenta': 3475800.00}
    ]
    st.session_state.inventario = pd.DataFrame(datos)

df = st.session_state.inventario

rol = st.sidebar.radio(
    'Seleccione Rol de Trabajo:',
    ['📱 Vaquero Finca (Despacho)', '🚛 Vaquero Subasta (Corrales/Loteo)', '📊 Comercial & Contabilidad', '🔎 Ficha Master de Animales']
)

if rol == '📱 Vaquero Finca (Despacho)':
    st.header('📱 Despacho de Campo (Vaquero Finca)')
    sexo = st.radio('Seleccione Sexo:', ['HEMBRAS (🐄)', 'MACHOS (🐂)'], horizontal=True)
    sexo_val = 'Hembra' if 'HEMBRAS' in sexo else 'Macho'
    df_act = df[(df['Estado'] == 'Activo') & (df['Sexo'] == sexo_val)]
    st.subheader(f'Reses Activas Disponibles ({len(df_act)})')
    st.dataframe(df_act[['NroAnimal', 'Cat_Ingreso', 'Finca', 'Costo_Unitario']])

elif rol == '🚛 Vaquero Subasta (Corrales/Loteo)':
    st.header('🚛 Corrales y Loteo en Subasta')
    st.caption('Reclasificación de Categoría Comercial y Pesaje Colectivo en Báscula')
    df_trans = df[df['Estado'] == 'En Tránsito']
    st.subheader(f'Reses En Tránsito ({len(df_trans)})')
    st.dataframe(df_trans)

elif rol == '📊 Comercial & Contabilidad':
    st.header('📊 Tablero Comercial y Conciliación Contable')
    activos = len(df[df['Estado'] == 'Activo'])
    vendidos = len(df[df['Estado'] == 'Vendido'])
    val_inv = df[df['Estado'] == 'Activo']['Costo_Unitario'].sum()
    val_ventas = df[df['Estado'] == 'Vendido']['ValorVenta'].sum()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Cabezas Activas', f'{activos}')
    c2.metric('Cabezas Vendidas', f'{vendidos}')
    c3.metric('Valor Inventario Activo', f'')
    c4.metric('Ventas Totales', f'')
    st.dataframe(df)

else:
    st.header('🔎 Ficha de Vida del Bovino')
    busq = st.text_input('Buscar Arete o Consecutivo:')
    if busq:
        st.dataframe(df[df['NroAnimal'].str.contains(busq, case=False, na=False)])
    else:
        st.dataframe(df)
