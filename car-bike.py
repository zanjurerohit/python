data = input ("what are you looking for car/bike:")
if data =='bike':
    bike= input("which company are you looking for:")
    if bike=='company':
        print('bmw \nhonda \nkawasaki \nroyal enfield')
        model = input('select any one company:')
        if model =="bmw":
            print('g 310 \ng 310gs \nr 1200 gs \ns 1000 rr')
            model = input('select any one bike:')
            if model == "g 310":
                print('''actual-price:250000\ndiscount-price:240000\ncc:350\nmanufacturer:bmw new york''')
            if model == "g 310gs":
                print('''actual-price:300000\ndiscount-price:280000\ncc:400\nmanufacturer:bmw new york''')
            if model == "r 1200 gs":
                print('''actual-price:350000\ndiscount-price:330000\ncc:280\nmanufacturer:bmw new york''')
            if model == "s 1000 rr":
                print('''actual-price:400000\ndiscount-price:380000\ncc:400\nmanufacturer:bmw new york''')
        if model =="honda":
            print('honda sp 125 \nshine \nunicorn \nhness cb350 \nhornet2.0')
            model = input('select any one bike:')
            if model == "honda sp 125":
                print('''actual-price:90000\ndiscount-price:85000\ncc:123\nmanufacturer:honda pune''')
            elif model == "shine":
                print('''actual-price:83000\ndiscount-price:80000\ncc:123\nmanufacturer:honda pune''')
            elif model == "unicorn":
                print('''actual-price:109000\ndiscount-price:100000\ncc:162\nmanufacturer:honda pune''')
            elif model == "hness cb350":
                print('''actual-price:216000\ndiscount-price:209000\ncc:348\nmanufacturer:honda pune''')
        if model =="kawasaki":
            print('ninja h2r \nninja zx-6r \nninja 1000 \nninja 650 \nninja w175')
            model = input('select any one bike:')
            if model == "ninja h2r":
                print('''actual-price:7900000\ndiscount-price:7500000\ncc:998\nmanufacturer:kawasaki philippines:''')
            if model == "ninja zx-6r":
                print('''actual-price:110000\ndiscount-price:1020000\ncc:636\nmanufacturer:kawasaki philippines:''')
            if model == "ninja 1000":
                print('''actual-price:1151000\ndiscount-price:1110000\ncc:1043\nmanufacturer:kawasaki philippines:''')
            if model == "ninja w175":
                print('''actual-price:135000\ndiscount-price:122000\ncc:177\nmanufacturer:kawasaki philippines:''')
                model = input('select any one company:')
        if model =="royal enfield":
            print('bullet 350 \ncontinental gt 650 \ninterceptor 650 \nmeteor 350')
            model = input('select any one bike:')
            if model == "bullet 350":
                print('''actual-price:7900000\ndiscount-price:7500000\ncc:998\nmanufacturer:kawasaki philippines:''')
            if model == "continental gt 650":
                print('''actual-price:110000\ndiscount-price:1020000\ncc:636\nmanufacturer:kawasaki philippines:''')
            if model == "interceptor 650":
                print('''actual-price:1151000\ndiscount-price:1110000\ncc:1043\nmanufacturer:kawasaki philippines:''')
            if model == "meteor 350":
                print('''actual-price:135000\ndiscount-price:122000\ncc:177\nmanufacturer:kawasaki philippines:''')

elif data=='car':
    car=input("which car company are you looking for:")
    if car=="company":
        print('tata motors\nmahindra \nvolkswagen \nrange rover')
        model = input('select any one company:')
        if model =="tata motors":
            print('tata punch \ntata safari \ntata nexon \ntata altroz')
            model = input('select any one car:')
            if model == "tata punch":
                print('''actual-price:955000\ndiscount-price:920000\nmanufacturer:tata motors pune''')
            if model == "tata safari":
                print('''actual-price:2400000\ndiscount-price:2300000\nmanufacturer:tata motors pune''')
            if model == "tata nexon":
                print('''actual-price:1431000\ndiscount-price:1350000\nmanufacturer:tata motors pune''')
            if model == "tata altroz":
                print('''actual-price:1040000\ndiscount-price:1000000\nmanufacturer:tata motors pune''')
        if model =="mahindra":
            print('xuv300 \nxuv 700 \nthar \nscorpio classic ')
            model = input('select any one car:')
            if model == "xuv 300":
                print('''actual-price:1008000\ndiscount-price:988000\nmanufacturer:mahindra mumbai''')
            if model == "xuv 700":
                print('''actual-price:2447000\ndiscount-price:2050000\nmanufacturer:mahindra mumbai''')
            if model == "thar":
                print('''actual-price:1648000\ndiscount-price:1525000\nmanufacturer:mahindra mumbai''')
            if model == "scorpio classic":
                print('''actual-price:1475000\ndiscount-price:1615000\nmanufacturer:mahindra mumbai''')
        if model =="volkswagen":
            print('tata punch \ntata safari \ntata nexon \ntata altroz')
            model = input('select any one car:')
            if model == "tata punch":
                print('''actual-price:955000\ndiscount-price:920000\nmanufacturer:tata motors pune''')
            if model == "tata safari":
                print('''actual-price:2400000\ndiscount-price:2300000\nmanufacturer:tata motors pune''')
            if model == "tata nexon":
                print('''actual-price:1431000\ndiscount-price:1350000\nmanufacturer:tata motors pune''')
            if model == "tata altroz":
                print('''actual-price:1040000\ndiscount-price:1000000\nmanufacturer:tata motors pune''')
        if model =="range rover":
            print('tata punch \ntata safari \ntata nexon \ntata altroz')
            model = input('select any one car:')
            if model == "tata punch":
                print('''actual-price:955000\ndiscount-price:920000\nmanufacturer:tata motors pune''')
            if model == "tata safari":
                print('''actual-price:2400000\ndiscount-price:2300000\nmanufacturer:tata motors pune''')
            if model == "tata nexon":
                print('''actual-price:1431000\ndiscount-price:1350000\nmanufacturer:tata motors pune''')
            if model == "tata altroz":
                print('''actual-price:1040000\ndiscount-price:1000000\nmanufacturer:tata motors pune''')
            











    
            
