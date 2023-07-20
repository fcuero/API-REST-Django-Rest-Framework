
from django.test import TestCase
from rest_framework.test import APIClient



class TestAvatarViewSet(TestCase):
    

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/avatar/'

    
    def get_avatars(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    
    def filter_avatar(self):
        data = {'name': 'Yoda'}
        response = self.client.get(self.url, data, format='json')
        self.assertEqual(response.status_code, 200 )
    
   
    def delete_avatar(self):
        data = {'name': 'Yoda'}
        response = self.client.delete(self.url, data, format='json')
        self.assertEqual(response.status_code, 405)
        
    
    def cannot_add_avatar(self):
        data = {'name': 'Yoda23','movie':'The Empire Strikes Back'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, [])
        

        
class TestProductorViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/productor/'

    def get_productors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def delete_productor(self):
        data = {'name': 'George Lucas'}
        response = self.client.delete(self.url, data, format='json')
        self.assertEqual(response.status_code, 405)
    
    def test_addproductor(self):
        data = {'name': 'George Lucas'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])
        
        

class TestMoviesViewSet(TestCase):
    
        def setUp(self):
            self.client = APIClient()
            self.url = '/api/addmovie/'
    
        def get_movies(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, [])
    
        def delete_movies(self):
            data = {'name': 'The Empire Strikes Back'}
            response = self.client.delete(self.url, data, format='json')
            self.assertEqual(response.status_code, 405)
        
        def test_addmovies(self):
            data = {'name': 'The Empire Strikes Back'}
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, [])

class TestDirectorViewSet(TestCase):
        
            def setUp(self):
                self.client = APIClient()
                self.url = '/api/director/'
        
            def get_director(self):
                response = self.client.get(self.url)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data, [])
        
            def delete_director(self):
                data = {'name': 'George Lucas'}
                response = self.client.delete(self.url, data, format='json')
                self.assertEqual(response.status_code, 405)
            
            def test_adddirector(self):
                data = {'name': 'George Lucas'}
                response = self.client.post(self.url, data, format='json')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data, [])
    
