problems = {'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
            '변수': '데이터를 저장하는 메모리공간',
            '함수': '작업을 수행하는 문장들의 집합에 이름을 붙인것',
            '리스트': '서로 관련이 없는 항목들의 모임', }

# 파이썬, 변수, 함수, 리스트에 대한 딕셔너리를 정의함


def show_words(problems):  # show_words 함수를 정의
    display_meassage = ""  # 공백 선언
    i = 1                 # 객관식 보기 출력을 위해 i = 1선언
    for word in problems.keys():
        display_meassage += "("+str(i)+")"  # 숫자를 감쌀 괄호를 넣음
        display_meassage += word + " "  # problem의 있는 key값 그리고 공백을 더해준다.
        i += 1  # 다시 1을 더하고 다음 값을 출력하게 만든다
    print(display_meassage)  # 객관식 메세지를 출력시킴


for meaning in problems.values():  # meaning은 problems에 있는 value값 만큼 반복문 돌림
    print("다음은 어떤 단어에 대한 설명일까요? ")  # 출력
    print("\"" + meaning + "\"")  # 큰 따옴표로 묶고 problems의value값들을 차례대로 입력함

    correct = False  # 기본을 False로 초기화시킴
    while not correct:  # correct가 True일 때 돌아감
        show_words(problems)  # key값을 차례대로 출력함
        guess_word = input("")  # 맞출 값을 입력
        if problems[guess_word] == meaning:  # 추측값과 meaning값이 같으면
            print("정답입니다 !")  # 정답입니다 출력
            correct = True  # correct가 바뀌면서 다음 포문으로 넘어감
        else:
            print("정답이 아닙니다.")  # 아니면 정답이 아닙니다. 출력
