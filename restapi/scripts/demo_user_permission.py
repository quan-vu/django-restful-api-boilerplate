from django.contrib.auth.models import User, Group

# Create a user 
jack = User.objects.create_user('jack', 'jack@example.com', 'topsecretagentjack')
admins = Group.objects.create(name='admins')
jack.has_perm('change_group', admins)

print("jack.has_perm('change_group', admins): ", jack.has_perm('change_group', admins))


from guardian.models import UserObjectPermission

UserObjectPermission.objects.assign_perm('change_group', jack, obj=admins)
# <UserObjectPermission: admins | jack | change_group>
jack.has_perm('change_group', admins)
print("jack.has_perm('change_group', admins): ", jack.has_perm('change_group', admins))