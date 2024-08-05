import streamlit as st

# Define the questions and answers for each module and mock test
questions = {
    "PET Design": {
        "Mock Test 1": [
            {"question": "Question 1?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 2?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 3?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 4?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 5?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 6?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 7?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 8?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 9?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 10?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 11?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 12?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 13?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 14?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 15?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 16?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 17?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 18?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 19?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 20?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 21?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 22?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 23?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 24?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 25?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 26?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 27?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 28?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 29?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 30?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 31?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 32?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 33?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 34?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 35?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 36?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 37?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 38?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 39?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 40?", "options": ["A", "B", "C", "D"], "answer": "B"}
            
            # Add more questions here...
        ],
        "Mock Test 2": [
            {"question": "Question 1?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 2?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 3?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 4?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 5?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 6?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 7?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 8?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 9?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 10?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 11?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 12?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 13?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 14?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 15?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 16?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 17?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 18?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 19?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 20?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 21?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 22?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 23?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 24?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 25?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 26?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 27?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 28?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 29?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 30?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 31?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 32?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 33?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 34?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 35?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 36?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 37?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 38?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 39?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 40?", "options": ["A", "B", "C", "D"], "answer": "B"}
            # Add more questions here...
        ],
        "Mock Test 3": [
            {"question": "Question 1?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 2?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 3?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 4?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 5?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 6?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 7?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 8?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 9?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 10?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 11?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 12?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 13?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 14?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 15?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 16?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 17?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 18?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 19?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 20?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 21?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 22?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 23?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 24?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 25?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 26?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 27?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 28?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 29?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 30?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 31?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": "Question 32?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 33?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 34?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 35?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 36?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 37?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 38?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 39?", "options": ["A", "B", "C", "D"], "answer": "B"},
            {"question": "Question 40?", "options": ["A", "B", "C", "D"], "answer": "B"}
            # Add more questions here...
        ],
    },
    # Define other modules and their mock tests similarly...
}

# App title
st.title("CXA Exam Preparation")

# Select module
module = st.selectbox("Select Module", list(questions.keys()))

if module:
    # Select mock test
    mock_test = st.selectbox("Select Mock Test", list(questions[module].keys()))

    if mock_test:
        # Get selected questions
        selected_questions = questions[module][mock_test]

        # User's answers
        user_answers = []

        for i, q in enumerate(selected_questions):
            st.write(f"Q{i+1}: {q['question']}")
            options = q['options']
            user_answer = st.radio(f"Select your answer for Q{i+1}", options, key=f"q{i+1}")
            user_answers.append({"question": q['question'], "user_answer": user_answer, "correct_answer": q['answer']})

        # Submit button
        if st.button("Submit"):
            score = sum(1 for a in user_answers if a['user_answer'] == a['correct_answer'])
            st.write(f"Your score is: {score}/{len(selected_questions)}")

            # Detailed feedback
            for i, a in enumerate(user_answers):
                st.write(f"Q{i+1}: {a['question']}")
                st.write(f"Your answer: {a['user_answer']} | Correct answer: {a['correct_answer']}")
