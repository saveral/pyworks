# Person 클래스 생성과 사용
class Person:
    def __init__(self):  # 초기자(생성자) 함수
        self.name = "강하늘"
        self.age = 30

    def getname(self):      # 멤버변수에 직접 접근하지 않도록 get()을 사용
        return self.name
    def getage(self):
        return self.age

p = Person()   # 객체변수 - 인스턴스(instance)
#p.name = "빅바다"
#print(p.name, p.age)
print(p.getname(),p.getage())