import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
data=pd.read_csv(r"C:\Users\vinen\OneDrive\Desktop\assignment\iris.csv")
menu=st.sidebar.radio("MENU",["HOME","SEPAL LENGTH","SEPAL WIDTH","PETAL LENGTH","PETAL WIDTH","VARIETY"])
if menu=="HOME":
    st.title(" web app using streamlit ")
    st.image("download.png",width=550)
    st.title("case study on iris dataset")
    st.write("shape of the dataset",data.shape)
    st.header("Tabular data for head")
    if st.checkbox("Tabular data for head"):
        st.table(data.head(100))
    st.header("Tabular data for tail")
    if st.checkbox("Tabular data for tail"):
        st.table(data.tail(100))
if menu=="SEPAL LENGTH":
    st.title("DESCRIPTION:")
    st.subheader("This is regarding length of each data point")
    st.header("sepal length column")
    if st.checkbox("sepal length column"):
        st.table(data["sepal.length"])
if menu=="SEPAL WIDTH":
    st.title("DESCRIPTION:")
    st.subheader("This is regarding width of each data point")
    st.header("sepal width column")
    if st.checkbox("sepal width column"):
        st.table(data["sepal.width"])
if menu=="PETAL LENGTH":
    st.title("DESCRIPTION:")
    st.subheader("This is regarding petal length of each data point")
    st.header("petal length column")
    if st.checkbox("petal length column"):
        st.table(data["petal.length"])
if menu=="PETAL WIDTH":
    st.title("DESCRIPTION:")
    st.subheader("This is regarding petal width of each data point")
    st.header("petal width column")
    if st.checkbox("petal width column"):
        st.table(data["petal.width"])
if menu=="VARIETY":
    st.header("VARIETY is divided by 3 categories ")
    st.subheader("1.Setosa")
    st.subheader("2.Virginica")
    st.subheader("3.Versicolor")




    
        


