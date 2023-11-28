import streamlit as st

#First output
st.write('Hello World')

import streamlit as st

option = st.selectbox(
    'What do you want for lunch?',
    ('Kaiserschmarrn', 'Wok', 'Kürbissuppe', 'Sandwich', 'Fritten'))

st.write('Good choice! We will have', option)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
