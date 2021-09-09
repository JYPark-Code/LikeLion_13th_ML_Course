import wordcloud
from wordcloud import WordCloud, STOPWORDS
from matplotlib import rc
import matplotlib.pyplot as plt


# print(wordcloud.__version__)

## 파일 읽기 - open()
f = open("샹치댓글(50).csv", encoding="utf-8")
text = f.read()
print(text)
f.close()

rc("font", family="NanumGothic")

wcloud = WordCloud("./D2coding.ttf",
                   max_words=1000,
                   relative_scaling=0.2).generate(text)

plt.figure(figsize=(12, 12))
plt.imshow(wcloud, interpolation="bilinear")
plt.axis("off")
plt.show()