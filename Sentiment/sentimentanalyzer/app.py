import streamlit as st
import pickle
import numpy as np
import os


data=pickle.load(open('models.p', 'rb'))
data1=pickle.load(open('models1.p', 'rb'))
data2=pickle.load(open('models2.p', 'rb'))
mn=data['mn']
cv=data['cv']
lr=data1['lr']
cv_l=data1['cv_l']
lr_tv=data2['lr_tv']
tv=data2['tv']
#@st.cache(suppress_st_warning=True)
def predict_sen(text_inp):
    vec=cv.transform([text_inp])
    pred=mn.predict(vec)[0]
    return pred


def predict_sen1(text_inp):
    vec1=cv_l.transform([text_inp])
    pred=lr.predict(vec1)[0]
    return pred


def predict_sen2(text_inp):
    vec2=tv.transform([text_inp])
    pred=lr_tv.predict(vec2)[0]
    return pred

def main():
    html_temp = """
    <div style="background-color:#008080;padding:30px">
    <h1 style="color:#000000;text-align:center;">Sentiment analyzer </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    pos_html="""  
      <div style="background-color:#3CB371;padding:10px >
      <br><br>
       <h2 style="color:#000000;"> The sentiment is : POSITIVE</h2>
       <br><br>
      </div>
    """
    neg_html="""  
      <div style="background-color:#F08080;padding:10px >
      <br><br>
       <h2 style="color:#000000;> The sentiment is : NEGATIVE</h2>
       <br><br>
      </div>
    """
    inp=st.text_input("Enter text","Type Here")
    if st.button("Predict using Naive Bayes"):
        output=predict_sen(inp)
        if output=='positive':
            st.markdown(pos_html,unsafe_allow_html=True)
        if output=='negative':
            st.markdown(neg_html,unsafe_allow_html=True)

    if st.button("Predict using LSTM"):
        output=predict_sen1(inp)
        if output==1:
            #st.write("Positive")
            st.markdown(pos_html,unsafe_allow_html=True)
        if output==0:
            #st.write("Negative")
            st.markdown(neg_html,unsafe_allow_html=True)

    if st.button("Predict with TF-IDF Vectorizer"):
        output=predict_sen2(inp)
        if output==1:
            st.markdown(pos_html,unsafe_allow_html=True)
        if output==0:
            st.markdown(neg_html,unsafe_allow_html=True)
        #st.success('Your sentiment : {}'.format(output))

if __name__=='__main__':
    main()