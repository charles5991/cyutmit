from django.test import TestCase
from django.core.urlresolvers import reverse
from news.models import News
from main.tests.util import createSuperuser


class NewsViewTestCase(TestCase):


    def setUp(self):
        self.maxNumNews = 10    # Max number of news in a page
        self.numNews = 5
        for i in range(self.numNews):    # Create 5 news
            News.objects.create(title='標題'+str(i))
        createSuperuser()
        

    def test最新消息使用正確範本(self):
        with self.assertTemplateUsed('news/news.html'):
            response = self.client.get(reverse('news:news'))
            self.assertEqual(response.status_code, 200)


    def test最新消息頁面顯示最多10筆資料(self):
        response = self.client.get(reverse('news:news'))
        self.assertContains(response, '<tr>', self.numNews+1)    # 加上一列表格標題
        for i in range(self.numNews, self.numNews+self.maxNumNews):  # Create 10 more news
            News.objects.create(title='標題'+str(i))
        response = self.client.get(reverse('news:news'))
        self.assertContains(response, '<tr>', self.maxNumNews+1)    # 加上一列表格標題


    def test點擊最新消息回覆正確範本(self):
        news = News.objects.first()
        with self.assertTemplateUsed('news/viewNews.html'):
            response = self.client.get(reverse('news:viewNews', args=(news.id, )))
            self.assertEqual(response.status_code, 200)


    def test點擊某個消息回覆正確資料(self):
        news = News.objects.create(title='標題999')
        response = self.client.get(reverse('news:viewNews', args=(news.id, )))
        self.assertContains(response, '標題999')


    def test搜尋關鍵詞回覆正確資料(self):
        News.objects.create(title='消息標題111', content='內容111')
        News.objects.create(title='最新222', content='消息內容222')
        response = self.client.get(reverse('news:searchNews'), {'searchTerm':'消息'})
        self.assertContains(response, '標題111')
        self.assertContains(response, '最新222')


    def test管理者未登入無法新增消息(self):
        response = self.client.get(reverse('news:addNews'))
        self.assertEqual(response.status_code, 302)
            

    def test管理者點擊新增消息回覆正確範本(self):
        self.client.login(username='admin', password='admin')
        with self.assertTemplateUsed('news/addNews.html'):
            response = self.client.get(reverse('news:addNews'))
            self.assertEqual(response.status_code, 200)


    def test管理者新增消息表單空白標題或內容會顯示錯誤訊息(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('news:addNews'), data={'title':'標題'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('news:addNews'), data={'content':'內容'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('news:addNews'))
        self.assertIn('必填', response.content.decode('utf-8'), 2)


    def test管理者新增消息表單可正確儲存消息(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('news:addNews'), data={'title':'title', 'content':'content'})
        self.assertNotIn('必填', response.content.decode('utf-8'))
        news = News.objects.filter(title='title', content='content')
        self.assertTrue(news)


    def test非管理者無法修改消息(self):
        news = News.objects.first()
        response = self.client.get(reverse('news:editNews', args=(news.id, )))
        self.assertEqual(response.status_code, 302)  # Go to login page

    
    def test管理者點擊某消息回覆正確範本(self):
        self.client.login(username='admin', password='admin')
        news = News.objects.first()
        with self.assertTemplateUsed('news/editNews.html'):
            response = self.client.get(reverse('news:editNews', args=(news.id, )))
            self.assertEqual(response.status_code, 200)

    
    def test管理者修改消息不能有空白欄位(self):
        self.client.login(username='admin', password='admin')
        news = News.objects.create(title='標題', content='內容')
        response = self.client.post(reverse('news:editNews', args=(news.id, )), data={'title':'改標題'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('news:editNews', args=(news.id, )), data={'content':'改內容'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('news:editNews', args=(news.id, )))
        self.assertIn('必填', response.content.decode('utf-8'), 2)


    def test管理者可正確修改消息(self):
        self.client.login(username='admin', password='admin')
        news = News.objects.create(title='標題', content='內容')
        response = self.client.post(reverse('news:editNews', args=(news.id, )), data={'title':'改標題', 'content':'改內容'})
        self.assertEqual(response.status_code, 302)  # Post-redirect-get
        news = News.objects.filter(title='改標題', content='改內容')
        self.assertTrue(news)


    def test管理者使用GET方法不可刪除消息(self):
        self.client.login(username='admin', password='admin')
        news = News.objects.create(title='標題', content='內容')
        self.client.get(reverse('news:deleteNews', args=(news.id, )))
        news = News.objects.filter(title='標題', content='內容')
        self.assertTrue(news)


    def test管理者可刪除消息(self):
        self.client.login(username='admin', password='admin')
        news = News.objects.create(title='標題', content='內容')
        response = self.client.post(reverse('news:deleteNews', args=(news.id, )))
        self.assertEqual(response.status_code, 302)  # Post-redirect-get
        news = News.objects.filter(title='標題', content='內容')
        self.assertFalse(news)


    def test最新消息分頁(self):
        for i in range(20):    # Totally 25 news
            News.objects.create(title='標題'+str(i), content='內容'+str(i))
        response = self.client.get(reverse('news:news'))
        self.assertNotIn('上一頁', response.content.decode('utf-8'))
        self.assertIn('下一頁', response.content.decode('utf-8'), 1)
        response = self.client.get(reverse('news:news')+'?page=2')
        self.assertIn('上一頁', response.content.decode('utf-8'), 1)
        self.assertIn('下一頁', response.content.decode('utf-8'), 1)
        response = self.client.get(reverse('news:news')+'?page=3')
        self.assertIn('上一頁', response.content.decode('utf-8'), 1)
        self.assertNotIn('下一頁', response.content.decode('utf-8'))
        
        