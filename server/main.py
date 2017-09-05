#!/usr/bin/env python

import os
import sys
topdir = os.path.dirname(os.path.abspath(__file__))

# tmpl_dir = os.path.join(topdir, 'tmpl')
static_dir = os.path.join(topdir, 'static')

import tornado.web
from tornado.options import define, options
from tornado.httpserver import HTTPServer

import handlers

routers = [
  (r'/stats', handlers.StatsHandler),
  # TODO: query page
  (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_dir}),
]

def main():
  define("port", default=8000, help="run on the given port", type=int)
  define("debug", default=False, help="debug mode", type=bool)

  tornado.options.parse_command_line()
  application = tornado.web.Application(
    routers,
    gzip = True,
    debug = options.debug,
    # template_path = tmpl_dir,
    # cookie_secret = settings['cookie_secret'],
  )
  http_server = HTTPServer(application)
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
