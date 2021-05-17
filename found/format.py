name = "minsu"
score = 90

#<<c언어 스타일>>
# %s-> 문자열 %d -> 정수 %f -> 실수
# %o-> 8진수 %x -> 16진수 %% 문자 '%' 표현
print("%s의 점수는 %d 점입니다. " % (name, score))
#format 메서드
print("{}의 점수는 {} 점입니다.".format(name,score))

#직접 대입
s1 = 'name : {0}'.format('BlockDMask')
#변수 대입
age = 55
s2 = 'age : {0}'.format(age)
#이름 대입
s3 = 'number : {num}, gender : {gen}'.format(num=1234, gen='남')
# 왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
print(s9)
 
 
# 오른쪽 정렬
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')
print(s10)
 
# 가운데 정렬
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c')
print(s11)

#공백 말고 다른 거 채우기
s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a')
print(s12)

#자리수와 소수점 표현하기

# 정수 N자리
s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
print(s15)
 
 
# 소수점 N자리
s16 = '아래 2자리 : {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.1234567, 3.14)



#f-string
print(f"{name}의 점수는 {score} 점입니다.")

