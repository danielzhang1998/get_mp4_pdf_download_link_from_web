import re, requests, ssl

headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Accept': 'text/html'
}

def open_url(url):
    # encoding: utf-8
    ssl._create_default_https_context = ssl._create_unverified_context
    html = requests.get(url,headers=headers).text # 获取url内容
    #print(html)
    return html

def get_link(url):
    html = open_url(url)
    m = r'<a href="([^"]+\.pdf|[^"]+\.mp4)"'
    match = re.findall(m, html)
    for each in range(len(match)):
        new = match[each].split('./')[-1]
        match[each] = 'https://teaching.csse.uwa.edu.au/units/CITS3003/' + new
        
    #print (match)
    with open('./result.txt', 'w') as f: #修改文件路径为自己的指定路径
        for each in match:
            f.write(each)
            f.write('\n')
    return match

if __name__ == '__main__':
    get_link('https://teaching.csse.uwa.edu.au/units/CITS3003/index.php?fname=lectures')