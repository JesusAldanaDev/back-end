import streamlit as st
import pandas as pd
import numpy as np


def get_df():
    df = pd.DataFrame(
        np.random.randint(
            low=-10,
            high=10,
            size=(10, 10),
        ),
        columns=("col %d" % i for i in range(10)),
    )
    return df


st.title("Streamlit Basics")
st.markdown("a brief project on Streamlit widgets :sunglasses:")
st.divider()
df = get_df()

st.data_editor(df)

df_max = df.max().max()
df_min = df.min().min()
df_mean = df.mean().mean()

st.metric(
    "Max Value",
    df_max,
    delta=None,
    delta_color="normal",
    help="The max value in the dataframe",
)

st.metric(
    "min Value",
    df_min,
    delta=None,
    delta_color="normal",
    help="The min value in the dataframe",
)

st.metric(
    "mean Value",
    df_mean,
    delta=None,
    delta_color="normal",
    help="The mean value in the dataframe",
)
