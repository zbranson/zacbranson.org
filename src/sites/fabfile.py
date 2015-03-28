"""
basic project tasks
"""

import re
import os
import time
from fabric.api import *
from fabric.contrib.files import sed
from fabric.contrib import django

#database = os.getenv("DATABASE")
#DEFAUL_DATABASE = database or 'languages'

env.hosts = ['lwinmoe@lwinmoe.webfactional.com']
serverdir = "/home/lwinmoe/webapps/lwinmoe/my_site/"
localdir = os.getcwd()

#If a line that equals init exists in the file on the server, replaces that line with change
def switch(init, change, file):
    run("""sed "s/%s/%s/g" %s>%s.tmp && mv %s.tmp %s""" % (init, change, file, file, file, file))

# Syncs all files in localdir (ignoring all files in --exclude="foo")
# Change DEBUG=True to DEBUG=False on the remote server.
def deploy():
    local("rsync -atzv --delete --exclude-from='exclude_list.txt' %s/ %s:%s" % (localdir, env.hosts[0], serverdir))
    #switch("URL_PREFIX = ''", "URL_PREFIX = '%s'" % urlprefix, serverdir + "LLWeb/settings.py")
    switch("DEBUG=True", "DEBUG=False", serverdir + "my_site/settings.py")

application_name = 'lwinmoe'
def production():
    global application_name 
    application_name = 'lwinmoe'

'''
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
'''

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
