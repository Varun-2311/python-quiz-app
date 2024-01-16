

#this function gives the result of the test
def test(name):
    print("QUIZ")
    print("instsructions:")
    print("there are 10 questions with 4 options each and only one is correct")
    count=0
    print("1.","number of planets in the solar syste? ")
    print('opt1-6','opt2-7','opt3-8','opt4-9')
    a = int(input('enter your ans:'))
    if a==3:
        count=count+1
    else:
        count=count
    print("2.","largest planet in the solar system? ")
    print('opt1-earth','opt2-mars','opt3-jupiter','opt4-saturn')
    a = int(input('enter your ans:'))
    if a==3:
        count=count+1
    else:
        count=count
    print("3.","smallest planet in the solar system? ")
    print('opt1-mercury','opt2-venus','opt3-earth','opt4-mars')
    a = int(input('enter your ans:'))
    if a==1:
        count=count+1
    else:
        count=count
    print("4.","the planet farthest from the sun in the solar system? ")
    print('opt1-saturn','opt2-jupiter','opt3-uranus','opt4-neptune')
    a = int(input('enter your ans:'))
    if a==4:
        count=count+1
    else:
        count=count
    print("5.","the planet closest to the sun in the solar system? ")
    print('opt1-mercury','opt2-earth','opt3-venus','opt4-mars')
    a = int(input('enter your ans:'))
    if a==1:
        count=count+1
    else:
        count=count
    print("6.","which planet is thought to be made up of a central iron core, rocky mantle and silicate crust? ")
    print('opt1-mercury','opt2-venus','opt3-earth','opt4-mars')
    a = int(input('enter your ans:'))
    if a==2:
        count=count+1
    else:
        count=count
    print("7.","which planet has the largest dust storms in the solar system? ")
    print('opt1-mercury','opt2-venus','opt3-earth','opt4-mars')
    a = int(input('enter your ans:'))
    if a==4:
        count=count+1
    else:
        count=count
    print("8.","which planet is also known as the morning star? ")
    print('opt1-mercury','opt2-venus','opt3-earth','opt4-mars')
    a = int(input('enter your ans:'))
    if a==2:
        count=count+1
    else:
        count=count
    print("9.","which planet is often referred to as an ICE GIANT in our solar system? ")
    print('opt1-jupiter','opt2-saturn','opt3-uranus','opt4-neptune')
    a = int(input('enter your ans:'))
    if a==3:
        count=count+1
    else:
        count=count
    print("10.","which planet is the most distant planet that can be seen with the naked eye? ")
    print('opt1-jupiter','opt2-saturn','opt3-uranus','opt4-neptune')
    a = int(input('enter your ans:'))
    if a==2:
        count=count+1
    else:
        count=count
    print("the test is complete")
    print(count,"/10")
    return count


#for defining number of users and then calling the fuction as per that
n=int(input("enter number of users for the test"))
d={}
for i in range(n):   
    user=input("enter your name:")
    score=test(user)

    if user not in d:
        d[user]=[]
        d[user].append(score)
    else:
        d[user].append(score)
print(d)#gives us output value of dictionary as a list with multiple scores
dmax={}
for i in d.keys():
    dmax[i]=max(d[i])
print(dmax)
sorted_scores=sorted(dmax.items(),key=lambda x:x[1],reverse=True)
converted_scores=dict(sorted_scores)
#this sorts the dictionary from highest to lowest score

    