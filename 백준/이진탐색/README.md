[이진탐색]
=====

1. 개념
* 어떤 값을 찾을때 정렬의 특징을 이요하여 빨리 찾음
* 정렬되어 있는 어떤 값을 찾을때 O(N) -> O(logN)
* 처음부터 생각하기 어려움, 쉬운 방법부터 생각
2. 시간복잡도
* O(logN)
3. 핵심코드 - 외우기
def search(st, en, target):
    if st==en:
        pass
        return
    mid = (st+en) // 2
    if nums[mid] < target:
        search(mid+1, en, target)
    else:
        search(st, mid, target)

----
