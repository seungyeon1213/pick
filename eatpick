import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="먹PICK!", page_icon="🍔", layout="centered")

st.title("🍔 먹PICK - 나만의 음식 추천 앱")
st.caption("기분・날씨・시간을 고려한 스마트 메뉴 추천 서비스")

# ---------------------------
# 사용자 입력 영역
# ---------------------------

st.subheader("1️⃣ 오늘의 상태 입력하기")

mood = st.selectbox("오늘 기분은 어때?", ["행복 😊", "보통 😐", "피곤 😩", "스트레스 😤", "신남 🤩"])
weather = st.selectbox("오늘 날씨는?", ["맑음 ☀️", "흐림 🌥️", "비 🌧️", "추움 🥶", "더움 🥵"])
meal_time = st.radio("지금은 어떤 시간대야?", ["아침", "점심", "저녁", "야식"])

st.write("---")

# ---------------------------
# 음식 추천 로직
# ---------------------------

foods = {
    "아침": ["샌드위치", "시리얼", "김밥", "아보카도토스트", "죽"],
    "점심": ["비빔밥", "돈까스", "김치찌개", "햄버거", "샐러드", "초밥"],
    "저녁": ["치킨", "파스타", "삼겹살", "볶음밥", "피자", "닭갈비"],
    "야식": ["라면", "떡볶이", "순대", "핫도그", "치즈볼"]
}

if st.button("🍴 추천받기"):
    rec_food = random.choice(foods[meal_time])
    st.success(f"오늘은 **{rec_food}** 어때요?")
    
    # 추천 이유 표시
    reason = []
    if "행복" in mood or "신남" in mood:
        reason.append("기분 좋은 날엔 새로운 메뉴가 어울려요!")
    if "피곤" in mood or "스트레스" in mood:
        reason.append("따뜻하고 든든한 음식이 힘이 돼요!")
    if "비" in weather:
        reason.append("비 오는 날엔 따뜻한 음식이 최고죠 ☔")
    if "더움" in weather:
        reason.append("시원하고 가벼운 음식이 좋아요 🧊")
    if "추움" in weather:
        reason.append("따뜻한 국물이 있는 메뉴를 추천해요 🍲")

    if reason:
        st.info("추천 이유: " + " ".join(reason))

# ---------------------------
# 주문 최적화 기능 (시간 기반)
# ---------------------------

st.write("---")
st.subheader("2️⃣ 주문 최적화")

now = datetime.now()
hour = now.hour

if 6 <= hour < 10:
    suggestion = "아침 식사 시간이네요. 지금 바로 주문하면 30분 안에 받을 수 있어요!"
elif 11 <= hour < 13:
    suggestion = "점심 러시아워 전이에요 🍱 지금 주문하면 대기 시간 최소!"
elif 18 <= hour < 20:
    suggestion = "저녁 피크시간이에요! 미리 예약주문을 추천드려요 🍔"
else:
    suggestion = "한가한 시간이에요 😋 여유롭게 주문해보세요."

st.write(suggestion)

# ---------------------------
# 실시간 피드백 기능
# ---------------------------

st.write("---")
st.subheader("3️⃣ 실시간 피드백")

feedback = st.radio("추천 메뉴 마음에 들어?", ["좋아요 👍", "별로예요 👎", "나중에 먹을래요 ⏰"])

if feedback == "좋아요 👍":
    st.success("좋아요! 다음 추천에 반영할게요 😄")
elif feedback == "별로예요 👎":
    st.warning("알겠어요. 비슷한 음식은 제외할게요 🙅‍♀️")
elif feedback == "나중에 먹을래요 ⏰":
    st.info("좋아요! 저녁쯤 다시 추천드릴게요 🍽️")

st.write("---")
st.caption("© 2025 먹PICK! Prototype - made with Streamlit")
