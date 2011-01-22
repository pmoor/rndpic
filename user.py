# rndpic - an App Engine app to display random pictures from Picasa Web.
# Copyright (C) 2010 Patrick Moor <patrick@moor.ws>
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
from google.appengine.ext.webapp.util import run_wsgi_app

from feed import FeedRepository
from album_repository import AlbumRepository
from picker import RandomPicturePicker


repository = AlbumRepository(FeedRepository())
picker = RandomPicturePicker(repository)


class UserHandler(webapp.RequestHandler):

  def get(self, user_name):
    size = self.request.get("size", "200u")
    link = bool(int(self.request.get("link", 1)))
    picture = picker.Pick(user_name, size)
    if picture:
      html = """<img src="%s" width="%d" height="%d"/>""" % (
          picture.GetThumbnailUrl(),
          picture.GetWidth(),
          picture.GetHeight())

      if link:
        html = """<a href="%s" target="_top">%s</a>""" % (
            picture.GetLink(),
            html)
      self.response.out.write("document.write('%s');" % html)
    else:
      self.response.set_status(204)




application = webapp.WSGIApplication(
    [(r'/user/([^/]+)', UserHandler)],
    debug=False)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
