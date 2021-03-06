from django.test import TestCase


from .models import User, Post


# test cases.
class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(self):
        # creating users an posts
        user1 = User(username='dennis', email='obide1@yahoo.com', password='123456789')
        user1.save()
        user2 = User(username='obide', email='obide1@gmail.com', password='123456')
        user2.save()
        post1 = Post(name='drf', description='drf is great', author=user1)
        post1.save()
        post2 = Post(name='Django2', description='django is great', author=user2)
        post2.save()
    
    def test_get(self):
        posts = Post.objects.all()
        print(posts)
        self.assertNotEqual(posts.count(), 0)  # our database contains 2 posts so must be different from 0

    def test_post(self):
        # testing the insertion of items in the Post model
        post = Post.objects.get(id=1)
        author = User.objects.get(id=1)
        self.assertEqual(author.username, 'dennis')
        self.assertEqual(str(author.email), 'obide1@yahoo.com')
        self.assertEqual(author.email, 'obide1@yahoo.com')
        self.assertEqual(post.name, 'drf')
        self.assertEqual(post.description, 'drf is great')
        self.assertEqual(post.author, author)
        self.assertEqual(str(author), 'obide1@yahoo.com')

    def test_update(self):
        post = Post.objects.get(id=1)
        # author = Post.objects.get(id=1)
        post.name = 'django'
        # post.save()
        self.assertEqual(post.name, 'django')

    def test_delete(self):
        # k = reverse('posts')
        # print(k)
        post = Post.objects.get(id=2)
        # user = User.objects.get(id=2)
        post.delete()
        # user.delete()
        xx = Post.objects.filter(id=2)
        self.assertEqual(xx.count(), 0)
        # self.assertEqual(post.description, None)
