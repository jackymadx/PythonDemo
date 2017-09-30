#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Student.py
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

class Student(object):
   def __init__(self, name):
        self.name = name
        
   def set_age(self, age):
		self.age = age    
		
   def set_major(self, major):
        self.major = major 
        
class MasterStudent(Student):
	internship = 'mandatory, from July to December'
	                
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    
    print('---')
    std = Student('John')
    std.set_age(22)
    std.set_major('Maths')
    
    print("# %s is %d years old  and major is %s" % (std.name,std.age,std.major))
    
    std2 = MasterStudent('Evone')
    std2.internship
    std2.set_age(29)
    std2.set_major('Physics')
    
    print("# %s is %d years old  and major is %s" % (std2.name,std2.age,std2.major))
    print("# Internship : [%s]" % std2.internship)
    
    sys.exit(main(sys.argv))
