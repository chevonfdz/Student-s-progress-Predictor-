
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839044        
  
# Date: 29/04/2020

#input marks from the user 
pass_mark=int(input('Please enter your credits at pass:'))
defer_mark=int(input('Please enter your credit at defer:'))
fail_mark=int(input('Please enter your credit at fail:'))

if pass_mark==120 and defer_mark==0 and fail_mark==0:#1
    print("Progress")
elif pass_mark==100 and defer_mark==20 and fail_mark==0:#2
    print("Progress (module trailer)")
elif pass_mark==100 and defer_mark==0 and fail_mark==20:#3
    print("Progress (module trailer)")
elif pass_mark==80 and defer_mark==40 and fail_mark==0:#4
    print("Do not Progress – module retriever")
elif pass_mark==80 and defer_mark==20 and fail_mark==20:#5
    print("Do not Progress – module retriever")
elif pass_mark==80 and defer_mark==0 and fail_mark==40:#6
    print("Do not Progress – module retriever")
elif pass_mark==60 and defer_mark==60 and fail_mark==0:#7
    print("Do not Progress – module retriever")
elif pass_mark==60 and defer_mark==40 and fail_mark==20:#8
    print("Do not Progress – module retriever")
elif pass_mark==60 and defer_mark==20 and fail_mark==40:#9
    print("Do not Progress – module retriever")
elif pass_mark==60 and defer_mark==0 and fail_mark==60:#10
    print("Do not Progress – module retriever")
elif pass_mark==40 and defer_mark==80 and fail_mark==0:#11
    print("Do not Progress – module retriever")
elif pass_mark==40 and defer_mark==60 and fail_mark==20:#12
    print("Do not Progress – module retriever")
elif pass_mark==40 and defer_mark==40 and fail_mark==40:#13
    print("Do not Progress – module retriever")
elif pass_mark==40 and defer_mark==20 and fail_mark==60:#14
    print("Do not Progress – module retriever")
elif pass_mark==40 and defer_mark==0 and fail_mark==80:#15
    print("Exclude")
elif pass_mark==20 and defer_mark==100 and fail_mark==0:#16
    print("Do not progress – module retriever")
elif pass_mark==20 and defer_mark==80 and fail_mark==20:#17
    print("Do not progress – module retriever")
elif pass_mark==20 and defer_mark==60 and fail_mark==40:#18
    print("Do not progress – module retriever")
elif pass_mark==20 and defer_mark==40 and fail_mark==60:#19
    print("Do not progress – module retriever")
elif pass_mark==20 and defer_mark==20 and fail_mark==80:#20
    print("Exclude")
elif pass_mark==20 and defer_mark==0 and fail_mark==100:#21
    print("Exclude")
elif pass_mark==0 and defer_mark==120 and fail_mark==0:#22
    print("Do not progress – module retriever")
elif pass_mark==0 and defer_mark==100 and fail_mark==20:#23
    print("Do not progress – module retriever")
elif pass_mark==0 and defer_mark==80 and fail_mark==40:#24
    print("Do not progress – module retriever")
elif pass_mark==0 and defer_mark==60 and fail_mark==60:#25
    print("Do not progress – module retriever")
elif pass_mark==0 and defer_mark==40 and fail_mark==80:#26
    print("Exclude")
elif pass_mark==0 and defer_mark==20 and fail_mark==100:#27
    print("Exclude")
elif pass_mark==0 and defer_mark==0 and fail_mark==120:#28
    print("Exclude")
