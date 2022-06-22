# 실습 6-1
# from typing import MutableSequence
#
# def bubble_sort(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(n - 1):
#         for j in range(n - 1, i, -1):
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#
# if __name__ == "__main__":
#     print("버블 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 원소 수가 num인 배열을 생성
#
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#
#     bubble_sort(x) # 배열 x를 버블 정렬
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# 실습 6-2
# from typing import MutableSequence
#
# def bubble_sort(a: MutableSequence) -> None:
#     ccnt = 0 # 비교 횟수
#     scnt = 0 # 교환 횟수
#     n = len(a)
#     for i in range(n - 1):
#         print(f"패스 {i + 1}") # 패스의 횟수(1 ~ n) 출력
#         for j in range(n - 1, i, -1): # 주목하는 원소의 인덱스(n-1 ~ 0)
#             for m in range(0, n - 1): # ?
#                 print(f"{a[m]:2}" + ('  ' if m != j - 1 else # ?
#                                     ' +' if a[j - 1] > a[j] else ' -'), # ?
#                                     end='') # ?
#             print(f"{a[n - 1]:2}")
#             ccnt += 1
#             if a[j - 1] > a[j]:
#                 scnt += 1
#                 a[j - 1], a[j] = a[j], a[j - 1]
#         for m in range(0, n - 1):
#             print(f"{a[m]:2}", end='  ')
#         print(f"{a[n - 1]:2}")
#     print(f"비교를 {ccnt}번 했습니다.")
#     print(f"교환을 {scnt}번 했습니다.")
#
# if __name__ == "__main__":
#     print("버블 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 원소 수가 num인 배열을 생성
#
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#
#     bubble_sort(x) # 배열 x를 버블 정렬
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# 실습 6-3
# from typing import MutableSequence
#
# def bubble_sort(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(n - 1):
#         exchng = 0 # 패스에서 교환 횟수
#         for j in range(n - 1, i, -1): # 주목하는 원소의 인덱스(n-1 ~ 0)
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 exchng += 1
#         if exchng == 0:
#             break
#
# if __name__ == "__main__":
#     print("버블 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 원소 수가 num인 배열을 생성
#
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#
#     bubble_sort(x) # 배열 x를 버블 정렬
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# 실습 6-4
# from typing import MutableSequence
#
# def bubble_sort(a: MutableSequence) -> None:
#     n = len(a)
#     k = 0
#     while k < n - 1:
#         last = n - 1
#         for j in range(n - 1, k, -1): # 주목하는 원소의 인덱스(n-1 ~ 0)
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 last = j
#         k = last
#
# if __name__ == "__main__":
#     print("버블 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 원소 수가 num인 배열을 생성
#
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#
#     bubble_sort(x) # 배열 x를 버블 정렬
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# from typing import MutableSequence
#
# def shaker_sort(a: MutableSequence) -> None:
#     left = 0
#     right = len(a) - 1
#     last = right
#     while left < right: # 오른쪽이 왼쪽보다 큰 경우 교환
#         for j in range(right, left, -1): # 원소를 맨 뒤에서 맨 앞으로 스캔
#             if a[j - 1] > a[j]: # 앞의 값이 뒤보다 큰 경우에 교환
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 last = j # 가장 작은 원소를 last에 저장
#         left = last # left에 last(가장 작은 원소)를 저장
#
#         for j in range(left, right): # 원소를 맨 앞에서 맨 뒤로 스캔
#             if a[j] > a[j + 1]: # 앞의 값이 뒤보다 큰 경우에 교환
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 last = j # 가장 작은 원소를 last에 저장
#         right = last # right에 last(가장 작은 원소)를 저장
#
# if __name__ == "__main__":
#     print("버블 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 원소 수가 num인 배열을 생성
#
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#
#     shaker_sort(x) # 배열 x를 버블 정렬
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# from typing import MutableSequence
#
# def selection_sort(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(n - 1):
#         min = i
#         for j in range(i + 1, n):
#             if a[j] < a[min]:
#                 min = j
#         a[i], a[min] = a[min], a[i]
#
# if __name__ == "__main__":
#     print("버블 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 원소 수가 num인 배열을 생성
#
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#
#     selection_sort(x) # 배열 x를 버블 정렬
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# from typing import MutableSequence
#
# def insertion_sort(a:MutableSequence) -> None:
#     n = len(a) # 배열의 길이를 담아줌
#     for i in range(1, n): # 1에서 n-1까지 순회
#         j = i # j에 i를 담아줌 (i는 1에서 n-1까지)
#         tmp = a[i] # tmp에 a[i]번째를 담아줌 (a[i]번째는 두번째 원소부터 n-1번째 원소까지
#         while j > 0 and a[j - 1] > tmp: # j가 0보다 크고, a[j-1]번째 원소가 tmp보다 클때 동안 진행(계속 스캔해야 하는 조건)
#             a[j] = a[j - 1] # 왼쪽 원소를 선택한 원소의 자리에 담아줌
#             j -= 1 # 왼쪽으로 1칸 이동
#         a[j] = tmp
#
#
# if __name__ == "__main__":
#     print("단순 삽입 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 배열 num개 생성
#
#     for i in range(num): # i를 0부터 num - 1번째까지 순회
#         x[i] = int(input(f"x[{i}]: ")) # 배열의 [0] ~ [num-1]번째에 값을 사용자로부터 입력받음
#
#     insertion_sort(x) # 배열 x를 매개변수로 전달하여 단순 삽입 정렬 실행
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x[{i}] = {x[i]}")

# from typing import MutableSequence
#
# def binary_insertion_sort(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(1, n):
#         key = a[i]
#         pl = 0 # 검색 범위의 맨 앞 원소 인덱스
#         pr = i - 1 # 검색 범위의 맨 끝 원소 인덱스
#
#         while True:
#             pc = (pl + pr) // 2 # 검색 범위의 가운데 원소 인덱스
#             if a[pc] == key: # 검색 성공
#                 break
#             elif a[pc] < key:
#                 pl = pc + 1 # 검색 범위를 뒤쪽 절반으로 좁힘
#             else:
#                 pr = pc - 1 # 검색 범위를 앞쪽 절반으로 좁힘
#             if pl > pr:
#                 break
#
#         pd = pc + 1 if pl <= pr else pr + 1 # 삽입해야 할 위치의 인덱스
#
#         for j in range(i, pd, -1):
#             a[j] = a[j - 1]
#         a[pd] = key
#
# if __name__ == "__main__":
#     print("이진 삽입 정렬을 수행합니다.")
#     num = int(input("원소 수를 입력하세요.: "))
#     x = [None] * num # 원소 수가 num인 배열 생성
#
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]: "))
#
#     binary_insertion_sort(x) # 배열 x를 이진 삽입 정렬
#
#     print("오름차순으로 정렬했습니다.")
#     for i in range(num):
#         print(f"x{[i]} = {x[i]}")

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)

if __name__ == "__main__":
    print("이진 삽입 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num # 원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    binary_insertion_sort(x) # 배열 x를 이진 삽입 정렬

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x{[i]} = {x[i]}")