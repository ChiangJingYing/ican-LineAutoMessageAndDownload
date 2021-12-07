<h1>慈大ican偵查今日有無作業、傳訊、下載</h1>
<h2>偵查</h2>



<h2>下載</h2>
<h4>對傳入的url加入cookie請求並取得回傳的html</h4>

    herf = url
    headers = {
        'User-Agent': 'XXXXXX',
        'Cookie': 'XXXXXX'
    }
    session = requests.Session()
    response = session.get(herf, headers=headers)
<h4>Beautifulsoup初始化</h4>

    soup = BeautifulSoup(response.text, "html.parser")
    sel = soup.find_all('a', href='#') #標籤是<a>且href='#'
<h4>篩選出檔案代碼</h4>

    # onclick = javascript:flv_filedownload('XXXXXX'); 原始取得的指令
    for s in sel:
        if s.attrs['onclick'] != 'More();':  
            code = (s.attrs['onclick'])[29:35:1] # 取出串列中29~35個（六碼）
<h4>請求html並寫入檔案</h4>
with open("檔名","寫入方式")

    file = requests.get('https://ican.tcu.edu.tw/ican5/Download.ashx?fileid=%s' % code)
        with open('/Users/jing/Downloads/%s題目.docx' % localltime, 'wb') as f:  
            f.write(file.content)
<h4>調用外部指令打開下載的檔案</h4>
os.system("指令")

    os.system("open /Users/jing/Downloads/%s題目.docx" % localltime)


<h2>傳訊（Line Notify)</h2>
<h4>格式化需要的Header</h4>

    header = {"Authorization": "Bearer " + token}
<h4>param字典 key->value => message->要傳送的話</h4>

    param = {'message': message}
<h4>通過對https://notify-api.line.me/api/notify 通過POST傳送Line訊息</h4>

    requests.post("https://notify-api.line.me/api/notify", headers=header, params=param)***  
<h4>回傳POST的html狀態code</h4>

    r.status_code