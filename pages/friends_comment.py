import streamlit as st
from datetime import datetime
import os

def app():
    st.title("Leave a Comment")

    # Create a form for comments
    with st.form("comment_form"):
        name = st.text_input("Name")
        comment = st.text_area("Comment")
        submit = st.form_submit_button("Submit")

        if submit:
            # Save the comment to a text file
            timestamp = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
            filename = f"data/comment/{name}_{timestamp}.txt"
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, "w") as f:
                f.write(comment)

            st.success("Thank you for your comment!")
            st.balloons()

    # Display existing comments
    st.subheader("Comments")
    comment_dir = "data/comment"
    comments = [p.path for p in os.scandir(comment_dir) if p.is_file()]

    print(comments)

    for comment_file in comments:
        with open(comment_file, "r") as f:
            comment_text = f.read()
        st.write(f"**{os.path.basename(comment_file)[:-4]}**")
        st.write(comment_text)
        st.write("---")

if __name__ == "__main__":
    app()