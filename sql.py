from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('models/gemini-2.0-flash-001')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - name, age, marks, class, section  
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in 10th class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="10th";
    Also the SQL code should not have ``` in beginning or end and SQL word in output
    while retrieving the data using section don't be case sensitive
    if someone asks for students in class 10, it should be treated as 10th class
    """
]

st.set_page_config(page_title="SQL Data Retrieval Using Prompt")
st.header("SQL Data Retrieval Using Prompt")

question = st.text_input("Input your prompt here", key="input")
submit = st.button("Submit")

if submit:
    # Generate SQL query from natural language question
    sql_query = get_gemini_response(question, prompt)
    print("Generated SQL Query:", sql_query)
    
    try:
        # Execute the SQL query
        sql_result = read_sql_query(sql_query, "student.db")
        print("Query Result:", sql_result)
        
        st.subheader("Result:")
        
        # Check if result is empty
        if not sql_result:
            st.header("No data found")
        else:
            # Display results
            for row in sql_result:
                st.write(row)  # Using write instead of header for better formatting
    except Exception as e:
        st.error(f"Error executing query: {str(e)}")