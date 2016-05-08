from django.test import TestCase
from django.core.urlresolvers import reverse
from introduction.models import Introduction
from main.tests.util import createSuperuser


class introductionViewTestCase(TestCase):


    def setUp(self):
        self.maxNumNews = 10    # Max number of news in a page
        self.numNews = 5
        for i in range(self.numNews):    # Create 5 news
            Introduction.objects.create(title='標題'+str(i))
        createSuperuser()
        

    def test最新消息使用正確範本(self):
        with self.assertTemplateUsed('introduction/introduction.html'):
            response = self.client.get(reverse('introduction:introduction'))
            self.assertEqual(response.status_code, 200)

    def test點擊最新消息回覆正確範本(self):
        introduction = Introduction.objects.first()
        with self.assertTemplateUsed('introduction/viewIntroduction.html'):
            response = self.client.get(reverse('introduction:viewIntroduction', args=(introduction.id, )))
            self.assertEqual(response.status_code, 200)


    def test點擊某個消息回覆正確資料(self):
        introduction = Introduction.objects.create(title='標題999')
        response = self.client.get(reverse('introduction:viewIntroduction', args=(introduction.id, )))
        self.assertContains(response, '標題999')

    def test管理者未登入無法新增消息(self):
        response = self.client.get(reverse('introduction:addNews'))
        self.assertEqual(response.status_code, 302)
            

    def test管理者點擊新增消息回覆正確範本(self):
        self.client.login(username='admin', password='admin')
        with self.assertTemplateUsed('introduction/addIntroduction.html'):
            response = self.client.get(reverse('introduction:addIntroduction'))
            self.assertEqual(response.status_code, 200)


    def test管理者新增消息表單空白標題或內容會顯示錯誤訊息(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('introduction:addNews'), data={'title':'標題'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('introduction:addNews'), data={'content':'內容'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('introduction:addNews'))
        self.assertIn('必填', response.content.decode('utf-8'), 2)


    def test管理者新增消息表單可正確儲存消息(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('introduction:addNews'), data={'title':'title', 'content':'content'})
        self.assertNotIn('必填', response.content.decode('utf-8'))
        introduction = Introduction.objects.filter(title='title', content='content')
        self.assertTrue(introduction)


    def test非管理者無法修改消息(self):
        introduction = Introduction.objects.first()
        response = self.client.get(reverse('introduction:editIntroduction', args=(introduction.id, )))
        self.assertEqual(response.status_code, 302)  # Go to login page

    
    def test管理者點擊某消息回覆正確範本(self):
        self.client.login(username='admin', password='admin')
        introduction = Introduction.objects.first()
        with self.assertTemplateUsed('introduction/editNews.html'):
            response = self.client.get(reverse('introduction:editIntroduction', args=(introduction.id, )))
            self.assertEqual(response.status_code, 200)

    
    def test管理者修改消息不能有空白欄位(self):
        self.client.login(username='admin', password='admin')
        introduction = Introduction.objects.create(title='標題', content='內容')
        response = self.client.post(reverse('introduction:editIntroduction', args=(introduction.id, )), data={'title':'改標題'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('introduction:editIntroduction', args=(introduction.id, )), data={'content':'改內容'})
        self.assertIn('必填', response.content.decode('utf-8'), 1)
        response = self.client.post(reverse('introduction:editIntroduction', args=(introduction.id, )))
        self.assertIn('必填', response.content.decode('utf-8'), 2)


    def test管理者可正確修改消息(self):
        self.client.login(username='admin', password='admin')
        introduction = Introduction.objects.create(title='標題', content='內容')
        response = self.client.post(reverse('introduction:editIntroduction', args=(introduction.id, )), data={'title':'改標題', 'content':'改內容'})
        self.assertEqual(response.status_code, 302)  # Post-redirect-get
        introduction = Introduction.objects.filter(title='改標題', content='改內容')
        self.assertTrue(introduction)




        