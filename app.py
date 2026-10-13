impotant streamlit as st

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Color Studio",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 Textile Color Studio")
st.subheader("Fabric Color Analysis Using L*a*b* Values")

st.write(
    "This application helps textile students explore "
    "fabric colors and understand L*a*b* color values."
)

st.divider()

st.header("🎨 Choose Your Fabric Color")

col1, col2 = st.columns(2)

with col1:
    color = st.color_picker(
        "Select a fabric color",
        "#2E86AB"
    )

    st.markdown(
        f"""
        <div style="
            background-color: {color};
            height: 180px;
            border-radius: 12px;
            border: 2px solid #dddddd;
        "></div>
        """,
        unsafe_allow_html=True
    )

    st.write("Selected color:", color)

with col2:
    st.header("L*a*b* Color Values")

    L = st.slider("L* — Lightness", 0.0, 100.0, 60.0)
    a = st.slider("a* — Green to Red", -128.0, 127.0, 20.0)
    b = st.slider("b* — Blue to Yellow", -128.0, 127.0, 30.0)

    st.metric("Lightness (L*)", f"{L:.1f}")
    st.metric("Green–Red (a*)", f"{a:.1f}")
    st.metric("Blue–Yellow (b*)", f"{b:.1f}")

st.divider()

st.header("📊 Color Analysis")

data = {
    "Parameter": ["L*", "a*", "b*"],
    "Value": [L, a, b],
    "Meaning": [
        "Lightness",
        "Green (-) / Red (+)",
        "Blue (-) / Yellow (+)"
    ]
}

st.dataframe(
    pd.DataFrame(data),
    use_container_width=True,
    hide_index=True
)

st.info(
    "Note: The L*a*b* sliders are manually adjustable. "
    "They do not automatically measure the selected HEX color. "
    "Real fabric measurements require a calibrated color "
    "measurement device or a validated color conversion method."
)

st.success("Welcome to Textile Color Studio!")
