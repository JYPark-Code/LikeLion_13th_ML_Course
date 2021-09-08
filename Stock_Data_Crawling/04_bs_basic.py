from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = "https://finance.naver.com/sise/"
# page = urlopen(url) # 웹 URL로부터 페이지를 가져오기
page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <img height="300" src="dog_01.jpg" width="500"/>
    <p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
    <p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
    <p class="p3"> [영역 1] 강아지 사진과 네이버 링크 </p>
    <p id="p4"> [영역 1] 간단한 나의 홈페이지를 만들다.</p>
    <p class="p3"> [영역 1] 강아지 사진과 네이버 링크222 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <img height="300" src="dog_01.jpg" width="500"/>
    <p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
    <p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
    <p class="p3"> [영역 2] 강아지 사진과 네이버 링크 </p>
    <p id="p4"> [영역 2] 간단한 나의 홈페이지를 만들다.</p>
    <p class="p3"> [영역 2] 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''

# soup = BeautifulSoup(page, 'lxml')
# print(soup.title)

# soup.태그명 => 해당되는 요소의 정보를 가져온다.
# print(soup.title)
# print(soup.body)
# print(soup.div)
# print(soup.img)
# print(soup.a)


# print(soup.a.text)
# print(soup.div.p.text)

# id, class을 활용해서 정보가져오기 - 하나의 요소 (find)
# print(soup.find("p", id="p4"))
# # id, class을 활용해서 정보가져오기 - 하나의 요소 (find_all)
# print(soup.find_all("p"))

# find, find_all
soup = BeautifulSoup(page, 'lxml')
# naver 정보
# print(soup.find("a"))
# print(soup.find("a" , href="https://www.naver.com/").text)
# # 모든 a 태그 정보 가져오기
# a_tag_list = (soup.find_all("a"))
# print(a_tag_list[1].text)
# print(soup.find_all("div"))
# print(soup.find("p", id="p4"))
#
# # 실습 2-3
# # 한줄 코드
# # class 정보를 이용해서 p3, 2번쨰 요소 text 가져오기
# print( soup.find_all("p", class_="p3")[1].text )
#
# #추가 링크 가져오기
# print( soup.find_all("a", href=True))
#
# # 구글 정보 가져오기
# print(a_tag_list[1].text)

one_info = soup.find_all("div")
print(len(one_info))