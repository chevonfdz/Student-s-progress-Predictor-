
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839044        
  
# Date: 29/04/2020


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
if (pass_mark+defer_mark+fail_mark)>120:
    print('Total incorrect')
else:


    if pass_mark==120 and defer_mark==0 and fail_mark==0:#1
        print("Progress\n")
    elif pass_mark==100 and defer_mark==20 and fail_mark==0:#2
        print("Progress (module trailer)\n")
    elif pass_mark==100 and defer_mark==0 and fail_mark==20:#3
        print("Progress (module trailer)\n")
    elif pass_mark==80 and defer_mark==40 and fail_mark==0:#4
        print("Do not Progress – module retriever\n")
    elif pass_mark==80 and defer_mark==20 and fail_mark==20:#5
        print("Do not Progress – module retriever\n")
    elif pass_mark==80 and defer_mark==0 and fail_mark==40:#6
        print("Do not Progress – module retriever\n")
    elif pass_mark==60 and defer_mark==60 and fail_mark==0:#7
        print("Do not Progress – module retriever\n")
    elif pass_mark==60 and defer_mark==40 and fail_mark==20:#8
        print("Do not Progress – module retriever\n")
    elif pass_mark==60 and defer_mark==20 and fail_mark==40:#9
        print("Do not Progress – module retriever\n")
    elif pass_mark==60 and defer_mark==0 and fail_mark==60:#10
        print("Do not Progress – module retriever\n")
    elif pass_mark==40 and defer_mark==80 and fail_mark==0:#11
        print("Do not Progress – module retriever\n")
    elif pass_mark==40 and defer_mark==60 and fail_mark==20:#12
        print("Do not Progress – module retriever\n")
    elif pass_mark==40 and defer_mark==40 and fail_mark==40:#13
        print("Do not Progress – module retriever\n")
    elif pass_mark==40 and defer_mark==20 and fail_mark==60:#14
        print("Do not Progress – module retriever\n")
    elif pass_mark==40 and defer_mark==0 and fail_mark==80:#15
        print("Exclude\n")
    elif pass_mark==20 and defer_mark==100 and fail_mark==0:#16
        print("Do not progress – module retriever\n")
    elif pass_mark==20 and defer_mark==80 and fail_mark==20:#17
        print("Do not progress – module retriever\n")
    elif pass_mark==20 and defer_mark==60 and fail_mark==40:#18
        print("Do not progress – module retriever\n")
    elif pass_mark==20 and defer_mark==40 and fail_mark==60:#19
        print("Do not progress – module retriever\n")
    elif pass_mark==20 and defer_mark==20 and fail_mark==80:#20
        print("Exclude\n")
    elif pass_mark==20 and defer_mark==0 and fail_mark==100:#21
        print("Exclude\n")
    elif pass_mark==0 and defer_mark==120 and fail_mark==0:#22
        print("Do not progress – module retriever\n")
    elif pass_mark==0 and defer_mark==100 and fail_mark==20:#23
        print("Do not progress – module retriever\n")
    elif pass_mark==0 and defer_mark==80 and fail_mark==40:#24
        print("Do not progress – module retriever\n")
    elif pass_mark==0 and defer_mark==60 and fail_mark==60:#25
        print("Do not progress – module retriever\n")
    elif pass_mark==0 and defer_mark==40 and fail_mark==80:#26
        print("Exclude\n")
    elif pass_mark==0 and defer_mark==20 and fail_mark==100:#27
        print("Exclude\n")
    elif pass_mark==0 and defer_mark==0 and fail_mark==120:#28
        print("Exclude\n")
