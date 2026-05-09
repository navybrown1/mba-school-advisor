import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(
    page_title="MBA School Advisor · Career Analytics",
    page_icon="🎓",
    layout="wide",
)

# Hide Streamlit chrome so the custom UI fills the window
st.markdown("""
<style>
  #MainMenu, header, footer { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stAppViewContainer"] { padding: 0; }
</style>
""", unsafe_allow_html=True)

html = pathlib.Path("MBA_Advisor.html").read_text(encoding="utf-8")
components.html(html, height=960, scrolling=True)
