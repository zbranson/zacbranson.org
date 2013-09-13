# ----------------------------------------------------------------------
# config file for SASS/Compass
# http://beta.compass-style.org/help/tutorials/configuration-reference/
# ----------------------------------------------------------------------
http_path       = "/"
project_path    = "."

sass_dir        = "assets/css_src"
css_dir         = "assets/css"
images_dir      = "assets/img"
#javascripts_dir = "content/js"

# toggle between the sass or scss syntax
sass_options = {
  :syntax => :scss
}

line_comments   = false
# build compass for production
# compass compile -e production --force
# other output styles are :nested, :expanded, :compact, or :compressed
# output_style    = (environment == :production) ? :compressed : :expanded
output_style    = :compressed
