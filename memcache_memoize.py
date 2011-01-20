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

from google.appengine.api import memcache
import os

APP_VERSION = os.environ["CURRENT_VERSION_ID"]

def _CachedLookup(name, ttl, function, other, args):
  cache_key = ":".join([APP_VERSION, name] + [str(x) for x in args])
  data = memcache.get(cache_key)
  if data is not None:
    return data

  data = function(other, *args)
  if data is not None:
    memcache.add(cache_key, data, ttl)
    return data


def MemCached(name, ttl):
  def apply(f):
    def cache(self, *args):
      return _CachedLookup(name, ttl, f, self, args)
    return cache
  return apply
