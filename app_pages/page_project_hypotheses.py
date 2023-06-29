import streamlit as st


def page_project_hypotheses_content():
    """
    Contents of Project Hypotheses
    """
    st.write("### Project Hypothesis and Validation")
    st.info(
        "1. I suspect that mildew-contained cherry leaves have clear signs on their surface to differentiate them from the uninfected leaves. \n"
        "2. We suggest that images of Cherry leaves with powdery mildew will have enough differences compared to those without the disease in order to train the model with an image dataset. \n"
        "3. The sample dataset contains images classified as infected and uninfected leaves. The binary classification will be the best way to determine the difference between infected and uninftected leaves."
    )
