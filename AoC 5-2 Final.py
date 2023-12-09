import re
import time

def najdi_rozsahy_radku_map():
    for mapa in range(1,number_of_maps+1):
        mapa_start = maps.index("map"+str(mapa))+1
        if mapa==7:
            mapa_end = len(maps)
        else:    
            mapa_end = maps.index("map"+str(mapa+1))
        #tuple = (mapa_start, mapa_end)
        rozsahy_map.append((mapa_start, mapa_end))
        
    return

def projdi_pres_mapy(mapa_start, mapa_end):
    seeds_changed=[]
    seeds_rest=[]
    
    for mapa_row in maps[mapa_start:mapa_end]:
        map_s = mapa_row[1]
        map_e = mapa_row[1] + mapa_row[2]-1
        map_change = mapa_row[0]-map_s
        mapa_row[0]
        #intervals = {(s,s+l) for s,l in zip(seeds[::2], seeds[1::2])}
        s=0
        for seeds_s, seeds_e in zip(seeds[::2], seeds[1::2]):

            if seeds_s == seeds_e == -1:
                s+=2
                continue

            #najdi shodne rozsahy mezi seeds-range a map_range
            

            #1 seeds se prekryvaji s dolni casti mapy 
            if map_s > seeds_s and map_s <= seeds_e <= map_e:
                #new seed range pred map
                seeds.append(seeds_s)
                seeds.append(map_s-1 )
                
                #new seed range v mape
                seeds_changed.append(map_s+map_change)
                seeds_changed.append(seeds_e +map_change)
                
                #maze ze seed
                seeds[s]=-1
                seeds[s+1]=-1
                
            #2 seeds zacinaji pred a konci za mapou 
            elif map_s > seeds_s and seeds_e > map_e:
                #new seed range pred map
                seeds.append(seeds_s)
                seeds.append(map_s-1 )

                #new seed range shodny s mapou
                seeds_changed.append(map_s+map_change)
                seeds_changed.append(map_e +map_change)

                #new seed range za mapou
                seeds.append(map_e+1)
                seeds.append(seeds_e) 

                #maze ze seed
                seeds[s]=-1
                seeds[s+1]=-1

            #3 vsechna seeds jsou v mape 
            elif map_s <= seeds_s <= map_e and map_s <= seeds_e <= map_e:
                seeds_changed.append(seeds_s+map_change)
                seeds_changed.append(seeds_e+map_change)

                #maze ze seed
                seeds[s]=-1
                seeds[s+1]=-1    

            #4 seeds se prekryvaji s horni casti mapy 
            elif map_s <= seeds_s <= map_e and seeds_e > map_e:
                #new seed range v mape
                seeds_changed.append(seeds_s+map_change)
                seeds_changed.append(map_e+map_change)

                #new seed range za map
                seeds.append(map_e+1)
                seeds.append(seeds_e )

                #maze ze seed
                seeds[s]=-1
                seeds[s+1]=-1

            s+=2
    

    for val in seeds_changed:
        seeds.append(val)
    
    return 

"""Main code-------------------------"""
start_time = time.time()
f= open('input.txt', 'r')
list = f.readlines()
f.close()

rozsahy_map = [(0,0)]
#seed =0
maps=[]
number_of_maps=0
seeds=[]
intervals = {}
#rozdeli vstupni soubor na seznam seeds a mapy
for row in list: #rozdělím soubor na seed and maps
    poz_znak = row[-1]
    if row[-1]!= '\n': 
        row += "\n" 
    if "seeds:" in row:
        rowx = row[7:-1]
        seeds = [int(x) for x in rowx.split()]
        seeds2=[]
        for s,l in zip(seeds[::2], seeds[1::2]):
            seeds2.append(s)
            seeds2.append(s+l-1)
        seeds=seeds2.copy()

    if re.match(r"[0-9]+ [0-9]+ [0-9]+", row[:-1]):
        tup = tuple(map(int,row.split())) #rozdeli string po mezerach, prevede na in a pote na tuple 
        maps.append(tup)
    
    if "map:" in row:
        number_of_maps +=1 
        maps.append("map"+str(number_of_maps))

najdi_rozsahy_radku_map()

for mapa in range(1,len(rozsahy_map)):
    mapa_start = rozsahy_map[mapa][0]
    mapa_end = rozsahy_map[mapa][1]
    ss=0
    while len(seeds)>ss:
        if seeds[ss]==-1:
            seeds.pop(ss)
        else:
            ss+=1
    projdi_pres_mapy(mapa_start, mapa_end)

ss=0
while len(seeds)>ss:
    if seeds[ss]==-1:
        seeds.pop(ss)
    else:
        ss+=1

result = min(seeds)

print(f"{seeds=}")

print(f"{result=}")

