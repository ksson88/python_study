# 문자열 포매팅 따라하기
# 1. 숫자 바로 대입
print("I eat %d apples." % 3)

# 2. 문자열 바로 대입
print("I eat %s apples." % "five")

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." %number)


# 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# 5. 문자열 포맷 코드
"""
%s 문자열,
%c 문자,
%d 정수,
%f 부동소수,
%o 8진수,
%x 16진수,
%% Literal 문자 %
"""

# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백
print("%10s" % "hi")
#        hi
print("%-10sJane." % 'hi')

#hi        Jane.

# 2. 소수점 표현하기
print("%10.4f" % 3.14159265358979323846)

# format 함수를 이용한 포캐팅
print("I eat {0} apples".format(3))

# 문자열 바로 대입하기
print("I eat {0} apples".format("five"))

# 숫자 가진 변수 대입
number = 10
print("I eat {0} apples".format(number))

# 2개 이상 값 넣기
number = 100
day = "three"
print("i ate {0} apples. so I was sick for {1} days".format(number, day))


# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

# 인덱스와 이름 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days".format(10, day=10))

# 왼쪽 정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))

# 소수점 표현하기
y = 3.1415926535897
print("{0:0.4f}".format(y))

print("{0:10.4f}".format(y))

# { 와 } 문자표현
print("{{ and }}".format())

# 문자열 관련 함수
a = "hobby"
print("a.count('b') : ", a.count('b'))

# 위치 알려주기 find
a = "Python is the best choice"
print("a.find('b')", a.find('b'))
print(a.find('k'))

# 위치 알려주기 index
a = "Life is too short"
print("a.index('t') : ", a.index('t'))
# print("a.index('k') : ", a.index('k'))
# index는 없으면 오류를 발생시킨다.

# 문자열 삽입 join
print('''",".join('abcd') : ''', ",".join('abcd'))

# 대문자로 바꾸기
a = "hi"
print("a.upper()", a.upper())

# 소문자로 바꾸기
a = "HI"
print("a.lower()", a.lower())

# 왼쪽 공백 지우기 lstrip
a = "         hi  "
print("a.lstrip() :\n", a.lstrip())

# 오른쪽 공백 지우기 rstrip
a = "       hi        "
print("a.rstrip() :\n", a.rstrip())


# 양쪽 공백 지우기 strip
a = "       hi       "
print("a.strip() :", "\n", a.strip())

# 문자열 바꾸기 replace
a = "Life is too short"
print("a : ", a)
print('''a.replace("Life", "Your leg") : ''', a.replace("Life", "Your leg"))


# 문자열 나누기 split
print("a.split() : ", a.split())

b = "a:b:c:d"
print("b : ", b)
print("b.split(':')", b.split(':'))
