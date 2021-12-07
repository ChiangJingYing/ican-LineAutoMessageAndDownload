<h1>慈大ican偵查今日有無作業、傳訊、下載</h1>
<h2>偵查</h2>



<br><h2>下載</h2>
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
* 篩選出檔案代碼
    ```
    # onclick = javascript:flv_filedownload('XXXXXX'); 原始取得的指令
    for s in sel:
        if s.attrs['onclick'] != 'More();':  
            code = (s.attrs['onclick'])[29:35:1] # 取出串列中29~35個（六碼）
* 請求html並寫入檔案
    ```
    with open("檔名","寫入方式")
         file = requests.get('https://ican.tcu.edu.tw/ican5/Download.ashx?fileid=%s' % code)
            with open('/Users/jing/Downloads/%s題目.docx' % localltime, 'wb') as f:  
                f.write(file.content)
* 調用外部指令打開下載的檔案os.system("指令")<br>
  ```
  os.system("open /Users/jing/Downloads/%s題目.docx" % localltime)
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