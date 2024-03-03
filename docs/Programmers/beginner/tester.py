def min_use(X, X_values):
    X_values.sort(reverse=True)  # X1, X2, X3를 큰 순서대로 정렬
    n_values = [0, 0, 0]  # n1, n2, n3의 초기값
    for i in range(3):
        while X >= X_values[i]:  # X가 각 X_value보다 크거나 같을 동안
            X -= X_values[i]  # X에서 X_value를 빼고
            n_values[i] += 1  # 해당 n_value를 1 증가
    return n_values if X == 0 else None  # X를 정확히 만들 수 없다면 None 반환

X = 100  # 예시
X_values = [25, 10, 1]  # X1, X2, X3의 값
print(min_use(X, X_values))  # n1, n2, n3의 값을 출력
