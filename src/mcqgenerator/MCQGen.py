import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data

# Langchain Packages
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


# Load the environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Defining the LLM model
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)

# Defining the Prompt Template nad the Chain for the Quiz Generation
TEMPLATE = """
Text : {text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs
###RESPONSE JSON
{response_json}"

"""

quiz_prompt = PromptTemplate(template=TEMPLATE, input_variables=[
                             "text", "number", "subject", "tone", "response_json"])

quiz_chain = LLMChain(llm=llm, prompt=quiz_prompt,
                      output_key="quiz", verbose=True)