import numpy as np
import streamlit as st
import matplotlib.pyplot as plt    # type: ignore


def trapezoidal_rule(f, a, b, n):
    """
    Menghitung integral dari fungsi f dari a ke b menggunakan metode Trapezoidal.
    
    Parameters:
    f : function
        Fungsi yang akan diintegralkan.
    a : float
        Batas bawah integral.
    b : float
        Batas atas integral.
    n : int
        Jumlah subinterval.
        
    Returns:
    float
        Aproksimasi integral dari f dari a ke b.
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        integral += f(a + i * h)
    
    integral *= h
    return integral

# Streamlit app
st.set_page_config(page_title="Metode Trapezoidal", layout="wide")
st.title("🔍 Metode Trapezoidal untuk Menghitung Integral")

st.markdown("""
    Aplikasi ini menggunakan metode Trapezoidal untuk menghitung integral dari fungsi yang Anda pilih.
    Silakan masukkan batas integral, jumlah subinterval, dan pilih fungsi yang ingin diintegralkan.
""")

# Input dari pengguna
col1, col2 = st.columns(2)

with col1:
    a = st.number_input("Masukkan batas bawah (a):", value=0.0)
    b = st.number_input("Masukkan batas atas (b):", value=np.pi)
    n = st.number_input("Masukkan jumlah subinterval (n):", value=1000, step=1)

with col2:
    function_options = {
        "sin(x)": np.sin,
        "cos(x)": np.cos,
        "x^2": lambda x: x**2,
        "e^x": np.exp
    }
    function_choice = st.selectbox("Pilih fungsi yang akan diintegralkan:", list(function_options.keys()))

# Hitung integral saat tombol ditekan
if st.button("Hitung Integral"):
    f = function_options[function_choice]
    result = trapezoidal_rule(f, a, b, n)
    
    st.success(f"Hasil integral dari **{function_choice}** dari **{a}** ke **{b}** adalah: **{result:.4f}**")

    # Visualisasi fungsi dan area di bawah kurva
    x = np.linspace(a, b, 100)
    y = f(x)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f'Fungsi: {function_choice}', color='blue', linewidth=2)
    plt.fill_between(x, y, where=((x >= a) & (x <= b)), color='lightblue', alpha=0.5, label='Area di bawah kurva')
    plt.title('Visualisasi Integral', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(a, color='red', lw=0.5, ls='--', label='Batas bawah (a)')
    plt.axvline(b, color='green', lw=0.5, ls='--', label='Batas atas (b)')
    plt.legend()
    plt.grid()
    st.pyplot(plt.gcf())

st.markdown("""
    ### Penjelasan
    Metode Trapezoidal adalah teknik numerik untuk menghitung integral dengan membagi area di bawah kurva menjadi trapesium.
    Semakin banyak subinterval yang digunakan, semakin akurat hasilnya.
""")