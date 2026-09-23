import streamlit as st

from ai.query_parser import parse_user_query
from ai.explainer import explain_recommendations
from recommendation.recommender import recommend_products


st.set_page_config(
    page_title="AI Smart Product Recommender",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI-Based Smart Product Recommendation System")

st.write(
    "Describe what product you are looking for, and the system "
    "will understand your requirements and recommend suitable products."
)

st.subheader("Enter Your Requirements")

query = st.text_area(
    "Describe your requirements",
    placeholder=(
        "Example: I need a smartphone under 30000 rupees "
        "with a very good camera, strong battery and good gaming performance."
    ),
    height=120
)


if st.button("🔍 Get Recommendations"):

    if not query.strip():
        st.warning("Please enter your product requirements.")
        st.stop()

    with st.spinner("Understanding your requirements..."):

        try:
            preferences = parse_user_query(query)

        except Exception as e:
            st.error(f"AI processing failed: {e}")
            st.stop()

    st.subheader("📋 Extracted Requirements")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Budget", f"₹{preferences.budget:,.0f}")
    col2.metric("Camera", f"{preferences.camera_priority:.0%}")
    col3.metric("Battery", f"{preferences.battery_priority:.0%}")
    col4.metric("Performance", f"{preferences.performance_priority:.0%}")

    with st.spinner("Calculating fuzzy recommendation scores..."):

        try:
            recommendations = recommend_products(preferences)

        except Exception as e:
            st.error(f"Recommendation failed: {e}")
            st.stop()

    st.subheader("🏆 Recommended Products")

    for product in recommendations[:3]:

        with st.container():

            st.markdown(f"### {product['product_name']}")

            col1, col2, col3, col4 = st.columns(4)

            col1.write(f"💰 **Price:** ₹{product['price']:,.0f}")
            col2.write(f"📷 **Camera:** {product['camera']}/100")
            col3.write(f"🔋 **Battery:** {product['battery']}/100")
            col4.write(
                f"⚡ **Performance:** {product['performance']}/100"
            )

            st.progress(
                min(int(product["score"]), 100),
                text=f"Recommendation Score: {product['score']}/100"
            )

            st.divider()

    with st.spinner("Generating AI explanation..."):

        try:
            explanation = explain_recommendations(
                preferences.model_dump(),
                recommendations[:3]
            )

        except Exception as e:
            st.error(f"Explanation generation failed: {e}")
            st.stop()

    st.subheader("💡 AI Explanation")

    st.write(explanation)