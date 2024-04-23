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



# loading json file 
with open('Response.json','r') as file:
    RESPONSE_JSON = json.load(file)

# Create a title for the app
st.title("MCQs Creator Application with LangChain 🦜️🔗")



# Create a form using st.form
with st.form("user_inputs"):
    # File Upload
    uploaded_file=st.file_uploader("Upload a PDF or txt file")

    # Input Field
    mcq_count= st.number_input("NO. of MCQs", min_value=3, max_value=50)

    # Subject
    subject=st.text_input("Insert Subject",max_chars=20)

    # Quiz Tone
    tone = st.text_input("Complexity Level of Questions",max_chars=20, placeholder="Simple")

    # Add Button
    button = st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have inputs
    if button and uploaded_file is not None and mcq_count and subject and tone :
        with st.spinner("loading...."):
            try:
                text = read_file(uploaded_file)

                # get response 
                response=generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject":subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                )
                
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            

            else:
                if isinstance(response,dict):
                    # Extract the quiz data from the response

                    quiz = response.get("quiz", None)
                    review = response.get("review",None);
                    if quiz and review is not None:
                        table_data = get_table_data(quiz)
                        
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            
                            

                        st.write(review)
                            

                    else :
                        st.error("Error in the table data")
                else:
                    st.write(response)

              



logging.info("Hi, I am going to start my excution....")

