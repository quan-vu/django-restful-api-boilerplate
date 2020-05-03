from django.db import models
from django.contrib.auth.models import Group, User


class Event(models.Model):
    name = models.CharField('Event Name', max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        permissions = (
                ('change_registration', 'Change Registration Setup'),
                ('change_submission', 'Change Submission Setup'),
                ('view_registration_admin', 'View Registration Admin'),
                ('add_users', 'Add New Users'),
                )

    def save(self, *args, **kwargs):
        from role.utils import roles_init_new

        is_create = False
        if not self.id:
            is_create = True

        if not self.slug:
            self.slug = unique_slugify(self, self.name)

        super(Event, self).save(*args, **kwargs)

        if is_create:
            roles_init_new(self)



class GroupEvent(models.Model):
    '''
    This model associates a group with an Event.
    Allows for easy retrieval of Group (Role Name) per event
    '''
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.group.name

    class Meta:
        unique_together = ['group', 'event']



def roles_init_new(event):
    '''
    Create new groups for the event
    '''
    g1 = Group.objects.get_or_create(name='%s: Admin - All' % event.name)[0]
    g2 = Group.objects.get_or_create(name='%s: Delegate' % event.name)[0]

    # ADMIN ALL GROUPS #
    assign('change_event', g1, event)  # change event details
    assign('change_registration', g1, event)  # change submission settings
    assign('change_submission', g1, event)  # change registration setup
    assign('view_registration_admin', g1, event)  # change registration tools
    assign('add_users', g1, event)  # user create functionality

    GroupEvent.objects.get_or_create(group=g1, event=event)
    GroupEvent.objects.get_or_create(group=g2, event=event)
    return True


def user_roles(request):
    '''
    Return a list of all the user roles
    '''
    try:
        g = Group.objects.filter(user=request.user)
        ge_list = []

        for group in g:
            if GroupEvent.objects\
                    .filter(group=group)\
                    .exists():
                ge = GroupEvent.objects.get(group=group)
                ge_list.append(ge)
    except:
        ge_list = []

    return {'USER_ROLES': ge_list}
