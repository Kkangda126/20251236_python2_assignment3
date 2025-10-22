class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}가 짖고 있습니다.")
    
    def info(self):
        print(f"이름:{self.name}, 나이:{self.age}살")
    
# 강아지 인스턴스 생성
dog1 = Dog("바둑이", 3)
dog2 = Dog("멍멍이", 5)

# 강아지가 짖는 메서드 호출
dog1.bark()
dog2.bark()

# 이름과 나이 호출
dog1.info()
dog2.info()