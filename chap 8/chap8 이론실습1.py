import random

quotes = []
quotes.append("고생끝에 낙이 온다")
quotes.append("엎친데 덮친 격")
quotes.append("나약한 태도는 성격도 나약하게 만든다.")
quotes.append("성공은 종종 실패가 불가피하다는 것을 모르는 사람들에 의해 달성된다")

dailyQuotes = random.choice(quotes)
print("# 오늘의 속담 #")
print(dailyQuotes)
