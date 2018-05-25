from random import choice
from uuid import uuid4
from unittest import TestCase, mock
import simplejson as json

from app import create_app
from app.domain.enums import ProvinceEnum, CountryEnum, UserEnum, EmployeeEnum
from app.domain.service import StoreService, UserService

class StoreTest(TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.store_data = {
            'name': str(uuid4()),
            'phone_number': str(uuid4()),
            'store_type': 'RETAIL',
            'address': {
                'address': str(uuid4()),
                'city': str(uuid4()),
                'province': choice(list(ProvinceEnum)).name,
                'country': choice(list(CountryEnum)).name,
                'postal_code': str(uuid4())
            }
        }

    def tearDown(self):
        self.app_context.pop()
    
    @mock.patch.object(StoreService, 'create_store')
    def test_post(self, create_store: mock.MagicMock):
        create_store.return_value = {}
        response = self.client.post('/store',
                                    data=json.dumps(self.store_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(create_store.called, True)

    @mock.patch.object(StoreService, 'update_store')
    def test_put(self, update_store):
        update_store.return_value = {}
        response = self.client.put('/store/' + str(uuid4()),
                                    data=json.dumps(self.store_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(update_store.called, True)

class EmployeeTest(TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.employee_data = {
            'employee_type': choice(list(EmployeeEnum)).name,
            'user': {
                'first_name': str(uuid4()),
                'last_name': str(uuid4()),
                'user_type': choice(list(UserEnum)).name,
                'username': str(uuid4()),
                'address': {
                    'address': str(uuid4()),
                    'city': str(uuid4()),
                    'province': choice(list(ProvinceEnum)).name,
                    'country': choice(list(CountryEnum)).name,
                    'postal_code': str(uuid4())
                }, 
                'contact_info': {
                    'emails': [],
                    'phone_numbers': []
                }
            }
        }

    def tearDown(self):
        self.app_context.pop()
    
    @mock.patch.object(StoreService, 'create_employee')
    def test_post(self, create_employee):
        create_employee.return_value = {}
        response = self.client.post('/store/'+ str(uuid4()) + '/employee',
                                    data=json.dumps(self.employee_data), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(create_employee.called, True)
    
    @mock.patch.object(StoreService, 'update_employee')
    def test_put(self, update_employee):
        update_employee.return_value = {}
        response = self.client.put('/store/' + str(uuid4()) + '/employee/' + str(uuid4()),
                                    data=json.dumps(self.employee_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(update_employee.called, True)


class UserTest(TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.user_data = {
            'first_name': str(uuid4()),
            'last_name': str(uuid4()),
            'user_type': choice(list(UserEnum)).name,
            'username': str(uuid4()),
            'address': {
                'address': str(uuid4()),
                'city': str(uuid4()),
                'province': choice(list(ProvinceEnum)).name,
                'country': choice(list(CountryEnum)).name,
                'postal_code': str(uuid4())
            }, 
            'contact_info': {
                'emails': [],
                'phone_numbers': []
            }
        }

    def tearDown(self):
        self.app_context.pop()
    
    @mock.patch.object(UserService, 'update_user')
    def test_put(self, update_user):
        update_user.return_value = {}
        response = self.client.put('/user/' + str(uuid4()),
                                    data=json.dumps(self.user_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(update_user.called, True)

