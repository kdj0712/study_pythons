# 문제

# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력

# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력

# 입력으로 주어진 숫자 N개의 합을 출력한다.
news = 0
x = int(input())
int_sum = input()
for j in range(x):
    sums = int(int_sum[j])
    news = news + sums
print(news)