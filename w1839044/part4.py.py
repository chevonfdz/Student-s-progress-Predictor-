
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839044        
  
# Date: 29/04/2020

pro=0
tra=0
ret=0
exc=0

def main():
    global pro
    global tra
    global ret
    global exc
    
    while True:#loop until the user gives the right input
        try:#to avoid value error
            pass_mark=int(input('Please enter your credits at pass:'))#input marks from the user 
            pass_mark=int(pass_mark)
            if 0 <= pass_mark <= 120 and (pass_mark%20)==0:#range
                break
                   
            else:
                print('Out of range') 
                
        except ValueError:
            print('Integer Required!')#integer required

    while True:#loop until the user gives the right input
        try:#to avoid value error
            defer_mark=int(input('Please enter your credit at defer:'))
            defer_mark=int(defer_mark)
            if 0 <= defer_mark <= 120 and (defer_mark%20)==0:#range
                break
                   
            else:
                print('Out of range')
                 
                  
        except ValueError:
            print('Integer Required!')#integer required
     
    while True:#loop until the user gives the right input
        try:#to avoid value error
            fail_mark=int(input('Please enter your credit at fail:'))
            fail_mark=int(fail_mark)
            if 0 <= fail_mark <= 120 and (fail_mark%20)==0:#range
                break
                
            else:
                print('Out of range')
                 
               
                   
        except ValueError:
            print('Integer Required!')#integer required

     #to check about the total

    if (pass_mark+defer_mark+fail_mark)>120 or(pass_mark+defer_mark+fail_mark)<120:
        print('Total incorrect')
    else:


        if pass_mark==120 and defer_mark==0 and fail_mark==0:#1
            pro=pro+1
            print("Progress\n")
        elif pass_mark==100 and defer_mark==20 and fail_mark==0:#2
            tra=tra+1
            print("Progress (module trailer)\n")
        elif pass_mark==100 and defer_mark==0 and fail_mark==20:#3
            tra=tra+1
            print("Progress (module trailer)\n")
        elif pass_mark==80 and defer_mark==40 and fail_mark==0:#4
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==80 and defer_mark==20 and fail_mark==20:#5
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==80 and defer_mark==0 and fail_mark==40:#6
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==60 and defer_mark==60 and fail_mark==0:#7
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==60 and defer_mark==40 and fail_mark==20:#8
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==60 and defer_mark==20 and fail_mark==40:#9
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==60 and defer_mark==0 and fail_mark==60:#10
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==40 and defer_mark==80 and fail_mark==0:#11
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==40 and defer_mark==60 and fail_mark==20:#12
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==40 and defer_mark==40 and fail_mark==40:#13
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==40 and defer_mark==20 and fail_mark==60:#14
            ret=ret+1
            print("Do not Progress – module retriever\n")
        elif pass_mark==40 and defer_mark==0 and fail_mark==80:#15
            exc=exc+1
            print("Exclude\n")
        elif pass_mark==20 and defer_mark==100 and fail_mark==0:#16
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==20 and defer_mark==80 and fail_mark==20:#17
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==20 and defer_mark==60 and fail_mark==40:#18
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==20 and defer_mark==40 and fail_mark==60:#19
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==20 and defer_mark==20 and fail_mark==80:#20
            exc=exc+1
            print("Exclude\n")
        elif pass_mark==20 and defer_mark==0 and fail_mark==100:#21
            exc=exc+1
            print("Exclude\n")
        elif pass_mark==0 and defer_mark==120 and fail_mark==0:#22
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==0 and defer_mark==100 and fail_mark==20:#23
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==0 and defer_mark==80 and fail_mark==40:#24
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==0 and defer_mark==60 and fail_mark==60:#25
            ret=ret+1
            print("Do not progress – module retriever\n")
        elif pass_mark==0 and defer_mark==40 and fail_mark==80:#26
            exc=exc+1
            print("Exclude\n")
        elif pass_mark==0 and defer_mark==20 and fail_mark==100:#27
            exc=exc+1
            print("Exclude\n")
        elif pass_mark==0 and defer_mark==0 and fail_mark==120:#28
            exc=exc+1
            print("Exclude\n")
            
#to continue the program until the user wants to quit
    print('Would you like to enter another set of data?')
    repeat=input(str("Enter 'y' for yes or 'q' to quit and view results:"))
    if repeat=='y':
        main()#start programe again
    else:
        repeat=='q'#if user quit this will print
        print('\n-------------------------------------------------------------\n')
        print('Horizontal Histogram')#horizontal histograme
        print('Progress',pro,':',pro*'*')
        print('Trailer',tra,':',tra*'*')
        print('Retriver',ret,':',ret*'*')
        print('Exclude',exc,':',exc*'*')
        print()
        print(pro+tra+ret+exc,'Outcomes in total.')
        print('\n-------------------------------------------------------------\n')
#vertical histrograme
        print('Progress',' Trailing',' Retriever',' Excluded')
        for x in range(max(pro,tra,ret,exc)):
            print("{0}          {1}          {2}         {3}".format
      ('*'if x<pro else '','*'if x<tra else '','*'if x<ret else '','*'if x<exc else ''))
          
        print(pro+tra+ret+exc,'Outcomes in total.')
          
main()
