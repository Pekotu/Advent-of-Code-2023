with open("test_input.txt", 'r') as f:
    input = f.read().split('\n')


results = 0

for r in input:
    r = r.split(",")
    for code in r:
        result=0
        for c in code:
            result = (result+ord(c))*17%256
            #result = result*17
            #result = result%256
    
        #print(code," >>> ", result)
        results += result
print(results)
