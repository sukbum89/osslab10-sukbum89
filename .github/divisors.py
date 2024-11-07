import sys

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    # 입력으로 받은 숫자를 정수로 변환
    number = int(sys.argv[1])
    # 약수를 찾고, 공백으로 구분하여 출력
    print(" ".join(map(str, find_divisors(number))))
