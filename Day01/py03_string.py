# 문자열

value = "Hello World"
print(value)
print('Hello World')

print('"큰 따옴표" 출력')
print('"헬"로 월드')
print("'작은 따옴표'출력")

value = '''
대신귀
여운알
파카를
드리겠
습니다
''' # 여러줄 문장

print(value)

'''
여러 줄 주석
파이썬은 여러 줄 주석이 없어서 여러줄 문자열로 이 역할을 대신함
'''

print('Hello' + 'World!') #(문자열 안됨)
print('Hello'*3) #Hello를 3번 반복(+는 안됨)

print(len('Life is short')) # 공백 포함 길이(13자리)
print(len('삶은..계란..')) # 8자리 

origin = 'Life is short, You need Python'
print(origin[0]) # N번째 글자 출력
print(origin[1])
print(origin[13])
print(origin[9] + origin[10] + origin[0] + origin[25] + 
      origin[4] + origin[6] + origin[9] + origin[1] + origin[12])
print(origin[0:4]) # == print(origin[:4]) [시작점:종료점]
print(origin[7:13])

print(origin[15:]) # index 15부터 끝까지
print(origin[15:-7]) # 음수는 뒤에서부터 인덱스 -1부터 시작

print('I ate %s apples' % ('three')) # & string formatting
print('I ate %d apples' % (3))
print('pi is %f' % 3.14159265359)
print('pi is %10.2f' % 3.14159265359)

# 날짜 문자열 포맷팅
import datetime as dt

curr_dt = dt.datetime.now()
print(curr_dt)
fmt_dt = curr_dt.strftime('%Y년%m월%d일')
print('오늘 날짜는 %s 입니다' % fmt_dt)