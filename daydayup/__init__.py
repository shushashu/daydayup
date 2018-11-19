from __future__ import absolute_import

import os

import pymysql

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

pymysql.install_as_MySQLdb()
