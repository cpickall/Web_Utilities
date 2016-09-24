import json
import urllib
import urllib2

# Replace USERNAME/BOARDNAME and ACCESS_TOKEN with your info
# See https://developers.pinterest.com/tools/api-explorer/
jsonResponse = json.load(urllib2.urlopen('https://api.pinterest.com/v1/boards/USERNAME/BOARDNAME/pins/?ACCESS_TOKEN&fields=image%2Cid'))
jsonData = jsonResponse['data']

# Download all the images. They'll save into the directory you run the script from
for item in jsonData:
   url = item['image']['original']['url']
   picId = item['id']
   urllib.urlretrieve(url, picId+".jpg")

