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
from google.appengine.ext.webapp.util import run_wsgi_app

from feed import FeedRepository
from album_repository import AlbumRepository
from picker import RandomPicturePicker

from user_handler import UserHandler
from json_handler import JsonHandler


repository = AlbumRepository(FeedRepository())
picker = RandomPicturePicker(repository)


def _ConstructUserHandler():
  return UserHandler(picker)


def _ConstructJsonHandler():
  return JsonHandler(picker)


application = webapp.WSGIApplication(
    [
      (r'/user/([^/]+)', _ConstructUserHandler),
      (r'/json/([^/]+)', _ConstructJsonHandler),
    ],
    debug=False)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
