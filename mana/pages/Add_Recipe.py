import streamlit as st
import os
import json
from datetime import datetime
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.rewards import award_user


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Add Recipe", page_icon="🧑‍🍳")

st.markdown("## 🧑‍🍳 Share a Traditional Telugu Recipe")

# Inputs
recipe_title = st.text_input("🍲 Recipe Name")
ingredients = st.text_area("📝 Ingredients (list them line by line)")
steps = st.text_area("🔥 Preparation Steps")
recipe_image = st.file_uploader("📸 Upload a photo of the dish", type=["jpg", "jpeg", "png"])

# Single Submit Button
if st.button("📤 Submit Recipe"):
    if recipe_title and ingredients and steps:
        os.makedirs("data/recipes", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        safe_title = recipe_title.replace(" ", "_").lower()

        # Save recipe text
        with open(f"data/recipes/{safe_title}_{timestamp}.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {recipe_title}\n")
            f.write(f"Ingredients:\n{ingredients}\n\n")
            f.write(f"Preparation Steps:\n{steps}\n")

        # Save image
        if recipe_image:
            img_path = f"data/recipes/{safe_title}_{timestamp}.jpg"
            with open(img_path, "wb") as img_file:
                img_file.write(recipe_image.read())

        # ✅ Give reward
        reward = award_user("recipe")
        st.success("✅ Recipe submitted successfully!")

        st.markdown(
            f"""<div class="reward-toast">🎉 మీకు **{reward['badge_name_tel']}** {reward['badge_emoji']} బహుమతి లభించింది (+{reward['points']} pts)!</div>""",
            unsafe_allow_html=True
        )

        # ✅ Optional tag
        feedback = st.text_input("💬 Add a tag or keyword for your submission (e.g., #sweet, #festival_food)", key="recipe_tag")
        if feedback:
            with open("data/tags.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps({
                    "tag": feedback.strip(),
                    "activity": reward['activity'],
                    "time": reward['timestamp']
                }, ensure_ascii=False) + "\n")
            st.success("✅ Tag saved! Thanks for improving the content search.")
    else:
        st.warning("⚠️ Please fill all the fields before submitting.")
