import sys
from urllib2 import *
import json
import urllib

MY_API_KEY = "AIzaSyDFldkruISVlid8C5iK774WFsrLgpMrSzY"

messageTitle = sys.argv[1]
messageBody = sys.argv[2]
# print(sys.argv[1])
# print(sys.argv[2])
# sys.argv[2]

data={
  "to" : "/topics/my_little_topic",
  "notification" : {
      "body" : messageBody,
      "title" : messageTitle
#     "icon" : "ic_cloud_white_48dp"
  }
}

dataAsJSON = json.dumps(data)

request = Request(
  "https://gcm-http.googleapis.com/gcm/send",
  dataAsJSON,
  { "Authorization" : "key="+MY_API_KEY,
    "Content-type" : "application/json"
  }
)

print urlopen(request).read()
