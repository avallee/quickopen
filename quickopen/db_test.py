# Copyright 2011 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import tempfile

import quickopen.settings as settings
import quickopen.db as db

class DBTest(unittest.TestCase):
  def setUp(self):
    self.settings_file_ = tempfile.NamedTemporaryFile()
    self.db_ = db.DB(settings.Settings(self.settings_file_.name))

  def test_init(self):
    assert self.db_

  def tearDown(self):
    self.settings_file_.close()
