# tester.py
import sys
sys.path.append('/c/Users/csclk/osslab10-sukbum89')  # geo 패키지 경로 추가

print("tester.py is running")  # 디버깅용 출력문

# geo 패키지에서 add와 subtract 함수 임포트
from geo.utils import add, subtract

# add 함수 테스트
result_add = add(5, 3)
print(f"5 + 3 = {result_add}")  # 예상 출력: 8

# subtract 함수 테스트
result_subtract = subtract(5, 3)
print(f"5 - 3 = {result_subtract}")  # 예상 출력: 2