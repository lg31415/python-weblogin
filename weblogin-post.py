# coding=utf8
# !/usr/bin/env python

import httplib
import sys
import time
import re
import socket
import urllib

timeout = 60
socket.setdefaulttimeout(timeout)


def PostIPMI(user,password, ipaddr):
    httpClient = None
    try:
        params = urllib.urlencode({'name':user,
                                   'pwd': password})

        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Connection": "keep-alive",
                   }
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/login.cgi", params, headers)

        response = httpClient.getresponse()
        #         print response.status
        #         print response.reason
        #         print response.read()
        #         print response.getheaders()
        cookie = response.getheader('Set-Cookie')
        cookie = re.split("[;,]", cookie)[3]
        #################################################
        paramsdel1 = urllib.urlencode({'mode': 'delete',
                                    'ruleno': '1',
                                    'time_stamp': 'Wed20Dec%2030%202015%2013%3A18%3A08%20GMT%2B0800'
                                    })
        params1 = urllib.urlencode({'mode': 'add',
                                    'ruleno': '1',
                                    'ipinfo': '114.80.124.182/32',
                                    'policy': 'ACCEPT',
                                    'time_stamp': 'Wed20Dec%2030%202015%2013%3A18%3A08%20GMT%2B0800'
                                    })
        params2 = urllib.urlencode({'mode': 'add',
                                    'ruleno': '2',
                                    'ipinfo': '10.0.0.0/8',
                                    'policy': 'ACCEPT',
                                    'time_stamp': 'Wed20Dec%2030%202015%2013%3A18%3A08%20GMT%2B0800'
                                    })
        params3 = urllib.urlencode({'mode': 'add',
                                    'ruleno': '3',
                                    'ipinfo': '115.231.111.0/24',
                                    'policy': 'ACCEPT',
                                    'time_stamp': 'Wed20Dec%2030%202015%2013%3A18%3A08%20GMT%2B0800'
                                    })
        params4 = urllib.urlencode({'mode': 'add',
                                    'ruleno': '4',
                                    'ipinfo': '113.215.9.0/24',
                                    'policy': 'ACCEPT',
                                    'time_stamp': 'Wed20Dec%2030%202015%2013%3A18%3A08%20GMT%2B0800'
                                    })
        params4 = urllib.urlencode({'mode': 'add',
                                    'ruleno': '5',
                                    'ipinfo': '116.211.105.0/24',
                                    'policy': 'ACCEPT',
                                    'time_stamp': 'Wed20Dec%2030%202015%2013%3A18%3A08%20GMT%2B0800'
                                    })
        params4 = urllib.urlencode({'mode': 'add',
                                    'ruleno': '6',
                                    'ipinfo': '0.0.0.0/0',
                                    'policy': 'DROP',
                                    'time_stamp': 'Wed20Dec%2030%202015%2013%3A18%3A08%20GMT%2B0800'
                                    })
        # init headers
        headers1 = {"Content-type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "X-Requested-With": "XMLHttpRequest",
                    "X-Prototype-Version": "1.5.0",
                    'Cookie':  cookie +"; mainpage=configuration; subpage=config_ip_ctrl;langSetFlag=0; language=English;"
                    }

        # send request1
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/config_ip_ctrl.cgi", paramsdel1, headers1)
        time.sleep(5)
        # send request2
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/config_ip_ctrl.cgi", paramsdel1, headers1)
        time.sleep(5)
        # send request2
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/config_ip_ctrl.cgi", paramsdel1, headers1)
        time.sleep(5)
        # send request3
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/config_ip_ctrl.cgi", params1, headers1)
        time.sleep(5)
        # send request4
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/config_ip_ctrl.cgi", params2, headers1)
        time.sleep(5)
        # send request5
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/config_ip_ctrl.cgi", params3, headers1)
        time.sleep(5)
        # send request6
        httpClient = httplib.HTTPConnection(ipaddr, 80, timeout=30)
        httpClient.request("POST", "/cgi/config_ip_ctrl.cgi", params4, headers1)
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

user=sys.argv[1]
password=sys.argv[2]
ipaddr=sys.argv[3]
PostIPMI(user,password,ipaddr)

