import streamlit as st
import json
import os

# JSON 파일 경로 설정
DATABASE_FILE = 'lecture_evaluation.json'

# 기존 데이터 로드 함수
def load_data():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = []
    return data

# 데이터 저장 함수
def save_data(data):
    with open(DATABASE_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Streamlit UI
st.title('우리학교 강좌 강의평가')

# 'with' 표기법으로 폼 작성하기
st.header('강의평가하기')

with st.form('lecture_evaluation_form'):
    st.subheader('과목 선택')
    subject_val = st.selectbox('과목명', [
        '연구윤리와사회적책임', '100세건강식생활론', '기후변화상식을넘어서', '생활속의건강관리',
        '스마트시대의여가', '미생물과인간생활', '인권감수성더하기', '생명공학기술과미래', 
        '논리와비판적사고', '광고와소비자심리', '글로벌이슈와관광', '비즈니스와매너',
        '디지털헬스케어', 'AI리터러시', 'AI융합코딩', '환경과생태', '문명과수학',
        '기초영어', '기초수학', '생물학'
    ])

    st.subheader('점수 (단위: 0.5)')
    scores_val = st.slider('점수를 선택하세요', min_value=0.0, max_value=5.0, value=2.5, step=0.5)

    st.subheader('강의평')
    evaluation_val = st.text_area("여러 줄의 글을 입력하세요:")

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    # 기존 데이터를 불러오기
    data = load_data()

    # 새 평가 정보를 딕셔너리로 작성
    new_evaluation = {
        "과목명": subject_val,
        "점수": scores_val,
        "강의평": evaluation_val
    }

    # 새 평가 정보를 기존 데이터에 추가
    data.append(new_evaluation)

    # JSON 파일로 저장
    save_data(data)

    st.success("강의 평가가 성공적으로 저장되었습니다!")
    st.markdown(f'''
        **입력된 강의평:**
        - 과목: `{subject_val}`
        - 별점: `{scores_val}`
        - 강의평: `{evaluation_val}`
        ''')
else:
    st.write('☝️ 강의평가를 입력하고 제출 버튼을 누르세요.')


# 강의 평가 정보 보기
st.header("저장된 강의 평가 보기")
if st.button('저장된 평가 보기'):
    data = load_data()
    if data:
        for idx, evaluation in enumerate(data):
            st.markdown(f"### {evaluation['과목명']} 평가")
            st.write(f"**과목명:** {evaluation['과목명']}")
            st.write(f"**점수:** {evaluation['점수']}")
            st.write(f"**강의평:** {evaluation['강의평']}")
    else:
        st.write("아직 저장된 평가가 없습니다.")
