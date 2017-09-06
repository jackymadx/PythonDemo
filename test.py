#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2017 Jacky <jackycck@jackycck-U32U>
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

import MySQLdb

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    print(">>>")
    
    # Open database connection
    db = MySQLdb.connect("127.0.0.1","root","","users" )

   # prepare a cursor object using cursor() method
    cursor = db.cursor()

   # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

   # Fetch a single row using fetchone() method.
    data = cursor.fetchone()

    print "Database version : %s " % data

   # disconnect from server
    db.close()
    sys.exit(main(sys.argv))
