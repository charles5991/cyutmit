from django.test import TestCase
from news.models import News 
 


class NewsModelTestCase(TestCase):

    
    def test可以建立與取出資料物件(self):
        objCreated = News.objects.create(title='最新消息', content='消息內容')
        objRetrieved = News.objects.get(id=objCreated.id)
        self.assertEqual(objCreated.title, objRetrieved.title)


    def test最新消息排序由近到遠(self):
        news1 = News.objects.create(title='標題1', content='內容1')
        news2 = News.objects.create(title='標題2', content='內容2')
        news3 = News.objects.create(title='標題3', content='內容3')
        self.assertEqual(list(News.objects.all()), [news3, news2, news1])