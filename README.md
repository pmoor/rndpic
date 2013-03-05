rndpic
======

App Engine application serving random Picasa Web images.

This application will always be deployed at rndpic.appspot.com. To simply use it as is, include the following snippet on your web page:

    <script type=”text/javascript” src=”http://rndpic.appspot.com/user/your.username“></script>

Replace "your.username" with the name of your Picasa Web username.

If you want to customize the size of the thumbnail returned pass a "?size=" option:

    <script type=”text/javascript” src=”http://rndpic.appspot.com/user/your.username?size=320u“></script>

A list of valid sizes can be found in the Picasa Web API reference at http://code.google.com/apis/picasaweb/docs/2.0/reference.html#Parameters. Look for explanations on "thumbsize".

If you don't want the image to be a link to the full version, simply add "?link=0":

    <script type=”text/javascript” src=”http://rndpic.appspot.com/user/your.username?link=0“></script>

If you want to restrict the choice to a single album append an "album_id" parameter:

    <script type=”text/javascript” src=”http://rndpic.appspot.com/user/your.username?album_id=8273376044385732429“></script>

To figure out the proper value for "album_id", simply visit your Picasa Web Album and look in the HTML sources for a string of the form "/albumid/1234567890123" - the digits after "/albumid/" represent the ID of the album.

In case you want to have full control over how the image is displayed, rndpic now also offers serving raw JSON:

    $ curl "http://rndpic.appspot.com/json/your.username?size=320u"
    {
      "target_url": "https:\/\/...",
      "width": 320,
      "thumbnail_url": "http:\/\/...",
      "height": 240
    }

An example of this in action can be seen at http://rndpic.appspot.com/examples/slideshow.html. To get an idea on how to use it, check out the sources at http://code.google.com/p/rndpic/source/browse/trunk/examples/slideshow.html

If you're not able to use JavaScript there's a simple integration method using an img-tag:

    <img src="http://rndpic.appspot.com/img/your.username"/>

Please note that this will just embed the picture on your site but it will not be linked to the full-resolution version on Picasa Web.
