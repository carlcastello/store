from uuid import uuid4
from unittest import TestCase, mock

from app.domain.enums import CountryEnum, UserEnum
from app.domain.service import UserService
from app.domain.models.info import Address, ContactInfo
from app.domain.models.users import User, UpdateUser
from app.infrastructure.repository import UserRepository, ChangeLogRepository

class UserServiceTest(TestCase):
    
    def setUp(self):
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
            )
        )

        user_repository = UserRepository()
        user_repository.find_by_id = mock.MagicMock(return_value=self._user)
        change_log_repository = ChangeLogRepository()
        self._user_service = UserService(user_repository, change_log_repository)
    
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
                emails=[],
                phone_numbers=[]
            )
        )

        updated_user = self._user_service.update_user(self._user.get_id(), new_user_info)
        
        self.assertEqual(updated_user.get_id(), self._user.get_id())
        self.assertNotEqual(updated_user, self._user)
        updated_user_dict = updated_user.to_dict()
        for key, value in new_user_info.to_dict().items():
            self.assertEqual(updated_user_dict.get(key), value)