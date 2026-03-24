import streamlit as st
import math

def cek_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    limit = math.isqrt(x) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    return True

st.title("Prime Number Checker")
number = st.number_input("masukkan angka yg mau di cek:", min_value=0)
if st.button("cek status prima atau bukan"):
    if cek_prime(number):
        st.success(f"{number} adlh angka prima!")
        st.balloons()
    else:
        st.error(f"{number} bukan angka prima!")
