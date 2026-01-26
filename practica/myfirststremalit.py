import streamlit as st
import pandas as pd

st.write("Hello, World!")

x = st.slider("x")
st.write(x, "Squared is", x * x)

my_text = st.text_input("Your name", key="name")
st.write(my_text)

df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

st.write("Here's a simple DataFrame:")
st.dataframe(df)
