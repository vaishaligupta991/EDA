import streamlit as st
import json
import os
st.set_page_config(page_title="మన భాష", page_icon="🌾", layout="wide")

st.markdown(
    """
    <style>
        .main-title {
            font-size: 3rem;
            font-weight: bold;
            color: #4B0082;
        }
        .sub-title {
            font-size: 1.5rem;
            color: #555;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="main-title">మన భాష</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">A Celebration of Telugu Stories, Art & Culture 🌾</p>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("👋 **Welcome to Mana Basha!** Explore and contribute to Telugu culture by sharing stories, memes, recipes, and art.")

# Sidebar navigation info
st.sidebar.success("👈 Select a page from the left sidebar to begin!")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌟 Pages")
st.sidebar.markdown("- Home")
st.sidebar.markdown("- Add Story")
st.sidebar.markdown("- Add Meme")
st.sidebar.markdown("- Add Recipe")
st.sidebar.markdown("- Add Art")
st.sidebar.markdown("- View Submissions")
st.sidebar.markdown("---")
st.sidebar.markdown("🚀 Built with ❤️ by Team Mana Basha")
st.sidebar.markdown("### 🎁 మీ బహుమతులు")
rewards_path = "data/rewards.jsonl"

if os.path.exists(rewards_path):
    with open(rewards_path, "r", encoding="utf-8") as f:
        recent = [json.loads(line) for line in f.readlines()][-3:]  # last 3 rewards
        for r in reversed(recent):
            st.sidebar.markdown(f"- {r['badge_emoji']} **{r['badge_name_tel']}** (+{r['points']} pts)")
else:
    st.sidebar.info("ఇంకా బహుమతులు లేవు. ఒకటి పోస్ట్ చేయండి!")

st.sidebar.markdown("---")
st.markdown(
    """
    <style>
    .reward-toast {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 1em;
        margin: 1em 0;
        font-size: 1.2rem;
        font-weight: bold;
        font-family: 'Noto Sans Telugu', sans-serif;
        animation: popin 0.5s ease-out;
        border-radius: 8px;
        color: #5c440d;
    }

    @keyframes popin {
        from { transform: scale(0.9); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)
