"""
Copyright 2008 Serge Matveenko

This file is part of Picket.

Picket is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Picket is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Picket.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.contrib.auth.models import User
from django.db                  import models
from django.db.models           import permalink
from django.utils.translation   import ugettext_lazy as _

from apps.picket.settings import ACCESS_LEVELS_CHOICES, \
                               ACCESS_LEVELS_CHOICES_DEFAULT

class Profile(models.Model):    
    user    = models.ForeignKey(User, unique = True)
    
    #some useful info
    phone   = models.CharField(_('phone number'), max_length=20)
    comment = models.TextField(_('comment'), blank=True)
    
    #access rights
    acl_picket  = models.PositiveIntegerField(_('picket access level'),
        choices=ACCESS_LEVELS_CHOICES, default=ACCESS_LEVELS_CHOICES_DEFAULT)
    
    def __unicode__(self):
        return u'%s: %s, %s' % (self.user, self.phone, self.comment)

    @permalink
    def get_absolute_url(self):
        return ('util.users.views.profile', (self.user.username,),)

