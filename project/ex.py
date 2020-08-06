import random

import time

word_k = ["아이폰", "파이썬", "자바", "코딩", "깃", "컴퓨터", "마우스", "키보드", "모니터", "어플리케이션"]
word_e = ["iphone", "python", "java", "coding", "git", "computer", "mouse", "keyboard", "monitor", "application"]

def setting():
    global word_k,word_e
    word_k = ["아이폰", "파이썬", "자바", "코딩", "깃", "컴퓨터", "마우스", "키보드", "모니터", "어플리케이션"]
    word_e = ["iphone", "python", "java", "coding", "git", "computer", "mouse", "keyboard", "monitor", "application"]

name = []
print("이름을 입력하세요.")
name = input()
print("=" * 30)
print("[타자 게임] \n1.한글 \n2.영어 ")
print("=" * 30)
s=int(input())
n = 1    # 문제 번호
start = time.time()   # 스톱워치를 실행


if s == 1:      # 한글문제 선택
    print("[한글문제] 시작합니다.")
    while n <= 3:     # 문제 갯수
        # q = random.choice(word_e)             # 랜덤으로 나오지만 중복됨
        q2 = random.randint(1,len(word_k))      # 랜덤으로 인덱스번호를 뽑음
        q = word_k.pop(q2-1)                    # 인덱스 번호는 0~9 / len의 요소 개수는 1~10 이기 때문에 -1함
        print("■■■■■문제",n,"번■■■■■")
        print(q)
        x = input() # 사용자 입력을 받습니다.

        if q == x:
            print("통과! 다음문제")
            n = n + 1
        elif q != x:
            print("오타! 다시 입력하세요")
            setting()                            # pop으로 문제를 빼다보면 없어지기 때문에 틀렸을땐 문제값을 초기화함
        else:
            print("수고하셨습니다 !")

if s == 2:      # 영어문제 선택
    print("[영어문제] 시작합니다.")
    while n <= 3:
        q2 = random.randint(1,len(word_e))
        q = word_e.pop(q2-1)
        print("■■■■■문제",n,"번■■■■■")
        print(q)
        x = input()

        if q == x:
            print("통과! 다음문제")
            n = n + 1
        elif q != x:
            print("오타! 다시 입력하세요")
        else:
            print("수고하셨습니다 !")

end = time.time()
et = end - start
et = format(et,".2f")    #정확한 기록을 위해 소수점 둘째 자리까지 출력합니다
print(name,"의 기록은? ",et,"초")

result = open("타자게임 기록.csv", "a")
result.write(str(name))
result.write(str(et))
