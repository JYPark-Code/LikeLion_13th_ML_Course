from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# url = 'https://www.amazon.com/HP-24-inch-Computer-Processor-24-dd0010/dp/B0849GZCQR/ref=sr_1_2?dchild=1&keywords=computer&qid=1631254252&sr=8-2'
url = "https://www.amazon.com/HP-24-inch-Computer-Processor-24-dd0010/product-reviews/B0849GZCQR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)

# ### 첫번째 리뷰 버튼 : //*[@id="acrCustomerReviewText"]
# first_review = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
# first_review.click()
#
# ### 두번째 리뷰 선택 : //*[@id="reviews-medley-footer"]/div[2]/a
# second_review = driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')
# second_review.click()

# 페이지 정보를 넘겨 받고 하나의 리뷰 가져오기
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
# print(soup.title)

txt = soup.find_all("span", class_="a-size-base review-text review-text-content")
# print(txt[0].text.strip())

all_review = []
for one in txt:
    tmp = one.text
    tmp.replace("Read more", "")
    all_review.append(tmp.strip())

# 8개 리뷰
# print(all_review[:8])

# .csv 파일 만들기
# dict_review = {"제품댓글": all_review}
# rvw_df = pd.DataFrame(dict_review)
# rvw_df.to_csv("아마존제품_댓글.csv", index=False)

# print(len(all_review), all_review)

next_page = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
next_page.click()

page2 = driver.page_source
soup2 = BeautifulSoup(page2, 'lxml')
txt2 = soup2.find_all("span", class_="a-size-base review-text review-text-content")

for one in txt2:
    tmp = one.text
    tmp.replace("Read more", "")
    all_review.append(tmp.strip())

# print(len(all_review), all_review)

dict_review = {"제품댓글": all_review}
rvw_df = pd.DataFrame(dict_review)
rvw_df.to_csv("아마존제품_p12_댓글.csv", index=False)