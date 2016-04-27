from django.test import TestCase
from django.core.urlresolvers import reverse
from main.tests.util import createSuperuser


class MainViewTestCase(TestCase):


    def test首頁使用正確範本並回覆200(self):
        with self.assertTemplateUsed('main/main.html'):
            response = self.client.get(reverse('main:main'))
            self.assertEqual(response.status_code, 200)


    def test管理者未登入首頁包含各按鈕及登入連結(self):
        self.client.logout()
        response = self.client.get(reverse('main:main'))
        self.assertContains(response, '課程查詢')
        self.assertContains(response, '上課紀錄')
        self.assertContains(response, '最新消息')
        self.assertContains(response, '用品查詢')
        self.assertContains(response, '回首頁')
        self.assertContains(response, '登入')
 
    '''
    def test管理者登入首頁包含各按鈕及登出連結(self):
        createSuperuser()
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('main:main'))
        self.assertContains(response, '課程管理')
        self.assertContains(response, '教師')
        self.assertContains(response, '舞蹈用品')
        self.assertContains(response, '用品銷售')
        self.assertContains(response, '薪資')
        self.assertContains(response, '學生')
        self.assertContains(response, '營業統計')
        self.assertContains(response, '分部')
        self.assertContains(response, '最新消息')
        self.assertContains(response, '系統設定')
        self.assertContains(response, '登出')
    '''