import requests
url = "https://m.stock.naver.com/sise/siseList.nhn?menu=market_sum&sosok=0"
resp = requests.get(url=url)
resp_text = resp.text
resp_array = resp_text.split('nm":"')
for i in range(1, 6):
    print(resp_array[i].split('"')+":"+resp_array[i].split(',"cv'))
    