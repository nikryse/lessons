# def count():
#     a = 0
#     shag = int(input("Введите шаг: "))
#     while a <= 10:
#         print(a)
#         a+=shag
#
# count()
def count(a=0):
    if a == 10:
        print(a )
        return
    else:
        print(a)
        return count(a + 1)
count()


