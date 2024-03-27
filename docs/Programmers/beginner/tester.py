# def min_use(X, X_values):
#     X_values.sort(reverse=True)  # X1, X2, X3를 큰 순서대로 정렬
#     n_values = [0, 0, 0]  # n1, n2, n3의 초기값
#     for i in range(3):
#         while X >= X_values[i]:  # X가 각 X_value보다 크거나 같을 동안
#             X -= X_values[i]  # X에서 X_value를 빼고
#             n_values[i] += 1  # 해당 n_value를 1 증가
#     return n_values if X == 0 else None  # X를 정확히 만들 수 없다면 None 반환

# X = 100  # 예시
# X_values = [25, 10, 1]  # X1, X2, X3의 값
# print(min_use(X, X_values))  # n1, n2, n3의 값을 출력


# def generate_combinations(chars, path="", combinations=None):
#     if combinations is None:
#         combinations = []

#     # 모든 문자를 사용한 경우, 결과 리스트에 추가
#     if not chars:
#         combinations.append(path)
#     else:
#         # 가능한 모든 문자에 대해 반복
#         for i in range(len(chars)):
#             # 다음 단계의 문자 리스트 생성 (현재 문자 제외)
#             next_chars = chars[:i] + chars[i+1:]
#             # 현재 문자를 경로에 추가하고, 재귀 호출
#             generate_combinations(next_chars, path + chars[i], combinations)

#     return combinations

# # 사용할 문자들
# chars = ['A', 'B', 'C']

# # 모든 조합 생성
# combinations = generate_combinations(chars)
# print(combinations)

# def generate_combinations(chars):
#     # 결과를 저장할 리스트 초기화
#     combinations = []

#     # 각 문자를 단독으로 리스트에 추가
#     for char in chars:
#         combinations.append(char)

#     # 두 문자 조합 생성 및 역순으로도 추가
#     for i in range(len(chars)):
#         for j in range(len(chars)):
#             if i != j:  # 같은 문자를 조합하지 않도록 함
#                 combination = chars[i] + chars[j]
#                 reverse_combination = chars[j] + chars[i]  # 역순 조합
#                 combinations.append(combination)
#                 combinations.append(reverse_combination)

#     # 중복 제거
#     combinations = list(set(combinations))

#     return combinations

# # 사용할 문자들
# chars = ['A', 'B', 'C']

# # 모든 조합 생성
# combinations = generate_combinations(chars)
# print(combinations)

def generate_combinations(chars, max_length):
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
    recurse([], chars, results)  # 초기 current를 빈 리스트로 시작
    return list(results)

# 사용할 문자들을 리스트로
chars = ['A', 'B', 'C', 'D']

# 최대 길이 4로 모든 조합 생성
combinations = generate_combinations(chars, 4)
print(combinations)
