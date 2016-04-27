from django.contrib.auth.models import User
from accounts.models import UserProfile
from branches.models import Branch


def createSuperuser():
    admin = User()
    admin.username = 'admin'
    admin.first_name = '管理員'
    admin.set_password('admin')
    admin.email = 'admin@gmail.com'
    admin.is_staff = True
    admin.is_superuser = True
    admin.save()
    
    userProfile = UserProfile()
    userProfile.branch = Branch.objects.create(name='總部', address='XX', phone='0912345678')
    userProfile.user = admin
    userProfile.save()
    return admin


def createBranchAdmin():
    user = User()
    user.username = 'branchA'
    user.first_name = 'A分部管理員'
    user.set_password('branchA')
    user.email = 'branchA@gmail.com'
    user.save()

    userProfile = UserProfile()
    userProfile.branch = Branch.objects.create(name='分部A', address='分部A', phone='0912345678')
    userProfile.user = user
    userProfile.save()
    return user