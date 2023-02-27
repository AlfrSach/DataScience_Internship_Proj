import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "image", "sales.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "all_data.csv")


st.title("Dashboard - Sales Data")

img = image.imread(IMAGE_PATH)
st.image(img)


dataset = pd.read_csv(DATA_PATH)
st.dataframe(dataset)

dataset.dropna(inplace=True)
updated_dataset = dataset[dataset["Order Date"].str[0:2] != "Or"]
updated_dataset["Month"] = updated_dataset["Order Date"].str[0:2]
updated_dataset["Month"] = updated_dataset["Month"].astype("int32")

updated_dataset["Quantity Ordered"] = pd.to_numeric(updated_dataset["Quantity Ordered"])
updated_dataset["Price Each"] = pd.to_numeric(updated_dataset["Price Each"])
updated_dataset["Sales"] = updated_dataset["Quantity Ordered"] * updated_dataset["Price Each"]

col1, col2 = st.columns(2)

data_ms = updated_dataset.groupby("Month").sum()
fig1 = px.bar(data_ms, x=data_ms.index, y="Sales", labels={"x": "Month", "y": "Sales"}, title="Monthly Sales")

col1.plotly_chart(fig1, use_container_width=True)

txt = "December has the highest sales and January has the lowest sales"
col2 = st.text(txt)

