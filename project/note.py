import random

import time

words = ["안녕 hi", "잘가 bye", "강아지 dog", "고양이 cat", "사자 tiger", "아이폰 apple",
         "파이썬 python", "자바 java", "코딩 coding", "깃 git", "컴퓨터 computer", "마우스 mouse",
         "키보드 keyboard", "모니터 screen"]

words2 = ["11","22","33","44"]
n = 1    # 문제 번호
print("[타자 게임] 준비되면 엔터 !! ")
input()    # 사용자가 엔터를 누를 때까지 기다립니다.

start = time.time()   # 스톱워치를 실행함
# q = random.choice(words)  # 위에 있는 단어들을 랜덤으로 출력



while n <= 3:
    q = random.choice(words2)
    print("==문제",n,"번==")
    print(q)
    x = input() # 사용자 입력을 받습니다.

    if q == x:
        print("통과, 다음문제 !")
        n = n + 1
        q = random.choice(words2)
    elif q != x:
        print("오타 ! 다시 입력하세요")
    else:
        print("수고하셨습니다 !")


end = time.time()
et = end - start
et = format(et,".2f")    #정확한 기록을 위해 소수점 둘째 자리까지 출력합니다
print("총 걸린 시간: ",et,"초")


