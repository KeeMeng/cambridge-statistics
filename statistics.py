import re
import html
import json
import requests

# year = "2021"
# subject = "Computer Science"
year = input("Year: ")
subject = input("Subject: ")

# Don't change request data
request_data = {
	"MIME Type": "application/x-www-form-urlencoded",
	"period": "year",
	"year": year,
	"app[applications]": "applications",
	"open[open]": "open",
	"off[offers]": "offers",
	"winter[winter]": "winter",
	"acc[acceptances]": "acceptances",
	"summer[summer]": "summer",
	"what": "course",
	"courses[]": subject,
	"college": "Churchill College",
	"course": subject,
	"group": "college",
	"op": "Show graph",
	"form_build_id": "form-rt9s6sYvkKyKQ0OY6uFSHzl1qlEc1ji2QagCWbv-RQA",
	"form_id": "cam_app_charts_my_form_1"
}

response = requests.post("https://www.undergraduate.study.cam.ac.uk/apply/statistics", request_data).text
# Post to get statistics of cambridge about subject in a specific year

stats = re.search("data-chart=\"(.*?)\"", response).group(1)
# Finds the data in the response (html file)

stats = html.unescape(stats)
# Escapes html characters

stats = json.loads(stats)
# Convert to json


colleges = stats["xAxis"][0]["categories"]

data = stats['series']

# Outputs a excel/sheets pasteable version of the data
output = "Colleges"
for i in range(6):
	output += "\t" + data[i]["name"]


for i in range(len(colleges)):
	output += f"\n{colleges[i]}\t{data[0]['data'][i]}\t{data[1]['data'][i]}\t{data[2]['data'][i]}\t{data[3]['data'][i]}\t{data[4]['data'][i]}\t{data[5]['data'][i]}"

print(output)
