from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length= 200)
    image = models.CharField(max_length= 200)
    likes = models.PositiveBigIntegerField(default=0)
    
class User(models.Model):
    title = models.CharField(max_length= 200)
    image = models.CharField(max_length= 200)
    likes = models.PositiveBigIntegerField(default=0)
    email = models.CharField(max_length= 200)
    password = models.CharField(max_length= 200)
    confirm_password = models.CharField(max_length= 200)
    def __str__(self):
        return self.email
    def isExist(self):      
        if User.objects.filter(email=self.email):
            return True
        return False
    def register(self):
        self.save()
    def doLogin(self):
        
    
## can u write a 5 tests to for the above class
## 1. test for isExist
## 2. test for register
## 3. test for doLogin
## 4. test for isExist when user does not exist

## 5. test for doLogin when user does not exist

## 6. test for doLogin when user exist but password is wrong



##  write a test for the above class in python 

class TestUser(TestCase):
    def test_isExist(self):
        u = User()
        u.email = "jd"
        self.assertEqual(u.isExist(), False)

    def isExist(self):
        u = User()
        u.email = "jd"
        u.register()
        self.assertEqual(u.isExist(), True)
    def test_doLogin(self):
        u = User()
        u.email = "jd"
        u.password = "123"
        u.doLogin()
        self.assertEqual(u.isExist(), True)
        