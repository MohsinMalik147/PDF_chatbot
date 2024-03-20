
import streamlit as st

def find_match(input, index, model):
    input_em = model.encode(input).tolist()
    result = index.query(vector=input_em, top_k=2, include_metadata=True)
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']

def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
        print(conversation_string)
    return conversation_string