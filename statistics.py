import re
import html
import json
import requests

request_data = {
	"MIME Type": "application/x-www-form-urlencoded",
	"period": "year",
	"year": "2021",
	"app[applications]": "applications",
	"open[open]": "open",
	"off[offers]": "offers",
	"winter[winter]": "winter",
	"acc[acceptances]": "acceptances",
	"summer[summer]": "summer",
	"what": "course",
	"courses[]": "Computer Science",
	"college": "Churchill College",
	"course": "Computer Science",
	"group": "college",
	"op": "Show graph",
	"form_build_id": "form-iBfHXjLV5ynTpTvfrC6T6_9VlgiQBtFaxOiKnlISU70",
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


for i in range(29):
	output += f"\n{colleges[i]}\t{data[0]['data'][i]}\t{data[1]['data'][i]}\t{data[2]['data'][i]}\t{data[3]['data'][i]}\t{data[4]['data'][i]}\t{data[5]['data'][i]}"

print(output)
