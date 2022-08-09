# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:20:19 2022

@author: Kunal
"""

import pandas as pd
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import codecs
import streamlit.components.v1 as components
import sweetviz as sv
from streamlit_lottie import st_lottie
import json
import requests
from  PIL import Image


## Define Functions to call lottie Animations
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

st.title("Explaratory Data Analysis in Minutes")
st.caption("Your own web based data story telling application")
lottie_hello=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_hx7ddrx9.json")
st_lottie(lottie_hello,speed=1,reverse=False,loop=True,quality="low",height=350,width=1200,key=None)


#Add a logo (optional) in the sidebar
logo = Image.open('image3.jpg')
st.sidebar.image(logo,  width=320)
st.sidebar.title(body="Exploratory Data Analysis")
linkedIN=("https://www.linkedin.com/in/aadityahamine")
st.sidebar.write(linkedIN)


     
     
## Sweetviz library function 
def st_display_sweetviz(report_html,width=1000,height=1000):
    report_file=codecs.open(report_html,'r')
    page=report_file.read()
    components.html(page,width=width,height=height,scrolling=True)

## Web Title

menu=["None","Sweetviz","Pandas Profiling"]
menu2=["Home","Sweetviz","Pandas Profiling"]
choice=st.sidebar.radio(label='Select Library  to explore your dataset',options=menu2)

example=pd.read_csv(r'example_file.csv',encoding='latin-1')
example2=example.copy()
#example2
data_file=st.file_uploader("Want to know what story your data is trying to tell ? - Upload a CSV file here", type=['csv'])

if data_file is not None:
    
    if choice == "Pandas Profiling":
        #st.subheader("Profile Report of example dataset prepared using Pandas Profiling Library")
        df=pd.read_csv(data_file)
        #st.dataframe(df.head())
        profile=ProfileReport(df)
        st_profile_report(profile)
    
    elif choice == "Sweetviz":
        #st.subheader("Profile Report of example dataset prepared using Sweetviz Library")
        df=pd.read_csv(data_file)
        #st.dataframe(df.head())
        report=sv.analyze(df)
        report.show_html()
            
    elif choice == "About":
                st.subheader("About App")
    
else:
    st.caption("Don't have a CSV file to upload ? Try with our example dataset")
    choice2=st.radio(label='Select Library to perform EDA on Example Dataset',options=menu)
    
    if st.button('Press here to perform EDA with Example Dataset'):
        
        if choice2 == "Pandas Profiling":
            #st.subheader("Profile Report of example dataset prepared using Pandas Profiling Library")
            pr=ProfileReport(example2,explorative=True)
            st_profile_report(pr)
            
        elif choice2 == "Sweetviz":
            #st.subheader("Profile Report of example dataset prepared using Sweetviz Library")
            report=sv.analyze(example2)
            report.show_html()
