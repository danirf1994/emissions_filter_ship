import pandas as pd
import streamlit as st

# Importar tabelas
tabela_emission = pd.read_excel(r"C:\Users\Danielle\Documents\Outros\Python class\emission.xlsx")
tabela_fn = pd.read_excel(r"C:\Users\Danielle\Documents\Outros\Python class\fn_aps.xlsx")


#juntar as tabelas
#tabela_final = pd.merge(tabela_fn, tabela_emission, on='IMO', how='inner')
#print(tabela_final)
# tabela_final.to_excel(r"C:\Users\Danielle\Documents\Outros\Python class\tabela_final.xlsx")

st.title("Emissões de CO₂ dos Navios ⚓")

# Converter coluna de data
tabela_fn['DataFt'] = pd.to_datetime(tabela_fn['DataFt']).dt.date #converte dados de data e hora em objetos de datetime do pandas


# Seleção do tipo de filtro
opcao = st.selectbox(
    "Escolha o tipo de filtro:",
    ["Filtrar por data", "Filtrar por tipo de navio"]
)


#  FILTRO POR DATA 
if opcao == "Filtrar por data":

    data_escolhida = st.date_input("Selecione a data:")
    st.write(f"Data selecionada: **{data_escolhida}**")

    filtro_data = tabela_fn[tabela_fn['DataFt'] == data_escolhida]

    # IMOs presentes na data
    imos_do_dia = filtro_data['IMO'].unique() # array p obter os valores exclusivos de uma coluna

    # Buscar emissões correspondentes
    dados_emission = tabela_emission[tabela_emission['IMO'].isin(imos_do_dia)] #verifica se o elemento existe e devolve um boolean
    dados_emission = dados_emission[['IMO', 'Tipo', 'E_CO2_TOTAL']]

    st.subheader("Emissões correspondentes:")
    st.dataframe(dados_emission)

    # Somar emissões
    soma_total = dados_emission['E_CO2_TOTAL'].sum() #Por padrão  soma os valores ao longo da coluna

    st.success(f"Emissão total no dia {data_escolhida}: **{soma_total:,.2f} kg CO₂**")


# FILTRO POR TIPO DE NAVIO 
elif opcao == "Filtrar por tipo de navio":

    lista_tipos = sorted(tabela_emission['Tipo'].dropna().unique())   # remover linhas ou colunas cm valores ausentes

    tipo_escolhido = st.selectbox("Selecione o tipo de navio:", lista_tipos)

    st.write(f"Tipo selecionado: **{tipo_escolhido}**")

    # IMOs do tipo escolhido
    filtro_tipo = tabela_emission[tabela_emission['Tipo'] == tipo_escolhido]
    imos_tipo = filtro_tipo['IMO'].unique() 

    # Buscar emissões correspondentes
    dados_emission = tabela_emission[tabela_emission['IMO'].isin(imos_tipo)]  #verifica se o elemento existe e devolve um boolean
    dados_emission = dados_emission[['IMO', 'Tipo', 'E_CO2_TOTAL']]

    st.subheader("Emissões correspondentes:")
    st.dataframe(dados_emission)

    # Somar emissões por tipo
    soma_total = dados_emission['E_CO2_TOTAL'].sum()  

    st.success(f"Emissão total para navios do tipo **{tipo_escolhido}**: "
               f"**{soma_total:,.2f} kg CO₂**")
    
# streamlit run "c:/Users/Danielle/Documents/Outros/Python class/assignment2.py"