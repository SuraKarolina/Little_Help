import unittest
from flask import url_for
from flask_testing import TestCase
from datetime import datetime

from app import app, db
from app.models import User, Post



class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///", 
                SECRET_KEY='TEST_KEY')
        return app

    def setUp(self):
        db.create_all()
        sample_user = User(id = 1, username = "Karolina", email = "karolina@op.pl", location = "Manchester", password = "password")
        sample_post = Post(id = 1, title = "New Post", content = "New post content", reward = "20£", user_id = 1)

        db.session.add(sample_user)
        db.session.add(sample_post)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_access_register(self):
        response = self.client.get(url_for('register'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_access_login(self):
        response = self.client.get(url_for('login'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_access_about(self):
        response = self.client.get(url_for('about'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_access_account(self):
        response = self.client.get(url_for('account'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class PostTests(TestBase):
    def test_access_register(self):
        response = self.client.get(url_for('register'), data=dict(username ="Karolina", password ="password"), follow_redirects=True)
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_access_register_new(self):
        response = self.client.get(url_for('register'), data=dict(username ="Ola", password ="password"), follow_redirects=True)
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_user_duplicate(self): 
        response = self.client.post ((url_for("register")),
                                    data = dict(username="Karolina", password="password"), 
                                    follow_redirects=True)
        self.assertIn(b'That username is taken. Please choose a different one.', response.data)

    def test_post_user_duplicate(self): 
        response = self.client.post ((url_for("register")),
                                    data = dict(email = "karolina@op.pl", password="password"), 
                                    follow_redirects=True)
        self.assertIn(b'That email is taken. Please choose a different one.', response.data)

    def test_user_can_login(self):
        response = self.client.get(url_for('login'), data=dict(username="Karolina", password="password"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_user_can_add_new_post(self):
        response = self.client.get(url_for('new_post'), data=dict(post_id= 1, username="Karolina", password="password"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        response = self.client.post(url_for('update_post', post_id = 1))
        self.assertEqual(response.status_code, 302)

    def test_add_post(self):
        response = self.client.post(url_for('user_posts', username = "Karolina"),data = dict(title="New Post", user_id = 1))
        self.assertIn(b'title',response.data)

    def test_add_post(self):
        response = self.client.post(url_for('update_post', post_id = 1),data = dict(title="New Post"))
        self.assertIn(b"title",response.data)

    def test_delete_post(self):
       response = self.client.post(url_for('delete_post', post_id = 1))
       self.assertEqual(response.status_code, 302)

    def test_delete_post(self):
        response = self.client.post(url_for('delete_post', post_id = 1),data = dict(title="New Post"))
        self.assertIn(b'title',response.data)
    
    def test_user_can_logout(self):
        response = self.client.get(url_for('logout'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_password_setter(self):
        u = User(password='password')
        self.assertTrue(u.password is not None)

