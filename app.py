import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import json

# Load model
model = tf.keras.models.load_model("medicinal_leaves_model.h5")

# Load leaf medicinal usage data
with open("leaf_medicinal_uses.json", "r", encoding="utf-8") as f:
    medicinal_data = json.load(f)

class_names = list(medicinal_data["en"].keys())

# Language mapping
lang_map = {"English": "en", "Hausa": "ha", "Yoruba": "yo", "Igbo": "ig"}

# CSS for enhanced design
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(135deg, rgba(46,125,50,0.9), rgba(27,94,32,0.9));
        color: #fff;
    }
    .leaf-card {
        background: white;
        border-radius: 20px;
        padding: 2em;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        text-align: center;
        max-width: 500px;
        margin: auto;
    }
    .upload-btn {
        background-color: #4caf50;
        color: white;
        padding: 0.75em 1.5em;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
    }
    .leaf-bg {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        background-image: url('https://cdnjs.cloudflare.com/ajax/libs/ionicons/5.1.0/collection/components/icon/svg/leaf.svg');
        background-repeat: repeat;
        background-size: 100px;
        opacity: 0.5;
        z-index: -1;
    }
    </style>
    <div class="leaf-bg"></div>
""", unsafe_allow_html=True)

# App header
with st.container():
    #st.markdown('<div class="leaf-card" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown('''
    <div style="
        background: transparent;
        text-align: center;
        padding: 2em;
        margin: auto;">
''', unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios-filled/100/ffffff/leaf.png", width=120)
    st.markdown("## <strong><span style='color:ffffff;'>LeafMedic</span><strong>", unsafe_allow_html=True)
    st.write("Upload or capture a leaf image to identify it and discover its medicinal benefits.")
    st.markdown("</div>", unsafe_allow_html=True)

# Image input
col1, col2 = st.columns(2)
with col1:
    option = st.radio("Input Method:", ["Upload Image", "Snap Photo"])
with col2:
    language = st.selectbox("Language:", list(lang_map.keys()))

img = None
if option == "Upload Image":
    uploaded_file = st.file_uploader("Choose a leaf image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
elif option == "Snap Photo":
    camera_img = st.camera_input("Take a leaf photo")
    if camera_img:
        img = Image.open(camera_img).convert("RGB")

# Process image and show result
if img:
    st.image(img, caption="🌿 Input Leaf Image", use_column_width=True)
    with st.spinner("Identifying leaf..."):
        img = img.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = model.predict(img_array)
        class_idx = np.argmax(prediction)
        leaf_name = class_names[class_idx]
        lang_code = lang_map[language]
        usage = medicinal_data.get(lang_code, {}).get(leaf_name, "Usage not available.")

    # Output card
    st.markdown(f"""
        <div class="leaf-card">
            <h4 style='color:#2e7d32; font-family: sans-serif; font-weight: 600;'>
                🌿 Identified Leaf: <span style='color:#4caf50;'>{leaf_name}</span>
            </h4>
            <p style='font-size: 16px; color:#333; font-family: sans-serif;'>
                💊 <strong style='margin-right: 0.5em;'>Medicinal Usage:</strong>{usage}
            </p>
        </div>
    """, unsafe_allow_html=True)

