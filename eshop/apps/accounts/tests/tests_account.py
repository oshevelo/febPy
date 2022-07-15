
class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_list_permissions(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/discount',follow=True)
#        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        #print(response.data['results'][0]['user'], self.user.id)
        self.assertEqual(response.data['results'][0]['user'], self.user.id)

    def test_this_users_account_permission(self):
        self.c.login(username=self.user.username, password='password')
        # print(f'/api/accounts/pointcount/{self.user.id}/')
        response = self.c.get(f'/api/accounts/discount/{self.user.id}/')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_users_pointcount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/discount/6', follow=True)
        #print('response other user', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


#class RatingTest(TestCase):
