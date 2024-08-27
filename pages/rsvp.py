import streamlit as st

def app():
    st.title("RSVP")

    # Create a form for RSVP
    with st.form("rsvp_form"):
        name = st.text_input("Name")
        attending = st.radio("Will you attend?", ["Yes", "No"])
        num_guests = st.number_input("Number of guests", min_value=0, value=0)
        submit = st.form_submit_button("Submit")

        if submit:
            # Handle RSVP submission
            st.write(f"Thank you, {name}! Your RSVP has been received.")
            st.write(f"Attending: {attending}")
            st.write(f"Number of guests: {num_guests}")


if __name__ == "__main__":
    app()