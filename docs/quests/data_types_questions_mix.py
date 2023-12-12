def get_question(): # 문제와 답안들, 정답 번호, 점수를 입력받아 딕셔너리로 반환하는 함수를 선언합니다.
    question_info = {"question": "", "answers": ["", "", "", ""], "correct_answer": "", "score": ""}
    # 항목과 관련된 키 값을 부여한 뒤, 해당 키값의 밸류는 비어있는 딕셔너리를 생성합니다.
    question_info["question"] = input("문제를 입력하세요: ") #질문을 입력받는 곳인 question_info에서 "question"이라는 key에 access한 뒤 밸류인 문제를 입력받아 할당하도록 합니다.
    for i in range(4): # 질문의 보기에 해당되는 내용을 4번 입력받기 위해 반복문에 4번의 회수를 지정한 뒤 해당 위치에 정보가 입력될 수 있도록 index화 합니다
        question_info["answers"][i] = input(str(i+1) + "번 보기를 입력하세요: ") 
        #"answers"키에 access한 뒤 인덱스 위치를 지정하고,인덱스는 0번부터 시작하므로 해당 위치에 1을 더해 어떤 것을 입력해야 하는지 표시한 뒤 value에 입력을 받아 할당하도록 한다.
    question_info["correct_answer"] = int(input("정답 번호를 입력하세요: "))
    # 마찬가지로 "correct_answer"에 access한 뒤 어떤 것을 입력해야 하는지 출력한 뒤,정답 번호의 정수 숫자 데이터를 value에 입력받아 할당하도록 한다.
    question_info["score"] = int(input("배점을 입력하세요: "))
    # 이것도 "score"에 access한 뒤 어떤 것을 입력해야 하는 지 출력한 뒤 배점의 정수 숫자 데이터 value를 입력 받아 할당하도록 한다.
    
    return question_info # 입력된 question_info 딕셔너리를 반환한다.

mixed_questions = [] # mixed_questions라는 빈 리스트를 선언한다. 이곳은 나중에 return으로 반환받은 데이터가 적립되는 공간이다.

for i in range(3): # 해당 행동을 3번 반복하기 위해 range를 3으로 설정하고 이것을 인덱스화 한다. 구문 안에 있는 내용을 3회 반복한다.
    print(str(i+1) + "번 문제") # 3번 반복할 동안 0번 위치에 있을 인덱스 값에 1을 더해 몇번째인지 표시한다.(내가 몇 번째 문제를 입력받는 지 알 수 있게 한다.)
    question = get_question() #get_question이라는 function을 호출하여 question이라는 변수에 할당한다.
    mixed_questions.append(question) # 1회 순회할 동안 적립받은 get_question의 입력 데이터를 받환하여 mixed_questions라는 리스트에 보낸다

# print(mixed_questions) # 적립된 mixed_questions에 들어간 데이터들을 출력한다.
for i in range(len(mixed_questions)): # 반복문을 사용하여 mixed_question의 개수만큼 반복하여 출력하도록 한다.
    print(str(i+1) + "번 문제") # 인덱스는 0번부터 시작하므로 +1하여 몇 번째 문제인지 출력한다.
    print("질문: " + mixed_questions[i]['question']) # 인덱스의 값과 동일한 위치의 질문을 받아온 뒤 출력한다.
    for j in range(len(mixed_questions[i]['answers'])): # mixed_question의 'answers'의 개수만큼 반복하는 구문을 작성한다.
        print(str(j+1) + "번 보기: " + mixed_questions[i]['answers'][j]) # 인덱스의 값과 동일한 위치의 보기를 인덱스화 한 각 항목별로 받아온 뒤 출력한다.
    print("정답 번호: " + str(mixed_questions[i]['correct_answer']))# 인덱스의 값과 동일한 위치의 정답의 값을 받아온 뒤 출력한다.
    print("배점: " + str(mixed_questions[i]['score']))# 인덱스의 값과 동일한 위치의 배점을 받아온 뒤 출력한다.
