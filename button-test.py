import streamlit as st
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

st.title('Tello Control')
if st.button("command"):
    #st.write("command")
    sent = sock.sendto(b'command', tello_address)
if st.button("take off"):
    #st.write("take off")
    sent = sock.sendto(b'takeoff', tello_address)
if st.button("land"):
    #st.write("land")
    sent = sock.sendto(b'land', tello_address)
