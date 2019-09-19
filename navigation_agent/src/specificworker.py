#
# Copyright (C) 2019 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os, traceback, time

from PySide import QtGui, QtCore
from genericworker import *

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map):
        super(SpecificWorker, self).__init__(proxy_map)
        self.timer.timeout.connect(self.compute)
        self.Period = 2000
        self.timer.start(self.Period)
        
        self.dummy_state = True

    def setParams(self, params):
        #try:
        #    self.innermodel = InnerModel(params["InnerModelPath"])
        #except:
        #    traceback.print_exc()
        #    print "Error reading config params"
        return True

    @QtCore.Slot()
    def compute(self):
        print self.dummy_state
        
        if self.dummy_state:
            self.differentialrobot_proxy.setSpeedBase(0, 0)
        else:
            self.differentialrobot_proxy.setSpeedBase(100, 0)

        self.dummy_state = not self.dummy_state

        return True


    #
    # structuralChange
    #
    def structuralChange(self, w):
        #
        #subscribesToCODE
        #
        pass


    #
    # edgesUpdated
    #
    def edgesUpdated(self, modifications):
        #
        #subscribesToCODE
        #
        pass


    #
    # edgeUpdated
    #
    def edgeUpdated(self, modification):
        #
        #subscribesToCODE
        #
        pass


    #
    # symbolUpdated
    #
    def symbolUpdated(self, modification):
        #
        #subscribesToCODE
        #
        pass


    #
    # symbolsUpdated
    #
    def symbolsUpdated(self, modifications):
        #
        #subscribesToCODE
        #
        pass


    #
    # reloadConfigAgent
    #
    def reloadConfigAgent(self):
        ret = bool()
        #
        #implementCODE
        #
        return ret


    #
    # activateAgent
    #
    def activateAgent(self, prs):
        ret = bool()
        #
        #implementCODE
        #
        return ret


    #
    # setAgentParameters
    #
    def setAgentParameters(self, prs):
        ret = bool()
        #
        #implementCODE
        #
        return ret


    #
    # getAgentParameters
    #
    def getAgentParameters(self):
        ret = ParameterMap()
        #
        #implementCODE
        #
        return ret


    #
    # killAgent
    #
    def killAgent(self):
        #
        #implementCODE
        #
        pass


    #
    # uptimeAgent
    #
    def uptimeAgent(self):
        ret = int()
        #
        #implementCODE
        #
        return ret


    #
    # deactivateAgent
    #
    def deactivateAgent(self):
        ret = bool()
        #
        #implementCODE
        #
        return ret


    #
    # getAgentState
    #
    def getAgentState(self):
        ret = StateStruct()
        #
        #implementCODE
        #
        return ret

