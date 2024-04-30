data = input("what are you looking for car/bike:")

if data == 'bike':
    bike = input("chose any one(bmw,honda,bajaj,kawasaki):")
if data =='honda':
    if bike=='honda':
        print('drimyuga\n unicon')
        model = input("select any one bike to see detail:")
        elif model=="drimyuga":
            print('''actual-price:250000\ndiscount-price:240000\n
                   cc:300\n manufacturer:honda-pune''')
        elif model=="unicon":
            print('''actual-price:250000\ndiscount-price:240000\n
                   cc:300\n manufacturer:honda-pune''')
elif data=='bmw':
    print('bmw R300 \n BMW RC500 \n BMW R280 \n KAWASAKI')
    model = input("select any one bike to see detail:")
    if model=="bmw r300":
        print('''actual-price:250000\ndiscount-price:240000\n
                     cc:300\n manufacturer:BMW-NEWYORK''')
        if model=="BMW RC500":
            print('''actual-price:300000\ndiscount-price:280000\n
                        cc:500\n manufacturer:BMW-NEWYORK''')
        elif model=="BMW R280":
                print('''actual-price:200000\ndiscount-price:180000\n
                            cc:280\n manufacturer:BMW-NEWYORK''')
        elif model=="KAWASAKI":
                print('''actual-price:240000\ndiscount-price:220000\n
                             cc:350\n manufacturer:BMW-NEWYORK''')
elif data == 'car':
    car=input("which company car are you looking for:")
    
        
 
