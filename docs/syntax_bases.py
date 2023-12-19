# 코드 기본 형식
import Classes_format
from Classes_format import Person, Arithmetics, Class_name


# Class의 기본 구조(Ref)
class Class_name:
    def __init__(self): # 자체적으로 내재되어 있는 function(Class 생성자)
        pass            # (기술하지 않아도 원래 내포하고 있으며 자동으로 반영된다.)
                        # 초기 상태를 설정하는 등의 작업이 필요하므로 직접 작성하여 사용한다.
                        # return을 기재하지는 않지만, 모든 자원을 return한다.(다른 Function들)
    def function_name(self): #self = 이 function이 class에 종속되어 있음을 선언하는 키워드
        try :
            pass   # 업무 코드
        except:
            pass   # 업무 코드가 문제 발생 시 대처 코드
        finally:
            pass   # try나 except가 끝난 후 무조건 실행 코드
        return 0
    
# 기본 function 형식 - stand-bying. 호출되었을 때만 기능.
def function_name(): 
    try :
        pass   # 업무 코드
    except:
        pass   # 업무 코드가 문제 발생 시 대처 코드
    finally:
        pass   # 기능할 내용 입력하는 자리
    return 0

if __name__ == "__main__":
    try :
        pass   # 업무 코드
    except:
        pass   # 업무 코드가 문제 발생 시 대처 코드
    finally:
        pass   # try나 except가 끝난 후 무조건 실행 코드

