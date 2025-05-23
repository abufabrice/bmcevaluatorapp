import streamlit as st
from evaluator import evaluate_bmc
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# Set page config
st.set_page_config(page_title="BMC Evaluator AI", page_icon="📊", layout="wide")

# Sidebar branding
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/1/1f/Business_Model_Canvas.png", use_container_width=True)
st.sidebar.title("The Business Model Engineer")
st.sidebar.markdown("**Course Tool:** Business Modeling Innovation and Financial Engineering (BMIFE)")
st.sidebar.markdown("Made with ❤️ by [Your Name or Brand]")

# Hero image and headline
st.image("https://miro.medium.com/v2/resize:fit:1400/1*Du58QcZQn7LmsYtuvEnH9Q.png", use_container_width=True)
st.title("📊 Business Model Canvas Evaluator AI")
st.subheader("Optimize and analyze startup strategies using AI-powered feedback.")

# Instructions
st.markdown("""
Welcome to your Business Model Evaluator. Paste or upload your BMC and get instant feedback across all 9 blocks.
Use it to refine your strategy and improve alignment before presenting your model.
""")

# BMC input area
bmc_input = st.text_area("Paste your BMC as text (or simulate):", height=300)

# Evaluate button
if st.button("Evaluate"):
    if bmc_input.strip() == "":
        st.warning("Please paste your BMC content before evaluating.")
    else:
        total, scores, feedback = evaluate_bmc(bmc_input)
        st.success(f"Total Score: {total}/100")

        # Display feedback and scores
        st.subheader("Section-by-Section Scores and Feedback")
        for section in scores:
            st.markdown(f"**{section}**  \nScore: {scores[section]}  \nFeedback: _{feedback[section]}_")

        # Convert scores to DataFrame
        df = pd.DataFrame({
            "Section": list(scores.keys()),
            "Score": list(scores.values())
        })

        # Bar Chart
        st.subheader("📊 Bar Chart of Scores")
        st.bar_chart(df.set_index("Section"))

        # Pie Chart
        st.subheader("📈 Pie Chart of Scores")
        fig, ax = plt.subplots()
        ax.pie(df["Score"], labels=df["Section"], autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

        # CSV Download
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Evaluation Results (CSV)",
            data=csv,
            file_name="bmc_evaluation_results.csv",
            mime="text/csv"
        )

# Footer
st.markdown("---")
st.caption("© 2025 The Business Model Engineer — Empowering Stra
