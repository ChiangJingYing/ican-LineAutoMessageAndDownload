<h1>慈大ican偵查今日有無作業、傳訊、下載</h1>
<h3>偵查</h3>
<h3>下載</h3>  
<h3>傳訊（Line Notify)</h3>  
***header = {"Authorization": "Bearer " + token}***  
格式化需要的Header  
  
***param = {'message': message}***  
param字典 key->value => message->要傳送的話  

***requests.post("https://notify-api.line.me/api/notify", headers=header, params=param)***  
通過對https://notify-api.line.me/api/notify 通過POST傳送Line訊息

***r.status_code***  
回傳POST的html狀態code

    header = {"Authorization": "Bearer " + token}  #init Header 
    param = {'message': message} # init param
    r = requests.post("https://notify-api.line.me/api/notify", headers=header, params=param)  # send message
    print(str(r.status_code) + message)  # r.status_code查看傳送結果
    if r.status_code == 200:
        exit()
    time.sleep(1.5)  # delay 1.5 second.