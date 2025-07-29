import streamlit as st
import pandas as pd
import os

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📂 View Submissions")
st.markdown("See all the beautiful contributions by users! ✨")

tabs = ["Stories", "Recipes", "Memes", "Art"]
choice = st.radio("Select what you want to view:", tabs)

file_map = {
    "Stories": "data/stories.csv",
    "Recipes": "data/recipes.csv",
    "Memes": "data/memes.csv",
    "Art": "data/art.csv"
}

selected_file = file_map.get(choice)

if os.path.exists(selected_file):
    df = pd.read_csv(selected_file)

    # Show the table
    st.dataframe(df, use_container_width=True)

    # Allow downloading
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=f"📥 Download {choice} CSV",
        data=csv,
        file_name=f"{choice.lower()}.csv",
        mime='text/csv',
    )
else:
    st.warning(f"No {choice.lower()} submissions found yet.")
