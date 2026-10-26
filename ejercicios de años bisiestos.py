años=[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]
for año in años:
    if año%4==0:
        print(f"{año} es bisiesto")
    elif año%100==0:
        print(f"{año} no es bisiesto")
    elif año%400==0:
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")
        