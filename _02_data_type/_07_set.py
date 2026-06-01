

# set(집합)
# - 중복 허용 X
# - 시퀀스 타입 X
# - 순회(iterable) O
# - 집합 관련 메서드 제공
# - 기호 : {}

print("--- set ---")
st = {2,1,4,1,3,2,4,1,2,3,4,3}
print(st, type(st)) # 중복 제거 확인

print("--- list -> set 변경 (중복 제거) ---")
lst = [2,3,1,3,1,2,4,2]
st2 = set(lst) # set 변경
print("st2: ", st2)

# set -> list 변환
lst2 = list(st2)
print("lst2[2]: ", lst2[2])

print("--- tuple -> set 변경 (중복 제거) ---")
tpl = (2,3,1,3,1,2,4,2)
print("tpl: ", type(tpl))
st3 = set(tpl)
print("st3: ", type(st3))

# 요소 추가 (add)
print("--- 요소 추가 ---")
my_nums = {20, 30 ,40}
my_nums.add(10)
my_nums.add(10) # 중복 제거
my_nums.add(10) # 중복 제거
print("my_nums: ", my_nums) # {40, 10, 20, 30}

# 요소 제거 (remove)
print("--- 요소 제거 ---")
my_nums.remove(10)
print("my_nums: ", my_nums)

# 전체 제거 (clear)
my_nums.clear()
print("clear 후 my_nums: ", my_nums)

# set 순회
my_nums = {30, 50, 70, 90}

# my_nums에서 값을 하나 꺼내어 num 변수에 저장(반복)
for num in my_nums:
    print(num)

# 집합연산
print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합