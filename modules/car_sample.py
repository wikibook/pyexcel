# File name: car.py
class Car(): # 클래스 선언
    def __init__(self, size, color):
        self.size = size    # 인스턴스 변수 생성 및 초기화
        self.color = color  # 인스턴스 변수 생성 및 초기화
        
    def move(self):
        print("자동차({0} & {1})가 움직입니다.".format(self.size, self.color))
