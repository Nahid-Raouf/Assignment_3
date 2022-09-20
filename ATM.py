password=1381
i=0
for i in range(3):
    password=int(input('please enter your password:'))
    if password==1381:
        
        print('open:)')
        
        break
    elif password==1831:
        #call police
        print('!we calld the police!')
        break  
    elif password!=1381:
        print('password is wrong')
        i+=1
    else:
        continue
if i<=3:
    print('locked')
    