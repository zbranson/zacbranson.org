"""
basic project tasks
"""

import re
import os
import time
from fabric.api import local, cd
from fabric.contrib.files import sed
from fabric.contrib import django

#database = os.getenv("DATABASE")
#DEFAUL_DATABASE = database or 'languages'

application_name = 'lwinmoe'
def production():
    global application_name 
    application_name = 'lwinmoe'

def deploy():
    compile_js()
    app_yml = open('app.yml.tmpl').read()
    app_yml = app_yml % {'application_name': application_name }
    open('app.yml', 'w').write(app_yml)
    #local("python manage.py compilemessages");
    #local("cp -r locale app/locale")
    local("appcfg.py --no_cookies update . ")
    # remove duplicated files
    #local("rm -rf app/locale")

def _get_javascript_files():
    javascripts = (
      "js/libs/jquery.min.js",
      "js/libs/jquery-ui.min.js",
      "js/browser_check.js",
      "js/libs/selectivizr.min.js",
      "js/libs/underscore-min.js",
      "js/plugins/jquery.mousewheel.js",
      "js/plugins/jquery.jscrollpane.min.js",
      "js/plugins/markerclusterer.js",
      "js/plugins/chosen.jquery.min.js",
      "js/plugins/jquery.easing.js",
      "js/plugins/jquery.slides.js",
      "js/plugins/jquery.cookie.js",
      "js/plugins/jquery.bootstrap.js",
      "js/plugins/jquery.stylish.js",
      "js/plugins/jquery.valum.js",
      "js/plugins/jquery.tagit.js",
      "js/plugins/jquery.addresspicker.js",
      "js/plugins/jquery.address.js",
      "js/plugins/jquery.address.js",
      "js/plugins/bootstrap-tooltip.js",
      "js/plugins/bootstrap-collapse.min.js",
    )
    return ['assets/' + x for x in javascripts]

def concat_files(files):
    for x in files:
        if 'min' in x or 'jquery.bootstrap.js' in x:
            local("cat %s >> /tmp/_concat.js" % x)
        else:
            local("java -jar ../tools/compiler.jar --js %s >> /tmp/_concat.js" % x)

def compile_js():
    local("rm -rf /tmp/_concat.js")
    js = _get_javascript_files()
    concat_files(js)
    local("rm -rf assets/js/all.js")
    local("cp /tmp/_concat.js assets/js/all.js")
    #local("java -jar ../tools/compiler.jar --js /tmp/_concat.js --js_output_file assets/js/all.js")
