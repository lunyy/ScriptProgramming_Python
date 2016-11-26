import urllib.request
import re

def main():
    url = "http://cs.armstrong.edu/liang/data/Lincoln.txt"
    # URL 저장
    web_page = urllib.request.urlopen(url)
    # 해당 url에서 data를 받아옴.
    string = web_page.read().decode()
    # html 코드의 body 부분의 text를 가져옴.
    string = re.findall(r"[\w']+",string)
    # re.findall 함수를 이용해 알파뉴메릭 단어만 가져와 리스트로 만듦.
    print(len(string))
    # 문자열 리스트의 길이 출력
    web_page.close()

main()