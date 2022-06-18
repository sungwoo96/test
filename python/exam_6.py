import random

pro = [
        "동일한 테스트 케이스로 동일한 테스트를 반복하면 더이상 결함이 발견되지 않는 현상은 무엇인가?", "애플리케이션의 20%에 해당하는 코드에서 전체 결함의 80%가 발견된다는 법칙은 무엇인가?",\
        "소프트웨어의 결함을 모두 제거해도 사용자의 요구사항을 만족시키지 못하면 해당 소프트웨어는 품질이 높다고 말할 수 없는 것은 무엇인가?", "애플리케이션을 실행하지 않고, 소스 코드에 대한 코딩 표준, 코딩 스타일, 코드 복잡도 및 남은 결함을 발견하기 위하여 사용하는 테스트는 무엇인가?",\
        "사용자의 시각에서 생산된 제품의 결과를 테스트하는 것은 어떤 테스트인가?", "시스템에 과다 정보량을 부과하여 과부하시에도 시스템이 정상적으로 작동되는지를 확인하는 테스트는 어떤 테스트인가?",\
        "소프트웨어의 실시간 성능이나 전체적인 효율성을 테스트하며, 모든 단계에서 수행되는 테스트는 어떤 테스트인가?", "개발자의 입장에서 소프트웨어가 요구사항에 맞는지를 추적하는 데 중점을 두는 테스트는 어떤 테스트인가?",\
        "소프트웨어가 수행할 특정 기능을 알기 위해서 각 기능이 완전히 작동되는 것을 입증하는 테스트이고, 동치클래스 분해 및 경계값 분석을 이용하고, 의도대로 작동하고 있는지 확인하는 어떤 테스트인가?",\
        "테스트케이스를 정하고, 해당 입력 자료에 맞는 결과가 출력되는지 확인하는 기법(예상결과+실제결과)은 무엇인가?", "최소 한 번은 모든 문장이 수행되도록 구성하는 검증 기준은 무엇인가?",\
        "모든 조건문이 한번이상 수행되고, 조건식이 참/거짓일때 수행되도록 구성하는 검증기준은 무엇인가?", "조건식에 상관없이 개별 조건이 참/거짓일때 수행되도록 구성하는 검증기준은 무엇인가?",\
        "입력 조건의 중간값보다 경계값에서 오류가 발생할 확률이 높다는 점을 이용하는 분석방법은 무엇인가?", "입력조건이 유효한 경우와 그렇지 않은 경우의 입력 자료의 개수를 균등하게 정하는 것은 무엇인가?",\
        "그래프를 활용하여 입력 데이터간의 관계와 출력에 영향을 미치는 상황을 체계적으로 분석한 다음 효용성이 높은 테스트케이스를 선정하여 검사하는 기법은 무엇인가?",\
        "개발자의 장소에서 사용자가 개발자 앞에서 행하는 테스트 기법은 무엇인가?", "알파테스트, 베타테스트와 가장 밀접한 연관이 있는 테스트로, 개발한 소프트웨어가 사용자의 요구사항을 충족하는지에 중점을 두고 테스트하는 기법은 무엇인가?",\
        "하향식 통합에 있어서 모듈간의 통합 시험을 위해 일시적으로 필요한 조건만을 가지고 임시로 제공되는 시험용 모듈은 무엇인가?", "깊이우선방식과 너비우선방식이 있으며, 상위 컴포넌트 테스트에서 점진적으로 하위 컴포넌트 테스트로 가고, 하위 컴포넌트 개발이 완료되지 않은 경우 스텁을 사용하기도 하는 테스트는 무엇인가?",\
        "상향식 통합 테스트 순서를 서술하시오.", "하나의 주요 제어 모듈과 관련된 종속 모듈의 그룹인 클러스터가 필요하고, 데이터의 입출력을 확인하기 위해 더미모듈인 드라이버를 생성하는 테스트는 무엇인가?",\
        "샘플링 오라클에 대해 서술하시오.", "전수테스트가 불가능한 경우에 사용하고, 경계값 및 구간별 예상값 결과 작성시 사용하는 오라클은 무엇인가?", "테스트의 결과가 참인지 거짓인지 판단하기 위해서 사전에 정의된 참값을 입력하여 비교하고, 종류에는 참,샘플링,휴리스틱,일관성 검사가 있는 것은 무엇인가?",\
        "구현된 소프트웨어가 사용자 요구사항을 정확하게 준수했는지를 확인하기 위해 설계된 입력값, 실행조건, 기대결과 등으로 구성된 테스트 항목에 대한 명세서를 무엇이라 하는가?",\
        "테스트케이스를 적용하는 순서에 따라 여러개의 테스트 케이스들을 묶은 집합으로, 테스트 케이스들을 적용하는 구체적인 절차를 명세한 문서이고, 테스트 순서에 대한 구체적인 절차, 사전조건, 입력데이터 등이 설정되어 있는 것은 무엇인가?",\
        "가상의 사용자를 만들어 테스트를 수행함으로써 성능의 목표 달성 여부를 확인하는 도구는 무엇인가?", "프로그램을 실행하지 않고 분석하는 도구를 무엇이라 하는가?",\
        "테스트하네스의 종류 중 테스트 대상의 하위 모듈을 호출하고, 파라미터를 전달하고, 모듈 테스트 수행 후의 결과를 도출하는 것은 무엇인가?", "테스트하네스의 종류 중 제어모듈이 호출하는 타 모듈의 기능을 단순 수행하고, 일시로 필요한 조건만 가지고 있는 테스트용 모듈은 무엇인가?",\
        "테스트하네스의 종류 중 자동화된 테스트 실행 절차에 대한 명세서는 무엇인가?", "테스트하네스의 종류 중 사전에 사용자의 행위를 조건부로 입력하여 그 상황에 맞는 예정된 행위를 수행하는 객체는 무엇인가?",\
        "소프트웨어 개발자가 설계한 것과 다르게 동작하거나 다른 결과가 발생되는 것을 무엇이라 하는가?", "결함관리프로세스의 순서를 서술하시오.",\
        "결함 관리 측정지표의 종류를 서술하시오.", "클린코드작성원칙을 서술하시오.", "외계인 코드에 대해 서술하시오.", "정적분석도구의 종류에 대해 서술하시오.",\
        "클린코드에 대해 서술하시오.", "시스템에 여러가지 결함을 주어 실패하도록 한 후 올바르게 복구되는지를 확인하는 테스트는 무엇인가?",\
        "시스템에 과도한 정보량이나 빈도 등을 부과하여 과부하시에도 소프트웨어가 정상적으로 실행되는지를 확인하는 테스트는 무엇인가?", "소프트웨어의 변경 또는 수정된 코드에 새로운 결함(오류)이 없음을 확인하는 테스트는 무엇인가?",\
        "변경된 소프트웨어와 기존 소프트웨어에 동일한 데이터를 입력하여 결과를 비교하는 테스트는 무엇인가?", "화이트박스테스트의 종류를 서술하시오.",\
        "모듈의 논리적 구조를 체계적으로 점검하는 것은 무엇인가?", "애플리케이션의 컴포넌트 및 모듈을 테스트하는 환경의 일부분으로, 테스트를 지원하기 위해 생성된 코드와 데이터를 의미하는 것은 무엇인가?",\
        "애플리케이션 성능측정지표의 종류에 대해 서술하시오.", "모든 테스트케이스의 입력값에 대해 기대하는 결과를 제공하고, 발생된 모든 오류 검출이 가능한 것은 무엇인가?",\
        "클린코드작성원칙 중 누구든지 쉽게 이해하는 코드를 작성하고, 이해하기 쉬운 용어를 사용하고, 들여쓰기를 사용하는 원칙은 어떤 것인가?", "블랙박스테스트기법의 종류를 서술하시오."
]

ans = [
        "살충제 패러독스", "파레토법칙", "오류-부재의 궤변", "정적테스트", "확인테스트", "강도테스트", "성능테스트", "검증테스트", "블랙박스테스트",\
        "동치분할검사", "문장검증기준(구문검증기준)", "분기검증기준(결정검증기준)", "조건검증기준", "경계값분석", "동치분할검사", "원인-효과 그래프 검사",\
        "알파테스트", "인수테스트", "스텁", "하향식통합테스트", "하위모듈들을 클러스터로 결합->드라이버작성->클러스터단위테스트->드라이버를 제거하고 클러스터를 상위로 결합",\
        "상향식통합테스트", "특정한 몇몇 테스트 케이스의 입력 값들에 대해서만 기대하는 결과를 제공하는 오라클", "샘플링오라클", "테스트오라클", "테스트케이스",\
        "테스트시나리오", "성능테스트도구", "정적분석도구", "테스트드라이버", "테스트스텁", "테스트스크립트", "목오브젝트", "결함관리", "결함관리계획->결함기록->결함검토->결함수정->결함재확인->결함상태추적 및 모니터링 활용->최종결함분석 및 보고서 작성",\
        "결함분포,결함추세,결함에이징", "가독성, 단순성, 의존성배제, 중복성최소화, 추상화", "아주 오래되거나, 개발자가 없어 유지보수 작업이 어려운 코드",\
        "pmd, cppcheck, SonarQube, checkstyle, ccm, cobertura", "누구나 쉽게 이해하고 수정 및 추가할 수 있는 단순, 명료한 코드, 잘 작성된 코드",\
        "회복테스트", "강도테스트", "회귀테스트", "병행테스트", "기초경로검사, 조건검사, 데이터흐름검사, 루프검사", "화이트박스테스트",\
        "테스트하네스", "처리량, 응답시간, 경과시간, 자원사용률", "참오라클", "가독성", "경계값분석, 오류예측, 동등분할기법, 동치클래스분해, 원인-결과 그래프"
]
print(len(pro))
j = int(input("랜덤 돌릴 끝 번호 입력: "))
while True:
    i = random.randrange(j-10, j)
    print(pro[i])
    user = input("답: ")
    print(ans[i], end="\n-------------------------------------------------------------------------------------------------------------------------\n")