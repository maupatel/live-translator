import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Live AI Translator", page_icon="🎙️", layout="centered")

st.title("🎙️ Live AI Translator")
st.caption(
    "Real-time speech → English. Press **Translate**, allow the microphone, "
    "and read the live English below. Works best in Chrome or Edge."
)

PAGES_URL = "https://maupatel.github.io/live-translator/"

# Reliable fallback: open the tool full-screen in a new tab (top-level = full mic access).
st.link_button("🔊 Open full-screen translator (best for microphone)", PAGES_URL, use_container_width=True)

st.divider()
st.write("**Embedded version** (microphone may be blocked inside Streamlit's frame — use the button above if so):")

# Embed the tool. allow="microphone" delegates mic permission into the inner frame.
components.html(
    f"""
    <iframe src="{PAGES_URL}"
            allow="microphone; clipboard-write"
            style="width:100%; height:640px; border:1px solid #334155; border-radius:14px;">
    </iframe>
    """,
    height=660,
)

st.divider()
with st.expander("ℹ️ Notes & limitations"):
    st.markdown(
        """
- **Browser:** live speech recognition works in **Chrome / Edge** (desktop, and Chrome on Android). iPhone Safari won't do the mic part.
- **Translation:** AI-powered, auto-detects the spoken language (any of ~80), renders English.
- If the embedded mic is blocked by Streamlit's sandbox, click **Open full-screen translator** above — that always works.
        """
    )
