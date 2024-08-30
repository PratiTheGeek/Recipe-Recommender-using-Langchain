import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")
cuisine=st.sidebar.selectbox('Pick a Cuisine',("Indian","Italian","MExican","Korean","Japanese"))


if cuisine:
    response=langchain_helper.generate_name_menu(cuisine)
    st.header(response["restaurant_name"])
    menu_items=response["menu_items"].strip().split(",")
    st.write("** Menu Items **")
    for item in menu_items:
        st.write("-",item)

