import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import Image
import numpy as np
import joblib
#  load model
model=joblib.load("model.joblib")
# get label
def get_label(img):
    # convert into grayscale
    img_g=img.convert('L')
    # resize to 100 100
    img_res=img_g.resize((100,100))
    # convert in to numpy array and flatten
    img_a=np.array(img_res).flatten()
    #  convert in to df and transpose
    img_df=pd.DataFrame(img_a).T
    # predict with the model
    pre=model.predict(img_df)
    # return the value
    return pre

# Title 
st.title("Bone Fracture Detection")
file=st.file_uploader("Upload your file",type='png')
try:
    if file is not None:
        # Read Image
        img=Image.open(file)
        # Show Image
        st.write(img,"The uploaded Image")
        label_map={0:'Fracture',1:'Non_fracture'}
        prediction=get_label(img)
        prediction=label_map[prediction[0]]
        st.write(f" The Bone is : {prediction}")
    else:
        st.write('Empty file cannot be read')

except Exception as e:
    st.write(f"{e} occured")
finally:
    st.write("Thank you for using our service")
