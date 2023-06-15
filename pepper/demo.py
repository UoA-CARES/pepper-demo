#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import naoqi
from robot import Pepper
import time
import random
import teleoperation as teleop


language = "en-US"

PeppperIP = "172.22.1.21"
robot = Pepper(PeppperIP,9559)

teleop.teleoperate_robot(robot)

