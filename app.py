import openai
import streamlit as st
import time
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App Title
st.title("Streamlit Demo App")

# Tabs for different functionalities
tab1, tab2, tab3, tab4 = st.tabs(["GenAI Code Reviewer", "Long-Running Task Example", "Error Handling", "Debugging Example"])

# Tab 1: GenAI Code Reviewer
with tab1:
    st.header("GenAI Code Reviewer")
    st.write("Submit your Python code below, and our AI will review it for potential bugs and suggest fixes.")

    # Text area for code input
    user_code = st.text_area("Enter your Python code:", height=300)

    # Function to review the code using OpenAI API
    def review_code(user_code):
        try:
            # Call the OpenAI API
            response = openai.Completion.create(
                model="code-davinci-002",
                prompt=f"Please review the following Python code for bugs, errors, and areas for improvement. Provide a detailed explanation and suggest fixed code if possible:\n\n{user_code}",
                max_tokens=500,
                temperature=0.3,
            )
            # Extract feedback
            feedback = response.choices[0].text.strip()

            # Display feedback
            st.subheader("AI's Feedback:")
            st.write(feedback)

            # Display fixed code if included
            if "Fixed Code" in feedback:
                fixed_code = feedback.split("Fixed Code:")[1].strip()
                st.subheader("Suggested Fixed Code:")
                st.code(fixed_code, language="python")
        except Exception as e:
            st.error(f"Error reviewing code: {e}")

    # Button to trigger code review
    if st.button("Review Code", key="review_code"):
        if user_code.strip() == "":
            st.error("Please enter your Python code to review.")
        else:
            st.write("Analyzing code... Please wait.")
            review_code(user_code)

# Tab 2: Long-Running Task Example
with tab2:
    st.header("Long-Running Task Example")
    if st.button("Start Task", key="long_task"):
        with st.spinner("Processing..."):
            time.sleep(5)  # Simulate a long task
        st.success("Task Completed!")

# Tab 3: Error Handling Example
with tab3:
    st.header("Error Handling Example")
    try:
        # Example of risky code
        result = 10 / 0  # This will raise an exception
        st.write(f"Result: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Tab 4: Debugging Example
with tab4:
    st.header("Debugging Example")
    with st.echo():
        # Code block to debug
        value = 5 + 10
        st.write(f"The value is {value}")

