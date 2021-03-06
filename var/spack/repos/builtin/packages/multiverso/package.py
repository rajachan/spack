##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Multiverso(CMakePackage):
    """Multiverso is a parameter server based framework for
    training machine learning models on big data with numbers of machines."""

    homepage = "https://github.com/Microsoft/Multiverso"
    url      = "https://github.com/Microsoft/Multiverso/archive/v0.2.tar.gz"

    version('master', git='https://github.com/Microsoft/Multiverso.git',
            branch='master')
    version('143187', git='https://github.com/Microsoft/Multiverso.git',
            commit='143187575d1cfa410100037b8aea2e767e0af637')
    version('0.2', '483ca7524fea14a311389e421f2bc098')

    depends_on('mpi')
    depends_on('boost')

    patch('cmake-143187.patch', when='@143187')

    def cmake_args(self):
        spec = self.spec
        return ['-DBOOST_ROOT:PATH=%s' % spec['boost'].prefix]
