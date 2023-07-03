# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.test import TestCase
# from django.urls import reverse


# class UserRegistrationTest(TestCase):
#     def test_registration_form(self):
#         response = self.client.get(reverse('registration'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration.html')

#         data = {
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'email': 'john.doe@example.com',
#             'phone_number': '1234567890',
#             'password1': 'testpassword',
#             'password2': 'testpassword',
#         }
#         response = self.client.post(reverse('registration'), data)
#         self.assertEqual(response.status_code, 302)  # Redirect after successful registration
#         self.assertEqual(User.objects.count(), 1)  # One user should be created
#         self.assertRedirects(response, reverse('login'))

#     def test_user_login(self):
#         user = User.objects.create_user(username='john.doe@example.com', password='testpassword')

#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'login.html')

#         data = {
#             'email': 'john.doe@example.com',
#             'password': 'testpassword',
#         }
#         response = self.client.post(reverse('login'), data)
#         self.assertEqual(response.status_code, 302)  # Redirect after successful login
#         self.assertRedirects(response, reverse('dashboard'))
#         self.assertEqual(str(response.wsgi_request.user), 'john.doe@example.com')

#     def test_password_reset(self):
#         user = User.objects.create_user(username='john.doe@example.com', password='testpassword')

#         response = self.client.get(reverse('password_reset'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'password_reset.html')

#         data = {'email': 'john.doe@example.com'}
#         response = self.client.post(reverse('password_reset'), data)
#         self.assertEqual(response.status_code, 302)  # Redirect after submitting password reset request
#         self.assertRedirects(response, reverse('password_reset_done'))

#         # Retrieve the password reset token
#         token = default_token_generator.make_token(user)

#         # Generate a new password and confirm it
#         new_password = 'newtestpassword'
#         confirm_data = {
#             'new_password1': new_password,
#             'new_password2': new_password,
#         }
#         confirm_url = reverse('password_reset_confirm', kwargs={'uidb64': user.pk, 'token': token})
#         response = self.client.post(confirm_url, confirm_data)
#         self.assertEqual(response.status_code, 302)  # Redirect after resetting password
#         self.assertRedirects(response, reverse('password_reset_complete'))

#         # Verify that the new password works
#         login_data = {
#             'email': 'john.doe@example.com',
#             'password': new_password,
#         }
#         response = self.client.post(reverse('login'), login_data)
#         self.assertEqual(response.status_code, 302)  # Redirect after successful login
#         self.assertRedirects(response, reverse('dashboard'))
#         self.assertEqual(str(response.wsgi_request.user), 'john.doe@example.com')
