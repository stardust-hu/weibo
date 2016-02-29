#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#          佛祖保佑       永无BUG

#coding:utf-8
import requests
import json
import time

class weibo:
	def __init__(self, username, password):
		self.__username = username
		self.__password = password
		try:
			self.cookies = self.__login__().cookies
			self.status = True
		except:
			self.cookies = None
			self.status = False

	def __login__(self):
		url = r'https://passport.weibo.cn/sso/login'
		header = {
			'Host':'passport.weibo.cn',
			'User-Agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding':'gzip, deflate',
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			'Pragma':'no-cache',
			'Cache-Control':'no-cache',
			'Referer':'https://passport.weibo.cn/signin/login',
			'Connection':'keep-alive'}
		post_data = {
			'username':'%s' % self.__username,
			'password':'%s' % self.__password,
			'savestate':'1',
			'ec':'0',
			'pagerefer':'',
			'entry':'mweibo',
			'loginfrom':'',
			'client_id':'',
			'code':'',
			'qq':'',
			'hff':'',
			'hfp':''}
		try:
			response = requests.post(url, data = post_data, headers = header)
			print u'登陆成功\nuid:'+json.loads(response.text)['data']['uid']
			return response
		except:
			print u'登录失败'
			return None

	def update(self, text):
		url = r'http://m.weibo.cn/mblogDeal/addAMblog'

		header = {
			'Host':'m.weibo.cn',
			'User-Agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25',
			'Accept':'application/json, text/javascript, */*; q=0.01',
			'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding':'gzip, deflate',
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			'X-Requested-With':'XMLHttpRequest',
			'Referer':'http://m.weibo.cn/mblog',
			'Connection':'keep-alive'
		}

		post_data = {
			'content':text
		}
		try:
			response = requests.post(url = url, data = post_data, headers = header, cookies = self.cookies)
			print json.loads(response.text)['msg']
			return response
		except:
			try:
				time.sleep(10)
				try:
					self.cookies = self.__login__().cookies
				except:
					self.cookies = None
					return None
				response = requests.post(url = url, data = post_data, headers = header, cookies = self.cookies)
				print json.loads(response.text)['msg']
				return response
			except:
				print u'发送失败'
				return None

if __name__ == '__main__':
	username = raw_input('username:')
	password = raw_input('password:')
	w = weibo(username, password)
	while(1):
		t = time.localtime()	
		if(w.status == False):
			print u'已退出'
			return 0
		if ((t.tm_min == 0) and (t.tm_sec == 0)):
			text = u'#打更机器人#当前时间%d年%d月%d日%d时%d分%d秒' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
			w.update(text)
			time.sleep((t_unix+60*60)+2 - time.time())	# 59*60-10


