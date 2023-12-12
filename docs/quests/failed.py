dict_questions = {"question" : ""}
dict_answer = {[]}
dict_correct_index = {"answer" : ""}
dict_score = {"score" : ""}


def __init__(self,dict_questions,dict_answer,dict_correct_index,dict_score):
    self.dict_questions = dict_questions
    self.dict_answer = dict_answer
    self.dict_correct_index = dict_correct_index 
    self.dict_score = dict_score

def input_question(self):
    for i in range(len(dict_questions)) :
        if dict_answer[i] == dict_score[i]:
            questions = str(input("출제하실 문제를 입력해 주세요 : "))
            self.dict_question.append(dict_questions[i],True)
    return self.dict_question

def input_answer(self):
    for i in range(len(dict_answer)):
        for i in range(len(list_answer)):
        list_answer = str(input("문제에 해당하는 보기를 입력해 주세요 : "))
        

def input_score(self):
    for i in range(len(dict_score)):
        score = int(input("배점하실 점수를 입력해 주세요. : "))
        self.list_score.append(score)
        
        
list_correct_index
        




get_num = int(input("정답 : "))
print("{}".format(list_option[i]))