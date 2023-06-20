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
