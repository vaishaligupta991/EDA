import streamlit as st
from PIL import Image
import os
import json
from datetime import datetime
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.rewards import award_user


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Logo (optional)
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, use_container_width=True)

# Title
st.markdown("<h2 style='text-align: center; color: #9C27B0;'>🎨 Upload Your Telugu Art</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Share your drawings, rangoli, folk paintings, or modern creations!</p>", unsafe_allow_html=True)

# Inputs
artist_name = st.text_input("👩‍🎨 Artist Name (optional)")
art_title = st.text_input("🖼️ Art Title")
description = st.text_area("📝 Describe your art")
uploaded_art = st.file_uploader("📤 Upload your artwork (JPG/PNG)", type=["jpg", "jpeg", "png"])

# ✅ Single Submit Button
if st.button("📤 Submit Artwork"):
    if art_title and description and uploaded_art:
        os.makedirs("data/art", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        safe_title = art_title.replace(" ", "_").lower()

        # Save image
        art_path = f"data/art/{safe_title}_{timestamp}.jpg"
        with open(art_path, "wb") as img_file:
            img_file.write(uploaded_art.read())

        # Save description
        with open(f"data/art/{safe_title}_{timestamp}.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {art_title}\n")
            f.write(f"Artist: {artist_name or 'Anonymous'}\n")
            f.write(f"Description:\n{description.strip()}\n")

        # ✅ Show preview
        st.success("✅ Artwork submitted successfully!")
        st.markdown(f"### 🖌️ {art_title} by {artist_name or 'Anonymous'}")
        st.image(art_path, use_column_width=True)
        st.markdown("#### 📝 Description:")
        st.markdown(f"<pre>{description}</pre>", unsafe_allow_html=True)

        # ✅ Trigger reward
        reward = award_user("art")
        st.markdown(
            f"""<div class="reward-toast">🎉 మీకు **{reward['badge_name_tel']}** {reward['badge_emoji']} బహుమతి లభించింది (+{reward['points']} pts)!</div>""",
            unsafe_allow_html=True
        )

        # ✅ Optional tag
        feedback = st.text_input("💬 Add a tag or theme (e.g., #rangoli, #folkart)", key="art_tag")
        if feedback:
            with open("data/tags.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps({
                    "tag": feedback.strip(),
                    "activity": reward['activity'],
                    "time": reward['timestamp']
                }, ensure_ascii=False) + "\n")
            st.success("✅ Tag saved! Helps us organize better.")
    else:
        st.error("❌ Please fill all required fields and upload an image.")
