"""
날짜 : 2021/1/06
이름 : 양대석
내용 : 파이썬 클래스 실습하기 교재 p148
"""

from Study.Lib.Account import Account

kb = Account('국민은행', '101-11-1111', '김유신', 10000)
kb.deposite(30000)
kb.withdraw(5000)
kb.show()

wr = Account('우리은행', '101-11-2222', '김춘추', 20000)
wr.deposite(50000)
wr.withdraw(5000)
wr.show()

