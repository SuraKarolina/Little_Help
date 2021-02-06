import unittest 
from flask import url_for
from flask_testing import TestCase 

from app import app, db, User, Post

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://qatraining:qatraining@localhost/test",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
            )
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()
        sample1 = User(id = '1', username = "Karolina Sura", email = 'karolina.sura@outlook.com', location = 'Manchester', image_file = 'default.jpg', password = 'password')
        sample2 = Post(id = '1', title = 'First Post', date_posted = datetime.utcnow, content = 'First Post content', user_id = '1', reward = '20£')
        db.session.add(sample1, sample2)
        db.session.commit()

    def tearDown(self):
        db.drop_all()


class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_access_about(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_access_account(self):
        response = self.client.get(url_for('account'))
        self.assertEqual(response.status_code, 200)
    
    def test_access_create_post(self):
        response = self.client.get(url_for('create_post'))
        self.assertEqual(response.status_code, 200)

    def test_access_login(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_access_post(self):
        response = self.client.get(url_for('post'))
        self.assertEqual(response.status_code, 200)

    def test_access_register(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_access_user_posts(self):
        response = self.client.get(url_for('user_posts'))
        self.assertEqual(response.status_code, 200)

class Test_Find_User(TestBase):
    def test_find_user(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'Karolina Sura', response.data)

class Test_Imput(TestBase:
    def test_imput_home(self):
        response = self.client.post(url_for('update'), data=dict(review), follow_redirects=True)
        self.assertIn(b'home', response.data)
        #pretend that you put data in formularz i czy cie przekieruje ?
        