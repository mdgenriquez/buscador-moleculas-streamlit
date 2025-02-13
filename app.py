def Home():
    st.header('De nombre común a 2D :cat:', divider='rainbow')
    st.sidebar.markdown("# Nombre clásico:")
    st.sidebar.markdown("Trivial name, non-systematic name for a chemical substance, son otras denominaciones en inglés")

    entrada = st.text_input("Escribe el nombre común en inglés:", "glucose")
    
    st.markdown("### IUPAC")  
    nombreiupac = pcp.get_compounds(entrada,'name')
    st.text(nombreiupac[0].iupac_name)
    
    st.markdown("### SMILES Isomérico")
    smilesisomerico = get_compounds(entrada, 'name')
    st.text(smilesisomerico[0].isomeric_smiles)

    st.markdown("### Masa molecular (g/mol)")
    masamolecular = get_compounds(entrada, 'name')
    st.text(masamolecular[0].exact_mass)
  
    st.markdown("### Coeficiente de partición")
    coeficientedeparticion = get_compounds(entrada, 'name')
    st.text(coeficientedeparticion[0].xlogp)

    st.markdown("### PubChem ID")
    id_pubchem = pcp.get_compounds(entrada, 'name')
    st.text(id_pubchem)

    st.markdown("### Representación simplificada")
    m0 = Chem.MolFromSmiles(smilesisomerico[0].isomeric_smiles)    
    Draw.MolToFile(m0,'mol0.png')
    #st.pyplot()
    st.write('Molecule 2D :smiley:')
    st.image('mol0.png')

#############################Pagina 2############################## 

def page2():
    st.header('De SMILES a 2D :smiley:', divider='rainbow')
    st.sidebar.markdown("# Simplified Molecular Input Line Entry System")
    st.sidebar.markdown("Sistema de introducción molecular lineal simplificada")
    
    entrada = st.text_input("Escribe el nombre SMILES: ", "C1=CC2=C(C3=C(C=CC=N3)C=C2)N=C1")
    st.markdown("### PubChem ID:")
    identificador = pcp.get_compounds(entrada, 'smiles')
    st.text(identificador)

    st.markdown("### Nombre IUPAC")  
    nombreiupac = pcp.get_compounds(entrada,'smiles')
    st.text(nombreiupac[0].iupac_name)

    st.markdown("### Representación simplificada")
    m1 = Chem.MolFromSmiles(entrada)    
    Draw.MolToFile(m1,'mol1.png')
    st.write('Molecule 2D :smiley:')
    st.image('mol1.png')
