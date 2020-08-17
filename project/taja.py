import random
import time


class typing_game():

    def __init__(self, word_k, word_e):
        self.word_k = word_k
        self.word_e = word_e

    def run(self):
        self.game_setting()

    def game_setting(self): #게임시작 전
        print("----타자 게임----")
        print("이름을 입력하세요.")
        self.name = input()
        print("=" * 30)
        print("[타자 게임] \n1.한글 \n2.영어 ")
        print("=" * 30)
        self.s = int(input())
        self.n = 1 # 문제 번호
        self.start = time.time() # 스톱워치를 실행
        self.make_game()

    def make_game(self):
        lang = '한글문제'
        lang_list = self.word_k.copy()

        if self.s == 1:
            pass
        elif self.s == 2:
            lang = '영어문제'
            lang_list = self.word_e.copy()
        else:
            print("게임을 다시 선택해 주세요")
            self.game_setting()
            return

        print(f'{lang} 시작합니다.')

        while True: # 문제 갯수
            # q = random.choice(word_e) # 랜덤으로 나오지만 중복됨
            q2 = random.randint(1,len(lang_list)) # 랜덤으로 인덱스번호를 뽑음
            q = lang_list.pop(q2-1) # 인덱스 번호는 0~9 / len의 요소 개수는 1~10 이기 때문에 -1함
            print("■■■■■문제",self.n,"번■■■■■")
            print(q)
            x = input() # 사용자 입력을 받습니다.

            if q == x:
                print("통과! 다음문제")
                self.n += 1
            elif q != x:
                print("오타! 다시 입력하세요")
                lang_list = self.reset_lang() # pop으로 문제를 빼다보면 없어지기 때문에 틀렸을땐 문제값을 초기화함
            else:
                print("수고하셨습니다 !")

            if self.n > 3:
                break

        self.end_game()

    def reset_lang(self):
        return self.word_k.copy() if self.s == 1 else self.word_e.copy()

    def end_game(self):
        end = time.time()
        et = end - self.start
        et = format(et,".2f") #정확한 기록을 위해 소수점 둘째 자리까지 출력합니다
        print(self.name,"의 기록은? ",et,"초")
        self.save_file(et)

    def save_file(self, et):
        result = open("타자게임 기록.csv", "a")
        result.write("\n{}".format(str(self.name)))
        result.write("{}\n".format(str(et)))


def main():

    rang_list = ['word_k.txt', 'word_e.txt']
    set_list = []

    for i in rang_list:
        f = open(i, "r", encoding = "utf-8")
        word_k = f.readline()
        f.close()
        list_lang = word_k.split(",")
        set_list.append(list_lang)

    game = typing_game(*set_list)
    game.run()


if __name__ == '__main__':
    main()