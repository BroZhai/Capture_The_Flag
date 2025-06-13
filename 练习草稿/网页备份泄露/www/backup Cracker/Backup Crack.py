import os

with open('front.txt', 'r') as f:
    flines = [line.strip() for line in f.readlines()]  
    
with open('back.txt', 'r') as b:
    blines = [line.strip() for line in b.readlines()] 

for fl in flines:
    for bl in blines:
        # 注: 该沙箱URL已解出关闭, 访问无效
        url = f"http://challenge-3626f6d236461d88.sandbox.ctfhub.com:10800/{fl}.{bl}"  # f-string模版字符串
        print(f'current URL: {url}')
        os.system(f"curl {url}")
        print()

input('按任意键继续...')