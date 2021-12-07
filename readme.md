<h1>慈大ican偵查今日有無作業、傳訊、下載</h1>
<h2>偵查</h2>



<h2>下載</h2>

<h5>取得當前日期(s)並格是化成「年/月/日」</h5>
```python
localltimetime.strftime("%Y%m%d", time.localtime())
```
<h5>對傳入的url加入cookie並取得回傳的html</h5>
```python
herf = url
headers = {
    'User-Agent': 'XXXXXX',
    'Cookie': 'XXXXXX'
}
session = requests.Session()
response = session.get(herf, headers=headers)
```
<h5>Beautifulsoup初始化</h5>
```python
soup = BeautifulSoup(response.text, "html.parser")
sel = soup.find_all('a', href='#')
```
<h5>篩選出檔案代碼</h5>
```python
for s in sel:
    if s.attrs['onclick'] != 'More();':  
        code = (s.attrs['onclick'])[29:35:1] # 取出串列中29~35個（六碼）
```
<h5>請求html並寫入檔案</h5>
```python
file = requests.get('https://ican.tcu.edu.tw/ican5/Download.ashx?fileid=%s' % code)
    with open('/Users/jing/Downloads/%s題目.docx' % localltime, 'wb') as f:  
        f.write(file.content)
```
<h5>調用外部指令打開下載的檔案</h5>
```python
os.system("open /Users/jing/Downloads/%s題目.docx" % localltime)
```


<h2>傳訊（Line Notify)</h2>
<h5>格式化需要的Header</h5>
```python
header = {"Authorization": "Bearer " + token}
```
<h5>param字典 key->value => message->要傳送的話</h5>
```python
param = {'message': message}
```
<h5>通過對https://notify-api.line.me/api/notify 通過POST傳送Line訊息</h5>
```python
requests.post("https://notify-api.line.me/api/notify", headers=header, params=param)***  
```
<h5>回傳POST的html狀態code</h5>
```python
r.status_code
```