def dobpop():
    time=0
    pop=int(input("Enter Population."))
    grate=float(input("Enter groth rate."))
    pop2=pop*2
    while pop<=pop2:
          pop=pop+pop*grate
          time=time+1
    print("Population:",pop.round())
    print("Time:",time,"min.")
    print(10*"*","END",10*"*")
dobpop()
