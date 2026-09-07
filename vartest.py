# vartest.py
a = 1
def vartest(a):
    a = a +1   # 지역변수 범위 --> 함수 내에서 존재, 함수 호출- 실행- 끝 -> 메모리에서 사라진다

vartest(a)
print(a)

