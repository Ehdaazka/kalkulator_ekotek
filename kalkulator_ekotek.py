import streamlit as st
import math


#HALAMAN HITUNG BUNGA MAJEMUK

st.title('Kalkulator Suku Bunga Majemuk') 



st.title('1.Menghitung Nilai Akhir') 
Mo = st.number_input ("masukkan nilai awal modal",0)
i = st.number_input ("Masukkan bunga dalam tahun")
n = st.number_input ("masukkan periode dalam tahun",0)
Mn = st.button("Hitung Nilai Akhir")

if Mn :
    nilai_akhir = Mo*(1+i)**n
    st.write("nilai akhir = ", nilai_akhir)
    st.success(f"Sehingga didapat nilai akhirnya adalah = {nilai_akhir} ")



st.title('2.Menghitung Nilai Awal') 
Mn = st.number_input ("masukkan nilai akhir",0)
i = st.number_input ("Masukkan bunga per tahun")
n = st.number_input ("masukkan periode dalam satuan tahun",0)
M0 = st.button("Hitung Nilai Awal")

if M0 :
    nilai_awal = Mn/((1+i)**n)
    st.write("nilai awal = ", nilai_awal)
    st.success(f"Sehingga didapat nilai awalnya adalah = {nilai_awal} ")



st.title('3.Menghitung Bunga') 
M0 = st.number_input ("masukkan nilai awal",0)
Mn = st.number_input ("Masukkan nilai akhir",00)
n = st.number_input ("masukkan periode-tahun",0)
i = st.button("Hitung Bunga per tahun")

if i :
    bunga = ((Mn**(1/n))/(M0**(1/n)))-1
    st.write("bunga = ", bunga)
    st.success(f"Sehingga didapat nilai bunganya adalah = {bunga} ")



st.title('4.Mengetahui Periode') 
M0 = st.number_input ("masukkan nilai awalnya",0)
Mn = st.number_input ("Masukkan nilai akhirnya",0)
i = st.number_input ("masukkan bunga")
n = st.button("ketahui periode dalam tahun")

if n :
    periode = math.log(Mn/M0,(1+i))
    st.write("periode = ", periode)
    st.success(f"Sehingga didapat periodenya adalah = {periode} ")


