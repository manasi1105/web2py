# -*- coding: utf-8 -*-

from gluon.fileutils import read_file

response.title = T('web2py Web Framework')
response.keywords = T('web2py, Python, Web Framework')
response.description = T('web2py Web Framework')

session.forget()
cache_expire = not request.is_local and 300 or 0


@cache('index', time_expire=cache_expire)
def index():
    return response.render()


@cache('what', time_expire=cache_expire)
def what():
    import urllib
    try:
        images = XML(urllib.urlopen(
            'http://web2py.com/poweredby/default/images').read())
    except:
        images = []
    return response.render(images=images)


@cache('download', time_expire=cache_expire)
def download():
    return response.render()


@cache('who', time_expire=cache_expire)
def who():
    return response.render()


@cache('support', time_expire=cache_expire)
def support():
    return response.render()


@cache('documentation', time_expire=cache_expire)
def documentation():
    return response.render()


@cache('usergroups', time_expire=cache_expire)
def usergroups():
    return response.render()


def contact():
    redirect(URL('default', 'usergroups'))


@cache('videos', time_expire=cache_expire)
def videos():
    return response.render()


def security():
    redirect('http://www.web2py.com/book/default/chapter/01#security')


def api():
    redirect('http://web2py.com/book/default/chapter/04#API')


@cache('license', time_expire=cache_expire)
def license():
    import os
    filename = os.path.join(request.env.gluon_parent, 'LICENSE')
    return response.render(dict(license=MARKMIN(read_file(filename))))


def version():
    return 'Version %s.%s.%s (%s) %s' % request.env.web2py_version


@cache('examples', time_expire=cache_expire)
def examples():
    return response.render()


@cache('changelog', time_expire=cache_expire)
def changelog():
    import os
    filename = os.path.join(request.env.gluon_parent, 'CHANGELOG')
    return response.render(dict(changelog=MARKMIN(read_file(filename))))
