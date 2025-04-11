import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="prox-GPT",initial_sidebar_state="collapsed")
st.subheader('')
st.latex(r'''
    \textsf{\Huge \textbf {prox-GPT}} 
         ''')
html_string = '''
  <center style="color:#bfbfbf;"> jingax </center>
 '''
st.markdown(html_string, unsafe_allow_html=True)
st.subheader('', divider='rainbow')
st.write('View source [here](https://github.com/jingax/prox-GPT)')

role_avatars = {
    "user": "images/chill.jpg", 
    "assistant": "images/jinga.png",
}
def chat_with_bot(user_message):
    # Append user query to the message history
    # st.session_state.messages.append({"role": "user", "content": user_message})
    
    # Call the OpenAI API
    model = "llama-4-maverick-17b-128e-instruct-fp8"
    response = st.session_state.client.chat.completions.create(
        model=model,
        messages=st.session_state.messages,
        temperature=0.7,
    )
    
    # Get the assistant's reply
    # print(response)
    assistant_reply = response.choices[0].message.content
    
    # Add the assistant's reply to the message history
    # st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    st.session_state.use_count += 1
    return assistant_reply

def main():
    if "messages" not in st.session_state:
        st.session_state.use_count = 0
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant named prox-GPT created bi jingax AKA Aastik. Keep your your answers as brief as possible unless specified otherwise"},
            {"role": "assistant", "content": "Hi, I am prox-GPT! Here to help"},
        ]
        st.session_state.gif = True
        openai_api_key = st.secrets['api']['openai'] 
        openai_api_base = "https://api.lambda.ai/v1"

        st.session_state.client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )


    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"], avatar=role_avatars[message["role"]]):
            st.markdown(message["content"], unsafe_allow_html=True)
            if st.session_state.gif:
                # st.markdown(gif_html, unsafe_allow_html=True)
                st.session_state.gif = False
                



    if prompt := st.chat_input("Write something"):
        # Display user message in chat message container
        with st.chat_message("user", avatar=role_avatars['user']):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        try:
            response = chat_with_bot(prompt)
        except Exception as e:
            response = "I have issues, I'll ask Aastik to fix me ❤️‍🩹"
            # st.write(e)
        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar=role_avatars['assistant']):
            st.markdown(response, unsafe_allow_html=True)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
    
def password():
    with st.form("login_form"):
        password = st.text_input("Enter password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if password == st.secrets['api']['pass']:
                st.session_state.auth = True
                st.success("✅ Logged in successfully!")
                st.rerun()
                
            else:
                st.error("❌ Incorrect password.")
    

if __name__ == "__main__":
    if 'auth' in st.session_state:
        main()
    else:
        password()
