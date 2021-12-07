<h1>慈大ican偵查今日有無作業、傳訊、下載</h1>
<h2>偵查</h2>

* 對傳入的url加入cookie請求並取得回傳的html
    ```
    herf = url
    headers = {
        'User-Agent': 'XXXXXX',
        'Cookie': 'XXXXXX'
    }
    session = requests.Session()
    response = session.get(herf, headers=headers)
* Beautifulsoup初始化
    ```
    soup = BeautifulSoup(response.text, "html.parser")
    sel = soup.find_all('a', href='#') #標籤是<a>且href='#'
* 篩選出要的資料
  * 篩出要的文字
    ```
    for k in sel:
        message = []  # 串列初始化
        url = ''  # uel initial
        for s in k.find_next_siblings('td'):
            content = s.contents
            if len(content) == 3:  # 確定s裡有<herf>標籤
                url = "https://ican.tcu.edu.tw" + content[1].attrs['href']  # 將<herf>標籤內容物存入url
            if s.text.strip() != '':  # 去除頭尾空白後還有文字的
                message.append(s.text.strip())  # 將文字存到message串列中最後面
        message.append(url)
        message[:2] = []  # 將在串列中的繳交方式、作業類別去除(前兩個)
    ```
  * 篩選出檔案代碼 
    ```
    # onclick = javascript:flv_filedownload('XXXXXX'); 原始取得的指令
    for s in sel:
        if s.attrs['onclick'] != 'More();':  
            code = (s.attrs['onclick'])[29:35:1] # 取出串列中29~35個（六碼）
    
<br><h2>下載</h2>

* 請求html並寫入檔案
  * with open("檔名","寫入方式")
  ```
  file = requests.get('https://ican.tcu.edu.tw/ican5/Download.ashx?fileid=%s' % code)
      with open('/Users/jing/Downloads/%s題目.docx' % localltime, 'wb') as f:  
      f.write(file.content)
* 調用外部指令打開下載的檔案
  * os.system("指令") 使用terminal指令<br>
  ```
  os.system("open /Users/jing/Downloads/%s題目.docx" % localltime)
  ```
<br><h2>格式化文字</h2>
* 將文字加入到串列中
  ```
  localltime = time.strftime("%Y/%-m/%-d", time.localtime())  # 取得現在的時間並格式化成（Y/M/D)
    if len(message) != 4:  # 若為繳交狀態，則增加一個"XD"以防後續判斷串列超出範圍
        message.append('XD')
    if message[3] != '已繳交' and message[3] != '未開始' and message[3] != '已逾期':  # 篩選為繳交的項目出來
        coutoggTime = time.mktime(time.strptime(message[2], '%Y/%m/%d %H:%M'))  # 結束日期秒數
        if localltime in message[1]:  # 去除無繳交狀態且已預期的項目
            messages = ('\n作業標題：' + message[0] + "\n起始日期：" + message[1] + '\n結束日期：' + message[2])
  ```
<br><h2>傳訊（Line Notify)</h2>
* 格式化需要的Header<br>
    ```
    header = {"Authorization": "Bearer " + token}
* param字典 key->value => message->要傳送的話<br>
    ```
    param = {'message': message}
* 通過對https://notify-api.line.me/api/notify 通過POST傳送Line訊息<br>
    ```
    requests.post("https://notify-api.line.me/api/notify", headers=header, params=param)
* 回傳POST的html狀態code<br>
    ```
    r.status_code