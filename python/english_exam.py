import random

pro = [
       # Unit1 주관식
       "취미를 가지고 있는 지 물어보는 표현", "테니스를 좋아한다는 표현", "수영을 즐긴다는 표현", "친구들과 영화보러 간다는 표현", \
       "매 주", "주말", "목요일이라는 표현", "길에서라는 표현", "우리 집 근처라는 표현", "강가라는 표현", \
       "Hobbies for Your Health", "Why do people have hobbies?", "Most people have h________ for f_______.", \
       "A hobby can i_______ your health and make your life i________.",\
       "Doctors say people with hobbies are h________.", "You need to t______ to play chess.", "Swimming or playing basketball helps to keey your body a______.",\
       "Hobbies are an interesting way to m______ people.", "People can make f______ because they have common i______.",\
       "29 percent of people in the United States like r______ as a hobby.",\
       # Unit1 객관식
       "What is true about hobbies?\na. They can keep you happy.\nb. They are fun.\nc. They can make your life more interesting.\nd. All of the above.\n",\
       "Which of the following is good exercise for your brain?\na. Dancing.\nb. Playing chess.\nc. Swimming\nd. Playing table tennis.\n", \
       "Which hobby keeps your body healthy?\na. Watching TV.\nb. Reading.\nc. Doing puzzles.\nd. Playing sports.",\
       "What is another good thing about hobbies?\na. You can keep old friends.\nb. A hobby is a good friend.\nc. You can make new friends.\nd. Friends join clubs together.",\
       # Unit2 주관식
       "What do we need from the store?", "사야할 게 뭐가 있지? 라는 표현", "What do we need to buy?", "크림이 좀 필요해 라는 표현",\
       "사과가 필요해 라는 표현", "우리 물을 좀 살 필요가 있어 라는 표현", "우리 계란 필요해? 라는 표현", "우리 사과 필요할까? 라는 표현", "수프를 사야할까? 라는 표현",\
       "우리 우유가 좀 필요할까? 라는 표현", "아니. 우리 좀 있어 라는 표현", "그래 우리는 그게 좀 필요해(그걸 좀 살 필요가 있어) 라는 표현", "아니 계란은 살 필요 없어라는 표현", "여기 빵 있어? 라는 표현",\
       "여기 누들 있어? 라는 표현", "우리 쌀 있나? 라는 표현", "서랍장 확인해 봐 라는 표현", "그것들은 서랍장에 있어 라는 표현", "서랍장 체크해봐 라는 표현",\
       "나는 슈퍼마켓에서 사는 것을 좋아한다 라는 표현", "얼마인가요? 라는 표현(2가지)", "you / Can / a / get / Eric? / basket,",\
       "over / is / The / section / dairy / there.", "cream. / need / buy / Next, / we / to / ice", "do / we / What / need? / else",\
       "last / is / The / jam. / thing", "we / need / Now / pay. / to", "Fruit is a natural s_______. It is d_______ and healthy.",\
       "Fruit is more than just f______. It has different m_______ in different cultures.", "Apples mean p_______ in Chinese culture.",\
       "Cherries are l_______ for f_______ in England.", "People bring pomegranates to w_______ in Greece.",\
       "Pomegranates have lots of s_______. They are a sign of many c_______ in China.",\
       # Unit2 객관식
       "Which of these is NOT true of fruit?\na. It tastes great.\nb. It is healthy.\nc. Some fruits have interesting meanings.\nd. It is Greek.\n",\
       "Which fruit has the most seeds?\na. Oranges\nb. Pomegranates\nc. Pears\nd. Apples\n",\
       "What do cherry blossoms mean to the Japanese?\na. Luck\nb. Beauty\nc. Love\nd. Peace\n",\
       "What is another appropriate title for the article?\na. Fruit Is Good for You\nb. China Has a Lot of Fruit\nc. Fruits Have Many Meanings\nd. Pomegranates Have a Lot of Seeds\n",\
       # Unit3 주관식
       "무슨 날씨를 좋아하니? 라는 표현", "날씨가 어떻니? 라는 표현", "여름이 가장 좋아 라는 표현", "가을은 나의 좋아하는 계절이야 라는 표현",\
       "나의 가장 좋아하는 계절은 겨울이야 라는 표현", "나는 맑은 날을 좋아해라는 표현", "내가 좋아하는 날씨는 맑은 날씨야 라는 표현", "흐린 날이 가장 좋아 라는 표현",\
       "좋은 날씨에요 라는 표현", "하늘은 맑고 푸르다 라는 표현", "날씨가 아주 안좋다 라는 표현",\
       # Unit4 주관식
       "네 컴퓨터를 가지고 있니? 라는 표현", "네 컴퓨터는 괜찮니? 라는 표현", "너는 컴퓨터를 자주 사용하니? 라는 표현", "컴퓨터 자판으로 숙제를 하니? 라는 표현",\
       "아니. 나는 내 여동생과 컴퓨터를 같이 써 라는 표현", "아니. 나는 내 룸메이트의 컴퓨터를 써 라는 표현",\
       "아니. 너무 느려 라는 표현", "사실은 아니야. 나는 새 것이 필요해 라는 표현", "응 나는 매일 컴퓨터를 사용해 라는 표현", "아니 나는 그것을 자주(종종) 사용하지 않아 라는 표현",\
       "아니. 나는 손으로 쓰면서 숙제를 해 라는 표현", "응. 나는 타이핑으로 숙제를 해 라는 표현",\
       "에릭(Eric's)의 폰에 문제가 생겼어요 라는 표현", "작동하지 않는다 라는 표현", "팸(Pam's)의 카메라가 깨졌어요 라는 표현", "그녀는 그것을 수리해야한다",\
       "Almost everyone owns a s_______", "Today, many people prefer to use their phones to surf the I_______",\
       "You can use the Mobile Internet for Facebook, e-mails, and g_______",\
       "Mobile Internet users don't need to be at h_______ or at w________", "You can use the Mobile Internet from a bus or a t________",\
       "Some c________ can use a smartphone, but they cannot speak in full sentences",\
       # Unit5 주관식
       "동물을 좋아하니? 라는 표현", "애완동물이 있니? 라는 표현", "개를 키우는 게 어렵니? 라는 표현", "너의 애완동물을 어디에 기르니? 라는 표현",\
       "응. 나는 동물을 좋아해 라는 표현", "아니. 나는 동물을 좋아하지 않아 라는 표현", "아니 나는 동물을 싫어해 라는 표현",\
       "응. 나는 개를 길러(가지고있어) 라는 표현", "물론이지. 우리 집엔 고양이가 있어 라는 표현", "아니. 난 애완동물이 없어 라는 표현",\
       "응 그건 힘들어(개를 기르는 건)", "응 쉽지 않아(개를 기르는 건)", "아니야 쉬워(개를 기르는 건)", "사실 그렇지 않아. 문제 없어(개를 기르는 건)",\
       "나는 그것을 케이지(우리) 안에 보관해 라는 표현", "내 애완동물은 마당에 살아 라는 표현",\
       "Jessica is the Joubert family's pet h______",\
       "She's like a d______ to Tonie and Shirley Joubert. They t______ her like family",\
       "She u______ some English words.",\
       "She enjoys d______ coffee. She drinks it every day.",\
       "She swims with w______ hippos in the river after she has b______",\
       "She can leave a_____ t_____, but she is always back for dinner",\
       "Tonie leaves Jessica in the y______ at night",\
       "Sometimes, Jessica enters the house and breaks f______",\
       "Dylan is a teenager. He is (young / old.)",\
       "About half of all humans live in cities. (Animals / People) like to live together.",\
       "I understand a little French. I (know / ask) the meanings of a few words.",\
       "These wild flowers grow in (nature / the basement).",\
       "My son break things a lot. We (often / seldom) need to fix them.",\
       "The store sells furniture. You can find some nice (T-shirts and pants / tables and chairs) there.",\
       "He's a very gentle boy. He (always / never) fights.",\
       "That river is dangerous. It runs very (fast / slow)",\
       # A4용지 긴글
       # "<Conversation 1>\nSam : Do you have our shopping list, Lisa?\nLisa : Yes. We'll go to Homeplus.\n(At the Supermarket)\nSam : What's the first thing to buy?\nLisa : The first thing is some tomatoes. The vegetables are over there.\nSam : We need the strong adhesive.\nLisa : Why?\nSam : Our desk is broken. I have to fix it.\nLisa : Okay. Here is the adhesive.\n\tThe next thing is rice. We don't have any rice.\nSam : Where is rice?\nLisa : Here it is.\nSam : Ok. Let's pay now.\n",\
       # "<Conversation 2>\nJohn : Hi, Sera. It's cloudy today.\nSera : Yeah. It seems that it will rain.\nJohn : That sounds bad. I don't like the rain.\nSera : Me, too. It's very uncomfortable on rainy days.\nJohn : I agree. Did you bring an umbrella?\nSera : No. That's that I worried about.\nJohn : Don't worry. I have a very big umbrella.\nSera : Oh, that's good. Can I share your umbrella?\nJohn : No problem.\n",\
       # "<Conversation 3>\nJin : Hi, John. Do you know much about computers?\nJohn : Of course. What's wrong?\nJin : I think my computer is broken. Can you help me fix it?\nJohn : Okay. I'll take a look.\n(after ten minutes later...)\nJohn : Jin, the computer looks quite old and hard to fix it.\n\tYou had better buy a new one.\nJin : Ok. I'll buy one.\n",\
       ]
ans = [
       # Unit1 주관식 답
       "Do you have any hobbies?", "I like to play tennis", "I enjoy swimming", "I go to the movies with my friends", \
       "every week", "on weekends", "on Thursdays", "on the street", "near my house", "by the river", "당신의 건강을 위한 취미",\
       "건강증진, 두뇌발달", "hobbies,fun", "improve,interesting", "healthier", "think", "active", "meet", "friends,interests",\
       "reading",\
       # Unit1 객관식 답
       "d", "b", "d", "c",\
       # Unit2 주관식 답
       "사야할 게 뭐가 있지?", "What is on our shopping list?", "사야할 게 뭐가 있지?", "We need some cream", "We need some apples",\
       "We need to buy some water", "Do we need eggs?", "Do we need any apples?", "Do we need to buy soup?", "Should we get some milk?",\
       "No. We have some", "Yes. We should buy some", "No. We don't need to buy eggs", "Is there any bread?", "Are there any noodles?",\
       "Do we have any rice?", "Look in the drawer", "They are in the drawer", "Check in the drawer", "I like to buy at the supermarket",\
       "How much do the cost?,How much does the cost?", "Can you get a basket, Eric?", "The dairy section is over there",\
       "Next, we need to buy ice cream", "What else do we need?", "The last thing is jam", "Now we need to pay",\
       "snack,delicious", "food,meanings","peace", "lucky,farmers","weddings","seeds,children",\
       # Unit2 객관식 답
       "d", "b", "b", "c",\
       # Unit3 주관식 답
       "What's the weather like?", "How is the weather?", "I like summer best", "Fall is my favorite season",\
       "My favorite season is winter", "I love sunny days", "My favorite weather is sunny", "Cloudy days are the best",\
       "It's a lovely day", "The skies are clear and blue", "The weather is terrible",\
       # Unit4 주관식 답
       "Do you have your own computer?", "Is your computer OK?", "Do you use your computer often?", "Do you type up homework on your computer?",\
       "No. I share a computer with my sister", "No. I use my roommate's computer",\
       "No. It's very slow", "Not really. I need a new one", "Yes. I use my computer every day", "No. I don't often use it",\
       "No. I write my homework by hand", "Yes. I type up some of my homework",\
       "There is a problem with Eric's phone", "It doesn't work", "Pam's camera is broken", "She needs to fix it",\
       "smartphone", "Internet", "games", "home,work", "train", "children",\
       # Unit5 주관식 답
       "Do you like animals?", "Do you have any pets?", "Is it difficult to keep a dog?", "Where do you keep your pet?",\
       "Yes. I love animals", "No. I don't like animals", "No. I hate animals",\
       "Yes. I have a dog", "Sure. We have a cat at home",  "No. I don't have any pets",\
       "Yeah. It's hard work", "Yes. It's not easy", "No. It's easy", "Not really. It's no problem",\
       "I keep it in a cage", "My pet lives in the yard",\
       "hippo", "daughter,treat", "understands", "drinking", "wild,breakfast", "any,time", "yard", "furniture",\
       "young", "People", "know", "nature", "often", "tables and chairs", "never", "fast",\

       ]


while True:
       rd = random.randrange(126)
       print(pro[rd])
       user_input = input("답 입력: ")
       if ans[rd] == user_input:
              print("정답! \n")
       else:
              print(f"오답, 답: {ans[rd]}\n")