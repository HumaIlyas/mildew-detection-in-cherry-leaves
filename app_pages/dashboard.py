import streamlit as st


class DashBoard:
    """ Class to generate multiple Streamlit pages using an object
    oriented approach
    """

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🍂" # add an icon to personalize the App
            # Links for icons reference
            # https://docs.streamlit.io/en/stable/api.html#streamlit.set_page_config
            # https://twemoji.maxcdn.com/2/test/preview.html
        )

    def add_page(self, title, func) -> None:
        """ Appends title"""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """Set title and menu names"""
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
