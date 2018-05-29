from uuid import uuid4
from datetime import datetime

from unittest import TestCase, mock

from app.domain.enums import CountryEnum, UserEnum
from app.domain.service import UserService, StoreService
from app.domain.models.info import Address, ContactInfo, ChangeLog
from app.domain.models.stores import Store
from app.domain.models.users import User, UpdateUser
from app.infrastructure.repository import UserRepository, ChangeLogRepository, StoreRepository


class UserServiceTest(TestCase):
    
    @mock.patch('app.infrastructure.repository.ChangeLogRepository')
    @mock.patch('app.infrastructure.repository.UserRepository')
    def setUp(self, user_repository, change_log_repository):
        self._user_repository = user_repository
        self._change_log_repository = change_log_repository

        self._user = User(
            id=str(uuid4()),
            first_name=str(uuid4()),
            last_name=str(uuid4()),
            username=str(uuid4()),
            user_type=UserEnum['EMPLOYEE'],
            address=Address(
                address=str(uuid4()),
                city=str(uuid4()),
                province=str(uuid4()),
                country=CountryEnum['CAN'],
                postal_code=str(uuid4())
            ),
            contact_info=ContactInfo(
                emails=[],
                phone_numbers=[]
            ),
            created_date=datetime.now()
        )

        self._user_repository.find_by_id.return_value = self._user
        self._user_service = UserService(self._user_repository, self._change_log_repository)
    
    def test_update_user(self):
        new_user_info = UpdateUser(
            first_name=str(uuid4()),
            last_name=str(uuid4()),
            username=str(uuid4()),
            user_type=UserEnum['OWNER'],
            address=Address(
                address=str(uuid4()),
                city=str(uuid4()),
                province=str(uuid4()),
                country=CountryEnum['CAN'],
                postal_code=str(uuid4())
            ),
            contact_info=ContactInfo(
                emails=['new@email.ca'],
                phone_numbers=['0803432342']
            )
        )

        updated_user_dict = self._user_service.update_user(self._user.get_id(), new_user_info).to_dict()
    
        self._user_repository.save_user.assert_called_once_with(
            User(id=self._user.get_id(), created_date=self._user.get_created_date(), **new_user_info.to_dict(is_nested=False))
        )
        self._change_log_repository.save_user_change_log.assert_called_once_with(
            ChangeLog(id=self._user.get_id(), message=ChangeLog.USER_INFO_CHANGED, created_date=mock.ANY)
        )

        for key, value in new_user_info.to_dict().items():
            self.assertEqual(updated_user_dict[key], value)


class StoreServiceTest(TestCase):
    
    @mock.patch('app.infrastructure.repository.ChangeLogRepository')
    @mock.patch('app.infrastructure.repository.StoreRepository')
    def setUp(self, store_repository: StoreRepository, change_log_repository: ChangeLogRepository):
        self._store_repository = store_repository
        self._change_log_repository = change_log_repository

        self._store = Store(
            id=str(uuid4), 
            name=str(uuid4),
            store_type=str(uuid4),
            phone_number=str(uuid4), 
            address=Address(
                address=str(uuid4()),
                city=str(uuid4()),
                province=str(uuid4()),
                country=CountryEnum['CAN'],
                postal_code=str(uuid4())
            ),
            employees=[],
            created_date= datetime.now()
        )

        self._store_service = StoreService(self._store_repository, self._change_log_repository)

    def test_create_store(self):
        self._store_repository.save_store.return_value = self._store
        
        created_store = self._store_service.create_store(self._store)
        self._store_repository.save_store.assert_called_once_with(
            self._store
        )
        self._change_log_repository.save_store_change_log.assert_called_once_with(
            ChangeLog(self._store.get_id(), ChangeLog.STORE_CREATED, self._store.get_created_date())
        )
        self.assertEqual(created_store, self._store)