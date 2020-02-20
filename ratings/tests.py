from django.test import TestCase
from .models import Profile,Project,User


class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.new_user = User(username='simonkim', email='kimanisimon856@gmail.com', password='qwertyuiop121')
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user,contact='kimanisimon856@gmail.com')
        
        def test_instance(self):
            self.assertTrue(isinstance(self.new_profile,Profile))
            
        def test_save_method(self):
            self.new_profile.save_profile()
            profile = Profile.objects.all()
            self.assertTrue(len(profile)>0)
        def test_delete_method(self):
            self.new_profile.save_profile()
            self.new_profile.delete_profile()
            profile = Profile.objects.all()
            self.assertTrue(len(profile)==0)   
            

class ProjectTestClass(TestCase):

    def setUp(self):
        self.new_user = User(username='simonkim', email='kimanisimon856@gmail.com', password='qwertyuiop121')
        
        self.new_user.save()
        self.new_post=Project(title="Nairobi",image='travel.png',description="Party the night away",link="https://w3resource.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Project))    

    def test_save_post(self):
        self.new_post.save_post()
        post = Project.objects.all()
        self.assertTrue(len(post)>0)

  