from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.krafton



# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.test.drop()  # mystar 콜렉션을 모두 지워줍니다.
    doc = {
        "name": "강영훈",
        "phnum": "01033592000",
        "room": "211",
        "team": "red",
        "email": "dudgns113@gmail.com",
        "pw": "1",
        "blog": "https://blog.naver.com/dudgns113",
        "time": "0"
    }
    doc2 = {
        "name": "강의진",
        "phnum": "01044106456",
        "room": "212",
        "team": "red",
        "email": "rkddmlwls2@gmail.com",
        "pw": "1",
        "blog": "https://blog.naver.com/rkddmlwls2",
        "time": "0"
    }
    doc3 = {
    "name": "김상윤",
    "phnum": "01085000230",
    "room": "213",
    "team": "red",
    "email": "w2300n@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/w2300n",
    "time": "0"
}
    doc4 = {
    "name": "김상주",
    "phnum": "01045361701",
    "room": "214",
    "team": "red",
    "email": "rlatkdwn3379@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/w2300n",
    "time": "0"
}
    doc4 = {
    "name": "김서영",
    "phnum": "01051278522",
    "room": "215",
    "team": "red",
    "email": "asdf13531@yonsei.ac.kr",
    "pw": "1",
    "blog": "https://blog.naver.com/asdf13531",
    "time": "0"
}
    doc5 = {
    "name": "김영우",
    "phnum": "01085727792",
    "room": "216",
    "team": "red",
    "email": "uddn@naver.com",
    "pw": "1",
    "blog": "https://blog.naver.com/uddn",
    "time": "0"
}
    doc6 = {
    "name": "김주현",
    "phnum": "01088329747",
    "room": "217",
    "team": "red",
    "email": "dydgla36@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/dydgla36",
    "time": "0"
}
    doc7 = {
    "name": "김희령",
    "phnum": "01088762951",
    "room": "218",
    "team": "red",
    "email": "keronruss@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/keronruss",
    "time": "0"
}
    doc8 = {
    "name": "문승현",
    "phnum": "01038785240",
    "room": "219",
    "team": "red",
    "email": "victorymsh@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/victorymsh",
    "time": "0"
}
    doc9 = {
    "name": "박도형",
    "phnum": "01074882623",
    "room": "220",
    "team": "red",
    "email": "slstls218@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/slstls218",
    "time": "0"
}
    doc10 = {
    "name": "박성환",
    "phnum": "01041109471",
    "room": "221",
    "team": "red",
    "email": "psung9510@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/psung9510",
    "time": "0"
}
    doc11 = {
    "name": "황현성",
    "phnum": "01040878050",
    "room": "381",
    "team": "blue",
    "email": "hyunsung109@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/hyunsung109",
    "time": "0"
}
    doc12 = {
    "name": "홍윤표",
    "phnum": "01064876278",
    "room": "371",
    "team": "blue",
    "email": "yoon84268426@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/yoon84268426",
    "time": "0"
}
    doc13 = {
    "name": "최원",
    "phnum": "01090493970",
    "room": "361",
    "team": "blue",
    "email": "chldnjs8899@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/chldnjs8899",
    "time": "0"
}
    doc14 = {
    "name": "최도의",
    "phnum": "01026293871",
    "room": "351",
    "team": "blue",
    "email": "macker1005@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/macker1005",
    "time": "0"
}
    doc15 = {
    "name": "최광민",
    "phnum": "01052117616",
    "room": "341",
    "team": "blue",
    "email": "ckm7907cb@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/ckm7907cb",
    "time": "0"
}
    doc16 = {
    "name": "장혁",
    "phnum": "01071182438",
    "room": "331",
    "team": "blue",
    "email": "programmingonly17@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/programmingonly17",
    "time": "0"
}
    doc17 = {
    "name": "이지현",
    "phnum": "01039420184",
    "room": "321",
    "team": "blue",
    "email": "doragimoochim@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/doragimoochim",
    "time": "0"
}
    doc18 = {
    "name": "이성헌",
    "phnum": "01077942286",
    "room": "311",
    "team": "blue",
    "email": "aoao1023@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/aoao1023",
    "time": "0"
}
    doc19 = {
    "name": "윤지우",
    "phnum": "01073163811",
    "room": "301",
    "team": "blue",
    "email": "lacvert13@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/lacvert13",
    "time": "0"
}
    doc20 = {
    "name": "유대겸",
    "phnum": "01024919341",
    "room": "313",
    "team": "blue",
    "email": "hyunbin9341@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/hyunbin9341",
    "time": "0"
}
    doc21 = {
    "name": "강원영",
    "phnum": "01099227624",
    "room": "401",
    "team": "green",
    "email": "onezerokang@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/onezerokang",
    "time": "0"
}
    doc22 = {
    "name": "김범기",
    "phnum": "01039807629",
    "room": "411",
    "team": "green",
    "email": "bknote71@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/bknote71",
    "time": "0"
}
    doc23 = {
    "name": "김인제",
    "phnum": "01053111550",
    "room": "421",
    "team": "green",
    "email": "kij2646@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/kij2646",
    "time": "0"
}
    doc24 = {
    "name": "김재성",
    "phnum": "01089333444",
    "room": "431",
    "team": "green",
    "email": "tocomon09@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/tocomon09",
    "time": "100"
}
    doc25 = {
    "name": "김태영",
    "phnum": "01063611542",
    "room": "441",
    "team": "green",
    "email": "markdj9205@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/markdj9205",
    "time": "1000"
}
    doc26 = {
    "name": "김현수",
    "phnum": "01068000312",
    "room": "451",
    "team": "green",
    "email": "hsk7953@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/hsk7953",
    "time": "10"
}
    doc27 = {
    "name": "노원주",
    "phnum": "01063580535",
    "room": "461",
    "team": "green",
    "email": "wonju@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/wonju",
    "time": "20"
}
    doc28 = {
    "name": "박주영",
    "phnum": "01030168134",
    "room": "471",
    "team": "green",
    "email": "optimisticnihilism2007@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/optimisticnihilism2007",
    "time": "30"
}
    doc29 = {
    "name": "박준익",
    "phnum": "01086427643",
    "room": "481",
    "team": "green",
    "email": "cod2048@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/cod2048",
    "time": "40"
}
    doc30 = {
    "name": "이민지",
    "phnum": "01077636970",
    "room": "491",
    "team": "green",
    "email": "minji0479@gmail.com",
    "pw": "1",
    "blog": "https://blog.naver.com/minji0479",
    "time": "50"
}


    db.test.insert_one(doc)
    db.test.insert_one(doc2)
    db.test.insert_one(doc3)
    db.test.insert_one(doc4)
    db.test.insert_one(doc5)
    db.test.insert_one(doc6)
    db.test.insert_one(doc7)
    db.test.insert_one(doc8)
    db.test.insert_one(doc9)
    db.test.insert_one(doc10)
    db.test.insert_one(doc11)
    db.test.insert_one(doc12)
    db.test.insert_one(doc13)
    db.test.insert_one(doc14)
    db.test.insert_one(doc15)
    db.test.insert_one(doc16)
    db.test.insert_one(doc17)
    db.test.insert_one(doc18)
    db.test.insert_one(doc19)
    db.test.insert_one(doc20)
    db.test.insert_one(doc21)
    db.test.insert_one(doc22)
    db.test.insert_one(doc23)
    db.test.insert_one(doc24)
    db.test.insert_one(doc25)
    db.test.insert_one(doc26)
    db.test.insert_one(doc27)
    db.test.insert_one(doc28)
    db.test.insert_one(doc29)
    db.test.insert_one(doc30)

insert_all()

# db.test.drop()

