import streamlit as st
from model import generar_receta
from config import MODEL_OPTIONS 

def main():
    
    st.title("🍽️✨ Generador de Receta✨🍽️")
    selected_model = st.selectbox("Selecciona un modelo:", list(MODEL_OPTIONS .keys()))
    model_name = MODEL_OPTIONS [selected_model]
    st.write(f"🤖Modelo seleccionado: **{model_name}🤖**")
    st.write("Introduce ingredientes y se  generará una receta.")

    ingredientes = st.text_input("📋❓ Ingresa ingredientes separados por comas:")

    if st.button("Generar Receta"):
        if ingredientes:
            lista_ingredientes = [i.strip() for i in ingredientes.split(",")]
            with st.spinner("Generando receta... 👨‍🍳"):
                receta_generada = generar_receta(lista_ingredientes, model_name)
            st.subheader("😄🍽️ Receta Generada🍲😋:")
            st.write(receta_generada)
        else:
            st.warning("⚠️😤 Por favor, introduce al menos un ingrediente.")

if __name__ == "__main__":
    main()
