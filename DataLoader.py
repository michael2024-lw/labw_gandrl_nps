import urllib.request
import zipfile
import os
import shutil
import sys
import re


if not os.path.isfile('train.json'):
    if not os.path.isfile('karel-dataset.zip'):
        url = "https://rhfkuq.bn.files.1drv.com/y4m_FYchV21HnHZlj_4JF1zNr9L1e8QdvrI5et0w_32nTMli_-Njy9skX6nbUJB02Yu-8rDEWoFK0wtzESiLn2uE0cT1wz3y1GKujwua6axBM3oBCmWr0L2VhlRyfh6R4wnbCtdn8uslCiO-Xnslv5HmE0spU8dV6VBlkIZv56WehToBVur8JL5cuZb8B_vtD7FLx85qKkYmeLBA4ByMQd1Hw"
        urllib.request.urlretrieve(url, os.getcwd() + '/karel-dataset.zip')
    
    with zipfile.ZipFile('karel-dataset.zip', 'r') as zip_ref:
        with zip_ref.open('1m_6ex_karel/train.json', 'r') as zf, open(os.getcwd() + '/train.json', 'wb') as f:
            shutil.copyfileobj(zf, f)

percentage = [1]
try: 
    percentage = [int(re.match(r"(\d+)%", sz).group(1)) for sz in sys.argv[1:]]
    if any((itm <= 0 or itm >= 100) for itm in percentage):
        raise
except:
    print('write percentages like this (you can write more than one): 1% 10% 90%', file=sys.stderr)



divisors = [100.0 / pc for pc in percentage]

dfiles = [(idx, os.getcwd() + '/train'+str(prc)+'.json') for idx,prc in enumerate(percentage)]
dfiles = [(divisors[idx],name) for idx,name in dfiles if not os.path.isfile(name)]

def transition_detected(a:int,b:float):
    pres = abs(a - 1) / b
    cres = a / b
    prem = pres - int(pres)
    crem = cres - int(cres)
    if crem < prem:
        return True
    else:
        return False

if dfiles:
    index = -1
    with open(os.getcwd() + '/train.json', 'r') as f:
        for line in f:
            index += 1
            for prc,name in dfiles:
                if transition_detected(index, prc):
                    with open(name, 'a') as wf:
                        wf.write(line)
