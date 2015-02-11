import json
import urllib2, urllib, string
 
access_token = '<Put your access Token here>'
 
def GetJsonResponse(requestUrl, content = None):
        request = urllib2.Request(requestUrl)
        response = urllib2.urlopen(request, content)
        result = json.load(response)
        return result
 
def MakeComment(messageId, content):
        url = 'https://graph.facebook.com/' + messageId + '/comments'
        print url
        formPosts = {}
        formPosts['access_token'] = access_token
        formPosts['message'] = content
        data = urllib.urlencode(formPosts)
        print data
        f = urllib.urlopen(url, data)
        print f.read()
        
 
feedUrl='https://graph.facebook.com/me/feed?access_token=' + access_token + '&limit=10'
'''
To limit 10 number of feeds at a time.
'''
 
response = GetJsonResponse(feedUrl)
for counter in range(0, 10):
        if ('message' in response['data'][counter]) and \
           (string.find(response['data'][counter]['message'].lower(), 'happy') != -1) \
           and ('comments' not in response['data'][counter]):
                thanks_message = 'Thanks a lot :)'
                message_id = response['data'][counter]['id']
                print message_id
                MakeComment(message_id, thanks_message)
