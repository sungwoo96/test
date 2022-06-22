import random

# 텍스트 추출하기
pro = [
    # 주관식 문제
    "지금부터 Employees 데이터 베이스를 사용하겠으니 모든 쿼리는 empolyees에서 수행하라는 의미의 SQL문을 쓰시오",\
    "다음 설명이 맞으면 O 틀리면 X 표시를 하시오 \n 1. SQL은 대·소문자를 구분한다. (  ) \n 2. ABC 테이블에서 DEF 열을 가져오라는 구문은 'SELECT ABC FROM DEF' 이다. (  ) \n 3. 테이블 개체에 접근할 때는 항상 '데이터베이스이름.테이블 이름' 형식을 갖춰야 한다. (  ) \n 4. 주석을 삽입할 때는 -- 또는 /* */ 을 사용한다. (  ) \n 5. 열 이름을 별도의 별칭으로 지정할 때는 열 이름 뒤에 'AS 별칭' 형식으로 붙인다.",\
    "데이터베이스, 테이블, 뷰, 인덱스 등의 데이터베이스 개체를 생성, 삭제, 변경하는 데 사용하는 SQL문(    )",\
    "데이터를 검색 및 삽입, 수정, 삭제하는 데 사용하는 SQL 문(    )",\
    "사용자에게 어떤 권한을 부여하거나 빼앗을 때 주로 사용하는 SQL 문(    )",\
    "다음 UPDATE 문의 빈칸을 채우시오 \n UPDATE testTBL4 \n (  ㄱ  ) Lname = '없음' \n (  ㄴ  ) Fname = 'Kyichi';",\
    "다음 빈칸에 들어갈 말은 무엇인가? \n 대용량 테이블의 데이터를 모두 삭제할 때 (  ㄱ  ) 명령을 사용하면 데이터가 상당히 느리게 삭제되고, (  ㄴ  ) 명령을 사용하면 데이터가 빠르게 삭제되면서 테이블의 형태는 남아있다. 또한 (  ㄷ  ) 명령을 사용하면 데이터가 빠르게 삭제되면서 테이블 자체도 사라진다.",\
    "다음 구문의 첫 번째 행은 입력 데이터에 오류가 있어도 중단하지 않고 삽입하는 INSERT 문이고, 두 번째 행은 기본키가 중복되어 세 번째 행의 UPDATE 문을 수행하는 INSERT 문이다. 빈칸을 채우시오. \n INSERT (  ㄱ  ) INTO memberTBL VALUES ('THOMAS', '토마스', '영국'); \n INSERT INTO memberTBL VALUES ('THOMAS', '톰하스', '미국') \n (  ㄴ  ) UPDATE userName = '톰하스', addr='미국';",\
    "다음은 cookDB의 회원 테이블(userTBL)에서 지역별로 가입일이 빠른 순으로 정렬하는 쿼리문이다. 빈칸을 채우시오. \n SELECT addr, (  ㄱ  ) OVER( (  ㄴ  ) addr ORDER BY mDate ASC) '지역별 가입일 빠른 순위', userName, mDate \n From userTBL;",\
    "다음 CTE 구문의 빈칸을 채우시오. \n WITH myTable(uid, total) \n AS \n ( SELECT userid, SUM(price+*amount) \n From buyTBL GROUP BY userid \n Select uid, (  ㄱ  ) From (  ㄴ  ) ORDER BY total DESC;",\
    "다음 숫자 데이터 형식의 바이트 수는 얼마인지 쓰시오 \n 1. TINYINT (  ) \n 2. BOOL (  ) \n 3. SMALLINT (  ) \n 4. MEDIUMINT (  ) \n 5. INT (  ) \n 6. BIGINT (  ) \n 7. FLOAT (  ) \n 8. DOUBLE (  )",\
    "문자 데이터 형식의 최대 크기가 작은 것부터 순서대로 나열하시오. \n ㄱ - Text   ㄴ - MEDIUMTEXT      ㄷ - TINYTEXT    ㄹ - LONGTEXT",\
    "다음은 두 변수의 값을 더하는 코드이다. 오류를 찾아 바르게 고치시오. \n SET var1 = 5; \n SET var2 =3; \n SELECT var1 + var2;",\
    "다음은 cookDB의 회원 테이블(userTBL)에서 키가 큰 사람 5명만 출력하기 위해 LIMIT 값을 변수로 사용하는 코드이다. 빈 칸을 채우시오. \n SET @cnt = 5; \n (  ㄱ  ) sqlText \n From 'SELECT userName, height FRM userTBL ORDER BY height DESC LIMIT (  ㄴ  )'; \n (  ㄷ  ) sqlText (  ㄹ  ) @cnt;",\
    "다음은 cookDB의 구매 테이블(buyTBL)에서 구매 개수를 정수로 보기 위해 CAST() 함수를 사용한 구문이다. 밑줄 친 부분을 CONVERT() 함수로 변환하시오. \n SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' From buyTBL;",\
    "각 쿼리의 실행 결과를 쓰시오. \n SELECT '100' + '200'; \n SELECT 100 + '200'; \n SELECT '100' + 200; \n SELECT 100 + 200;",\
    "각 쿼리의 실행 결과를 쓰시오. \n SELECT IF (200>100, '참', '거짓'); \n SELECT NULLIF(200,100); \n SELECT CONCAT_WS ('-', '2020', '01', '01'); \n SELECT ELT (2, 'IT', 'COOK', 'BOOK'); \n SELECT INSERT ('12345678', 3, 2, '@@@@'); \n SELECT REPEAT ('COOK',3); \n SELECT CEILING(5.4);",\
    "다음은 [그림 8-1]에 대한 설명이다. 빈칸을 채우시오 \n 분리된 데이터들은 서로 관계를 맺고 있는데 그중에서 가장 많이 사용되는 관계는 cookDB의 회원 테이블(userTBL)과 구매 테이블 (buyTBL)이 맺고 있는 (  ㄱ  ) 관계이다.",\
    "다음은 [그림 8-1]의 cookDB에서 KJD라는 아이디의 회원이 구매한 물건을 발송하기 위해 아이디, 이름, 물품, 주소, 연락처를 조인한 후 검색하는 쿼리문이다. 빈칸을 채우시오. \n SELECT U.userID, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS PHONE \n From userTBL U \n (  ㄱ  ) buyTBL B \n ON (  ㄴ  ) \n WHERE B.userID = 'KJD';",\
    "다음은 [그림 8-1]의 cookDB에서 구매 기록이 하나라도 있는 회원의 목록을 출력하는 쿼리문이다. 빈칸을 채우시오. \n SELECT (  ㄱ  ) U.userID, U.userName \n From userTBL U \n INNER JOIN buyTBL B \n ON U.userID = B.userID \n ORDER BY U.userID;",\
    "다음은 [그림 8-1]의 cookDB에서 구매 기록이 없는 회원을 포함한 전체 회원을 출력하는 쿼리문이다. 빈칸을 채우시오. \n SELECT U.userID, U.userName, B.prodName \n From userTBL U \n LEFT (  ㄱ  ) buyTBL B \n ON (  ㄴ  ) \n ORDER BY U.userID;",\
    "테이블 A(tableA)와 테이블 B(tableB)가 상호 조인하는 쿼리문을 작성하시오.",\
    "다음은 숫자를 음수와 양수로 구분하는 SQL 프로그램의 일부이다. 빈칸을 채우시오. \n DECLARE myData SMALLINT; \n SET myData = -1000 ;4 \n (  ㄱ  ) myData < 0 THEN \n SELECT '음수입니다.'; \n (  ㄴ  ) \n SELECT '양수입니다'; \n (  ㄷ  );",\
    "UNION ALL 연산자와 UNION 연산자의 기능 및 차이점을 간단히 설명하시오.",\
    "다음은 테이블이 없을 때 오류를 직접 처리하는 코드의 일부이다. 빈칸을 채우시오. \n DECLARE (    ) FOR 1146 SELECT '테이블이 없어요';",\
    "다음은 테이블 생성 시 기본키 제약 조건을 설정하는 문구이다. 빈칸을 채우시오. \n CREATE TABLE userTBL \n ( userID CHAR(8) NOT NULL, \n userName VARCHAR (10) NOT NULL, \n birthYear INT NOT NULL, \n (    ) PK_userTBL_userid (userID) \n ); \n \n 또는 \n \n CREATE TABLE userTBL \n ( userID CHAR(8) NOT NULL , \n userName VARCHAR (10) NOT NULL, birthYear INT NOT NULL \n ); \n ALTER TABLE userTBL \n (  ㄴ  ) PK_userTBL_userID \n (  ㄷ  ) (userID);",\
    "다음은 테이블 생성 시 외래키 제약 조건을 설정하는 문구이다. 빈칸을 채우시오. \n CREATE TABLE buyTBL \n ( num INT AUTO_INCREMENT NOT NULL PRIMARY KEY, \n userID CHAR(8) NOT NULL, \n prodName CHAR(6) NOT NULL \n ); \n ALTER TABLE buyTBL \n (  ㄱ  ) FK_userTBL_buyTBL \n (  ㄴ  ) KEY (userID) \n (  ㄷ  ) userTBL (userID);",\
    "다음은 테이블 생성 시 출생연도 (birthYear)를 입력하지 않으면 -1을 자동으로 입력하는 DEFAUET제약 조건을 설정하는 구문이다. 빈칸을 채우시오. \n DROP TABLE IF EXISTS userTBL; \n CREATE TABLE userTBL \n ( userID CHAR(8) NOT NULL PRIMARY KEY, \n username VARCHAR(10) NOT NULL, \n birthYear int NOT NULL \n ); \n ALTER TABLE userTBL \n (  ㄱ  ) birthYear (  ㄴ  ) -1;",\
    "다음 빈칸에 들어갈 말은 무엇인가? \n 1. 테이블을 생성할 때 특정 열을 압축하려면 테이블의 정의문 뒤에 (    ) 구문을 붙인다. \n 2. 임시 테이블은 CREATE (     ) TABLE 문으로 생성한다.",\
    "다음은 테이블을 수정하는 ALTER TABLE 문에 대한 설명이다. 빈칸을 채우시오. \n 1. 열추가 : ALTER TABLE 테이블명 (    ) 열이름 형식 ····; \n 2. 열 삭제 : ALTER TABLE 테이블명 (    ) 열 이름; \n 3. 열 이름 변경 : ALTER TABLE 테이블명 (    ) 기존열 새열 ····; \n 4. 기본키 제거 : ALTER TABLE 테이블명 (    ) ;",\
    "다음 빈칸에 들어갈 말은 무엇인가? \n 외래키의 (    ) 옵션은 기준 테이블의 데이터가 변경되었을 때 외래키 테이블의 데이터도 자동으로 변경되게 한다. [그림9-1]의 회원 테이블에서 강호동의 아이디가 KHD에서 Kang으로 변경되면 구매 테이블의 아이디 KHD도 Kang으로 자동 변경된다.",\
    "다음은 뷰를 생성하는 구문이다. 빈칸을 채우시오. \n CREATE (  ㄱ  ) 뷰 이름 \n (  ㄴ  ) \n SELECT 문장들;",\
    "다음 빈칸에 들어갈 말은 무엇인가? \n (  ㄱ  ) 인덱스는 테이블당 하나만 생성할 수 있고, (  ㄴ  ) 인덱스는 테이블당 여러 개를 생성할 수 있다. 또한 (  ㄱ  ) 인덱스는 행 데이터를 인덱스로 지정한 열에 맞춰서 자동으로 정렬한다.",\
    "다음 쿼리를 실행하면 각 열에 어떤 인덱스가 생성되는가? \n CREATE TABLE myTable \n ( a INT UNIQUE NOT NULL, \n b INT UNIQUE, \n c INT PRIMARY KEY \n );",\
    "다음은 보조 고유 인덱스를 생성하는 구문이다. 빈칸을 채우시오. CREATE (  ㄱ  ) 인덱스이름 \n (  ㄴ  ) 테이블이름 (열이름);",\
    "다음 설명이 맞으면 O 틀리면 X 를 표시하시오. \n 1. 인덱스는 행 단위에 생성한다. (  ) \n 2. WHERE 절에서 사용되는 열에 인덱스를 만드는 것이 좋다. (  ) \n 3. 데이터 중복도가 높은 열에 인덱스를 만들어야 효과적이다. (  ) \n 4. 외래키를 설정한 열에는 되도록 인덱스를 생성하는 것이 좋다. (  ) \n 5. 조인에 자주 사용되는 열에는 인덱스를 생성하지 않는 것이 좋다. (  ) \n 6. 클러스터형 인덱스는 테이블당 하나만 생성할 수 있다. (  ) \n 7. 사용하지 않는 인덱스는 제거하는 것이 좋다. (  )",\
    "다음은 스토어드 프로시저를 생성하고 호출하는 구문이다. 빈칸을 채우시오. \n (  ㄱ  ) $$ \n CREATE (  ㄴ  ) 스토어드프로시저이름(IN 또는 OUT 매개변수) \n BEGIN \n \n    이 부분에 SQL 프로그래밍 코딩 \n \n END $$ \n (  ㄱ  ) ; \n (  ㄷ  ) 스토어드프로시저이름 ();",\
    "다음은 스토어드 프로시저의 매개변수와 관련된 설명이다. 빈칸을 채우시오. \n 스토어드 프로시저에서 입력 매개변수는 (  ㄱ  ) 문을 앞에 붙이고, 출력 매개변수는 (  ㄴ  ) 문을 앞에 붙인다. 출력 매개변수에 값을 대입하기 위해서는 주로 (  ㄷ  ) 문을 사용한다.",\
    "다음은 정수형(int) 데이터 형식의 오버플로가 발생하면 실행을 멈추는 스토어드 프로시저의 일부다. 빈칸을 채우시오. \n DECLARE (    ) \n BEGIN \n  INT 형 오버플로가 발생하면 이 부분 수행 \n END;",\
    "다음 코드는 입력 매개변수로 테이블 이름을 전달하기 위한 스토어드 프로시저의 일부이다. 빈칸을 채우시오. \n SET @sqlQuery = CONCAT ('SELECT * FROM', tableName); \n (  ㄱ  ) myQuery FROM @sqlQuery; \n (  ㄴ  ) myQuery; \n DEALLOCATE (  ㄱ  ) myQuery;",\
    "다음은 스토어드 함수를 선언하고 호출하는 SQL 문이다. 빈칸을 채우시오. \n DELIMITER $$ \n CREATE FUNCTION calcAge(bYear INT) \n (  ㄱ  ) INT \n BEGIN \n    DECLARE age INT; \n     SET age = YEAR(CURDATE()) - bYear; \n   (  ㄴ  ) age; \n END $$ \n DELIMITER; \n SELECT (  ㄷ  ) (1979);",\
    "커서의 처리 과정을 순서대로 나열하시오. \n ㄱ - 커서열기 (OPEN) \n ㄴ - 커서 선언하기 (DECLARE CURSOR) \n ㄷ - 커서에서 데이터 가져오기 (FETCH) \n ㄹ - 반복 조건 선언하기 (DECLARE CONTINUE HANDLER) \n ㅁ - 커서 닫기 (CLOSE)",\
    "다음은 AFTER 트리거를 생성하는 SQL 문이다. 빈칸을 채우시오. DELIMITER // \n CREATE TRIGGER 트리거 이름 \n      (  ㄱ  ) DELETE 또는 INSERT 또는 UPDATE \n      (  ㄴ  ) 테이블이름 \n      (  ㄷ  ) \n BEGIN \n    트리거 실행 시 작동되는 코드 \n END // \n DELIMITER;",\
    "다음은 myUser(비밀번호 : my1234) 라는 사용자를 생성하는 문구이다. 빈칸을 채우시오. \n (  ㄱ  ) 'myUser'@'%'(  ㄴ  ) mysql_native_password BY 'my1234'; \n (  ㄷ  ) ALL PRIVILEGES ON *.* TO 'myUser'@'%' (  ㄹ  ) GRANT OPTION; \n FLUSH PRIVILEGES;",\
    
    # 객관식 문제 
    "MySQL의 한글 처리와 관련된 설명 중 옳지 않은 것은? \n 1. CHAR, VARCHAR는 영문과 한글을 모두 저장할 수 있다. \n 2. 내부적으로  UTF-8 코드를 사용한다. \n 3. 영문과 한글은 모두 3바이트를 할당한다. \n 4. CHAR(10)으로 영문과 한글 모두 10자까지 저장할 수 있다.",\
    "데이터베이스 개체의 이름에 대한 설명 중 옳은 것은? \n 1. a ~ , A ~ Z, 0 ~ 9, $, _ 를 사용할 수 있으며 영문은 대·소문자를 구분한다. \n 2. 예약어를 사용할 수 있다. \n 개체 이름 중간에 공백을 사용하려면 백틱(``)으로 묶어야 한다. \n 4. 개체 이름은 최대 64자로 제한된다.",\
    "examTable1 테이블이 다음과 같이 정의되었을 때 오류가 발생하는 INSERT 문은 무엇인가? \n 보기 - CREATE TABLE examTable1 (id int, uName char (5), age int); \n 1. INSERT INTO examTable1 VALUES (1, '토마스', 16); \n 2. INSERT INTO examTable1 (id, uName), VALUES (2, '에드워드'); \n INSTRT INTO examTable1 (uName, age, id) VALUES (1, '헨리', 14);",\
    "다음 중 JSON 관련 함수가 아닌 것을 모두 고르시오 \n ㄱ - JSON_VALID() ㄴ - JSON_FIND() \n ㄷ - JSON_EXTRACT() ㄹ - JSON_INSERT() \n ㅁ - JSON_REPLACE() ㅅ - JSON_ERASE()",\
    "대용량 데이터를 저장하는 방법에 대한 설명 중 틀린 것을 모두 고르시오. \n 1. LONGTEXT, LONGBLOB 데이터 형식은 최대 4GB 크기를 지원한다. \n 2. LONGTEXT는 텍스트 파일 또는 동영상 파일을 저장할 때 사용한다. \n 3. 테이블을 생성할 때 한글을 처리하는 데 문제가 없도록 기본 문자 세트를 utf8mb4로 지정하는것이 좋다. \n 4. 파일을 데이터로 입력할 때는 UPLOAD_FILE() 함수를 사용한다.",\
    "테이블에 관한 설명 중 옳은 것을 모두 고르시오. \n 1. 기본키는 하나의 열에만 설정해야 한다. \n 2. 기본키는 테이블당 하나씩만 설정해야 한다. \n 3. 기본키에 NULL 값을 입력할 수 없다. \n 4. 두 열을 합쳐서 하나의 기본키로 설정할 수 있다.",\
    "다음 중 뷰의 특징으로 적절하지 않은 것은? \n 1. 보안에 도움이 된다. \n 2. 복잡한 쿼리를 단순화해준다. \n 3. 가상의 테이블이라고도 불린다. \n 4. 프로그래밍 기능을 제공한다.",\
    "다음 중 MySQL의 속도를 느리게 하는 데 가장 큰 영향을 미치는 것은? \n 1. 루트노드   2. 리프노드 \n 3. 페이지 분할    4. B-Tree",\
    "다음 중 클러스터형 인덱스의 특징으로 옳지 않은 것은? \n 1. 클러스터형 인덱스 생성 시 데이터 페이지 전체가 다시 정렬된다. \n 2. 클러스터형 인덱스의 리프 페이지에는 데이터가 위치하는 주소 값이 저장된다. \n 3. 클러스터형 인덱스 보조 인덱스를 이용하는 것보다 검색속도가 빠르다. \n 4. 클러스터 인덱스는 테이블당 하나만 생성할 수 있다.",\
    "스토어드 프로시저의 매개변수 정보가 들어 있는 데이터 베이스와 테이블 이름은 무엇인가? \n 1. Information_schema.parameters \n 2. cookDB.parameters \n 3. mysql.parameters \n 4. procedure.parameters",\
    "다음 중 스토어드 함수에 대한 설명으로 옳지 않은 것을 모두 고르시오. \n 1. 스토어드 함수의 매개변수는 모두 입력 매개변수로 사용된다. \n 2. RETURN 문으로 하나 또는 여러 개의 값을 변환한다. \n 3. 주로 SELECT 문 안에서 호출된다. \n 4. 집합 결과를 반환하는 SELECT 문을 사용할 수 있다. \n 5. 어떤 계산을 통해 하나의 값을 반환하는 데 주로 사용한다. \n 6. 스토어드 함수를 생성하려면 시스템 변수인 log_bin_trust_function_creators를 ON으로 변경해야 한다.",\
    "다음 중 XAMPP에 포함되지 않는 제품은 무엇인가? \n 1. Xlink     2.Apache \n 3. MySQL 또는 MariaDB   4. PHP \n 5. perl",\
    "다음 중 윈도우용 MySQL의 설정 파일 이름은 무엇인가? \n 1.mysql.ini     2.my.ini \n 3.init.ini      4.my.php \n 5. mysql.php",\
    "다음 중 HTML 파일의 특징에 대한 설명으로 옳지 않은 것은? \n 1. HTML 파일의 확장자는 *.htm 또는 *.html이다. \n 2. HTML 파일은 텍스트 파일이므로 메모장 등의 편집기에서 작성하면 된다. \n 3. HTML 태그는 <> 안에 쓴다. \n 4. HTML은 대문자와 소문자를 구분한다. \n 5. HTML 파일은 <HTML> 태그로 시작해서 </HTML> 태그로 종료한다.",\
    "다음 중 HTML 태그에 대한 설명으로 옳지 않은 것을 모두 고르시오. \n 1. <BR> : 글자를 두껍게 한다. \n 2. <U> ··· </U> : 글자에 밑줄을 긋는다. \n 3. <HR> : 수직선을 긋는다. \n 4. <FONT> ··· </FONT> : 글자의 크기나 색상을 지정한다. \n 5. <A> ··· </A> : 표를 만든다. \n 6. <IMG> : 이미지 파일을 화면에 표시한다.",\
    "다음 중 PHP에 대한 설명으로 옳지 않은 것을 모두 고르시오. \n 1. 주석은 # 또는 /* */로 표현한다. \n 2. 변수 앞에는 $를 붙인다. \n 3.echo는 화면에 변수 등을 출력한다. \n 4. 변수 이름에는 밑줄 (_)을 사용하면 안 된다. \n 5. 데이터 형식에는 정수형(int), 실수형(double), 문자열형(string), 불형(boolean) 등이 있다. \n 6. PHP 문자열은 큰따옴표 또는 작은따옴표로 묶는다.",\
    "다음 중 PHP 내장 함수에 대한 설명으로 옳지 않은 것을 모두 고르시오. \n 1. max() : 최대값을 반환한다.   2. cell() : 소수점 아래 반올림 한다. \n 3.trim() : 문자열을 구분자로 잘라낸다.  4. str_split() : 문자열을 길이만큼 잘라서 배열로 분리한다. \n 5. explode() : 문자열을 구분자로 분리하여 배열로 저장한다."

    ]

ans = [
    # 주관식 답
    #5장 답 
    "USE empolyees", "X, X, X, O, O",\
    #6장 답
    "DDL", "DML", "DCL", "ㄱ - Auto_INCREMENT ㄴ - @@AUTO_INCREMENT_INCREMENT", "ㄱ - SET ㄴ - WHERE", "ㄱ - DELETE ㄴ - TRUNCATE ㄷ - DROP", "ㄱ - IGNORE ㄴ - DUPLICATE KEY", "ㄱ - ROW_NUMBER() ㄴ - PARTITION BY addr", "ㄱ - total ㄴ - buyTBL"\
    #7장 답
    "1, 1, 2, 3, 4, 8, 4, 8", "ㄷ -> ㄱ -> ㄴ -> ㄹ", "SET @Var1 = 5; \n SET @Var2 = 3; \n SELECT @Var1 + @Var2;", "ㄱ - PREPARE ㄴ - ? ㄷ - EXECUTE ㄹ - USING", "CONVERT(AVG(amount), SIGNED INTEGER", "300 \n 100200 \n 100200 \n 300", "거짓 \n 200 \n 2020-01-01 \n cook \n 12@@@@5678 \n cookcookcook \n 6",\
    #8장 답
    "1 : 다 (일대다)", "ㄱ - INNER JOIN ㄴ - B.userID = U.userID", "DISTINCT", "ㄱ - OUTER JOIN ㄴ - U.userID = B.userID", "SELECT * FROM tableA CROSS JOIN tableB;", "IF, ELSE, END ID", "UNION ALL - 중복값을 포함하여 모두 출력 UNISON 연산자 - 중복값을 제거하고 정렬하여 출력", "CONTINUE HANDLER",\
    #9장 답
    "ㄱ - CONSTRAINT PRIMARY KEY ㄴ - ADD CONSTRAINT ㄷ - PRIMARY KEY", "ㄱ - ADD CONSTRAINT ㄴ - FOREIGN ㄷ - REFERENCES", "ㄱ - ALTER COLUMN ㄴ - SET DEFAULT", "ㄱ - ROW_FORMAT = COMPRESSED ㄴ - TEMPORARY", "1. ADD homepage \n 2. DROP COLUMN \n 3. CHANGE COLUMN \n 4. DROP PRIMARY KEY", "ON UPDATE CASCADE", "ㄱ - VIEW ㄴ - AS",\
    #10장 답
    "ㄱ - 클러스터형 ㄴ - 보조", "1. myTable 테이블 생성 \n  2. a열에는 UNIQUE 제약 조건에 NOT NULL 설정 및 보조 인덱스 생성 \n 3. c열에는 기본키 설정 * 클러스터형 인덱스 생성", "ㄱ - UNIQUE INDEX ㄴ - ON", "X, O, X, O, X, O, O",\
    #11장 답    
    "ㄱ - DELIMITER ㄴ - PROCEDURE ㄷ - CALL", "ㄱ - IN ㄴ - OUT ㄷ - SELECT · INTO", "EXIT HANDLER FOR", "ㄱ - PREPARE ㄴ - EXECUTE", "ㄱ - RETURNS ㄴ - RETURN ㄷ - getAgeFunc", " ㄴ -> ㄹ -> ㄱ -> ㄷ -> ㅁ", "ㄱ - AFTER ㄴ - ON ㄷ - FOR EACH ROW",\
    #13장 답 
    "ㄱ - CREAT ㄴ - GRANT ㄷ - WITH",\
    # 객관식 답
    #5장 답
    "3", "3",\
    #6장 답
    "2",\
    #7장 답
    "ㄴ, ㅅ", "2, 4",\
    #9장 답
    "2, 4", "4",\
    #10장 답
    "1, 5", "3", "2",\
    #11장 답
    "1", "2, 4","4, 5, 6, 7",\
    #13장 답
    "1", "2", "4", "1, 3, 5", "1, 4", "3",\

]

while(True):
    rand = random.randrange(len(pro))

    print(pro[rand])

    user = input("답: ")
    print("\n")
    print("정답:", ans[rand])
    print("\n")
