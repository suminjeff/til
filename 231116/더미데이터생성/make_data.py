# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     nickname = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     money = models.IntegerField(blank=True, null=True)
#     salary = models.IntegerField(blank=True, null=True)
#     # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
#     financial_products = models.TextField(blank=True, null=True)
    
#     # superuser fields
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)


import random
import requests

first_name_samples = "김이박최정강조윤장임한오서신권황안송전홍유고문양손배조백허유남심노정하곽성차주우"
middle_name_samples = "민서예지도하주윤채현지수우윤재승영유준운건일찬해상도금대진"
last_name_samples = "준윤우원호후서연아은진민원주정언빈경용규휘수은영호의란범광훈현"

city_samples = [
  "서울특별시",
  "인천광역시",
  "대전광역시",
  "광주광역시",
  "대구광역시",
  "울산광역시",
  "부산광역시",
  "경기도",
  "강원도",
  "충청북도",
  "충청남도",
  "전라북도",
  "전라남도",
  "경상북도",
  "경상남도",
  "제주도"
]

gu_samples = {
    "서울특별시": ["강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구","노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성동구","성북구","송파구","양천구","영등포구","용산구","은평구","종로구","중구","중랑구"],
    "인천광역시": ["계양구","남구","남동구","동구","부평구","서구","연수구","중구","강화군","옹진군"],
    "대전광역시": ["대덕구","동구","서구","유성구","중구"],
    "광주광역시": ["광산구","남구","동구", "북구","서구"],
    "대구광역시": ["남구","달서구","동구","북구","서구","수성구","중구","달성군"],
    "울산광역시": ["남구","동구","북구","중구","울주군"],
    "부산광역시": ["강서구","금정구","남구","동구","동래구","부산진구","북구","사상구","사하구","서구","수영구","연제구","영도구","중구","해운대구","기장군"],
    "경기도": ["고양시","과천시","광명시","광주시","구리시","군포시","김포시","남양주시","동두천시","부천시","성남시","수원시","시흥시","안산시","안성시","안양시","양주시","오산시","용인시","의왕시","의정부시","이천시","파주시","평택시","포천시","하남시","화성시","가평군","양평군","여주군","연천군"],
    "강원도": ["강릉시","동해시","삼척시","속초시","원주시","춘천시","태백시","고성군","양구군","양양군","영월군","인제군","정선군","철원군","평창군","홍천군","화천군","횡성군"],
    "충청북도": ["제천시","청주시","충주시","괴산군","단양군","보은군","영동군","옥천군","음성군","증평군","진천군","청원군"],
    "충청남도": ["계룡시","공주시","논산시","보령시","서산시","아산시","천안시","금산군","당진군","부여군","서천군","연기군","예산군","청양군","태안군","홍성군"],
    "전라북도": ["군산시","김제시","남원시","익산시","전주시","정읍시","고창군","무주군","부안군","순창군","완주군","임실군","장수군","진안군"],
    "전라남도": ["광양시","나주시","목포시","순천시","여수시","강진군","고흥군","곡성군","구례군","담양군","무안군","보성군","신안군","영광군","영암군","완도군","장성군","장흥군","진도군","함평군","해남군","화순군"],
    "경상북도": ["경산시","경주시","구미시","김천시","문경시","상주시","안동시","영주시","영천시","포항시","고령군","군위군","봉화군","성주군","영덕군","영양군","예천군","울릉군","울진군","의성군","청도군","청송군","칠곡군"],
    "경상남도": ["거제시","김해시","마산시","밀양시","사천시","양산시","진주시","진해시","창원시","통영시","거창군","고성군","남해군","산청군","의령군","창녕군","하동군","함안군","함양군","합천군"],
    "제주도": ["서귀포시","제주시","남제주군","북제주군"],
}

random_ascii_username = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
def random_username():
    length = random.randint(8, 15)
    result = ""
    for _ in range(length):
        result += str(chr(random_ascii_username[random.randint(0, 61)]))
    return result


def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result


def random_address():
    result = ""
    city = random.choice(city_samples)
    gu = random.choice(gu_samples[city])
    result += city + " " + gu
    return result


# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '87e58aba3d85bf50fb8d9f671679c025'

# financial_products = []
deposit_products = []
saving_products = []

params = {
  'auth': API_KEY,
  # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
  'topFinGrpNo': '020000',
  'pageNo': 1
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])
for product in baseList:
    deposit_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])
for product in baseList:
    saving_products.append(product['fin_prdt_cd'])

# dict_keys = ['username', 'gender', 'financial_products', 'age', 'money', 'salary']
dict_keys = ['username', 'gender', 'deposit_products', 'saving_products', 'age', 'balance', 'salary']

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []
name_list = []
nickname_list = []
address_list = []
N = 10000
i = 0

while i < N:
    ru = random_username()
    rn = random_name()
    ra = random_address()
    if rn in name_list or ru in username_list:
        continue
    username_list.append(ru)
    name_list.append(rn)
    nickname_list.append(rn+str(random.randint(1, 100)))
    address_list.append(ra)
    i += 1


  

    
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = './user_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file["model"] = "accounts.User"
        file["pk"] = i+1
        file["fields"] = {
            'username': username_list[i],  # 유저 ID 생성
            'first_name': name_list[i][1:],
            'last_name': name_list[i][0],
            'nickname': nickname_list[i],
            'email': username_list[i] + "@" + "dummymail.com",
            'address': address_list[i],
            'gender': bool(random.randint(0, 1)),
            # 랜덤한 0~5개의 상품을 가입하도록 삽입됨
            # 'deposit_products': ','.join([random.choice(deposit_products) for _ in range(random.randint(0, 5))]), # 금융 상품 리스트
            # 'saving_products': ','.join([random.choice(saving_products) for _ in range(random.randint(0, 5))]), # 금융 상품 리스트
            # 'age': random.randint(1, 100),  # 나이
            'balance': random.randrange(0, 1500000000,1000000),    # 현재 가진 금액
            'salary': random.randrange(0, 100000000, 100000), # 연봉
            'password': "1234",
            'birth_date': str(random.randint(1930, 2005))+'-'+str(random.randint(1, 12)).zfill(2)+'-'+str(random.randint(1, 28)).zfill(2),
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()
print(f'데이터 생성 완료 / 저장 위치: {save_dir}')



# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
board_types = ['free', 'notice', 'qna']
save_dir = './article_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(1000):
        # 랜덤한 데이터를 삽입
        file["model"] = "articles.Article"
        file["pk"] = i+1
        file["fields"] = {
            'user' : random.randint(1, 10000),
            'title': f'title{i}',
            'content': f'content{i}',
            'board_type': board_types[random.randint(0, 2)],
            'created_at' : '2023-11-'+str(random.randint(1, 15)).zfill(2)+' '+str(random.randint(0, 23)).zfill(2)+':'+str(random.randint(0, 59)).zfill(2)+'.000000-08:00',
            'updated_at' : '2023-11-'+str(random.randint(16, 30)).zfill(2)+' '+str(random.randint(0, 23)).zfill(2)+':'+str(random.randint(0, 59)).zfill(2)+'.000000-08:00'
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != 1000-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')

# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = './comment_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(3000):
        # 랜덤한 데이터를 삽입
        file["model"] = "articles.Comment"
        file["pk"] = i+1
        file["fields"] = {
            'user' : random.randint(1, 10000),
            'article': random.randint(1, 1000),
            'content': f'content{i}',
            'created_at' : '2023-11-'+str(random.randint(16, 20)).zfill(2)+' '+str(random.randint(0, 23)).zfill(2)+':'+str(random.randint(0, 59)).zfill(2)+'.000000-08:00',
            # 'updated_at' : '2023-11-'+str(random.randint(21, 30)).zfill(2)+' '+str(random.randint(0, 23)).zfill(2)+':'+str(random.randint(0, 59)).zfill(2)+'.000000-08:00'
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != 3000-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')