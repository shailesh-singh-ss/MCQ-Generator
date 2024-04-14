import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file
from src.mcqgenerator.utils import get_table_data
import streamlit as st
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging 

# logging.info("Hi, I am going to start my excution....")
with open('./Response.json','r') as file:
    RESPONSE_JSON = json.load(file)
print(RESPONSE_JSON)