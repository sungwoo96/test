import random

pro = [
        "여기 빵 있어? 라는 표현", "무슨 날씨를 좋아하니? 라는 표현", "아니 계란은 살 필요 없어라는 표현", "흐린 날이 가장 좋아라는 표현",\
        "개를 키우는 게 어렵니? 라는 표현", "사야할 게 뭐가 있지? 라는 표현", "우리 쌀 있나? 라는 표현", "너는 컴퓨터를 자주 사용하니? 라는 표현",\
        "컴퓨터로 숙제를 하니? 라는 표현", "그녀는 그것을 수리해야 한다.", "그래 우리는 좀 필요해(좀 살 필요가 있어) 라는 표현",\
        "People can make f________ because they have common i_________.", "아니 나는 그것을 자주(종종) 사용하지 않아 라는 표현",\
        "하늘은 맑고 푸르다 라는 표현"
]

ans = [
        "Is there any bread?", "What is the weather like?", "No. We don't need to buy eggs", "Cloudy days are the best",\
        "Is it difficult to keep a dog?", "What is on our shopping list?", "Do we have any rice?",\
        "Do you use your computer often?", "Do you type up homework on your computer?", "She needs to fix it",\
        "Yes. We should buy some", "friends,interests", "No. I don't often use it", "The skies are clear and blue"
]

while True:
    i = random.randrange(0, 14)
    print(pro[i])
    user = input("답: ")
    if user == ans[i]:
        print("정답! ")
    else:
        print(f"오답, 답: {ans[i]}")