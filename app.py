import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av

st.title("Webrtc Camera")
model_face = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")

class VideoProcessor:
    def recv(self, frame):
        frame = frame.to_ndarray(format="bgr24")

        #####
        faces = model_face.detectMultiScale(frame,scaleFactor=1.8,minNeighbors=4, flags=cv2.CASCADE_DO_ROUGH_SEARCH | cv2.CASCADE_SCALE_IMAGE)
        for face in faces:
            x,y,w,h = face
            roi = frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),1)
        #####  

        return av.VideoFrame.from_ndarray(frame, format="bgr24")


webrtc_streamer(key="example", video_processor_factory=VideoProcessor)






