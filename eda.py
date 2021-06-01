import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

st.balloons()
#to avoid warning
st.set_option('deprecation.showPyplotGlobalUse',False)
#setting an title
st.title('tips_dataset')

#setting dataset 
datas = pd.read_csv('/home/sanosh_jacob/seaborn-data/tips.csv')
#selceting the top 12
tips=datas.head(10)
#displaying them in the form of table
st.table(tips)

#setting an header
st.header("Visualiztion using seaborn")

st.subheader("bar plot")
#for bar plot
tips.plot(kind='bar')
st.pyplot()


st.subheader("Displot")
sns.displot(tips['total_bill'])
st.pyplot()

st.header("violin plot")
sns.barplot(x='total_bill',y='size',hue='size',data=tips)
st.pyplot()


st.header("heamap")
sns.heatmap(tips.corr(),cmap='coolwarm')
st.pyplot()