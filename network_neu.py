import requests


url_1 = 'http://ipgw.neu.edu.cn/include/auth_action.php'
data_1 = {
    'action': 'logout',
    'ajax': '1',
    'password': '294411',
    'username': '20163223'
}
url_2 = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&'
data_2 = {
    'ac_id':'1',
    'action': 'login',
    'nas_ip':'',
    'password': '294411',
    'save_me': '0',
    'url':'',
    'user_ip':'',
    'user_mac': '',
    'username': '20163223'
}
header = {
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 58.0.3029.110Safari / 537.36Edge / 16.16299',
    'Referer': 'http: // ipgw.neu.edu.cn / srun_portal_pc.php?ac_id = 1 &'
}

requests.post(url_1,headers = header,data= data_1)
requests.post(url_2,headers = header,data= data_2)
print('success')
