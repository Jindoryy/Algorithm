# Algorithm

코딩테스트 대비 알고리즘 문제 정리 (with Python)

# Pythonic Code

1. enumerate() = 인덱스, 값 반환
- ex) for idx, value in enumerate(리스트 기입):
2. key = lambda x : (조건)
- ex) sorted(리스트 기입, key = lambda x : (-x[0], -x[1])) = 인덱스 0을 기준으로 내림차순 후 1을 기준으로 내림차순
3. swap 구현 (튜플 이용)
- ex) a, b = b, a
4. join (str 문자형 일떄만 사용가능 - map을 이용해 int에서 str로 변경 하면서 사용 가능)
- ex) print(' '.join(map(str, int형 리스트 기입))
5. 리스트 자연스럽게 출력
- ex) print(list) => [1, 2, 3, 4, 5] / print(*list) => 1 2 3 4 5
6. while ~ else 구문, for ~ else 구문

# 시간복잡도
- 파이썬은 1초에 2천만번 연산을 함.
<img width="80%" src="https://user-images.githubusercontent.com/87755660/148132016-ac02ece1-4d2e-4ac6-912d-54748b89200d.JPG"/>

# 코딩테스트 시간 제한
코딩 테스트 문제에서 시간제한은 통상 1~5초가량이라는 점을 유의
혹여 문제에 명시되어 있지 않은 경우 대략 5초 정도라고 생각하고 문제를 푸는 것이 합리적
