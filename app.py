from langchain.chat_models import AzureChatOpenAI
import os
from dotenv import load_dotenv
import streamlit as st
# If you want AI‑generated pictures, you’ll need the OpenAI client:
#   pip install openai
import openai                           # <-- only needed for AI images

# ──────────────────────────────────
# 1️⃣  ENV & PAGE CONFIG
# ──────────────────────────────────
load_dotenv()
st.set_page_config(page_title="Backod GPT", page_icon="🧠")
st.title("Hnn.....bhai aur batao 🤓")
st.caption("8Owner of this chatbot is not responsible for any hallucination. Try at your own RISK")

# ──────────────────────────────────
# 2️⃣  OPTIONAL BANNER IMAGE
# ──────────────────────────────────
#   Put a file called 'backod_banner.png' in the same folder OR
#   replace with any public URL.
BANNER_PATH = "picpic.jpeg"
if os.path.exists(BANNER_PATH):
    st.image(BANNER_PATH, use_column_width=True)
else:
    st.image(
        "https://i.imgur.com/WOz8KdQ.png",   # fallback meme URL
        use_container_width=True,
        caption="Backod Gang aagaye! 😎"
    )

# ──────────────────────────────────
# 3️⃣  CHARACTER CONTEXT
# ──────────────────────────────────
CHARACTER_CONTEXT = """
You are chatting with a group of friends from Marwadi University:

• Aviral Bhai – SPOC & Apti Trainer  
• Rahul Bhai – Gym Boy  
• Abhinay Yadav – Sticker Boy  
• Ramesh Bhai – Silent Man  
• Kesu Bhai –  diet aachi kr rahe hai  
• Shrey Bhai – “Bhatar” of Khushi  
• Manan Bhai – IITian, greets with “Aur batao man”

They’re proud backod legends who love wasting time and roasting each other.
ALWAYS start your first reply with **“Aur batao bhai…”** and keep the tone Hinglish, light‑hearted, and packed with inside jokes.
"""

# ──────────────────────────────────
# 4️⃣  AZURE OPENAI CHAT MODEL
# ──────────────────────────────────
llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7,
)

# ──────────────────────────────────
# 5️⃣  USER INPUT + OPTIONAL IMAGE
# ──────────────────────────────────
query = st.text_input("Aur batao bhai ......? ")



# ──────────────────────────────────
# 6️⃣  GENERATE & SHOW BOT REPLY
# ──────────────────────────────────
if query:
    full_prompt = f"{CHARACTER_CONTEXT}\nUser: {query}\nAI:"
    response = llm.invoke(full_prompt)
    st.markdown(f"**Sun be:** {response.content}")
