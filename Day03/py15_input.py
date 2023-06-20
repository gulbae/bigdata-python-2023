# 입출력
import datetime #날짜를 확인하는 모듈 가져옴

# birth_year = int(input('출생년도를 입력하세요 > ')) # 키보드입력 1998(무조건 string) => int()로 형변환

# print(f'당신의 출생년도는 {birth_year}년 입니다') # 콘솔출력 당신의 출생년도는 1998년 입니다
# curr_year = datetime.datetime.now().year # yyyy-MM-dd hh:mm:ss.ms
# print(curr_year)
# age = curr_year - birth_year
# print(f'당신의 나이는 {age}세 입니다')

a = 123
a = [3,6,9]
print(a)

print('Life''is''short') # Lifeisshort
print('Life'+'is'+'short') #위와 동일 Lifeisshort
print('Life','is','short') # Life is short
print('Life', 3.141592, True)

for i in range(20):
    if i == (len(range(20))-1):
        print(i, end='\n') #엔터를 없앨때
    else:
        print(i, end=', ') # end=', '  <- 끝문자 지정

print('Life', 'is', 'short', sep='&') # sep 별로 안쓰임

pi = 3.14159265359

print(f'PI = {pi:.4f}') #format string
print(f'PI = {pi:10.2f}')