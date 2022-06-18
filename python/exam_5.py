import random

pro = [
        "소유권자의 사용자 ID가 ‘홍길동’인 스키마 ‘대학교’를 정의하는 SQL문 작성", "성별을 ‘남’ 또는 ‘여’와 같이 정해진 1개의 문자로 표현되는 도메인 SEX를 정의하는 SQL문 작성",\
        "<고객>테이블에서 ‘주소’가 ‘안산시’인 고객들의 ‘성명’과 ‘전화번호’를 ‘안산고객’이라는 뷰로 정의하는 SQL문 작성", "<고객>테이블에서 UNIQUE한 특성을 갖는 ‘고객번호’속성에 대해 내림차순으로 정렬하여 ‘고객번호_idx’라는 이름으로 인덱스를 정의하는 SQL문 작성",\
        "<학생>테이블에 최대 3문자로 구성되는 ‘학년’ 속성을 추가하는 SQL문 작성", "<학생>테이블의 ‘학번’ 필드의 데이터 타입과 크기를 VARCHAR(10)으로 하고 NULL값이 입력되지 않도록 변경",\
        "<학생>테이블을 제거하되, <학생>테이블을 참조하는 모든 데이터를 함께 제거하는 SQL문 작성", "ROLLBACK에 대해 서술하시오.",\
        "GRANT에 대해 서술하시오.", "DBA가 사용자 PARK에게 테이블 [STUDENT]의 데이터를 갱신할 수 있는 권한을 부여하는 SQL문 작성",\
        "김하늘에게 <학생>테이블에 대한 접근 및 조작에 관한 모든 권한을 부여하는 SQL문 작성", "김하늘에게 <강좌>테이블에 대해 삭제하는 권한을 부여하고, <강좌>테이블에 대해 삭제하는 권한을 다른 사람에게 부여할 수 있는 권한을  부여하는 SQL문 작성",\
        "임꺽정에게 부여된 <교수>테이블에 대한 SELECT, INSERT, DELETE권한을 취소하는 SQL문 작성", "<수강>테이블에 대해 임꺽정에게 부여된 UPDATE 권한과 임꺽정이 다른사람에게 UPDATE 권한을 부여할 수 있는 권한, 그리고 임꺽정이 다른 사람에게 부여한 UPDATE 권한을 모두 취소하는 SQL문 작성",\
        "COMMIT에 대해 서술하시오.", "SAVEPOINT P1으로 복원하는 SQL문 작성", "<사원>테이블에 (이름-홍승현, 부서-인터넷)을 삽입하는 SQL문 작성",\
        "<사원>테이블에 (장보고,기획,05/03/73,홍제동,90)을 삽입하는 SQL문 작성", "<사원>테이블에 있는 편집부의 모든 튜플을 편집부원(이름,생일,주소,기본급)테이블에 삽입하는 SQL문 작성",\
        "<사원>테이블에서 ‘임꺽정’에 대한 튜플을 삭제하는 SQL문 작성", "<사원>테이블에서 “인터넷”부서에 대한 모든 튜플을 삭제하는 SQL문 작성",\
        "<사원>테이블의 모든 레코드를 삭제하는 SQL문 작성", "<사원>테이블에서 “홍길동”의 주소를 “수색동”으로 수정하는 SQL문 작성", "<사원>테이블에서 “황진이”의 ‘부서’를 “기획부”로 변경하고 ‘기본급’을 5만원 인상하는 SQL문 작성",\
        "LIKE 연산자 %와 _와 #은 무슨 역할을 하는가?", "<사원>테이블에서 ‘주소’만 검색하되 같은’주소’는 한번만 출력하는 SQL문 작성", "<사원>테이블에서 ‘기본급’에 특별수당 10을 더한 월급을 “XX부서의 XXX의 월급 XXX” 형태로 출력하는 SQL문 작성",\
        "<사원>테이블에서 ‘기획’부의 모든 튜플을 검색하는 SQL문 작성", "<사원>테이블에서 “기획”부서에 근무하면서 “대흥동”에 사는 사람의 튜플을 검색하는 SQL문 작성",\
        "<사원>테이블에서 ‘부서’가 ‘기획’이거나 ‘인터넷’인 튜플을 검색하는 SQL문 작성", "<사원>테이블에서 성이 ‘김’인 사람의 튜플을 검색하는 SQL문 작성",\
        "<사원>테이블에서 ‘생일’이 ’01/01/69’에서 ’12/31/73’ 사이인 튜플을 검색하는 SQL문 작성", "<사원>테이블에서 ‘주소’가 NULL인 튜플을 검색하는 SQL문 작성",\
        "<사원>테이블에서 ‘주소’를 기준으로 내림차순 정렬시켜 상위 2개 튜플만 검색하는 SQL문 작성", "<사원>테이블에서 ‘부서’를 기준으로 오름차순 정렬하고, 같은 ‘부서’에 대해서는 ‘이름’을 기준으로 내림차순 정렬시켜서 검색하는 SQL문 작성",\
        "‘취미’가 ‘나이트댄스’인 사원의 ‘이름’과 ‘주소’를 검색하는 SQL문 작성(하위질의이용)", "취미활동을 하지 않는 사원들을 검색하는 SQL문을 작성(하위질의이용)",\
        "취미활동을 하는 사원들의 부서를 검색하는 SQL문을 작성(하위질의이용)", "사원과 여가활동 테이블에서 ’경력’이 10년 이상인 사원의 ‘이름’,’부서’,’취미’,’경력’을 검색하는 SQL문 작성",\
        "3,4학년의 학번, 이름을 조회하는 SQL문 작성(IN예약어 사용, <학생>테이블)", "학생(STUDENT)테이블에 전기과 50명, 전산과 100명, 전자과 50명이 있을 때 각각의 튜플의 수는?\n(1) SELECT DEPT FROM STUDENT;\n(2) SELECT DISTINCT DEPT FROM STUDENT;\n(3) SELECT COUNT(DISTINCT DEPT) FROM STUDENT WHERE DEPT=‘전산과’;",\
        "<Product>테이블에서 ‘price’속성 값이 NULL인 상품의 name을 오름차순 정렬하는 SQL문 작성", "<Staff>테이블과 Shop테이블을 이용하여 직원’id’가 10인 직원이 담당하는 상점의 이름(name)을 검색하는 SQL을 작성(단, 중복되는 레코드는 한번만 표시하고, 하위질의를 이용해 작성할 것)",\
        "<학생>테이블에서 학년이 3학년이고 점수가 80점 이상인 과목을 중복값을 제거하고 검색하는 SQL문 작성", "<CUSTOMER>테이블에서 모든 데이터를 ID를 기준으로 내림차순 정렬하여 검색하는 SQL문 작성",\
        "<상여금>테이블에서 ‘부서’별 ‘상여금’의 평균을 구하는 SQL문 작성", "<상여금>테이블에서 부서별 튜플 수를 검색하는 SQL문 작성", "<상여금>테이블에서 ‘상여금’이 100 이상인 사원이 2명 이상인 ‘부서’의 튜플 수를 구하는 SQL문 작성",\
        "<상여금>테이블의 ‘부서’, ‘상여내역’, 그리고 ‘상여금’에 대해 부서별 상여내역별 소계와 전체 합계를 검색하는 SQL문 작성(단, 속성명은 ‘상여금 합계’, ROLLUP 함수를 사용)",\
        "<상여금>테이블의 ‘부서’,’상여내역’, 그리고 ‘상여금’에 대해 부서별 상여내역별 소계와 전체합계를 검색하는 SQL문 작성(단, 속성명은 ‘상여금합계’, CUBE 함수를 사용)",\
        "<사원>테이블과 <직원>테이블을 통합하는 질의문을 작성하는 SQL문 작성(같은 레코드 중복X)", "<사원>테이블과 <직원>테이블에 공통으로 존재하는 레코드만 통합하는 SQL문 작성",\
        "<학생>테이블에서 학과별 튜플의 개수를 검색하는 SQL문 작성(WHERE사용x, GROUP BY 반드시 포함, 집계함수 사용)", "<성적>테이블에서 과목별 점수의 평균이 90점 이상인 ‘과목이름’, ‘최소점수’, ‘최대점수’를 검색(WHERE문x, GROUP BY와 HAVING 이용, 집계함수이용, ‘최소점수’와 ‘최대점수’는 AS 이용)",\
        "<학생정보>테이블의 ‘학번’과 <신청정보>테이블의 ‘학번’이 같고, ‘신청과목’이 “Java”인 학생들만을 대상으로 ‘이름’, ‘전공’, ‘신청과목’을 검색하는 SQL문 작성, 검색된 데이터는 ‘이름’, ‘전공’, ‘신청과목’을 기준으로 그룹을 지정하되 ‘전공’이 “컴퓨터공학”인 그룹만 표시",\
        "<sale>테이블과 <Product>테이블을 이용하여 상품명(name)이 “USB”로 시작하는 상품의 판매량(psale)합계를 검색하는 SQL문 작성(하위질의 이용)", "데이터베이스에 저장되어 있는 모든 데이터 개체들에 대한 정보의 집합체이고, 내용변경 권한은 데이터베이스 관리시스템(DBMS)이 가지며 사용자는 단순 조회만 가능하고, 시스템 카탈로그라고도 하는 것은 무엇인가?",\
        "사용자정보, 객체정보, 무결성 제약정보 등과 같이 데이터 관리를 위한 데이터를 무엇이라 하는가?", "<사원>테이블과 <자격증>테이블에서 하위질의를 이용하여 사원중에 자격증이 없는 사원의 ‘이름’, ‘재직년도’, ‘기본급’을 검색하는 SQL문 작성",\
        "<사원>테이블과 <자격증>테이블에서 자격증을 2개 이상 가진 사원의 ‘이름’을 검색하는 SQL문 작성(GROUP BY이용)", "<학생>테이블에서 3학년 학생에 대한 모든 속성을 추출한 <3학년학생>뷰를 정의하는 SQL문 작성(단, <3학년학생>뷰는 갱신이나 삽입 연산이 수행될 때 뷰 정의 조건을 따라야 함)",\
        "<강좌>테이블과 <교수>테이블에서 ‘교수번호’가 같은 튜플을 조인하여 ‘강좌명’, ‘강의실’, ‘수강제한인원’, ‘교수이름’ 속성을 갖는 <강좌교수>뷰 정의\n강좌(강좌번호, 강좌명, 학점, 수강인원, 강의실, 학기, 연도, 교수번호)\n교수(교수번호, 주민등록번호, 이름, 직위, 재직년도)",\
        "홍길동에게 <강좌>테이블을 검색하는 권한을 부여하는 SQL문을 작성", "홍길동에게 <학생>테이블에 대한 접근 및 조작에 관한 모든 권한을 부여하고, 해당 권한을 다른 사람에게 부여할 수 있는 권한을 부여하는 SQL문을 작성",\
        "박문수에게 부여된 <교수>테이블에 대한 INSERT 권한을 취소하는 SQL문을 작성", "<수강>테이블에 대해 박문수에게 부여된 SELECT 권한과 박문수가 다른 사람에게 SELECT 권한을 부여할 수 있는 권한, 박문수가 다른 사람에게 부여한 SELECT 권한을 모두 취소하는 SQL문을 작성",\
        "<상품>테이블에서 ‘제품코드’가 “P-20”인 제품을 모두 삭제하고 (“P-20”,”PLAYER”,8800,6600)인 제품을 다시 입력하는 SQL문을 작성\n삭제:\n삽입:",\
        "<거래내역>테이블에서 ‘총액’이 가장 큰 거래처의 ‘상호’와 ‘총액’을 검색하는 SQL문을 작성", "<성적>테이블에서 이름이 ‘LEE’인 모든 튜플의 ‘점수’속성에 10을 더하는 SQL문을 작성"
]

ans = [
        "CREATE SCHEMA 대학교 AUTHORIZATION 홍길동;", "CREATE DOMAIN SEX CHAR(1) DEFAULT ‘남’ CONSTRAINT VALID-SEX CHECK(VALUE IN(‘남’, ‘여’));",\
        "CREATE VIEW 안산고객(성명,전화번호) AS SELECT 성명,전화번호 FROM 고객 WHERE 주소=‘안산시’;", "CREATE UNIQUE INDEX 고객번호_idx ON 고객(고객번호 DESC);",\
        "ALTER TABLE 학생 ADD 학년 VARCHAR(3);", "ALTER TABLE ‘학생’ ALTER 학번 VARCHAR(10) NOT NULL;", "DROP TABLE 학생 CASCADE;",\
        "변경되었으나 아직 COMMIT되지 않은 모든 내용들을 취소하고 데이터베이스를 이전 상태로 되돌린다.", "권한을 부여하는 데 사용된다.",\
        "GRANT UPDATE ON STUDENT TO PARK;", "GRANT ALL ON 학생 TO 김하늘;", "GRANT DELETE ON 강좌 TO 김하늘 WITH GRANT OPTION;",\
        "REVOKE SELECT, INSERT, DELETE ON 교수 FROM 임꺽정;", "REVOKE UPDATE ON 수강 FROM 임꺽정 CASCADE;", "트랜잭션이 수행한 내용을 데이터베이스에 반영하는 명령어",\
        "ROLLBACK TO P1;", "INSERT INTO 사원(이름,부서) VALUES(‘홍승현’, ‘인터넷’);", "INSERT INTO 사원 VALUES(‘장보고’,’기획’,#05/03/73#,’홍제동’,90);",\
        "INSERT INTO 편집부원(이름,생일,주소,기본급) SELECT 이름,생일,주소,기본급 FROM 사원 WHERE 부서=‘편집’;", "DELETE FROM 사원 WHERE 이름=‘임꺽정’;",\
        "DELETE FROM 사원 WHERE 부서=‘인터넷’;", "DELETE FROM 사원;", "UPDATE 사원 SET 주소=‘수색동’ WHERE 이름=‘홍길동’;", "UPDATE 사원 SET 부서=‘기획’,기본급=기본급+5 WHERE 이름=‘황진이’;",\
        "모든문자대표,문자하나대표,숫자하나대표", "SELECT DISTINCT 주소 FROM 사원;", "SELECT 부서+’부서의’ AS 부서2, 이름+’의 월급’ AS 이름2, 기본급+10 AS 기본급2 FROM 사원;",\
        "SELECT * FROM 사원 WHERE 부서=‘기획’;", "SELECT * FROM 사원 WHERE 부서=‘기획’ AND 주소=‘대흥동’;", "SELECT * FROM 사원 WHERE 부서=‘기획’ OR 부서-‘인터넷’;",\
        "SELECT * FROM 사원 WHERE 이름 LIKE ‘김%’;", "SELECT * FROM 사원 WHERE 생일 BETWEEN #01/01/69# AND #12/31/73#;", "SELECT * FROM 사원 WHERE 주소 IS NULL;",\
        "SELECT TOP 2 * FROM 사원 ORDER BY 주소 DESC;", "SELECT * FROM 사원 ORDER BY 부서 ASC, 이름 DESC;", "SELECT 이름,주소 FROM 사원 WHERE 이름=(SELECT 이름 FROM 여가활동 WHERE 취미=‘나이트댄스’);",\
        "SELECT * FROM 사원 WHERE 이름 NOT IN(SELECT 이름 FROM 여가활동);", "SELECT 부서 FROM 사원 WHERE EXISTS(SELECT 이름 FROM 여가활동 WHERE 여가활동.이름=사원.이름);",\
        "SELECT 사원.이름, 사원.부서, 여가활동.취미, 여가활동.경력 FROM 사원,여가활동 WHERE 여가활동.경력>=10 AND 사원.이름=여가활동.이름;", "SELECT 이름,학번 FROM 학생 WHERE 학생 IN(3,4);",\
        "200, 3, 1", "SELECT name FROM Product WHERE price IS NULL ORDER BY name;", "SELECT DISTINCT name FROM Shop WHERE id IN(SELECT shopid FROM Staff WHERE id=10);",\
        "SELECT DISTINCT 과목 FROM 학생 WHERE 학년>=3 AND 점수>=80;", "SELECT * FROM CUSTOMER ORDER BY ID DESC;", "SELECT 부서, AVG(상여금) AS 평균 FROM 상여금 GROUP BY 부서;",\
        "SELECT 부서, COUNT(*) AS 사원수 FROM 상여금 GROUP BY 부서;", "SELECT 부서, COUNT(*) AS 사원수 FROM 상여금 WHERE 상여금>=100 GROUP BY 부서 HAVING COUNT(*)>=2;",\
        "SELECT 부서, 상여내역, SUM(상여금) AS 상여금합계 FROM 상여금 GROUP BY ROLLUP(부서,상여내역);", "SELECT 부서, 상여내역, SUM(상여금) AS 상여금합계 FROM 상여금 GROUP BY CUBE(부서,상여내역);",\
        "SELECT * FROM 사원 UNION SELECT * FROM 직원;", "SELECT * FROM 사원 INTERSECT SELECT * FROM 직원;", "SELECT 학과, COUNT(*) AS 학과별튜플수 FROM 학생 GROUP BY 학과;",\
        "SELECT 과목이름, MIN(점수) AS 최소점수, MAX(점수) AS 최대점수 FROM 성적 GROUP BY 과목이름 HAVING AVG(점수)>=90;", "SELECT 이름, 전공, 신청과목 FROM 학생정보, 신청정보 WHERE 학생정보.학번=신청정보.학번 AND 신청과목=‘Java’ GROUP BY 이름,전공,신청과목 HAVING 전공=‘컴퓨터공학’;",\
        "SELECT SUM(psale) FROM sale WHERE pid IN(SELECT id FROM Product WHERE name LIKE ‘USB%’);", "데이터사전", "메타데이터",\
        "SELECT 이름, 재직년도, 기본급 FROM 사원 WHERE 이름 NOT IN(SELECT 이름 FROM 자격증);", "SELECT 이름 FROM 자격증 GROUP BY 이름 HAVING COUNT(*)>=2;",\
        "CREATE VIEW 3학년학생 AS SELECT * FROM 학생 WHERE 학년=3 WITH CHECK OPTION;", "CREATE VIEW 강좌교수(강좌명,강의실,수강제한인원,교수이름) AS SELECT 강좌명,강의실,수강인원,이름 FROM 강좌,교수 WHERE 강좌.교수번호=교수.교수번호;",\
        "GRANT SELECT ON 강좌 TO 홍길동;", "GRANT ALL ON 학생 TO 홍길동 WITH GRANT OPTION;", "REVOKE INSERT ON 교수 FROM 박문수;",\
        "REVOKE SELECT ON 수강 FROM 박문수 CASCADE;", "삭제:DELETE FROM 상품 WHERE 제품코드=‘P-20’;\n삽입:INSERT INTO 상품 VALUES(‘P-20’, ‘PLAYER’, 8800, 6600);",\
        "SELECT 상호,총액 FROM 거래내역 WHERE 총액 IN(SELECT MAX(총액) FROM 거래내역);", "UPDATE 성적 SET 점수=점수+10 WHERE 이름=‘LEE’;"
]
print(len(pro))

while True:
    i = random.randrange(0, 14)
    print(pro[i])
    user = input("답: ")
    if user == ans[i]:
        print("정답! ")
    else:
        print(f"오답, 답: {ans[i]}")