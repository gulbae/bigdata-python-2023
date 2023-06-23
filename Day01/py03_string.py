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

# 문자열 포매팅
# % => string formating
print('I ate %s apples' % ('three')) # & string formatting
print('I ate %d apples' % (3))
print('pi is %f' % 3.14159265359)
print('pi is %10.2f' % 3.14159265359)

# 날짜 => 문자열 포맷팅
import datetime as dt

curr_dt = dt.datetime.now()
print(curr_dt)
fmt_dt = curr_dt.strftime('%Y년%m월%d일')
print('오늘 날짜는 %s 입니다' % fmt_dt)


# 최신 포매팅
apple_num = 3
print(f'I ate {apple_num} apples') # => I ate 3 apples
print(f'I ate {apple_num:0.4f} apples') # => I ate 3.0000 apples
apple_num = 'three'
print(f'I ate {apple_num} apples') # => I ate three apples

print(f'오늘 날짜는 {fmt_dt}') # => 오늘 날짜는 2023년 06월 16일

# 문자열 함수
# Life is short, You need Python
print(origin.count('o')) # => 3 # count => 문자, 문자열의 개수
print(origin.find('Python')) # => 24 # find => 문자(열)의 시작 인덱스
print(origin.find('python')) # => -1
print(origin.find('w')) # => -1 (일치하는 결과가 없을 때) 

print('/'.join(origin)) # => L/i/f/e/ /i/s/ /s/h/o/r/t/,/ /Y/o/u/ /n/e/e/d/ /P/y/t/h/o/n
# '문자(열)'을 join() 에 있는 문자열이랑 하나씩 합침
print(origin.upper()) # => LIFE IS SHORT, YOU NEED PYTHON # 대문자로
print(origin.lower()) # => life is short, you need python # 소문자로
print(origin.capitalize()) # => life is short, you need python # 시작 문자만 대문자
print(origin.title()) # => Life Is Short, You Need Python # 단어의 첫번째 글자만 대문자로

#공백지우기
print('start','     Hello    ', 'end') # start      Hello     end
print('start','     Hello    '.lstrip(), 'end') # start Hello     end # 왼쪽 공백 지우기 # , 는 자동 공백 하나
print('start'+'     Hello    '.lstrip() +'end') # startHello    end
print('start','     Hello    '.rstrip(), 'end') # start      Hello end # 오른쪽 공백 지우기
print('start','     Hello    '.strip(), 'end') # start Hello end # 양쪽 공백 지우기

result = origin.split(' ') # 공백으로 자르기
print(result) # => ['Life', 'is', 'short,', 'You', 'need', 'Python']
result = origin.replace(',', '').split(' ') # , 를 지우고 공백으로 자르기
print(result) # => ['Life', 'is', 'short', 'You', 'need', 'Python']

print(result[2]) # => short