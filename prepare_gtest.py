# Copyright (c) 2014-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

import os
import urllib2
import zipfile

gtest = urllib2.urlopen('https://github.com/google/googletest/archive/release-1.7.0.zip').read()
with open('lib/gtest/gtest.zip', 'w') as f:
    f.write(gtest)
with zipfile.ZipFile('lib/gtest/gtest.zip', 'r') as zip:
    zip.extractall('./lib/gtest')
os.remove('lib/gtest/gtest.zip')
