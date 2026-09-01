def add(a,b):
    return a+b

def safe_add(a,b):
    if type(a) != type(b):
        print('자료형이 다를 경우 연산 할 수 없습니다')
    else:
        result = add(a,b)
        return result
