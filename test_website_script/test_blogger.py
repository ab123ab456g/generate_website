from bs4 import BeautifulSoup
import requests



class TestWebiste(object):
	"""docstring for TestWebiste
		goal : Use this class to test all flask build website
		input: website url

	"""
	def __init__(self, urlList, contentDict):
		self.urlList = urlList
		self.contentDict = contentDict
		self.l = len(urlList)
		self.Need = False
		self.SetHowItWork()

	def SetHowItWork(self):
		if self.l != len(self.contentDict):
			self.howItWork  = False
		else:
			self.howItWork = True

	def checkAllUrlWork(self):
		if self.howItWork:
			for i in range(self.l):
				url = self.urlList[i]
				self.checkUrlWork(url)
		else:
			print('url and content length not equal')

	def checkUrlWork(self, url):
		if self.howItWork:
			html_obj = requests.get(url)
			soup = BeautifulSoup(html_obj.text, 'html.parser')
			content = self.contentDict[url]
			if soup.h1.get_text() == content:
				if self.Need:
					print( content + ' Ok')
			else:
				print(content + ' Fail')

	def ChangeNeed(self):
		if self.Need:
			self.Need = False
		else:
			self.Need = True

urlList = []
urlList.append('http://127.0.0.1:5000')
urlList.append('http://127.0.0.1:5000/home')
urlList.append('http://127.0.0.1:5000/index')
urlList.append('http://127.0.0.1:5000/login')
urlList.append('http://127.0.0.1:5000/registor')
urlList.append('http://127.0.0.1:5000/user/test_user')
urlList.append('http://127.0.0.1:5000/edit')
urlList.append('http://127.0.0.1:5000/404')
urlList.append('http://127.0.0.1:5000/500')

contentList = []
contentList.append('home')
contentList.append('home')
contentList.append('home')
contentList.append('login')
contentList.append('registor')
contentList.append('user')
contentList.append('edit profile')
contentList.append('404')
contentList.append('500')


contentDict = dict(zip(urlList,contentList))
t = TestWebiste(urlList, contentDict)
t.checkAllUrlWork()