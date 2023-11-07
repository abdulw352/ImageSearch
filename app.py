import streamlit as st
from multimodel_search import MultiModalSearch

st.set_page_config(
    layout="wide"
)

def main():
    st.markdown("<h1 style = `text-align: center, color: green;`> Search the right Fashion for you! </h1>", unsafe_allow_html=True)

    query = st.text_input("Enter your query:")
    if st.button("Search"):
        if len(query) > 0:
            results = MultiModalSearch.search(query)
            st.warning("Searching for: ", query)
            st.warning("Search Results: ")
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                st.write(f"Score: {round(results[0].score*100, 2)}%")
                st.image(results[0].content, use_column_width=True)
            with col2:
                st.write(f"Score: {round(results[1].score*100, 2)}%")
                st.image(results[1].content, use_column_width=True)
            with col3:
                st.write(f"Score: {round(results[2].score*100, 2)}%")
                st.image(results[2].content, use_column_width=True)
        
        else:
            st.warning("Search clothes ...")


if __name__ == "__main__":
    main()