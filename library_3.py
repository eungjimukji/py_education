#1, 2, 3이라는 숫자가 적힌 3장의 카드에서 2장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하려면?
import itertools
#반복 가능 객체 중 r개를 선택한 순열을 이터레이터로 리턴
a= list(itertools.permutations(['1','2','3,'],2))
print(a)


from operator import itemgetter
students = [
    ("jane",22, "A"),
    ("dave",39, "B"),
    ("alice",17, "C"), ]

result = sorted(students, key=itemgetter(1))
print(result)

