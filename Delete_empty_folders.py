#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:56:02 2019

@author: juanm55

License: http://creativecommons.org/licenses/by-nc-sa/4.0/
"""

import os
#If you are looking to delete empty folders in an external disk you may look for it on the Volumes folder, located in root
for root, dirs, files in os.walk('/test_folder_with_too_many_folders', topdown=False):
   for name in dirs:
      print('Checking: ' + os.path.join(root, name))
      if len(os.listdir(os.path.join(root, name)) ) == 0 or os.listdir(os.path.join(root, name)) == ['.DS_Store']:
          if os.path.exists(os.path.join(root, name) + '/.DS_Store'):
              os.remove(os.path.join(root, name) + '/.DS_Store')
          print(os.path.join(root, name) + ' => Is empty')
          os.rmdir(os.path.join(root, name))