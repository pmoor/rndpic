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

from google.appengine.api.urlfetch import fetch
from xml.dom.minidom import parseString

class FeedRepository(object):

  def GetUserFeed(self, user_name):
    url = "http://picasaweb.google.com/data/feed/api/user/%s?kind=album&access=public&fields=entry(title,gphoto:numphotos,link(@rel,@href))" % user_name
    result = fetch(url, follow_redirects=False, headers={"Accept-Encoding": "compress, gzip"})
    assert result.status_code == 200
    doc = parseString(result.content).documentElement
    return list(doc.getElementsByTagName("entry"))

  def GetAlbumFeed(self, feed_base_url, size):
    feed_url = feed_base_url + "?kind=photo&thumbsize=%s&fields=entry(link[@rel='alternate'],media:group(media:thumbnail))" % size
    result = fetch(feed_url, follow_redirects=False, headers={"Accept-Encoding": "compress, gzip"})
    assert result.status_code == 200
    doc = parseString(result.content).documentElement
    return list(doc.getElementsByTagName("entry"))
