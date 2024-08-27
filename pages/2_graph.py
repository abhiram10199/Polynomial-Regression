import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import values


def chart():
    x = [1,2,3]
    y = [2,10,4]
    plt.plot(x, y, 'ob')

    st.pyplot(plt)

st.title('Chart')
chart()
