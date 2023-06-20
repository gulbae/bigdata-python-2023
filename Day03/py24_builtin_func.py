# 내장함수
print(abs(-4)) # 절대값
print(chr(65)) # 숫자를 캐릭터로 변경 65 - A, 97 - a # ascii코드 번호
print(ord('a')) # ascii코드값으로 바꿔줌
print(chr(44032)) # utf-8 코드
print(ord('각')) # 유니코드 값으로 바꿔줌
print(chr(13)) # enter
print(min(1,4)) # 최소값
print(max(1,4)) # 최대값
print(eval('1 + 4')) # eval[uate] 실행
print(hex(234)) # 16진수
a = 0
b = 1
print(id(a)) # a변수의 메모리 주소
print(id(b)) # b변수의 메모리 주소

print(int('3')) # digit number 문자열을 정수로 변환... 그만하고 싶어요... 집에 갈래요....
print(pow(2, 10)) # 제곱승 함수
print(2 ** 10) # 제곱승 연산자..............................................ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ........ 그만......

# map(f, iterable) 함수(f)와 반복가능한(iterable) 데이터
def three_times(numberlist):
    result = []
    for n in numberlist:
        result.append(n*3)
    return result

l1 = [3, 6, 9, 12]
print(three_times(l1)) # 함수가 파라미터로 리스트 받아서 for문으로 전부 처리

def threetimes(x):
    return x * 3

print(list(map(threetimes, l1))) 
# 함수를 첫번째 파라미터로, 두번째를 적용시킬 리스트로
# 리스트 요소 하나씩을 함수를 통해서 처리를 해주는 방법

print(list(map(str, l1))) # ['3', '6', '9', '12']
print(list(map(float, l1))) # [3.0, 6.0, 9.0, 12.0]
# map결과가 map object이기 때문에 list, tuple, set로 형변환필요


#range list 두개를 잘 활용하면 순차적인 리스트를 쉽게 만들 수 있음
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10,15))) #[10, 11, 12, 13, 14]
print(list(range(3,100,3))) # 3부터 100까지 3씩증가 [3, 6, 9, 12, ..., 99]
print(sum(list(range(3,100,3)))) # 3의 배수 99까지의 합계 py12_control.py 연습문제와 동일

# round - 올림,반올림
print(round(4.6)) # 5
print(round(3.141592, 4)) # 3.1416
l1.sort()
sorted(l1) #정렬

print(type(21)) # 변수/값의 타입을 리턴 <class 'int'>
print(type('21')) # <class 'str'>
print(type(True))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type(None))
