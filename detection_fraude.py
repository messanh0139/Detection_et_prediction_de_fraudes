import streamlit as st 
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    return joblib.load("fraud_detection_model.pkl")


model = load_model()

st.title("Application de détection et de prédiction de fraudes")
st.markdown("Veuillez saisir les détails de la transaction puis cliquer sur le bouton Prédire pour obtenir le résultat.")
st.divider()


distance_from_home = st.number_input("Distance from home", min_value=0.0, value=1000000.0)
distance_from_last_transaction = st.number_input("Distance from last transaction", min_value=0.0, value=1000000.0)
ratio_to_median_purchase_price = st.number_input("Ratio to median purchase price", min_value=0.0, value=1000000.0)
repeat_retailer = st.number_input("Repeat retailer", min_value=0.0, value=1.0)
used_chip = st.number_input("Used chip", min_value=0.0, value=1.0)
used_pin_number = st.number_input("Used PIN number", min_value=0.0, value=1.0)
online_order = st.number_input("Online order", min_value=0.0, value=1.0)

if st.button("Prédire"): 
    input_data = pd.DataFrame([{
        "distance_from_home": distance_from_home,
        "distance_from_last_transaction": distance_from_last_transaction,
        "ratio_to_median_purchase_price": ratio_to_median_purchase_price,
        "repeat_retailer": repeat_retailer,
        "used_chip": used_chip,
        "used_pin_number": used_pin_number,
        "online_order": online_order
    }]) 
    
    prediction = model.predict(input_data)[0]
    
    st.subheader(f"Prédiction : '{float(prediction)}'")
    
    if prediction == 1.0:
        st.error("Cette transaction est frauduleuse")
    else: 
        st.success("Cette transaction n'est pas frauduleuse")