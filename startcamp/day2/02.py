# Dictionary (딕셔너리)
# 순서가 없는 데이터 타입 (리스트와의 가장 큰 차이)

my_home = {
    'location': 'seoul',
    'area-code': '02'
}

# 딕셔너리 원소 접근
#1
print(my_home['location'])
#print(my_home['name'])
#2
print(my_home.get('location'))
print(my_home.get('name')) # None