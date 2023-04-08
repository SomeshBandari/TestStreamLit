import streamlit as st
import numpy as np

st.title("Sample Deploy")
rng = np.random.default_rng()

if "a" not in st.session_state:
    A = rng.random((1,5))
    st.session_state["a"] = A
else:
    A = st.session_state["a"]
    
st.write(A)

st.slider("A slider", 0,100,40,1)