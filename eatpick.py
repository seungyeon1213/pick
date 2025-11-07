import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="먹PICK!", page_icon="🍔", layout="centered")

st.title("🍔 먹PICK - 나만의 음식 추천 & 주문 서비스")
st.caption("기분, 날씨, 취향, 시간까지 고려한 스마트 메뉴 추천!")

# ---------------------------
# 사용자 정보 입력
# ---------------------------
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

# ---------------------------
# 오늘 상태 입력
# ---------------------------
st.subheader("🌤 오늘 상태 입력")

mood = st.selectbox("오늘 기분은 어때?", ["행복 😊", "보통 😐", "피곤 😩", "스트레스 😤", "신남 🤩"])
weather = st.selectbox("오늘 날씨는?", ["맑음 ☀️", "흐림 🌥️", "비 🌧️", "추움 🥶", "더움 🥵"])
meal_time = st.radio("지금은 어떤 시간대야?", ["아침", "점심", "저녁", "야식"])

st.write("---")

# ---------------------------
# 음식 데이터 + 이미지 링크
# ---------------------------

foods = {
    "한식": [("비빔밥", "https://cdn.pixabay.com/photo/2016/03/05/19/02/bibimbap-1238719_1280.jpg"),
            ("김치찌개", "https://cdn.pixabay.com/photo/2022/12/21/11/12/kimchi-stew-7669018_1280.jpg"),
            ("제육볶음", "https://cdn.pixabay.com/photo/2021/01/14/11/13/pork-5916710_1280.jpg")],
    "양식": [("파스타", "https://cdn.pixabay.com/photo/2017/12/09/08/18/spaghetti-3001432_1280.jpg"),
            ("피자", "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg")],
    "일식": [("초밥", "https://cdn.pixabay.com/photo/2017/08/17/11/21/sushi-2654036_1280.jpg"),
            ("라멘", "https://cdn.pixabay.com/photo/2020/09/18/15/08/ramen-5589723_1280.jpg")],
    "중식": [("짜장면", "https://cdn.pixabay.com/photo/2021/03/23/16/27/noodles-6118249_1280.jpg"),
            ("탕수육", "https://cdn.pixabay.com/photo/2022/02/13/06/46/sweet-and-sour-pork-7010455_1280.jpg")],
    "분식": [("떡볶이", "https://cdn.pixabay.com/photo/2022/09/09/09/10/tteokbokki-7442248_1280.jpg"),
            ("김밥", "https://cdn.pixabay.com/photo/2017/07/03/20/38/kimbap-2461967_1280.jpg")],
    "패스트푸드": [("햄버거", "https://cdn.pixabay.com/photo/2016/03/05/22/49/hamburger-1238246_1280.jpg"),
            ("치킨너겟", "https://cdn.pixabay.com/photo/2020/04/19/11/23/chicken-5061481_1280.jpg")],
    "건강식": [("샐러드", "https://cdn.pixabay.com/photo/2016/03/05/19/02/salad-1238255_1280.jpg"),
            ("닭가슴살 도시락", "https://cdn.pixabay.com/photo/2018/05/15/22/19/chicken-breast-3408952_1280.jpg")],
    "디저트": [("아이스크림", "https://cdn.pixabay.com/photo/2015/04/08/13/13/ice-711462_1280.jpg"),
            ("케이크", "https://cdn.pixabay.com/photo/2017/05/07/08/56/cake-2291908_1280.jpg")]
}

# ---------------------------
# 음식 추천
# ---------------------------
if st.button("🍴 나에게 맞는 메뉴 추천받기"):
    if not preference:
        st.warning("👉 먼저 음식 취향을 하나 이상 선택해줘!")
    else:
        chosen_type = random.choice(preference)
        rec_food, food_img = random.choice(foods[chosen_type])
        st.success(f"✨ {name}님에게 추천하는 오늘의 메뉴는 **{rec_food} ({chosen_type})** 입니다!")

        st.image(food_img, caption=f"{rec_food}", use_container_width=True)

        reason = []
        if "행복" in mood or "신남" in mood:
            reason.append("기분 좋은 날엔 새로운 음식이 잘 어울려요 😋")
        if "피곤" in mood or "스트레스" in mood:
            reason.append("따뜻하고 든든한 메뉴로 에너지 충전!")
        if "비" in weather:
            reason.append("비 오는 날엔 따뜻한 음식이 최고죠 ☔")
        if "더움" in weather:
            reason.append("시원하고 가벼운 음식 추천 🧊")
        if "추움" in weather:
            reason.append("따뜻한 국물이 있는 음식이 어울려요 🍲")
        if age < 20:
            reason.append("젊고 활기찬 입맛엔 자극적인 메뉴도 좋아요 🔥")
        if gender == "여성" and "디저트" in preference:
            reason.append("디저트로 마무리하면 완벽한 하루 🍰")

        st.info("추천 이유: " + " ".join(reason))

        order = st.button("🚀 이 메뉴로 주문하기")
        if order:
            with st.spinner("배달 주문을 접수 중입니다..."):
                time.sleep(2)
            st.success(f"주문이 완료되었습니다! 🛵 {rec_food}이(가) 곧 도착합니다 🍽️")
            st.balloons()

# ---------------------------
# 주문 시간 안내
# ---------------------------
st.write("---")
st.subheader("⏰ 주문 타이밍 안내")

now = datetime.now()
hour = now.hour

if 6 <= hour < 10:
    st.info("지금은 아침 시간이에요! 가벼운 식사로 하루를 시작해요 ☀️")
elif 11 <= hour < 13:
    st.info("점심 러시아워 직전이에요 🍱 지금 주문하면 대기 시간 최소!")
elif 18 <= hour < 20:
    st.warning("저녁 피크타임이에요 ⚠️ 조금 일찍 주문하는 걸 추천드려요!")
else:
    st.info("여유로운 시간이에요 😌 언제든 주문 가능!")

st.write("---")
st.caption("© 2025 먹PICK! Prototype v3. Made with Streamlit 💛")
