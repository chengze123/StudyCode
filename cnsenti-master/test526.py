from cnsenti import Sentiment

senti = Sentiment()
#test_text= '我好开心啊，非常非常非常高兴！今天我得了一百分，我很兴奋开心，愉快，开心'
test_text1='崇尚自然，尊重客户，在绿色环保、安全生产、公益慈善等方面持续作为，履行好对股东、对员工、对社会应尽的责任'
#result = senti.sentiment_count(test_text)
result = senti.sentiment_count(test_text1)
print(result)