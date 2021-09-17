import wordcloud
from wordcloud import WordCloud, STOPWORDS
from matplotlib import rc
import matplotlib.pyplot as plt

## 파일 읽기 - open()
f = open("2021-09-08_앱스토어_사용자_수_순위_모바일인덱스.csv", encoding="utf-8")
text = f.read()
f.close()

### 금지 단어
NGwords = ['Corp', 'Inc', 'Co', 'Ltd', 'Corporation', 'LLC']
stopwords = set(STOPWORDS)
for NGword in NGwords:
    stopwords.add(NGword)



rc("font", family="NanumGothic")

wc = WordCloud("./D2coding.ttf",
                   max_words=1000,
                   relative_scaling=0.2,
                   stopwords=stopwords)

wc.generate(text)

plt.figure(figsize=(20, 20))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

