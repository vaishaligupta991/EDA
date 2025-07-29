import streamlit as st
from PIL import Image
import os

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🎨 Page Styling
st.markdown(
    """
    <style>
        .big-title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #4B0082;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 40px;
        }
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
        }
        .card {
            background-color: #f9f9f9;
            border-radius: 20px;
            padding: 20px;
            width: 280px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .emoji {
            font-size: 40px;
        }
        .card-title {
            font-size: 22px;
            margin: 10px 0;
            color: #333;
        }
        .card-desc {
            font-size: 16px;
            color: #666;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 💜 Title and Subtitle
st.markdown("<div class='big-title'>మన భాష</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A Celebration of Telugu Stories, Art & Culture 🌾</div>", unsafe_allow_html=True)

# 👋 Welcome Text
st.success("👋 Welcome to Mana Basha! Explore and contribute to Telugu culture by sharing stories, memes, recipes, and art.")

# 🖼️ Optional: Featured Image
banner_path = "assets/logo.png"
if os.path.exists(banner_path):
    st.image(banner_path, use_container_width=True)

# 📦 Feature Cards
st.markdown("<div class='card-container'>", unsafe_allow_html=True)

cards = [
    {"emoji": "📖", "title": "Share Stories", "desc": "Tell your village tales, grandma's fables, or real-life Telugu experiences."},
    {"emoji": "🍛", "title": "Post Recipes", "desc": "Preserve and share your family’s secret recipes and dishes from your region."},
    {"emoji": "🎨", "title": "Upload Art", "desc": "Showcase your digital or hand-made Telugu-themed art and illustrations."},
    {"emoji": "😂", "title": "Add Memes", "desc": "Create and upload memes using Telugu language, dialects, and culture."},
    {"emoji": "🧠", "title": "Share Riddles", "desc": "Post Telugu riddles, puzzles or proverbs unique to your area."}
]

for card in cards:
    st.markdown(
        f"""
        <div class='card'>
            <div class='emoji'>{card["emoji"]}</div>
            <div class='card-title'>{card["title"]}</div>
            <div class='card-desc'>{card["desc"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)
