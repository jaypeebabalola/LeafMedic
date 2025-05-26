# 🌿 LeafMedic

**LeafMedic** is a Streamlit web app that uses a deep learning model to identify medicinal leaves and provide their traditional medicinal uses in multiple Nigerian languages.

## 🚀 Features

- Upload or capture a photo of a leaf
- Classifies the leaf using a trained TensorFlow model
- Displays the leaf name and its medicinal uses
- Supports 4 languages: English, Hausa, Yoruba, and Igbo
- Beautiful modern UI with responsive layout

## 🖼 Demo

![Demo Screenshot](https://img.icons8.com/ios-filled/100/ffffff/leaf.png)

## 🧠 How It Works

- The app uses a `.h5` model trained to classify leaf images.
- The class name is used to retrieve medicinal uses from a JSON file.
- Output is displayed in a styled Streamlit card.

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/jaypeebabalola/LeafMedic.git
cd LeafMedic
