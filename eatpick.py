import streamlit as st
import random
import time
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="먹PICK!", page_icon="🍔", layout="centered")

st.title("🍔 먹PICK - 나만의 음식 추천 & 주문 서비스")
st.caption("기분, 날씨, 취향, 시간까지 고려한 스마트 메뉴 추천!")

# ---------------------------------------------------
# 세션 상태 초기화
# ---------------------------------------------------
if "orders" not in st.session_state:
    st.session_state.orders = []
if "recommended" not in st.session_state:
    st.session_state.recommended = None

# ---------------------------------------------------
# 사용자 정보 입력
# ---------------------------------------------------
st.subheader("👤 나의 정보 입력하기")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("이름", placeholder="이승연")
    age = st.number_input("나이", min_value=10, max_value=100, step=1)
with col2:
    gender = st.selectbox("성별", ["여성", "남성", "기타"])

preference = st.multiselect(
    "좋아하는 음식 종류 (복수 선택 가능)", 
    ["한식", "양식", "일식", "중식", "분식", "패스트푸드", "건강식", "디저트"]
)

st.write("---")

# ---------------------------------------------------
# 오늘 상태 입력
# ---------------------------------------------------
st.subheader("🌤 오늘 상태 입력")

mood = st.selectbox("오늘 기분은 어때?", ["행복 😊", "보통 😐", "피곤 😩", "스트레스 😤", "신남 🤩"])
weather = st.selectbox("오늘 날씨는?", ["맑음 ☀️", "흐림 🌥️", "비 🌧️", "추움 🥶", "더움 🥵"])
meal_time = st.radio("지금은 어떤 시간대야?", ["아침", "점심", "저녁", "야식"])

st.write("---")

# ---------------------------------------------------
# 음식 데이터
# ---------------------------------------------------
foods = {
    "한식": [("비빔밥", "https://cdn.pixabay.com/photo/2016/03/05/19/02/bibimbap-1238719_640.jpg", 8500, 25),
            ("김치찌개", "https://cdn.pixabay.com/photo/2020/05/19/09/06/kimchi-soup-5190928_640.jpg", 9000, 30),
            ("제육볶음", "https://cdn.pixabay.com/photo/2021/01/14/11/13/pork-5916710_640.jpg", 9500, 27)],
    "양식": [("파스타", "https://cdn.pixabay.com/photo/2017/12/09/08/18/spaghetti-3001432_640.jpg", 12000, 35),
            ("피자", "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_640.jpg", 15000, 40)],
    "일식": [("초밥", "https://cdn.pixabay.com/photo/2017/08/17/11/21/sushi-2654036_640.jpg", 13000, 40),
            ("라멘", "https://cdn.pixabay.com/photo/2020/09/18/15/08/ramen-5589723_640.jpg", 11000, 30)],
    "중식": [("짜장면", "https://cdn.pixabay.com/photo/2021/03/23/16/27/noodles-6118249_640.jpg", 8000, 20),
            ("탕수육", "https://cdn.pixabay.com/photo/2022/02/13/06/46/sweet-and-sour-pork-7010455_640.jpg", 14000, 35)],
    "분식": [("떡볶이", "https://cdn.pixabay.com/photo/2022/09/09/09/10/tteokbokki-7442248_640.jpg", 6000, 15),
            ("김밥", "https://cdn.pixabay.com/photo/2017/07/03/20/38/kimbap-2461967_640.jpg", 4000, 10)],
    "패스트푸드": [("햄버거", "https://cdn.pixabay.com/photo/2016/03/05/22/49/hamburger-1238246_640.jpg", 7000, 20),
            ("치킨너겟", "https://cdn.pixabay.com/photo/2020/04/19/11/23/chicken-5061481_640.jpg", 6500, 15)],
    "건강식": [("샐러드", "https://cdn.pixabay.com/photo/2016/03/05/19/02/salad-1238255_640.jpg", 9000, 15),
            ("닭가슴살 도시락", "https://cdn.pixabay.com/photo/2018/05/15/22/19/chicken-breast-3408952_640.jpg", 10000, 25)],
    "디저트": [("아이스크림", "https://cdn.pixabay.com/photo/2015/04/08/13/13/ice-711462_640.jpg", 5000, 10),
            ("케이크", "https://cdn.pixabay.com/photo/2017/05/07/08/56/cake-2291908_640.jpg", 6500, 15)]
}

# ---------------------------------------------------
# 음식 추천
# ---------------------------------------------------
if st.button("🍴 나에게 맞는 메뉴 추천받기"):
    if not preference:
        st.warning("👉 먼저 음식 취향을 하나 이상 선택해줘!")
    else:
        chosen_type = random.choice(preference)
        rec_food, food_img, price, time_est = random.choice(foods[chosen_type])

        st.session_state.recommended = {
            "menu": rec_food,
            "type": chosen_type,
            "img": food_img,
            "price": price,
            "time_est": time_est
        }

# ---------------------------------------------------
# 추천 결과 표시
# ---------------------------------------------------
if st.session_state.recommended:
    rec = st.session_state.recommended
    st.success(f"✨ {name}님에게 추천하는 오늘의 메뉴는 **{rec['menu']} ({rec['type']})** 입니다!")
    st.image(rec["img"], caption=f"{rec['menu']}", use_container_width=True)
    st.markdown(f"💰 **가격:** {rec['price']:,}원 | 🕒 **예상 배달 시간:** 약 {rec['time_est']}분")

    # 주문 버튼
    if st.button("🚀 이 메뉴로 주문하기"):
        with st.spinner("배달 주문을 접수 중입니다..."):
            time.sleep(2)
        st.success(f"주문 완료! 🛵 {rec['menu']}이(가) {rec['time_est']}분 내 도착 예정입니다 🍽️")
        st.balloons()

        order_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.session_state.orders.append({
            "이름": name,
            "메뉴": rec["menu"],
            "종류": rec["type"],
            "가격": rec["price"],
            "배달예상시간(분)": rec["time_est"],
            "주문시간": order_time
        })

# ---------------------------------------------------
# 주문 기록
# ---------------------------------------------------
st.write("---")
st.subheader("🧾 내 주문 기록")
if len(st.session_state.orders) > 0:
    df = pd.DataFrame(st.session_state.orders)
    st.dataframe(df, use_container_width=True)
else:
    st.info("아직 주문 기록이 없습니다 🍔")

st.write("---")
st.caption("© 2025 먹PICK! Prototype v4.1. Made with Streamlit 💛")

