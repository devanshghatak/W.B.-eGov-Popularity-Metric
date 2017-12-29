from pytrends.request import TrendReq

def gotFile(relPath, trend):
	absPath = os.path.abspath(relPath)

    if os.path.isfile(absPath):
        file = open(absPath,'r')
    else:
        return False

    newPath = os.path.join(os.path.dirname(absPath),str(datetime.date.today()))
    if not os.path.isdir(newPath):
        os.makedirs(newPath)

	# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
	trend.build_payload(kw_list=file.readlines())

	# Interest Over Time
	interest_over_time_df = pytrend.interest_over_time()

	# Interest by Region
	interest_by_region_df = pytrend.interest_by_region()

	# Related Queries, returns a dictionary of dataframes
	related_queries_dict = pytrend.related_queries()

	# Get Google Hot Trends data
	trending_searches_df = pytrend.trending_searches()

	# Get Google Top Charts
	top_charts_df = pytrend.top_charts(cid='actors', date=201611)

	# Get Google Keyword Suggestions
	suggestions_dict = pytrend.suggestions(keyword='pizza')

if __name__ == "__main__":
	path = input("Enter the relative path of file storing keywords: ")
	emailID = input("Enter your email ID: ")
	passW = input("Enter your password: ")
	google_username = emailID
	google_password = passW
	path = ""

	pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
	k,fp = gotFile(path, pytrend)

	if k == 0:
		print("Couldn't not write the CSV file. Err: "+fp)

	else:
		print("The data is stored in "+fp)
