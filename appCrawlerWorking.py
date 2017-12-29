import requests, bs4, os, datetime

def getData(url):

	try:
		res = requests.get(url, timeout=30)
	except Exception as e:
		print("Timeout of request")
		print("For url: "+url)
		return '-1', False

	print(str(res.status_code)),

	if res.status_code == requests.codes.ok:
		doc = bs4.BeautifulSoup(res.text, "html.parser")
		item = doc.select("#mainContent .description-right")
		myItem = item[0].getText().strip()
		if myItem[0]=='M':
			splitItems = myItem.splitlines()
			print(str(int(splitItems[1])+int(splitItems[5])))
			print(url)
			print(' ')
			return str(int(splitItems[1])+int(splitItems[5])), True

		else:
			print(myItem)
			print(url)
			print(' ')
			return myItem,True
	else:
		return '-1', True

def gotFile(relPath, cnt):

	absPath = os.path.abspath(relPath)
	count = 0

	if os.path.isfile(absPath):
		urlFile = open(absPath)
		base = os.path.basename(absPath)
		file = base[:-4] + "-" + str(datetime.date.today()) + '.csv'
		saveFile = open(os.path.join(absPath[:-(len(str(base)))],file), "a+")
		if cnt == 0:
			saveFile.write(str(datetime.date.today())+'\n')
		for url in urlFile.readlines():
			if url != '' and count >= cnt:
				urlTrim = url[:-1]
				downloads,bool = getData(urlTrim)
				if bool:
					saveFile.write(str(downloads)+'\n')

				else:
					urlFile.close()
					saveFile.close()
					return 1, str(os.path.join(absPath[:-(len(str(base)))],file)), count

			count += 1
		urlFile.close()
		saveFile.close()
		return 1, str(os.path.join(absPath[:-(len(str(base)))],file)), count

	else:
		return 0, absPath + " does not exist", 0

if __name__ == "__main__":
	path = input("Enter the relative path of file storing URLs : ")
	count = input("Enter the last count: ")
	k,fp,count = gotFile(path, int(count))

	if k == 0:
		print("Couldn't not write the CSV file. Err: "+fp)

	else:
		print("The data is stored in "+fp)
		print("Last Count = "+str(count))
