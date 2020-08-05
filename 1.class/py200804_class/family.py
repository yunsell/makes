class Family:
    lastname = "김"
    def __init__(self, name):
        self.firstname = name # 객체변수

# Family 클래스의 인스턴스는 father이고, father는 객체이다.
father = Family("길동")
mother = Family("하니")
son= Family("우리")
Family.lastname # 김