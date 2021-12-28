# TopCom

The COVID dataset (Data/covid19-rumor-dataset) can be used for COVID-19 related rumor detection task.

This dataset is collected from Sina Weibo from 1st Jan to 30th in Chinese, which contains microblogs and corresponding comments in Chinese.

The data is organized as follows:

1. each line consists of a microblog, corresponding comments and its ground truth label (rumor or nonrumor)
2. Formats: microblog ###### comment 1 \t comment 2 \t ... comment n ###### label

Additionally, both microblogs and comments have gone through the word segmentation procedure, so the texts are in the format of " word1 word2 ..."
