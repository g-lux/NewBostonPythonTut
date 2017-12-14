from urllib import request

url = 'http://www.sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv'


def download_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'data.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_data(url)
