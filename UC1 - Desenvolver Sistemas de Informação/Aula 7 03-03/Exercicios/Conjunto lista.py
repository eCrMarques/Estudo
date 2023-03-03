#List

# 7. Write a Python program to remove duplicates from a list.
lista=['a','e','f','g']
li =['ab','bcd','cef','dghi','a','d','g']
def q7():
    x=0
    for i in li:
        if li.count(i)>1:
            li.pop(x)
            print(li[x])
        
    print(li)

#8. Write a Python program to check if a list is empty or not
def q8():
    l=[]
    if len(l)==0:
        print("Esta Vazio" )

#9. Write a Python program to clone or copy a list.
def q9():
    l=li.copy()
    print(l)

#10. Write a Python program to find the list of words that are longer than n from a given list of words
def q10():
    x =int(input(':' ))
    for i in li:
        if len(i)>x:
            print(i, len(i))

#11. Write a Python function that takes two lists and returns True if they have at least one common member
def q11():
    for l in lista:
     if l in li:
         print(l,"Ambos contem o msm elemento")

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
#14. Write a Python program to print the numbers of a specified lis
def q12():
    List.pop(0)
    print(len(List))
    List.pop(3)
    print(len(List))
    List.pop(3)
    print(len(List))
    
    print(List)

