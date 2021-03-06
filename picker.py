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

import random

class RandomPicturePicker(object):

  def __init__(self, album_repository):
    self._album_repository = album_repository

  def _PickWeighted(self, albums):
    total_pictures = sum(album.GetCount() for album in albums)
    if total_pictures > 0:
      pick = random.randint(0, total_pictures - 1)
      for album in albums:
        pick -= album.GetCount() 
        if pick < 0:
          return album 

  def _PickById(self, albums, album_id):
    for album in albums:
      if album.GetId() == album_id:
        return album

  def Pick(self, user_name, size, album_id=None):
    albums = self._album_repository.GetAlbums(user_name)
    if album_id:
      album = self._PickById(albums, album_id)
    else:
      album = self._PickWeighted(albums)
    if album:
      pictures = self._album_repository.GetPictures(album, size)
      if pictures:
        return random.choice(pictures)
