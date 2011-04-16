from django.test import TestCase
from django.core.urlresolvers import reverse

from profiles.models import UserProfile


class ProfileTest(TestCase):
    def test_listing_renders(self):
        UserProfile.objects.create(
            name='Alice',
            description='Hi!',
        )
        response = self.client.get(reverse('profiles_list'))
        self.assertContains(response, 'Alice')

