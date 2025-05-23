import streamlit as st
from evaluator import evaluate_bmc

st.set_page_config(page_title="BMC Evaluator AI", layout="wide")

st.title("📊 Business Model Canvas Evaluator AI")
st.write("Upload your BMC (as text) and receive instant feedback.")

bmc_input = st.text_area("Paste your BMC as text (or simulate):")

if st.button("Evaluate"):
    if bmc_input.strip() == "":
        st.warning("Please paste a BMC first.")
    else:
        total, scores, feedback = evaluate_bmc(bmc_input)
        st.success(f"Score: {total}/100")
        st.subheader("Detailed Breakdown")
        for k in scores:
            st.write(f"**{k}** — {scores[k]} pts — 💬 _{feedback[k]}_")
