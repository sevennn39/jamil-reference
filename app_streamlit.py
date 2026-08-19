import random
import streamlit as st

FUN_FACTS = [
    "Cat urine glows under a blacklight.",
    "A shrimp's heart is in its head.",
    "Dreamt is the only English word that ends in the letters mt.",
    "A dime has 118 ridges around the edge.",
    "A crocodile cannot stick its tongue out.",
    "The 'sixth sick sheik's sixth sheep's sick' is believed to be the toughest tongue twister in the English language.",
]

PREDICTIONS = [
    "You'll have a great day!",
    "Someone will derail your plans...",
    "Things won't work out how you think.",
    "You may end up tired by the end of the day.",
    "It'll just be a day.",
    "You may run into some issues.",
]

st.title("37039")
st.write("Hello! Welcome to 37039!")
st.write("Choose a game:")

choice = st.selectbox(
    "Select an option",
    ["High Card, Low Card", "Coin Flip", "Fun Facts", "Quiz", "Predictions"],
)

if choice == "Quiz":
    st.write("You have chosen Quiz!")

    with st.form("quiz_form"):
        question_one = st.text_input("What is the capital of Australia?")
        question_two = st.text_input("What is 12 x 29?")
        question_three = st.text_input("What is the powerhouse of the cell?")
        submitted = st.form_submit_button("Check my answers")

    if submitted:
        total_score = 0

        if question_one and question_one.strip().lower() == "canberra":
            total_score += 1
            st.write("Correct! Canberra is the capital of Australia.")
        else:
            st.write("Not quite. The correct answer is Canberra.")

        if question_two and question_two.strip() == "348":
            total_score += 1
            st.write("Correct! 12 x 29 = 348.")
        else:
            st.write("Not quite. The correct answer is 348.")

        if question_three and question_three.strip().lower() == "mitochondria":
            total_score += 1
            st.write("Correct! The mitochondria are the powerhouse of the cell.")
        else:
            st.write("Not quite. The correct answer is Mitochondria.")

        st.write(f"Total Score: {total_score}")

elif choice == "High Card, Low Card":
    st.write("You have chosen High Card, Low Card!")
    with st.form("high_low_form"):
        num = random.randint(1, 12)
        st.write(f"Starting number: {num}")
        guess = st.radio("Will the next number be higher or lower?", ["Higher", "Lower"])
        submitted = st.form_submit_button("Draw next number")

    if submitted:
        other = random.randint(1, 12)
        if num < other:
            result = f"It was higher! [{other}]"
        elif num > other:
            result = f"It was lower! [{other}]"
        else:
            result = f"It was the same! [{other}]"
        st.write(result)

elif choice == "Coin Flip":
    st.write("You have chosen Coin Flip!")
    if st.button("Flip coin"):
        result = "Heads!" if random.randint(1, 2) == 1 else "Tails!"
        st.write(result)

elif choice == "Fun Facts":
    st.write("You have chosen Fun Facts!")
    if st.button("Show a fact"):
        st.write(random.choice(FUN_FACTS))

elif choice == "Predictions":
    st.write("You have chosen Predictions! Here's how your day will go today:")
    if st.button("Get prediction"):
        st.write(random.choice(PREDICTIONS))
