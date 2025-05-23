import streamlit as st
from evaluator import evaluate_bmc
from PIL import Image

# Set page config with custom favicon and layout
st.set_page_config(
    page_title="BMC Evaluator AI",
    page_icon="📊",
    layout="wide"
)

# Sidebar branding
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/1/1f/Business_Model_Canvas.png", use_column_width=True)
st.sidebar.title("The Business Model Engineer")
st.sidebar.markdown("**Course Tool:** Business Modeling Innovation and Financial Engineering (BMIFE)")
st.sidebar.markdown("Made with ❤️ by [Your Name or Brand]")

# Hero Section with image and headline
st.image("https://miro.medium.com/v2/resize:fit:1400/1*Du58QcZQn7LmsYtuvEnH9Q.png", use_column_width=True)
st.title("📊 Business Model Canvas Evaluator AI")
st.subheader("Optimize and analyze startup strategies using AI-powered feedback.")

# Instructions
st.markdown("""
Welcome to your Business Model Evaluator. Paste or upload your BMC and get instant feedback across all 9 blocks.
Use it to refine your strategy and improve alignment before presenting your model.
""")

# BMC input text area
bmc_input = st.text_area("Paste your BMC as text (or simulate):", height=300)

# Evaluate Button
if st.button("Evaluate"):
    if bmc_input.strip() == "":
        st.warning("Please paste your BMC content before evaluating.")
    else:
        total, scores, feedback = evaluate_bmc(bmc_input)
        st.success(f"Total Score: {total}/100")
        st.subheader("Section-by-Section Scores and Feedback")
        for section in scores:
            st.markdown(f"**{section}**  \nScore: {scores[section]}  \nFeedback: _{feedback[section]}_")

# Footer
st.markdown("---")
st.caption("© 2025 The Business Model Engineer — Empowering Strategy Through Modeling")
