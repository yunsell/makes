# 파일읽기
# 현재 디렉토리의 202007 폴더에서 파일을 읽어 온다.

import os


def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        # line1은 파일 검증을 위해 사용 - zim의 텍스트 파일 참고
        line1 = f.readline()
        line2 = f.readline()
        print(line2)


with os.scandir('202007') as entries:
    for entry in entries:
        print(entry.name)
        read_data("202007\\%s" % entry.name)
