# freq = [0]*26 #개수
# alpha = input()
# #소문자 대문자로 변환
# alpha = alpha.upper()


# for i in alpha:
#     freq[ord(i)-65] += 1

# result_index = freq.index(max(freq))
# #중복 확인
# check = True
# for i in range(26):
#     if i != result_index and freq[i] == freq[result_index]:
#         check = False
#         break

# if check:
#     print(chr(65+result_index))
# else:
#     print("?")
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])