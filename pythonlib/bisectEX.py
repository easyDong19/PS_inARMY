import bisect

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    #bisect == bisect_right 함수는 동일
    pos = bisect.bisect([60,70,80,90],score)
    grade = 'FDCBA'[pos]