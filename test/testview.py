from flask import request
from flask_testing import TestCase
from _datetime import datetime

from flask_shorten.flask_shorten import app, db

from flask_shorten.models import AllLinks


class ViewsTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.session.add(AllLinks(origin_link='origintest1',
                                short_link='1',
                                date_create=datetime.now(),
                                counter=0))
        db.session.add(AllLinks(origin_link='origintest2',
                                short_link='shorttest2',
                                date_create=datetime.now(),
                                counter=0))
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_read_links_with_data(self):
        response = self.client.get('/')
        datatest = AllLinks.query.all()
        self.assert200(response)
        self.assertTemplateUsed('index.html')
        self.assertContext('next_id', 3)
        self.assertContext('url', request.url)
        self.assertContext('data', datatest)

    def test_read_links_without_data(self):
        AllLinks.query.delete()
        datatest = AllLinks.query.all()
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('index.html')
        self.assertContext('next_id', 1)
        self.assertContext('url', request.url)
        self.assertContext('data', datatest)

    def test_read_links_post_if(self):
        data = {'origin': 'origintest1', 'short': 'shorttest1'}
        response = self.client.post('/', data=data)
        linktest = AllLinks.query.filter_by(origin_link=data['origin']). \
            first()
        self.assert400(response)
        self.assertTemplateUsed('success.html')
        self.assertContext('link', linktest)
        self.assertContext('url', request.url)
        self.assertContext('result', 1)

    def test_read_links_post_elif(self):
        data = {'origin': 'origin', 'short': '1'}
        response = self.client.post('/', data=data)
        linktest = AllLinks.query.filter_by(short_link=data['short']). \
            first()
        self.assert400(response)
        self.assertTemplateUsed('success.html')
        self.assertContext('link', linktest)
        self.assertContext('url', request.url)
        self.assertContext('result', 2)

    def test_read_links_post_else_if(self):
        data = {'origin': 'origin', 'short': ''}
        response = self.client.post('/', data=data)
        self.assert400(response)
        self.assertTemplateUsed('success.html')
        self.assertContext('result', 5)

    def test_read_links_post_else_else(self):
        data = {'origin': 'origin', 'short': '123'}
        response = self.client.post('/', data=data)
        all_links = AllLinks.query.all()
        self.assert200(response)
        self.assertTemplateUsed('success.html')
        self.assertContext('result', 3)
        self.assertContext('url', request.url)
        self.assertEqual(len(all_links), 3)
        self.assertEqual(all_links[-1].short_link, '123')

    def test_go_link_if(self):
        response = self.client.get('/1123')
        self.assert404(response)
        self.assertTemplateUsed('success.html')
        self.assertContext('url', request.url + '1123')
        self.assertContext('result', 4)

    def test_go_link_else(self):
        response = self.client.get('/1')
        link = AllLinks.query.filter_by(short_link='1').first()
        self.assertEqual(response.status_code, 303)
        self.assertEqual(link.counter, 1)
