import streamlit as st


def page_project_summary_content():
    """
    Contents of Project Summary
    """
    st.write("### Project Summary")
    
    st.info(
        f"**General Information**\n"
        f"* Powdery Mildew is a fungal disease infecting herbaceous and woody plants, and can result "
        f"in a low fruit yield in the case of Cherry Trees.\n"
        f"* The current process is manual verification if a given cherry tree contains powdery"
        f"mildew or not.\n"
        f"* An employee spends around 30 minutes in each tree, taking a few samples of"
        f"tree leaves and verifying visually if the leaf tree is healthy or has powdery"
        f"mildew.\n"
        f"* [Powdery mildew](https://en.wikipedia.org/wiki/Powdery_mildew) is a "
        f"fungal disease that affects a wide range of plants, and is caused by "
        f"many different species of ascomycete fungi in the order Erysiphales. "
        f"Powdery mildew is one of the easier plant diseases to identify, "
        f"as its symptoms are quite distinctive. Infected plants display white "
        f"powdery spots on the leaves and stems.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains +4 thousand images of cherry leaves taken from the client's crop fields:\n"
        f"* 2104 images of cherry leaves which are healthy\n"
        f"* 2104 images of cherry leaves containing powdery mildew\n"
        f"* For additional information about the data, please visit "
        f"[Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/HumaIlyas/mildew-detection-in-cherry-leaves/blob/main/README.md).")


    st.success(
        f"**Business requirements**\n"
        f"* The project has two business requirements:\n"
        f"* The client is interested in conducting a study to visually differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )
