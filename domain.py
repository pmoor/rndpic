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

class Album(object):

  def __init__(self, title, count, feed):
    self._title = title
    self._count = int(count)
    self._feed = feed

  def GetFeed(self):
    return self._feed

  def GetCount(self):
    return self._count

  def __str__(self):
    return self._feed


class Picture(object):

  def __init__(self, thumbnail_url, width, height, link):
    self._thumbnail_url = thumbnail_url
    self._width = int(width)
    self._height = int(height)
    self._link = link

  def GetLink(self):
    return self._link

  def GetThumbnailUrl(self):
    return self._thumbnail_url

  def GetWidth(self):
    return self._width

  def GetHeight(self):
    return self._height
