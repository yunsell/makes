"""
MySale은 파일명을 전달받아 2차원 리스트로 변화하는 초기화작업을 진행
"""
class MySale:
    def __init__(self, source):
        self.souce = source
        self.sale_list = []
        self.transform_data()

    def transform_data(self):
        with open(self.souce, 'r', encoding='utf8') as f:
            line1 = f.readline()
            line2 = f.readline()
            temp_list = line2.split(",")
            length = len(temp_list)
            length = int(length / 2)
            for i in range(length):
                self.sale_list.append([temp_list[i * 2], int(temp_list[i * 2 + 1])])
