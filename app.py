import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw, rdFMCS
from rdkit.Chem.Draw import rdMolDraw2D
from io import BytesIO

def mol_to_svg(mol):
    drawer = rdMolDraw2D.MolDraw2DSVG(300, 300)
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()
    return drawer.GetDrawingText()

def find_bioisosteres(mol):
    # Función simulada para búsqueda de bioisósteros (se puede mejorar con una base de datos real)
    return [mol]  # Retorna la misma molécula como ejemplo

st.title("Buscador de Bioisósteros en 2D")

smiles_input = st.text_input("Introduce un SMILES:")
if smiles_input:
    try:
        mol = Chem.MolFromSmiles(smiles_input)
        if mol:
            st.subheader("Estructura ingresada:")
            st.image(Draw.MolToImage(mol), caption="Molécula ingresada", use_column_width=False)
            
            bioisosteres = find_bioisosteres(mol)
            st.subheader("Bioisósteros encontrados:")
            for bioiso in bioisosteres:
                st.image(Draw.MolToImage(bioiso), caption="Bioisóstero", use_column_width=False)
        else:
            st.error("No se pudo interpretar el SMILES ingresado.")
    except Exception as e:
        st.error(f"Error al procesar la molécula: {e}")
