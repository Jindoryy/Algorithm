Pythonic Code
==

1. enumerate() = 인덱스, 값 반환
2. key = lambda x : (조건)
* ex) sorted(리스트 기입, key = lambda x : (-x[0], -x[1])) = 인덱스 0을 기준으로 내림차순 후 1을 기준으로 내림차순
3. swap 구현 (튜플 이용)
* ex) a, b = b, a
4. join (str 문자형 일떄만 사용가능 - map을 이용해 int에서 str로 변경 하면서 사용 가능)
* print(' '.join(map(str, int형 리스트 기입))
