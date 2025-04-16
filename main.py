import streamlit as st

# 질문 목록과 이모지
questions = [
    "1. 👥 저는 새로운 사람을 만나는 것을 좋아합니다.",
    "2. 📅 사전에 계획을 세우는 것을 선호합니다.",
    "3. 🧠 저는 문제를 해결할 때 논리적인 접근을 중시합니다.",
    "4. 🎉 저는 혼자 보다는 사람들과 함께 하는 것을 더 좋아합니다.",
    "5. 🏡 저녁 모임에 참석하기 보다는 집에서 쉬는 것을 선호합니다.",
    "6. 💬 저는 비판을 듣는 것에 대해 개방적입니다.",
    "7. 🌍 저는 새로운 경험을 시도하는 것을 두려워하지 않습니다.",
    "8. 🗂️ 저는 확실한 계획을 세우는 것이 편안합니다.",
    "9. 😌 저는 감정을 잘 표현하는 편입니다.",
    "10. 🔍 저는 분석적인 사고를 중요시합니다.",
    "11. ❤️ 저는 다른 사람들의 감정을 잘 이해할 수 있다고 생각합니다.",
    "12. 🎲 저는 즉흥적으로 결정하는 것을 선호합니다.",
    "13. 🤗 저는 친구와 깊은 대화를 나누는 것을 좋아합니다.",
    "14. 📜 저는 규칙이나 절차를 준수하는 것이 중요하다고 생각합니다.",
    "15. 🌅 저는 일이 끝나고 여유 있는 시간을 즐깁니다.",
    "16. 🤝 저는 팀워크를 중시합니다.",
    "17. 🔄 저는 결과보다 과정이 중요하다고 생각합니다.",
    "18. 😌 저는 불확실한 상황에서 더 편안함을 느낍니다.",
    "19. 🎯 저는 목표를 세우고 달성하는 것을 중요시합니다.",
    "20. 🗣️ 저는 타인의 피드백을 중요하게 생각합니다."
]

# 리커트 척도 옵션
options = ["😩 전혀 동의하지 않음", "😐 동의하지 않음", "😕 보통", "😊 동의함", "😁 매우 동의함"]

# 사용자 입력을 위한 리스트
responses = []

# 스트림릿 페이지 제목
st.title("🌟 MBTI 테스트 🌟")

# 각 질문에 대한 응답 수집
for question in questions:
    response = st.radio(question, options, key=question)
    responses.append(options.index(response) + 1)  # 1부터 시작하는 점수로 변환

# 결과 확인 버튼
if st.button("🎉 결과 확인 🎉"):
    total_score = sum(responses)

    # MBTI 결과 판단 로직 (단순화된 예시)
    if total_score <= 20:
        mbti_result = "ISFJ 🤗"
    elif total_score <= 40:
        mbti_result = "ESFJ 😊"
    elif total_score <= 60:
        mbti_result = "ENTP 😄"
    elif total_score <= 80:
        mbti_result = "INTP 😐"
    else:
        mbti_result = "INFJ 💖"

    st.write(f"💥 당신의 MBTI 유형은 **{mbti_result}**입니다! 💥")
