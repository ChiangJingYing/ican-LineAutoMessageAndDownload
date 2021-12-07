import os
import time
import requests
from bs4 import BeautifulSoup

token = "no9tK0lpKIUAzHLV1dvjGsZMvt7mwwzOoVSFjl8q30h"  # LINE Notify token
classes = {1: '101UGNGE1A090205', 2: '1101UGNGE1A110500', 3: '1101UGNGE1A114000', 4: '1101UMNMI1A585200',
           5: '1101UGNGE1A582002', 6: '1101UMAAM1A108700', 7: '1101UMAAM1A315200', 8: '1101UMNMI1A210600',
           9: '1101UMNMI1A322000', 10: '1101UMNMI1A341200', 11: '1101UGNPE1A048900'}
classname = {1: '生命教育', 2: '休閒教育', 3: '地球科學', 4: '成規一實驗',
             5: '中文閱讀與書寫', 6: '生醫資訊導論', 7: '普通生物', 8: '計算機概論',
             9: '成規一', 10: '微積分', 11: '心肺體適能'}


def getHTML(ClassNumber):
    """""""""""""""""""""""""""
            取得目標html
    """""""""""""""""""""""""""
    herf = 'https://ican.tcu.edu.tw/ican5/TestBoard/TestList.aspx?cno=' + str(classes.get(ClassNumber))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
        'Cookie': 'cfid=courseindex10; _iCAN4_OPENCOURSE=1101UMNMI1A585200%7C%20%u7A0B%u5F0F%u898F%u5283%28%u4E00%29%u5BE6%u9A57%20Programming%20Design%20Lab%20%u2160%201A%7C%7CCourseDashboard.aspx%3Fcno%3D1101UMNMI1A585200; courseno=1101UMNMI1A585200; _iCAN4_FontSize=Small; _ShowHelper=N; .ASPXAUTH=5C062751089D4B2006A92EBAE22551A8BC96A8885592C59EEDF195D3E860FB56CEB9712F312A525BDA3F238036CA76C33444A3EDD92096513002BE4B970390F0EBD68E36CC79492D1BD16991D0DE7828B2548D2F86CA19EFF3E7C5332F8AC2F68AEF0C00817D93FA7266616F6302C7C55FE4B72B99963148D6FA5A693A8D46233DE8CC11FCB717F938B8E9C303002666; _Culture=zh-cht; .auth_tcu=48A763E10C02EEC2A21D8F04488AC856B4FB410346A8A58A220A85A4C7F7F0FAFC9611084D9CC874A93DE0CA85433077118EFFA3FB9FA6BB4E624797C29BC7546C79FA06D841CB4D53562F2118963DCEA6D4CF8D35BC0A11C48C27163AA5FED4BCE3A44EF392844963D900B34999D24EA9A2FC310138A9BD9BA0C904A515D4D111420E191B397E63EFBD2EC57A0242AD29A08863A406460921D7CC59A93BAFFD; ASP.NET_SessionId=5rrqeq2i5mx0jgs4evastjng; CAID=23CD2BF6C41ABA126480BED5D49684BE; _ga=GA1.3.1342182755.1637934336'
    }
    session = requests.Session()
    response = session.get(herf, headers=headers)
    separateNeedThings(response)


def getFileCood(url):
    localltime = time.strftime("%Y%m%d", time.localtime())  # 取得現在的時間並格式化成（YMD)
    herf = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
        'Cookie': 'cfid=courseindex10; _iCAN4_OPENCOURSE=1101UMNMI1A585200%7C%20%u7A0B%u5F0F%u898F%u5283%28%u4E00%29%u5BE6%u9A57%20Programming%20Design%20Lab%20%u2160%201A%7C%7CCourseDashboard.aspx%3Fcno%3D1101UMNMI1A585200; courseno=1101UMNMI1A585200; _iCAN4_FontSize=Small; _ShowHelper=N; .ASPXAUTH=5C062751089D4B2006A92EBAE22551A8BC96A8885592C59EEDF195D3E860FB56CEB9712F312A525BDA3F238036CA76C33444A3EDD92096513002BE4B970390F0EBD68E36CC79492D1BD16991D0DE7828B2548D2F86CA19EFF3E7C5332F8AC2F68AEF0C00817D93FA7266616F6302C7C55FE4B72B99963148D6FA5A693A8D46233DE8CC11FCB717F938B8E9C303002666; _Culture=zh-cht; .auth_tcu=48A763E10C02EEC2A21D8F04488AC856B4FB410346A8A58A220A85A4C7F7F0FAFC9611084D9CC874A93DE0CA85433077118EFFA3FB9FA6BB4E624797C29BC7546C79FA06D841CB4D53562F2118963DCEA6D4CF8D35BC0A11C48C27163AA5FED4BCE3A44EF392844963D900B34999D24EA9A2FC310138A9BD9BA0C904A515D4D111420E191B397E63EFBD2EC57A0242AD29A08863A406460921D7CC59A93BAFFD; ASP.NET_SessionId=5rrqeq2i5mx0jgs4evastjng; CAID=23CD2BF6C41ABA126480BED5D49684BE; _ga=GA1.3.1342182755.1637934336'
    }
    session = requests.Session()
    response = session.get(herf, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    sel = soup.find_all('a', href='#')
    for s in sel:
        if s.attrs['onclick'] != 'More();':  # 排除不知道為何出現的上傳更多『上傳更多』
            code = (s.attrs['onclick'])[29:35:1]  # 檔案代碼為六位數，取得JAVASCRIPT函式中的 code
            file = requests.get('https://ican.tcu.edu.tw/ican5/Download.ashx?fileid=%s' % code)
            with open('/Users/jing/Downloads/%s題目.docx' % localltime, 'wb') as f:  # 將檔案寫到『下載裡』檔名相同之後寫入會將之前的蓋掉
                f.write(file.content)
            os.system("open /Users/jing/Downloads/%s題目.docx" % localltime)


def separateNeedThings(response):
    """""""""""""""""""""""""""
       將取得的html擷取要的項目
    """""""""""""""""""""""""""
    soup = BeautifulSoup(response.text, "html.parser")
    sel = soup.find_all('td', style="width:4%;")
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
        formatMessage(message)  # 將串列送去格式化成要傳送的訊息


def formatMessage(message):
    """""""""""""""""""""""""""
            格式化傳入的串列
    """""""""""""""""""""""""""
    localltime = time.strftime("%Y/%m/%d", time.localtime())  # 取得現在的時間並格式化成（Y/M/D)
    if len(message) != 4:  # 若為繳交狀態，則增加一個"XD"以防後續判斷串列超出範圍
        message.append('XD')
    if message[3] != '已繳交' and message[3] != '未開始' and message[3] != '已逾期':  # 篩選為繳交的項目出來
        coutoggTime = time.mktime(time.strptime(message[2], '%Y/%m/%d %H:%M'))  # 結束日期秒數
        if localltime in message[1]:  # 去除無繳交狀態且已預期的項目
            messages = ('\n作業標題：' + message[0] + "\n起始日期：" + message[1] + '\n結束日期：' + message[2])
            getFileCood(message[3])
            Line_Notify(token, messages)


def Line_Notify(token, message):
    """""""""""""""""""""""""""
            傳Line給某人
    """""""""""""""""""""""""""
    header = {"Authorization": "Bearer " + token}
    param = {'message': message}
    r = requests.post("https://notify-api.line.me/api/notify", headers=header, params=param)  # 傳送訊息
    print(str(r.status_code) + message)  # r.status_code查看傳送結果
    if r.status_code == 200:
        exit()
    # print(message)
    time.sleep(1.5)  # delay 1.5 second.


if __name__ == '__main__':
    for i in range(5):
        time.sleep(30 * 60)
        getHTML(4)
    Line_Notify(token, '沒作業')
