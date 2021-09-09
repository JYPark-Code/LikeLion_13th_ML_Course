from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time
url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=187348&target=after"
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
# print(soup.title)

eval_box = soup.find_all("td", class_="title")

full_comment = []
for i in range(1, 50, 1):
    page_url = url + f"&page={i}"
    page = urlopen(page_url)
    soup = BeautifulSoup(page, "html.parser")
    eval_box = soup.find_all("td", class_="title")

    # comments = []
    for comment in eval_box:
        each_comment = (list(comment.children)[6]).strip()
        # comments.append(each_comment)
        full_comment.append(each_comment)
    time.sleep(0.1)
# print(full_comment)
print(len(full_comment))

dict_dat = {"영화댓글": full_comment}
dat = pd.DataFrame(dict_dat)
dat.to_csv("샹치댓글(50).csv", index=False)
dat.to_excel("샹치댓글(50).xlsx", index=False)