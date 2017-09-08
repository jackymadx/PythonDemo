#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  webAction.py
#  
#  Copyright 2017 Jacky <jackycck@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import web

urls = (
    '/', 'index', '/page', 'Page'
)

class index:
    def GET(self):
        return "Hello, Python !"

class Page(object):
    def GET(self):
        data = web.input()
        id = int(data.id)
        
        # all the inputs are now strings. Cast it to int, to get integer.
        action = data.action
        
        return "<h1>" + data.id + "</h1>" + data.action + ""

if __name__ == "__main__":
    app = web.application(urls, globals())
    print(">>>")
    app.run()
   
