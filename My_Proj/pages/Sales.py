import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px

st.title("Dashboard - Sales Data")

img = image.imread(r"C:\Users\tripl\OneDrive\Desktop\Python\Innomatics Internship\My_Proj\resources\image\sales.jpg")
st.image(img)


dataset = pd.read_csv(r"C:\Users\tripl\OneDrive\Desktop\Python\Innomatics Internship\My_Proj\resources\data\all_data.csv")
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
fig1.show()
col1.plotly_chart(fig1, use_container_width=True)

txt = "December has the highest sales and January has the lowest sales"
col2 = st.text(txt)

