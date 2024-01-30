from typing import Optional
class kwargs:
    def __init__(self,
        email: str = None,
        pswd: str = None,
        manager: str = None,
        name: str = None,
        sellist1 : str = None,
        text : str = None) -> None: # 생성자 초기화
        self.name = name
        self.pswd = pswd
        self.email = email
        pass
if __name__ == "__main__":
    user = {
        "name": "김철수",
        "email": "chulsoo.kim@example.com",
        "pswd": "Password123!"        
    }
    # kwargs(**user)  ##  ** = function에서 사용하는 연산자 : 자료를 통째로 넘겨주는 역할
    kwargs(user)
    pass