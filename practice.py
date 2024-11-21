import streamlit as st


page_one = st.Page(
    page= "sub/page1.py",
    title="page 1"
)

page_two = st.Page(
    page= "sub/page2.py",
    title="page 2"
)

page_three = st.Page(
    page= "sub/page3.py",
    title="page 3"
)

# CSS 스타일을 사용해 배경 색상을 검정색으로 설정
page_bg_style = """
    <style>
    body {
        background-color: #000000;  /* 배경 색상을 검정색(#000000)으로 설정 */
        color: #FFFFFF;  /* 텍스트 색상을 흰색으로 설정 (검정색 배경에서 잘 보이도록) */
    }
    </style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

st.markdown(page_bg_style, unsafe_allow_html=True)
with st.expander('이 사이트에 대하여'):
  st.write('이 앱은 Streamlit 앱을 구성하는 다양한 방법을 보여줍니다.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)


import streamlit as st

st.set_page_config(layout="wide")

st.title('Streamlit 앱 레이아웃 구성하기')

with st.expander('이 앱에 대하여'):
  st.write('이 앱은 Streamlit 앱을 구성하는 다양한 방법을 보여줍니다.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('입력')
user_name = st.sidebar.text_input('당신의 이름은 무엇인가요?')
user_emoji = st.sidebar.selectbox('이모티콘 선택', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('가장 좋아하는 음식은?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('출력')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 안녕하세요 {user_name}님!')
  else:
    st.write('👈  **이름**을 입력해 주세요!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji}는 당신이 좋아하는 **이모티콘**입니다!')
  else:
    st.write('👈 **이모티콘**을 선택해 주세요!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}**은 당신이 좋아하는 **음식**입니다!')
  else:
    st.write('👈 가장 좋아하는 **음식**을 선택해 주세요!')




pages = st.navigation(
    {
        "Home" : [page_one],
        "Products" : [page_two],
        "Contacts" : [page_three]
    }
)
pages.run()


import streamlit as st

st.title('Streamlit 앱의 테마 사용자 정의하기')

st.write('이 앱의 `.streamlit/config.toml` 파일 내용')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('숫자를 선택하세요:', 0, 10, 5)
st.write('슬라이더 위젯에서 선택된 숫자:', number)


