"""
날짜 : 2022/02/18
이름 : 양대석
내용 : 코딩테스트 선택정렬 실습
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            # swap - 위치 교환
            tmp = array[j-1]
            array[j-1] = array[j]
            array[j] = tmp
        else:
            # 자기 앞에 자기보다 작은 데이터가 위치할 경우
            break

print(array)
