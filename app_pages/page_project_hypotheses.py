import streamlit as st


def page_project_hypotheses_content():
    """
    Contents of Project Hypotheses
    """
    st.write("### Project Hypothesis and Validation")
    st.info(
        "1. I suspect that mildew-contained cherry leaves have clear signs on "
        "their surface to differentiate them from the uninfected leaves. \n"
        "* An average image and varability image study can help to "
        "investigate it. \n"
        "* There were clear white powdery spots on the surface of the mildew "
        "contained leaves. \n"
        "* An Image Montage shows that typically a mildew contained leaves "
        "have clear white powdery spots on the surface. \n"
        "2. I suggest that images of mildew-contained cherry leaves will have "
        "several differences compared with uninfected leaves in order to "
        "train the model with an image dataset. \n"
        "* The dataset will be analysed using train, validation, and test "
        "techniques to investigate the accuracy of image identification. \n"
        "3. The sample dataset contains images classified as infected and "
        "uninfected leaves. \n"
        "* The binary classification will be the best way to determine the "
        "difference between infected and uninftected leaves."
    )