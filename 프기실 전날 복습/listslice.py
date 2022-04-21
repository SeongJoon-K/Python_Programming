import time

# year = int(input("오늘의 연도를 입력하시오:"))
# month = int(input("오늘의 월을 입력하시오:"))
# day = int(input("오늘의 일자를 입력하시오:"))

# print("오늘은", year, "년", month, "월", day, "일 입니다")


now = time.time()
thisYear = int(1970+now//(365*24*3600))  # 현재 년도 입력
print("올해는", thisYear, "입니다")

age = int(input("몇 살이신지요?"))
print("2050년에는", (age+2050-thisYear), "살 이시군요")
