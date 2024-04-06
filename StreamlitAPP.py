import pandas as pd
import os
import json
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging
import streamlit as st
from src.mcqgenerator.MCQGen import generate_evaluate_chain

#Load the JSON Response

with open("C:\Development\mcq-generator\Response.json", "r") as f:
    response_json = json.loads(f)

# Title of the Web App
st.title("MCQ Generator using Generative Models")

# Creating a Form
with st.form("user_inputs"):
    
    #File Uploader
    uploaded_file = st.file_uploader("Choose a file (.txt or .pdf): ")

    #Input Fields
    question_count = st.number_input("Number of Questions", min_value=3, value=50)
    subject = st.text_input("Insert Subject")
    tone = st.text_input("Complexity Level: ", placeholder="Simple")
    button = st.form_submit_button("Generate MCQs")

    if button and uploaded_file is not None and question_count and subject and tone:
       with st.spinner("Loading... "):
           
