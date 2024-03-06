import urllib.request
import zipfile
import os
import shutil
import sys


if not os.path.isfile('train.json'):
    if not os.path.isfile('karel-dataset.zip'):
        url = "https://rhfkuq.bn.files.1drv.com/y4m_FYchV21HnHZlj_4JF1zNr9L1e8QdvrI5et0w_32nTMli_-Njy9skX6nbUJB02Yu-8rDEWoFK0wtzESiLn2uE0cT1wz3y1GKujwua6axBM3oBCmWr0L2VhlRyfh6R4wnbCtdn8uslCiO-Xnslv5HmE0spU8dV6VBlkIZv56WehToBVur8JL5cuZb8B_vtD7FLx85qKkYmeLBA4ByMQd1Hw"
        urllib.request.urlretrieve(url, 'karel-dataset.zip')
    
    with zipfile.ZipFile('karel-dataset.zip', 'r') as zip_ref:
        with zip_ref.open('1m_6ex_karel/train.json') as zf, open(os.getcwd() + '/train.json', 'wb') as f:
            shutil.copyfileobj(zf, f)

sizes = [int(sz) for sz in sys.argv[1:]]

