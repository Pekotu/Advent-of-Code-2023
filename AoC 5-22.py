import re
import time

def najdi_rozsahy_map():
    for mapa in range(1,number_of_maps+1):
        mapa_start = maps.index("map"+str(mapa))+1
        if mapa==7:
            mapa_end = len(maps)
        else:    
            mapa_end = maps.index("map"+str(mapa+1))
        #tuple = (mapa_start, mapa_end)
        rozsahy_map.append((mapa_start, mapa_end))
        
    return

def projdi_pres_mapy(seed):
    for mapa in range(1,len(rozsahy_map)):
        mapa_start = rozsahy_map[mapa][0]
        mapa_end = rozsahy_map[mapa][1]
        
        for r in range(mapa_start, mapa_end):
            start = maps[r][1]
            rng = maps[r][2]
            res = maps[r][0]
            if seed in range(start,start+rng):
                seed=seed-start+res
                break        
            
    return seed


"""Main code-------------------------"""
start_time = time.time()
f= open('test_input.txt', 'r')
list = f.readlines()
f.close()

rozsahy_map = [(0,0)]
#seed =0
maps=[]
number_of_maps=0
seeds=()
result = 999999999999999999999999999

for row in list: #rozdělím soubor na seed and maps
    if "seeds:" in row:
        seeds = tuple(map(int,row[6:-1].split()))
        
    
    if re.match(r"[0-9]+ [0-9]+ [0-9]+", row[:-1]):
        tup = tuple(map(int,row.split())) #rozdeli string po mezerach, prevede na in a pote na tuple 
        maps.append(tup)
    
    if "map:" in row:
        number_of_maps +=1 
        maps.append("map"+str(number_of_maps))

najdi_rozsahy_map()

#projdi s kazdym seminkem vsechny mapy
for s in range(0,len(seeds),2):
    for seed in range(seeds[s], seeds[s]+seeds[s+1]):              
        seed_result = projdi_pres_mapy(seed)
        if seed_result < result: result= seed_result




print(f"{result=}")
print("cas= " + time.time()-start_time)




