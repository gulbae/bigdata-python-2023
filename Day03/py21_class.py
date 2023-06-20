# 클래스 예제

class Calculator:
    def __init__(self) -> None:
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        pass            # 뭘 쓸지 모르겠을때 pass 쓰고 일단 넘어갈 수 있음
    
mycalc = Calculator() # java와 달리 new 없음 Item item = New Item()
print(mycalc.add(40))
print(mycalc.add(50))
print(mycalc.sub(25))

val = 10
if val != 10:
    pass