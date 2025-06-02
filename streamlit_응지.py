import streamlit as st
from PIL import Image


st.title('This is Eung G world')


# 이미지 불러오기
gomguk_img = Image.open("C:/eung_py/eungFolder/6ad6840c75a8979582616aa4a50898df.jpg")

with st.expander('응지에 대하여'):
  st.write('응지는 곰국을 제일 좋아합니니다.')
  st.image(gomguk_img, width=250)



# LAYOUT 짜기

col1, col2 = st.columns([2,3])
with col1 :
    st.title('메롱메롱')
    
with col2 :
    st.title('나는 누구 여긴 어디')
    st.checkbox('성은 이씨다')
    st.checkbox('키가 185cm이다')
    st.checkbox('발 사이즈는 225이다.')
    
col1.subheader('우후루꾸루꾸르후루구')

st.header('EunjiMukji')
st.subheader('Gyeongju choi go')


# TAB키

tab1, tab2 = st.tabs(['Tab A','Tab B'])

with tab1:
    # tab A를 누르면 표시될 내용
    st.write('까꿍')
    
with tab2:
    # tab B를 누르면 표시될 내용
    st.write('안뇽')
# 탭의 특징으로는 탭을 클릭과 동시에 데이터가 만들어지는 것이 아니라, 탭에 표시될 데이터가 이미 만들어져있는 것.
# 장점이 될 수도 있고 단점이 될 수도 있음    
    


# SIDE BAR

st.sidebar.title('이거슨 사이드바')
st.sidebar.checkbox('눌러보시지')