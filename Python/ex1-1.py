def add(c, d, a = 20, b = 10):
    # 기본 값은 뒤에서부터 넣어주어야 한다. 앞에서부터 넣으면 에러가 발생함.
    if(a > 1):
        return a + b + c + d        # return문은 함수를 호출한 측으로 값을 전달할 뿐만 아니라, 그 함수를 그냥
                                    # 종료시켜버림.
    else:   # a > 1가 아닌 경우가 모두 else에 들어옴.
        return a + b - c - d
    
    # if ~ else문을 이용해서 return문을 다르게 구성할 수는 있지만, 두 개를 동시에 실행하는 것은 불가능.

result = add(2, 4)

print(result)



