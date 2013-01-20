# rndpic - an App Engine app to display random pictures from Picasa Web.
# Copyright (C) 2013 Patrick Moor <patrick@moor.ws>
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

import webapp2

class ImgHandler(webapp2.RequestHandler):

  def get(self, user_name):
    size = self.request.get("size", "200u")
    album_id = int(self.request.get("album_id", 0))
    picture = webapp2.get_app().registry["picker"].Pick(
        user_name, size, album_id)
    if picture:
      self.redirect(picture.GetThumbnailUrl().encode())
    else:
      self.response.set_status(204)
