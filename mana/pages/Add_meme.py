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
st.markdown("<h2 style='text-align: center; color: #FF5722;'>🤣 Share a Telugu Meme</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Make someone laugh today with your funny Telugu meme!</p>", unsafe_allow_html=True)

# Meme creator name
meme_creator = st.text_input("😎 Meme Creator Name (optional)")

# Meme Title
meme_title = st.text_input("🏷️ Meme Title")

# Upload Meme Image
uploaded_meme = st.file_uploader("📤 Upload your meme (JPG/PNG)", type=["jpg", "jpeg", "png"])

# Optional Caption
meme_caption = st.text_area("📝 Add a caption (optional)")

# ✅ Single Submit Button
if st.button("📤 Submit Meme"):
    if meme_title and uploaded_meme:
        os.makedirs("data/memes", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        safe_title = meme_title.replace(" ", "_").lower()

        # Save image
        meme_path = f"data/memes/{safe_title}_{timestamp}.jpg"
        with open(meme_path, "wb") as img_file:
            img_file.write(uploaded_meme.read())

        # Save caption if any
        if meme_caption:
            with open(f"data/memes/{safe_title}_{timestamp}.txt", "w", encoding="utf-8") as f:
                f.write(f"Title: {meme_title}\n")
                f.write(f"Creator: {meme_creator or 'Anonymous'}\n")
                f.write(f"Caption:\n{meme_caption.strip()}\n")

        # Show preview
        st.success("✅ Meme submitted successfully!")
        st.markdown(f"### 🏷️ {meme_title} by {meme_creator or 'Anonymous'}")
        st.image(meme_path, use_column_width=True)
        if meme_caption:
            st.markdown("#### 🗨️ Caption:")
            st.markdown(f"<pre>{meme_caption}</pre>", unsafe_allow_html=True)

        # ✅ Reward system
        reward = award_user("meme")
        st.markdown(
            f"""<div class="reward-toast">🎉 మీకు **{reward['badge_name_tel']}** {reward['badge_emoji']} బహుమతి లభించింది (+{reward['points']} pts)!</div>""",
            unsafe_allow_html=True
        )

        # ✅ Optional tag
        feedback = st.text_input("💬 Add a tag or theme (e.g., #funny, #college_memes)", key="meme_tag")
        if feedback:
            with open("data/tags.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps({
                    "tag": feedback.strip(),
                    "activity": reward['activity'],
                    "time": reward['timestamp']
                }, ensure_ascii=False) + "\n")
            st.success("✅ Tag saved! Helps us organize better.")
    else:
        st.error("❌ Please provide at least a title and image.")
