# rndpic - an App Engine app to display random pictures from Picasa Web.
# Copyright (C) 2011 Patrick Moor <patrick@moor.ws>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from google.appengine.ext import webapp
from django.utils import simplejson 

class JsonHandler(webapp.RequestHandler):

  def __init__(self, picker):
    self._picker = picker

  def get(self, user_name):
    self.response.headers["Content-Type"] = "application/json"
    self.response.headers["Access-Control-Allow-Origin"] = "*"
    size = self.request.get("size", "200u")
    picture = self._picker.Pick(user_name, size)
    if picture:
      content = {
        "height": picture.GetHeight(),
        "width": picture.GetWidth(),
        "thumbnail_url": picture.GetThumbnailUrl(),
        "target_url": picture.GetLink(),
      }
      simplejson.dump(content, self.response.out)
    else:
      self.response.set_status(204)
