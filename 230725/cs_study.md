# 0. 개발자 필수지식
- 데이터 교환형식
    - JSON과 직렬화와 역직렬화
        - JSON
            - 클라이언트와 서버 간의 HTTP 통신을 위한 텍스트 데이터 포맷
            - 키:값으로 구성되며, 각 객체를 배열로 묶을 수 있다
            
            - JSON 내장 객체
                - JSON.stringfy(JSON형식의 객체)
                    - 객체 => 문자열로 변환하며, 이를 직렬화(serialize)라고 한다.
                    - 통신할 때는 문자열로 직렬화하여 주고 받는 것이 안전한다.
                - JSON.parse(JSON형식의 문자열)
                    - 문자열 => 객체로 변환하며, 이를 역직렬화(deserialize)라고 한다.
                    - 통신으로 받은 문자열은 객체로 역직렬화하여 사용하는 것이 편리하다.

    - XML
        - XML을 사용하면 공유 가능한 방식으로 데이터를 정의하고 저장할 수 있음
        