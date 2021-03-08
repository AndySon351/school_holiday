import requests
'''
url = "http://rank.ezme.net/?ckattempt=2"
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81","Referer":"http://rank.ezme.net/","cookie":"CUPID=722b43102fa07181ef7b9ca172ce0e92; _ga=GA1.2.664659738.1614773369; _gid=GA1.2.1522281994.1614773369; __gads=ID=096dd3b10f5f7387-22d000c40db900e0:T=1614773369:RT=1614773369:S=ALNI_MY_WitjpWG6N_RO7XD0rMRAXQcvDA; _gat=1","Accept-Language":"ko,en;q=0.9,en-US;q=0.8"}
resp = requests.get(url=url,headers=headers)
resp.encoding='utf-8'
abc = resp.text

resp_arr = resp_text.split('"demo-card-image__filename">')
for i in range(1,11):
    print(resp_arr[i].split('<')[0])
'''
url = "https://m.stock.naver.com/sise/siseList.nhn?menu=market_sum&sosok=0"
resp = requests.get(url=url)
resp_text = resp.text
resp_arr = resp_text.split('nm":"')
print(resp_arr)

