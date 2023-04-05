from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.krafton



# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.test.drop()  # mystar 콜렉션을 모두 지워줍니다.
    doc = {
        "date": "2022.05.01",
        "inOut": "in",
        "type": "profit",
        "item": "용돈",
        "price": 300000
    }
    db.test.insert_one(doc)


### 실행하기
# insert_all()
db.test.drop()
