import requests

url = " https://daytonabeach.erau.edu/campus-life/academic-calendar"

resp = requests.get(url=url)
resp_text = resp.text


pure_resp_text = resp.text.split('col-xs-12 col-md-8 col-sm-7')[1].split('col-xs-12 col-md-4')[0]
test = pure_resp_text.split('<div class="clearfix ">')
for i in range(1,len(test)):
    resp_arr = test[i].split('<td style="text-align: left;">')
    for j in range(1,len(resp_arr)):
        if(j%2==0):
            print(resp_arr[j].split('<')[0])
        else:
            print(resp_arr[j].split('<strong>')[1].split('<')[0])
        