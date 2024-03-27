#  (https://school.programmers.co.kr/learn/courses/30/lessons/120956)

# 문제

# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 

# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(babbling):
    def generate_combinations(possibles, max_length):
        def recurse(current, remaining, results):
            if 0 < len(current) <= max_length:
                results.add(''.join(current))  # 리스트를 문자열로 조합
                results.add(''.join(current[::-1]))  # 조합의 역순 추가

            if len(current) == max_length or not remaining:
                return

            for i in range(len(remaining)):
                # 다음 문자를 추가하여 재귀 호출
                next_chars = current + [remaining[i]]
                recurse(next_chars, remaining[:i] + remaining[i+1:], results)

        results = set()
        recurse([], possibles, results)
        return list(results)

    # 사용할 문자들
    possibles = ["aya", "ye", "woo", "ma" ]
    answer = 0
    # 최대 길이 4로 모든 조합 생성
    combinations = generate_combinations(possibles, 4)
    for x in range(len(babbling)):
        if babbling[x] in combinations:
            answer = answer + 1
        else:
            pass

    return answer



def solve():
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    answer = solution(babbling)
    print(answer)
    return

solve()