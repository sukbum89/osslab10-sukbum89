# tester.py

# geo 패키지에서 add와 subtract 함수 임포트
from geo.utils import add, subtract

# add 함수 테스트
result_add = add(5, 3)
print(f"5 + 3 = {result_add}")  # 예상 출력: 8

# subtract 함수 테스트
result_subtract = subtract(5, 3)
print(f"5 - 3 = {result_subtract}")  # 예상 출력: 2
