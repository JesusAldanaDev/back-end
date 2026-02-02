import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


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

generate_df = st.checkbox("Generate DataFrame")
if generate_df:
    df = get_df()


st.dataframe(df)
download_button = st.download_button(
    label="Download DataFrame",
    data=df.to_csv(),
    file_name="DataFrame.csv",
)

df_max = df.max().max()
df_min = df.min().min()
df_mean = df.mean().mean()

metrics_selections = st.multiselect(
    label="select metrics to show",
    options=["Max Value", "Min Value", " average"],
    placeholder="choose an option",
)

if "Max Value" in metrics_selections:
    st.metric(
        "Max Value",
        df_max,
        delta=f"{df_max}",
        delta_color="normal",
        help="The max value in the dataframe",
    )
if "Min Value" in metrics_selections:
    st.metric(
        "min Value",
        df_min,
        delta=f"{df_min}",
        delta_color="normal",
        help="The min value in the dataframe",
    )
if " average" in metrics_selections:
    st.metric(
        "mean Value",
        df_mean,
        delta=None,
        delta_color="normal",
        help="The mean value in the dataframe",
    )

plot_type = st.radio(
    label="Select plot library",
    options=["Matplotlib", "Plotly 2D", "Plotly 3D"],
)
if "matplotlib" in plot_type:
    fig = plt.figure()
    contour = plt.contour(df)
    plt.colorbar(contour)
    st.pyplot(fig)

if "Plotly 2D" in plot_type:
    fig2 = go.Figure(data=go.Contour(z=df))
    st.plotly_chart(fig2)

if "Plotly" in plot_type:
    fig2 = go.Figure(data=go.Surface(z=df))
    st.plotly_chart(fig2)


# min 48
