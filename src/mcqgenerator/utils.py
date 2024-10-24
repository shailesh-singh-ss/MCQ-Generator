import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text =""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        
        except Exception as e:
            raise Exception("error reading the PDF file" + str(e))
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file formate only pdf and text file supported"
        )
    


def get_table_data(quiz_str: dict):
    try:
        # convert the quiz from a str to dict
        # quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]

        # iterate over the quiz dictionary and extract the required information
        for key,value in quiz_str.items():
            mcq=value["mcq"]
            options=" || ".join(
                [
                    f"{option} -> {option_value}" for option,option_value in value["options"].items()
                ]
            )

            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})

        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
    
def extract_json_data(data_str):
    # Remove the enclosing ```json and ''' (or similar) from the string
    cleaned_str = data_str.strip('```json').strip("```").strip()
    
    try:
        # Parse the cleaned string into a JSON object
        data = json.loads(cleaned_str)
        
        return data
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"






