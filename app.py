import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(
    page_title="Noida House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

model = pickle.load(open("house_price_model.pkl", "rb"))
df = pd.read_csv("cleaned2.csv")

locations = sorted(df["Location"].unique())

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right, #eef2ff, #f8fafc);
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #475569;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .prediction-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: 20px;
    }

    .price {
        font-size: 40px;
        color: #16a34a;
        font-weight: bold;
    }

    .feature-card {
        background: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🏠 Noida House Price Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict estimated house prices in Noida</div>',
    unsafe_allow_html=True,
)

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns([2, 1])

with col1:

    location = st.selectbox("📍 Select Location", locations)

    bhk = st.slider("🛏 Number of BHK", min_value=1, max_value=10, value=3)

    area = st.number_input(
        "📐 Area in Square Feet",
        min_value=300,
        max_value=10000,
        value=1500,
        step=50,
    )

    area_per_bhk = area / bhk

    predict_btn = st.button("Predict Price", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80",
        use_container_width=True,
    )

# ---------------- PREDICTION ----------------
if predict_btn:
    input_df = pd.DataFrame(
        {
            "Area in Sqrt": [area],
            "No.of Bhk": [bhk],
            "Location": [location],
            "area_per_bhk": [area_per_bhk],
        }
    )

    prediction_log = model.predict(input_df)[0]
    prediction = np.expm1(prediction_log)

    # Convert into lakhs and crores for better display
    if prediction >= 10000000:
        display_price = f"₹ {prediction / 10000000:.2f} Cr"
    else:
        display_price = f"₹ {prediction / 100000:.2f} Lakhs"

    st.markdown(
        f"""
        <div class="prediction-box">
            <h2>Estimated House Price</h2>
            <div class="price">{display_price}</div>
            <p>for a {bhk} BHK house in <b>{location}</b> with area <b>{area} sq.ft</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Show similar properties
    st.subheader("Similar Properties from Dataset")

    similar = df[
        (df["Location"] == location)
        & (df["No.of Bhk"] == bhk)
    ].copy()

    if not similar.empty:
        similar = similar[["Location", "No.of Bhk", "Area in Sqrt", "price_rupees"]]
        similar = similar.rename(
            columns={
                "No.of Bhk": "BHK",
                "Area in Sqrt": "Area (sq.ft)",
                "price_rupees": "Price (₹)",
            }
        )
        st.dataframe(similar.head(10), use_container_width=True)
    else:
        st.info("No similar properties found in the dataset.")
