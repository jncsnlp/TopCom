import pandas as pd
import jieba
# jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持


# 创建停用词列表
def stopwordslist():
	stopwords = [line.strip('\n') for line in open('stopwords.txt',encoding='UTF-8').readlines()]
	return stopwords

# 分词+去停用词
def textProcess(text,stopwords):
	split_text = list(jieba.cut(text.strip(),use_paddle=True))
	# print(split_text)
	# 创建一个停用词列表
	# stopwords = stopwordslist()
	# 输出结果为outstr
	outstr = ''
	# 去停用词
	for word in split_text:
		word=word.strip()
		if word not in stopwords and len(word) < 10:
			outstr += word
			outstr += " "
	# print(outstr)
	return outstr

def generateoneline(content, comments, label, stopwords):
	content = textProcess(content, stopwords)
	oneline = content+"######"
	for idx in range(0,2):
		comment = textProcess(comments[idx], stopwords)
		oneline = oneline+comment+"\t"
	comment = textProcess(comments[2], stopwords)
	oneline = oneline+comment+"######"+label+"\n"
	return oneline

if __name__ == '__main__':
	# rmrdata_pt="covid-rumor/rumor.csv"
	rmrdata_pt="covid-rumor/rumor.xlsx"
	# nonrmrdata_pt="covid-rumor/nonrumor.csv"
	# nonrmrdata_pt="covid-rumor/nonrumor-random.csv"
	covid_pt="covid.txt"
	keywords=["肺炎","新冠","病毒","武汉","湖北","封城","确诊","疑似","疫情","钟南山","防控","口罩","感染","疫","肺","染"]


	rmrdf = pd.read_excel(rmrdata_pt)
	# rmrdf = pd.read_csv(rmrdata_pt)
	# nonrmrdf = pd.read_csv(nonrmrdata_pt)

	stopwords = stopwordslist()
	# print(rmrdf)

	with open(covid_pt, mode="w", encoding="utf-8") as covid_file:
		count = 0
		lineidxs = rmrdf.index.values
		# print(lineidxs)
		for idx in lineidxs:
			try:
				# 微博正文
				content = rmrdf.iloc[idx,2].split(":")[1].split("                                  ")[0].split("                      ")[0].split("              ")[0].split("             ")[0]
				# print(content)
				# 关键词筛选
				filter_bool = False
				for keyword in keywords:
					filter_bool = filter_bool or (keyword in content)
				if filter_bool:
					# 获取评论
					comments = rmrdf.iloc[idx,9].split(";")
					oneline = generateoneline(content, comments, "rumor", stopwords)
					# print(oneline)
					covid_file.write(oneline)

					count += 1
			except:
				print("===skip===")
		print("The number of Filtered COVID-19 Rumors ："+str(count))

