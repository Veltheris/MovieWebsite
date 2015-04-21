import webbrowser
import os
import re

# Styles and scripting for the page | Modified to have new info modal and new css 
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Great Films</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        /* Modifications to CSS */
        body {
            padding-top: 80px;
            background-color: #789;
        }
        .navbar-inverse {
        background-image: linear-gradient(to bottom, #003060 0px, #123 100%)
        }
        .navbar-inverse .navbar-brand {color: #08F;}
        #info-content {
        margin: 10px;
        }
        #info-content img {
        float: right;
        width: 220px;
        height: 342;
        }
        #info .modal-dialog {
            margin-top: 100px;
            width: 800px;
            height: 600px;
        }
        .info-tile {
        text-align: center;
        background-color: #DDD;
        border-radius: 5px
        padding: 3px;
        }
        .info-tile a {color: #468;}
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        footer {text-align: center;}
        /* End CSS Modifications */
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed | Modified to only function for the trailer modal
        $(document).on('click', '#trailer', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.info-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
<!-- New script for info modal -->
    <script type="text/javascript" charset="utf-8">
        $(document).on('click', '.movie-tile', function (event) {
            var infoURL = $(this).attr('data-trailer-youtube-id')
            var infoPoster = $(this).attr('data-poster')
            var infoMovieName = $(this).attr('data-name')
            var infoMovieDescription = $(this).attr('data-description')
            var infoRating = $(this).attr('data-rating')
            var infoRelease = $(this).attr('data-release')
            var infoDuration = $(this).attr('data-duration')
            var infoDirector = $(this).attr('data-director')
            var infoStars = $(this).attr('data-stars')
            $("#info-content").empty().append($("<img src='"+infoPoster+"'><h2>"+infoMovieName+"</h2><br /><b>Description: </b><p>"+infoMovieDescription+"</p><br /><p><b>Released: </b>"+infoRelease+"</p><br /><p><b>Rated: </b>"+infoRating+"</p><br /><p><b>Duration: </b>"+infoDuration+"</p><br /><p><b>Directed by: </b>"+infoDirector+"</p><br /><p><b>Starring: </b>"+infoStars+"</p><br /><div class='info-tile' data-trailer-youtube-id='"+infoURL+"' data-toggle='modal' data-target='#trailer'><a href='#'>Show Trailer</a>"));});
    </script>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html id="top" lang="en">
  <body>
    <!-- New Info Modal -->
    <div class="modal" id="info">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="media tile" id="info-content">
          </div>
        </div>
      </div>
    </div>
<!-- End New Info Modal -->
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#top">Great Films Info and Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
<footer>Copyright 2015 Great Films by Dylan Mountain</footer>
  </body>
</html>
'''

#New Template for storing the added information
#Template for a single movie tile with poster and name

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-poster="{poster_image_url}" data-name="{movie_title}" data-description="{movie_description}" data-rating="{movie_rating}" data-duration="{movie_duration}" data-release="{movie_release}" data-director="{movie_director}" data-stars="{movie_stars}" data-toggle="modal" data-target="#info">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_description=movie.description,
            movie_rating=movie.rating,
            movie_duration=movie.duration,
            movie_release=movie.release,
            movie_director=movie.director,
            movie_stars=movie.stars
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('great_films.htm', 'w')
  # To generate elsewhere Change the output_file to open('{url}/great_films.htm', 'w') 

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
