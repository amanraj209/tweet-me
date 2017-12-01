from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Tweet

User = get_user_model()


class TweetModelTest(TestCase):

    def setUp(self):
        User.objects.create(username='aman209')

    def test_tweet_item(self):
        obj = Tweet.objects.create(user=User.objects.first(), content='Random content')
        self.assertTrue(obj.content == 'Random content')

    def test_tweet_url(self):
        obj = Tweet.objects.create(user=User.objects.first(), content='Random content')
        absolute_url = reverse('tweet:detail', kwargs={'pk': 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
