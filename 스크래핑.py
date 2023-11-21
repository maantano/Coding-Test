# import requests
# from bs4 import BeautifulSoup

# # 스크래핑할 웹페이지의 URL
# url = 'https://www.teamblind.com/kr/company/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90'

# # requests를 사용하여 웹페이지의 HTML 내용을 가져옴
# response = requests.get(url)
# print('response ===>',response)
# # BeautifulSoup을 사용하여 HTML을 파싱
# soup = BeautifulSoup(response.text, 'html.parser')
# print('soup ===>',soup)

# # 스크래핑하고자 하는 요소의 CSS 선택자를 지정하여 가져옴
# elements = soup.select('.container .inner .img img')


# # 가져온 요소를 출력
# # print('????')
# print('elements ====>',elements)
# for element in elements:
#     print('element.text ===>',element.text)

import requests
from bs4 import BeautifulSoup

# 스크래핑할 웹페이지의 URL
url = 'https://www.jobplanet.co.kr/search?query=%EB%8D%94%EC%A1%B4%EB%B9%84%EC%A6%88%EC%98%A8'

# requests를 사용하여 웹페이지의 HTML 내용을 가져옴
response = requests.get(url)
# print('response ===>',response)
# BeautifulSoup을 사용하여 HTML을 파싱
soup = BeautifulSoup(response.text, 'html.parser')
# print('soup ===>',soup)

# 스크래핑하고자 하는 요소의 CSS 선택자를 지정하여 가져옴
elements = soup.select('.jpcont_lft .jpcont_wrap .is_company_card .llogo img')


# 가져온 요소를 출력
# print('????')
print('elements ====>',elements[0])
for element in elements:
    print('element.text ===>',element.text)

