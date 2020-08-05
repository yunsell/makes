prompt = """
문제. 나간다를 뜻하는 단어는? 
1. Add
2. Del
3. List
4. Quit
"""

number = 0
while number != 4:
    print(prompt)
    number = int(input("정답 : "))
    if number < 4:
        print("틀렸습니다.")
    elif number > 4:
         print("틀렸습니다.")
    else:
        number == 4
print("정답입니다.")