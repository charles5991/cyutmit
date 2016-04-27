from django.test import TestCase
from news.forms import NewsForm


class NewsFormTestCase(TestCase):


    def test新增消息表單內容正確(self):
        form = NewsForm()
        self.assertIn('標題', form.as_p())
        self.assertIn('內容', form.as_p())


    def test標題或內容不能空白(self):
        form = NewsForm(data={'content':'內容'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['必填'])
        form = NewsForm(data={'title':'標題'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], ['必填'])
