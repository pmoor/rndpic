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

from google.appengine.api.urlfetch import fetch, DownloadError
from xml.dom.minidom import parseString

class FeedRepository(object):

  def _Fetch(self, url):
    try:
      result = fetch(url, follow_redirects=False, headers={"Accept-Encoding": "compress, gzip"})
      if result.status_code == 200:
        return result
    except DownloadError:
      pass

  def GetUserFeed(self, user_name):
    url = "http://picasaweb.google.com/data/feed/api/user/%s?kind=album&access=public&fields=entry(title,gphoto:numphotos,link(@rel,@href))" % user_name
    result = self._Fetch(url)
    if result:
      doc = parseString(result.content).documentElement
      return doc.getElementsByTagName("entry")
    else:
      return []

  def GetAlbumFeed(self, feed_base_url, size):
    url = feed_base_url + "?kind=photo&thumbsize=%s&fields=entry(link[@rel='alternate'],media:group(media:thumbnail))" % size
    result = self._Fetch(url)
    if result:
      doc = parseString(result.content).documentElement
      return doc.getElementsByTagName("entry")
    else:
      return []
