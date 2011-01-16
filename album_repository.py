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

from domain import Album, Picture
from memcache_memoize import MemCached

class AlbumRepository(object):

  def __init__(self, feed_repository):
    self._feed_repository = feed_repository

  @MemCached("albums", 3600)
  def GetAlbums(self, user_name):
    user_feed = self._feed_repository.GetUserFeed(user_name)
    return [self._ParseUserFeedEntry(entry) for entry in user_feed]

  @MemCached("pictures", 86400)
  def GetPictures(self, album, size):
    album_feed = self._feed_repository.GetAlbumFeed(album.GetFeed(), size)
    return [self._ParseAlbumFeedEntry(entry) for entry in album_feed]

  def _ParseUserFeedEntry(self, entry):
    title = entry.getElementsByTagName("title")[0].firstChild.nodeValue
    num_photos = int(entry.getElementsByTagName("gphoto:numphotos")[0].firstChild.nodeValue)
    links = entry.getElementsByTagName("link")
    for link in links:
      if link.getAttribute("rel") == "http://schemas.google.com/g/2005#feed":
        return Album(title, num_photos, link.getAttribute("href"))

  def _ParseAlbumFeedEntry(self, entry):
    links = entry.getElementsByTagName("link")
    for link in links:
      if link.getAttribute("rel") == "alternate":
        alternate = link.getAttribute("href")
    thumb = entry.getElementsByTagName("media:thumbnail")[0]
    return Picture(thumb.getAttribute("url"), int(thumb.getAttribute("width")), int(thumb.getAttribute("height")), alternate)
