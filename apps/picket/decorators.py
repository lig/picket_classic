"""
Copyright 2009 Serge Matveenko

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

from django.shortcuts import get_object_or_404

from models import BugRelationship


def bug_relationship_to_bug(fn):
    def bug_relationship_to_bug_view(request, bug_relationship_id):
        
        bugRelationship = get_object_or_404(BugRelationship,
            id=bug_relationship_id)
        
        bug_id = bugRelationship.source_bug_id
        
        return fn(request, bug_id, bugRelationship)
    return bug_relationship_to_bug_view
