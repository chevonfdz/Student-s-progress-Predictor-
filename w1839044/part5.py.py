# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839044        
  
# Date: 29/04/2020

list=[(120,0,0),(100,20,0),(100,0,20),(80,20,20),(60,40,20),(40,40,40),
        (20,40,60),(20,20,80),(20,0,100),(0,0,120)]
pro=0
tra=0
ret=0
exc=0
val=0
def marks():
    
        if pass_mark==120 and defer_mark==0 and fail_mark==0:#1
            global pro
            pro=pro+1
            print("Progress")
        elif pass_mark==100 and defer_mark==20 and fail_mark==0:#2
            global tra
            tra=tra+1
            print("Progress (module trailer)")
        elif pass_mark==100 and defer_mark==0 and fail_mark==20:#3
            tra=tra+1
            print("Progress (module trailer)")
        elif pass_mark==80 and defer_mark==40 and fail_mark==0:#4
            global ret
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==80 and defer_mark==20 and fail_mark==20:#5
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==80 and defer_mark==0 and fail_mark==40:#6
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==60 and defer_mark==60 and fail_mark==0:#7
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==60 and defer_mark==40 and fail_mark==20:#8
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==60 and defer_mark==20 and fail_mark==40:#9
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==60 and defer_mark==0 and fail_mark==60:#10
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==40 and defer_mark==80 and fail_mark==0:#11
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==40 and defer_mark==60 and fail_mark==20:#12
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==40 and defer_mark==40 and fail_mark==40:#13
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==40 and defer_mark==20 and fail_mark==60:#14
            ret=ret+1
            print("Do not Progress – module retriever")
        elif pass_mark==40 and defer_mark==0 and fail_mark==80:#15
            global exc
            exc=exc+1
            print("Exclude")
        elif pass_mark==20 and defer_mark==100 and fail_mark==0:#16
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==20 and defer_mark==80 and fail_mark==20:#17
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==20 and defer_mark==60 and fail_mark==40:#18
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==20 and defer_mark==40 and fail_mark==60:#19
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==20 and defer_mark==20 and fail_mark==80:#20
            exc=exc+1
            print("Exclude")
        elif pass_mark==20 and defer_mark==0 and fail_mark==100:#21
            exc=exc+1
            print("Exclude")
        elif pass_mark==0 and defer_mark==120 and fail_mark==0:#22
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==0 and defer_mark==100 and fail_mark==20:#23
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==0 and defer_mark==80 and fail_mark==40:#24
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==0 and defer_mark==60 and fail_mark==60:#25
            ret=ret+1
            print("Do not progress – module retriever")
        elif pass_mark==0 and defer_mark==40 and fail_mark==80:#26
            exc=exc+1
            print("Exclude")
        elif pass_mark==0 and defer_mark==20 and fail_mark==100:#27
            exc=exc+1
            print("Exclude")
        elif pass_mark==0 and defer_mark==0 and fail_mark==120:#28
            exc=exc+1
            print("Exclude")


while val<10:
    total=list[val]
    pass_mark,defer_mark,fail_mark=total
    val=val+1
    marks()
    

else:
    print()
    print('Progress',pro,':',pro*'*')
    print('Trailer',tra,':',tra*'*')
    print('Retriver',ret,':',ret*'*')
    print('Exclude',exc,':',exc*'*')
    print()
    print(pro+tra+ret+exc,'Outcomes in total.')


       












        
