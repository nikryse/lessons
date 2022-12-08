import csv
# 111-112
# file = open ("Books.csv", "w")
# a = "To Kill a Mockingbird, Harper Lee, 1960\n"
# b = "A Brief History of Time, Stephen Hawking, 1988\n"
# c = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
# d = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
# e = "Pride and Prejudice,Jan Austen, 1813\n"
# books = input("Введите название книги: ")
# autor = input("Введите автора: ")
# year = input("Введите год издания: ")
# f = books + ", " + autor + ", " + year + "\n"
# file.write(str(a))
# file.write(str(b))
# file.write(str(c))
# file.write(str(d))
# file.write(str(e))
# file.write(str(f))
# file.close()
# 113
# file = open ("Books.csv", "w")
# t = "To Kill a Mockingbird, Harper Lee, 1960\n"
# o = "A Brief History of Time, Stephen Hawking, 1988\n"
# p = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
# h = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
# g = "Pride and Prejudice,Jan Austen, 1813\n"
# file.write(str(t))
# file.write(str(o))
# file.write(str(p))
# file.write(str(h))
# file.write(str(g))
# kol_vo = int(input("Введите кол-во записей(макс. 5): "))
# if kol_vo == 1:
#     books = input("Введите название книги: ")
#     autor = input("Введите автора: ")
#     year = input("Введите год издания: ")
#     a = books + ", " + autor + ", " + year + "\n"
#     file.write(str(a))
#     file.close()
# elif kol_vo == 2:
#     books = input("Введите название книги: ")
#     autor = input("Введите автора: ")
#     year = input("Введите год издания: ")
#     a = books + ", " + autor + ", " + year + "\n"
#     books1 = input("Введите название книги: ")
#     autor1 = input("Введите автора: ")
#     year1 = input("Введите год издания: ")
#     b = books1 + ", " + autor1 + ", " + year1 + "\n"
#     file.write(str(a))
#     file.write(str(b))
#     file.close()
# elif kol_vo == 3:
#     books = input("Введите название книги: ")
#     autor = input("Введите автора: ")
#     year = input("Введите год издания: ")
#     a = books + ", " + autor + ", " + year + "\n"
#     books1 = input("Введите название книги: ")
#     autor1 = input("Введите автора: ")
#     year1 = input("Введите год издания: ")
#     b = books1 + ", " + autor1 + ", " + year1 + "\n"
#     books2 = input("Введите название книги: ")
#     autor2 = input("Введите автора: ")
#     year2 = input("Введите год издания: ")
#     c = books2 + ", " + autor2 + ", " + year2 + "\n"
#     file.write(str(a))
#     file.write(str(b))
#     file.write(str(c))
#     file.close()
# elif kol_vo == 4:
#     books = input("Введите название книги: ")
#     autor = input("Введите автора: ")
#     year = input("Введите год издания: ")
#     a = books + ", " + autor + ", " + year + "\n"
#     books1 = input("Введите название книги: ")
#     autor1 = input("Введите автора: ")
#     year1 = input("Введите год издания: ")
#     b = books1 + ", " + autor1 + ", " + year1 + "\n"
#     books2 = input("Введите название книги: ")
#     autor2 = input("Введите автора: ")
#     year2 = input("Введите год издания: ")
#     c = books2 + ", " + autor2 + ", " + year2 + "\n"
#     books3 = input("Введите название книги: ")
#     autor3 = input("Введите автора: ")
#     year3 = input("Введите год издания: ")
#     d = books3 + ", " + autor3 + ", " + year3 + "\n"
#     file.write(str(a))
#     file.write(str(b))
#     file.write(str(c))
#     file.write(str(d))
#     file.close()
# elif kol_vo == 5:
#     books = input("Введите название книги: ")
#     autor = input("Введите автора: ")
#     year = input("Введите год издания: ")
#     a = books + ", " + autor + ", " + year + "\n"
#     books1 = input("Введите название книги: ")
#     autor1 = input("Введите автора: ")
#     year1 = input("Введите год издания: ")
#     b = books1 + ", " + autor1 + ", " + year1 + "\n"
#     books2 = input("Введите название книги: ")
#     autor2 = input("Введите автора: ")
#     year2 = input("Введите год издания: ")
#     c = books2 + ", " + autor2 + ", " + year2 + "\n"
#     books3 = input("Введите название книги: ")
#     autor3 = input("Введите автора: ")
#     year3 = input("Введите год издания: ")
#     d = books3 + ", " + autor3 + ", " + year3 + "\n"
#     books4 = input("Введите название книги: ")
#     autor4 = input("Введите автора: ")
#     year4 = input("Введите год издания: ")
#     e = books4 + ", " + autor4 + ", " + year4 + "\n"
#     file.write(str(a))
#     file.write(str(b))
#     file.write(str(c))
#     file.write(str(d))
#     file.write(str(e))
#     file.close()
# else:
#     print("Error")
# 114
# file = open ("Books.csv", "r")
# a = "To Kill a Mockingbird, Harper Lee, 1960\n"
# b = "A Brief History of Time, Stephen Hawking, 1988\n"
# c = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
# d = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
# e = "Pride and Prejudice,Jan Austen, 1813\n"
# print(a,b,c,d,e)
# search = input("Enter the data you are searching for: ")
# reader = csv.reader(file)
# for row in file:
#     if search in str(row):
#         print(row)
# 115
# file = open ("Books.csv", "r")
# reader = csv.reader(file)
# rows = list(reader)
# print(rows[2])

