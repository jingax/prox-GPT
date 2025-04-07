# 🚀 prox-GPT

prox-GPT is a Streamlit app that you can **fork, customize, and deploy for free** using [Streamlit Community Cloud](https://streamlit.io/cloud). Just plug in your own API keys and you're good to go!

---

## 🛠 Features

- ✨ Easy-to-use interface
- 🔐 Secure API key handling via Streamlit secrets
- ☁️ Instant deploy on Streamlit Cloud
- 🔌 Supports **OpenAI API** or **Lambda Labs API**

---

## 🚀 How to Deploy Your Own Version

### 1. **Fork this repo**

Click the **Fork** button in the top-right corner of this GitHub page.

---

### 2. **Deploy to Streamlit**

Go to [Streamlit Cloud](https://streamlit.io/cloud) and click **"New App"**.  
Select your forked repo and branch, and proceed.

---

### 3. **Set up Secrets**

Under **Advanced Settings**, add your secrets like this:

```toml
[api]
openai = "your-openai-api-key"
pass = "your-app-password"
```
