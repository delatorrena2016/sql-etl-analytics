import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

df = pd.read_excel(
    io='Adidas US Sales Datasets.xlsx',
    engine='openpyxl',
    sheet_name="Data Sales Adidas",
    skiprows=range(4), 
    usecols="B:N"
)


#---- SIDEBAR ---- 
st.sidebar.header("Please Filter Here:")

city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

df_selection = df.query(
    "City == @city "
)

#MAIN PAGE

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")


#TOP KPI's

total_sales = int(df_selection["Total Sales"].sum())
average_sales = round(df_selection["Total Sales"].mean(), 2)

left_column, right_column = st.columns(2)

with left_column:
    st.header("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with right_column:
    st.header("Average Sales:")
    st.subheader(f"US $ {average_sales:}")

st.markdown("""---""")

# SALES BY PRODUCT

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = df_selection.groupby(by=["Product"])[["Total Sales"]].sum().sort_values(by="Total Sales")
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total Sales",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

st.plotly_chart(fig_product_sales)