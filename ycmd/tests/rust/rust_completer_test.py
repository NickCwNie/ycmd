# Copyright (C) 2020 ycmd contributors
#
# This file is part of ycmd.
#
# ycmd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ycmd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ycmd.  If not, see <http://www.gnu.org/licenses/>.

from mock import patch
from nose.tools import ok_

from ycmd import user_options_store
from ycmd.completers.rust.hook import GetCompleter


def GetCompleter_RlsFound_test():
  ok_( GetCompleter( user_options_store.GetAll() ) )


@patch( 'ycmd.completers.rust.rust_completer.RLS_EXECUTABLE', None )
def GetCompleter_RlsNotFound_test( *args ):
  ok_( not GetCompleter( user_options_store.GetAll() ) )
