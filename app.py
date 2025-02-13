git clone https://github.com/TU_USUARIO/buscador-moleculas-streamlit.git
cd buscador-moleculas-streamlit
import streamlit as st
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw
import io
import requests
from PIL import Image

# Título de la app
st.title("Buscador de Moléculas 2D y Bioisósteros")

# Barra de búsqueda
search_query = st.text_input("Ingresa el nombre o CID de la molécula:")

# Función para obtener la estructura 2D de una molécula a partir de PubChem
def get_molecule_image(search_query):
    # Intentar obtener el CID (número de identificación de PubChem) de la molécula
    compound = None
    if search_query.isdigit():
        # Si el input es un CID
        compound = pcp.Compound.from_cid(int(search_query))
    else:
        # Si el input es un nombre
        compound = pcp.get_compounds(search_query, 'name')[0]
    
    # Obtenemos la estructura 2D de la molécula
    smiles = compound.isomeric_smiles
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        img = Draw.MolToImage(mol)
        return img
    else:
        return None

# Función para obtener bioisósteros o estructuras similares
def get_similar_molecules(search_query):
    # Buscando bioisósteros utilizando PubChem
    compound = pcp.get_compounds(search_query, 'name')[0]
    cid = compound.cid
    similar_compounds = pcp.get_compounds(cid, 'cid')[0].to_dict(properties=['synonyms', 'isomeric_smiles'])
    
    return similar_compounds

# Mostrar la imagen 2D de la molécula
if search_query:
    img = get_molecule_image(search_query)
    if img:
        st.image(img, caption="Estructura 2D de la molécula", use_column_width=True)
    else:
        st.write("No se encontró la molécula o estructura 2D válida.")
    
    # Mostrar bioisósteros o estructuras similares
    st.subheader("Bioisósteros o Estructuras Similares")
    similar_molecules = get_similar_molecules(search_query)
    if similar_molecules:
        st.write(similar_molecules)
    else:
        st.write("No se encontraron bioisósteros o estructuras similares.")
