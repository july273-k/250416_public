import streamlit as st

# 질문 및 선택지
questions = [
    "1. 사람들과의 대화에서 에너지를 얻는 편인가요?",
    "2. 친구와 영화를 보는 것보다 혼자 책을 읽는 것을 더 선호하나요?",
    "3. 계획을 세우는 것을 좋아하나요?",
    "4. 감정보다 논리적인 결정을 선호하나요?",
    "5. 사람들과의 교류를 즐기는 편인가요?",
    "6. 세부사항을 신경 쓰는 편인가요?",
    "7. 다가오는 일을 미리 계획하는 편인가요?",
    "8. 새로운 아이디어를 생각해내는 것을 좋아하나요?",
    "9. 사교 모임에서 더 많은 에너지를 얻는 편인가요?",
    "10. 규칙을 따르는 것이 좋나요?",
    "11. 변화가 두렵나요?",
    "12. 직관적인가요?",
    "13. 감정을 쉽게 표현하는 편인가요?",
    "14. 혼자서 자신을 발견하는 것을 더 좋게 느끼나요?",
    "15. 주어진 일에 대한 피드백을 잘 받아들이나요?",
    "16. 새로운 사람들을 쉽게 만나는 편인가요?",
    "17. 자발적인 모임에 참여하는 것을 좋아하나요?",
    "18. 혼자만의 시간을 소중하게 생각하나요?",
    "19. 마지막 순간에 결정을 내리는 것을 선호하나요?",
    "20. 즉흥적으로 행동하는 것을 좋아하나요?"
]

# MBTI 점수 초기화
mbti_score = {
    'E': 0,
    'I': 0,
    'S': 0,
    'N': 0,
    'T': 0,
    'F': 0,
    'J': 0,
    'P': 0,
}

# 애플리케이션 제목
st.title("MBTI 테스트 🧩")

# 질문에 대한 응답 수집
for question in questions:
    response = st.slider(question, 1, 5, 3)  # 1에서 5 사이의 점수를 받음
    # 점수에 따라 MBTI 평가
    if question.startswith("1") or question.startswith("5") or question.startswith("9"):
        mbti_score['E'] += response  # E의 경우
    else:
        mbti_score['I'] += response  # I의 경우

    if question.startswith("2") or question.startswith("3") or question.startswith("10"):
        mbti_score['S'] += response  # S의 경우
    else:
        mbti_score['N'] += response  # N의 경우

    if question.startswith("4") or question.startswith("10") or question.startswith("15"):
        mbti_score['T'] += response  # T의 경우
    else:
        mbti_score['F'] += response  # F의 경우

    if question.startswith("10") or question.startswith("13") or question.startswith("19"):
        mbti_score['J'] += response  # J의 경우
    else:
        mbti_score['P'] += response  # P의 경우

# MBTI 유형 결정
mbti_type = ""
mbti_type += 'E' if mbti_score['E'] > mbti_score['I'] else 'I'
mbti_type += 'S' if mbti_score['S'] > mbti_score['N'] else 'N'
mbti_type += 'T' if mbti_score['T'] > mbti_score['F'] else 'F'
mbti_type += 'J' if mbti_score['J'] > mbti_score['P'] else 'P'

# 결과 출력
st.subheader("결과 🎉")
st.write(f"당신의 MBTI 유형은: **{mbti_type}**")

# MBTI 설명 추가
mbti_descriptions = {
    "ISTJ": "규칙적이고 신뢰 있는 유형입니다. 책임감이 강하고 효율적으로 일을 처리합니다.",
    "ISFJ": "따뜻하고 배려하는 성격입니다. 사람들을 돕는 것을 좋아합니다.",
    "INFJ": "창의적이고 깊이 있는 사고를 하는 유형입니다. 사람들과 상황에 대한 직관이 뛰어납니다.",
    "INTJ": "전략적인 사고를 중요시하며 목표 지향적입니다. 독립적인 성향이 강합니다.",
    "ISTP": "문제 해결에 능하며 실용적인 성격입니다. 즉흥적인 행동을 좋아합니다.",
    "ISFP": "예술적이고 감정적으로 깊이 있는 성격입니다. 자신의 감정을 소중하게 여깁니다.",
    "INFP": "이상주의적이며 감정이 풍부한 유형입니다. 사람과의 관계를 중요시합니다.",
    "INTP": "논리적 사고가 뛰어나며 혁신적인 아이디어를 생각해내는 것을 좋아합니다.",
    "ESTP": "호기심이 많고 활동적인 성격입니다. 즉각적인 경험을 중시합니다.",
    "ESFP": "사교적이고 활기찬 성격입니다. 즐거움과 즐길 것을 중요시합니다.",
    "ENFP": "열정적이고 사람들과의 관계를 좋아하며 창의적인 사고를 합니다.",
    "ENTP": "도전적이고 창의적이며 논리적인 사고를 선호합니다.",
    "ESTJ": "조직적이고 효율적인 성격입니다. 명확한 규칙을 중시합니다.",
    "ESFJ": "사람들과의 관계를 중요시하며 헌신적입니다.",
    "ENFJ": "타인을 돕고 이해하는 것을 중요하게 여깁니다.",
    "ENTJ": "리더십과 목표 지향성이 강하며 전략적인 사고를 중요시합니다."
}

# 결과 설명 출력
if mbti_type in mbti_descriptions:
    st.write(f"**{mbti_type}**: {mbti_descriptions[mbti_type]} 🌟")

# 스트림릿 실행
