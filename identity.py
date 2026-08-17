str1 ="hello"
str2="welcome"
print(id(str1))
print(id(str2))

str5="kg"
str6="kg"

print(id(str5))
print(id(str6))

print(id(str5) is not id(str6))
print(str5 is str6)

word ="Python is high level programming language"
print("Python" in word)

print("hi welcome",sep="-")
print("python class")



date=13
month=8
year=2026
print(date,month,year,sep="-")