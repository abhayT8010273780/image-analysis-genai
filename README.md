# 🖼️ Image Analytics App (Streamlit + Gemini API)

This project is an **AI-powered Image Analytics web app** built with **Streamlit** and **Google Gemini Generative AI**.  
It allows users to upload an image, ask questions about it, and get intelligent responses from the Gemini model.  

---

## 🔹 Features
- 📤 Upload images (`.png`, `.jpg`, `.jpeg`)  
- 🖼️ Display uploaded image inside the app  
- 💬 Ask any question about the image using a text prompt  
- 🤖 Get responses powered by **Google Gemini (Generative AI)**  
- 🌐 Simple, interactive **Streamlit UI**  

---

## 🔹 Tech Stack
- **Python 3.9+**  
- **Streamlit** (frontend UI)  
- **Google Generative AI SDK** (`google-generativeai`)  
- **PIL (Pillow)** for image handling  

---

## 🔹 Installation & Setup

1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/image-analytics.git
   cd image-analytics
   
 # Install dependencies   
   pip install -r requirements.txt

**requirements.txt**
   pip install streamlit google-generativeai pillow
# Add your Google Gemini API Key
  Open the file app.py
  Replace the API key in:
   genai.configure(api_key="YOUR_API_KEY")
# Run the App
  streamlit run app.py
<img width="361" height="798" alt="{B0D643F5-8D51-4649-B270-31882C542038}" src="https://github.com/user-attachments/assets/cad40848-70cb-4739-a8af-c3bb6560048e" />

   
