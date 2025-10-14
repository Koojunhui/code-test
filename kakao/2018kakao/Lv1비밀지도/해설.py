def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # arr1[i]와 arr2[i]를 OR 연산하여 겹친 지도 생성
        row = bin(arr1[i] | arr2[i])[2:]  # 2진수 문자열로 변환 후 '0b' 제거
        row = row.zfill(n)  # n자리수 맞추기 (앞에 0 채우기)

        # 1 -> '#', 0 -> ' ' 로 변환
        row = row.replace('1', '#').replace('0', ' ')
        answer.append(row)
    return answer


# 예제 실행
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# ["#####","# # #", "### #", "# ##", "#####"]

print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
