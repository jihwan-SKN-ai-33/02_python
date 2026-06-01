

# sequence type(시퀀스 자료형)
# - str, list, tuple
# - 저장된 값의 순서가 유지됨
# - 인덱싱과 슬라이싱이 가능하다
# - 순회(iterable) 가능


# list
# - 여러 값(literal)을 묶어서 관리 (컨테이너 자료형)
# - 특징 : 동적으로 list 크기가 변할 수 있다 (수정 가능)

print("--- list ---")
lst = [1, 2, 3, 4, 5]
print("lst: ", lst)
print("len(lst): ", len(lst))
print("lst[0]: ", lst[0])
print("lst[1]: ", lst[1])
print("lst[4]: ", lst[4])

# list 저장 요소 추가/수정/삭제

# - list는 동적으로 크기 변경이 가능한 mutable 자료형이디ㅏ
# - mutable : list, set, dict
# - immutable : int, float, bool, str, tuple
print("--- list mutable check ---")
print("lst: ", lst)
print("추가 전 id: ", id(lst))

before_id = id(lst)

# list.append(값) : list 끝에 값 추가
lst.append(999)
print('append 후 lst ', lst)
print('append 후 lst ', id(lst))
print('append 전후 같은 list 인가? ', before_id == id(lst))

# list.insert(index, 값)
# - index에 값을 삽입하는 메서드
# - 지정된 index부터 뒤에있는
#   모든 list 값의 index가 1씩 증가(밀려남)
print("--- list.insert() ---")
lst.insert(1,1.5)
lst.insert(0,0)
print("insert 후 lst: ", lst)
print("insert 후 lst id: ", id(lst))
print("insert 후 id 비교: ", before_id == id(lst))

# list update(수정)
# list[인덱스] = 값     (변수에 값 대입해서 변경)
print('--- list update ---')
lst[0] = -10
print("lst: ", lst)

# 특정 인덱스 값 제거
# list.pop(index) : 해당 인덱스 값이 제거
# 제거된 index 뒤 요소들을 한 칸씩 당김
print('--- list remove ---')
lst.pop(2)
print("lst: ", lst)
print('id(lst): ', id(lst))

# 2차원 list
students = [
    ['홍길동', 30],
    ['이순신', 80],
    ['세종대왕', 100]
]

print("students: ", students)
print(students[0][0])
print(students[1][1])
print(students[2]) # 3(행)
print(len(students)) # 2(행)
print(len(students[0])) # 2(열)
print(len(students[0][0])) # 3(홍길동 글자 수)

# str.split(구분자)
# - str을 구분자를 기준으로 list 형태로 변환
# - csv(Comma Separated Value)
data = "홍길동,20,서울시,서초구"
data_ = data.split(',')
print("data_: ", data_, type(data_))

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print(name, age, addr1, addr2)

# list 슬라이싱 (str 슬라이싱 방법 동일)
print("--- list 슬라이싱 ---")
texts = ['hello', '안녕', '곤니찌와', 'hi']

# ['hello', '안녕']
print("list 슬라이싱: ", texts[:2])

# ['안녕', '곤니찌와']
print("list 슬라이싱: ", texts[1:3])

# ['hello', '곤니찌와']
print("list 슬라이싱: ", texts[0::2])

# ['곤니찌와', 'hi']
print("list 슬라이싱: ", texts[2:])

# slicing을 이용한 list 값 변경
print(texts)
print(texts[:2])
texts[:2] = ["aaa", "bbb"]
print(texts)
texts[1:3] = ["😁😁😁😁", "😊😊😊"]
print(texts)

# list 끼리 더하기(+) 연산
print("--- list 더하기 연산 ---")
a = [10, 20]
b = [30, 40]
a = a + b
print(a) # [10, 20, 30 ,40]

b = b + a
print(b) # [30, 40, 10 , 20, 30, 40]

# list 순회(순차 접근, 순차 반복)
# - iterable 특징을 가지는 자료형만 가능
print("--- list 순회 ---")
lst = ['a', 'b', 'c']

# list 요소 순회
for v in lst:
    print(v)

# list 인덱스, 요소 순회
# enumerate 나열하다
for index, v in enumerate(lst):
    print(f'lst[{index}]: {v}')

