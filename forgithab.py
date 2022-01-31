# def add(a,b):
#     print(a+b)
# add(5,5)
# def substrakt(c,d):
#     return(c-d)
# print(substrakt(8,4))
# def multiplay(e,f):
#     return(e*f)
# print(multiplay(5,5))
# def divide(s,r):
#     return(s/r)
# print(divide(4,2))



# kir=input('ваш возраст')
# q='18'
# w='17'
# e='16'
# r='15'
# if kir==q:
#     print('you can vote') 
# elif kir==w:
#     print('you can  learn to drive') 
# elif kir==e:
#     print('you can  bay a lottery ticket')
# elif kir==r:
#     print('you can go Trickor')
# else:
#     print('') 



# q=input('кайсы ай')
# if q=='март'or q=='апрель'or q=='май':
#     print('весна')
# elif q=='июнь'or q=='июль'or q=='август':
#     print('лето')    
# elif q=='сентябрь'or q=='октябрь'or q=='ноябрь':  
#     print('осень')  
# elif q=='декабрь'or q=='январь'or q=='февраль':  
#     print('зима') 



# name=input('name').lower()
# surname=input('surname').lower()
# fullname=(name+'  '+surname).title()
# print(fullname)




# money=100
# for x in range(money):
#     for y in range(money):
#         for z in range(money):               
#             if 10*x+5*y+0.5*z==money and x+y+z==money:
#                 print('bull {}, cow {}, calf {}' .format( x , y , z))




# menu={'manty':200,'plov':150,'lagman':130,'borsh':100}
# menu.update({'besh barmak':130})
# menu['lagman']=135
# menu.pop('borsh')
# print(menu)




# t=turtle.Turtle()
# s=turtle.Screen()
# s.bgcolor('black')
# t.speed(0)
# n=36
# h=0
# for i in range(360):
#     c=colorsys.hsv_to_rgb(h,1,0.8)
#     h+=1/n
#     t.color(c)
#     t.circle(180)
#     t.left(10)


# import random
# b=random.randint(0,20)
# for i in range(6):
#     q=int(input("Угадай число"))
#     if q>b:
#         print('число больше заданного числа')
#     elif q<b:    
#         print('число меньше заданнаго числа')
#     else:
#         print(q,'вы угадали')
#         break   





# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# total=0
# for i in lst:
#     if i<30 and i%3==0:
#         print(i)
#     else:
#         total+=1
# print(total)



# import random

# igra=['камень','ножницы','бумага']
# while True:

#     player1=random.choice(igra)

#     player2=input('камень, ножница ,бумага?')

#     if player2=="бумага" and player1=='камень':
#         print('ты победил')    

#     elif player2=="ножницы" and player1=='бумага':
#         print('ты победил')    

#     elif player2=="камень" and player1=='ножницы':
#         print('ты победил?')    

#     elif player1==player2:
#         print('у вас ничья')

    
#     elif player1=="бумага" and player2=='камень':
#         print('ты проиграл')    

#     elif player1=="ножницы" and player1=='бумага':
#         print('ты проиграл')    

#     elif player1=="камень" and player1=='ножницы':
#         print('ты проиграл')   


#     prodoljenie=input('хочешь продольжить' )
#     if prodoljenie=='у':
#         continue
#     else:
#         break



# q=('мы слишком долго ждали')
# vowels=0
# consonants=0
# total=len(q.split(' '))
# for i in q:
#     letter=i.lower()
#     if letter=='а' or letter=='ы'or\
#        letter=='и' or letter=='о':
#         vowels += 1   
#     else:
#         consonants +=1
# print("Vowels %i\nConsonants %i" % (vowels,consonants))
# print(f'в предложении{total} слов')




   # from translate import Translator

# from_lang=Translator(from_lang='english',to_lang='Russian')

# input_translste=input("напишите на английском:")

# translation=from_lang.translate(input_translste)

# print("перевод",translation)
# 
# 




# def mylen(project):
#     result=0
#     for _ in project:
#         result+=1
#     return result  
# print(mylen('asdfghjkwertyuio'))



# my_file=open('test.txt','r')
# # print(my_file.read())
# # for i in my_file.readline():  
# rd=my_file.readline()
# for i in rd:
#     print(i)



# q=('japan','russaia','kazak','china','Kyrguzstan')
# print(q)
# w=input('ввести название')
# print(w, 'индекс эьой страны',q.index(w))




# while True:
#     s=input('can you play football')
#     if s =='no':
#         print('i dont')    
#         break



# import random
# f=["Aibek",
# "Joomart", "Adinai", "Ermek", "Atai",
# "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek",
# "Alymbek", "Dastan",
# "Maksat"]
# w=[]
# for i in range(4):
#     w.append(random.choice(f))
# print(w)




# re=int(input('ввести чило'))
# x=1
# while x<=10:
#     print(str(re)+'*'+str(x)+'='+str(re*x))
#     x=x+1



# ri=int(input('назови число'))
# if ri%2==0:
#     print('это число не делится на две')
# else:
#      print('это число делится на две')



#     try:
#         if user == '+':
#             print(uzer+uzer1)
#         elif user == '-':
#             print(uzer-uzer1)  
#         elif user == '*':
#             print(uzer*uzer1)
#         elif user == '/':
#             print(uzer/uzer1)
#         else:
#             print("Простите я незнаю как это считать:(")

#         prodoljenie=input("хотите продолжить?\n")

#         if prodoljenie.lower()=='нет'or prodoljenie.lower()=='no':
#             break
#     except ZeroDivisionError:
#         print("деление на ноль запрещено") 




# while True:
#     user=input("введите знак:+,-,/,*")
#     uzer=int(input("Введите чило1:"))
#     uzer1=int(input("Введите чило2:"))















