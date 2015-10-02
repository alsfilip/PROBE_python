"""
September 23rd, 2015 - Alex Filipowicz

This is a python version of the PROBE task. 
It uses the exact same sequence, size, and colour scheme as the MATLAB version, but will be implemented in psychopy
rather than Psych TOOLBOX. This is the version that will be used with undergrads and potentially WRAP participants.

STILL TO DO - Check trial indexing and feedback mapping - instruction/break screens
"""
from psychopy import core, visual, event
import os
import time
import random

############################
# Participants information #
############################

#Test parameters
subNum = 1
subID = 999
category = 'test'#"UG"
sess = 1
run = 1

#for testing purposes - goes through task automatically and quickly - just change key recording in trials() line 198
test = True
#############
# Task sets #
#############

# Episode - i.e., nth mapping the person's been exposed to
#ep1 = ['1','1','1'] for testing
ep1 = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4']
ep2 = ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8']
ep3 = ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12']
ep4 = ['13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '14', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16']
ep5 = ['17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '18', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '19', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20']
ep6 = ['21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '21', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '22', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '23', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24', '24']
eps = [ep1,ep2,ep3,ep4,ep5,ep6]

# Number (1,2 or 3) to be displayed (e.g., in the 1,3,5 set, 1=1,2=3,3=5) - applies to both conditions
#nums1= ['2', '3', '3']#for testing
nums1 = ['2', '3', '3', '1', '2', '2', '3', '3', '1', '2', '1', '3', '2', '2', '1', '2', '3', '2', '1', '3', '1', '1', '1', '3', '1', '2', '3', '1', '2', '2', '2', '3', '3', '1', '2', '1', '3', '1', '2', '1', '2', '2', '3', '3', '1', '3', '1', '3', '2', '1', '1', '2', '3', '3', '1', '3', '3', '2', '2', '3', '2', '1', '1', '1', '3', '3', '2', '1', '3', '1', '2', '2', '3', '1', '2', '2', '3', '1', '3', '1', '1', '2', '3', '1', '3', '2', '3', '1', '3', '3', '1', '1', '2', '2', '2', '2', '2', '2', '2', '3', '2', '2', '3', '3', '3', '3', '3', '1', '3', '3', '1', '1', '2', '1', '3', '3', '1', '2', '3', '1', '2', '1', '1', '2', '3', '3', '2', '2', '1', '2', '2', '1', '2', '3', '2', '1', '1', '1', '3', '1', '3', '1', '1', '2', '1', '1', '1', '2', '2', '2', '1', '3', '2', '3', '3', '3', '2', '1', '1', '1', '2', '1', '3', '3', '2', '2', '1', '3', '3', '1', '2', '3', '3', '3', '1', '3', '2', '1', '2', '2']
nums2= ['3', '1', '3', '2', '2', '3', '3', '2', '1', '3', '3', '3', '1', '3', '1', '1', '1', '2', '1', '1', '1', '2', '1', '3', '2', '1', '2', '2', '1', '2', '2', '2', '2', '1', '1', '3', '3', '3', '2', '3', '3', '2', '1', '2', '1', '2', '3', '2', '2', '2', '1', '2', '3', '3', '3', '1', '3', '3', '1', '2', '3', '3', '1', '2', '1', '2', '3', '2', '3', '1', '3', '1', '2', '1', '1', '3', '3', '2', '2', '1', '2', '1', '1', '3', '2', '3', '3', '1', '1', '2', '1', '3', '2', '2', '1', '3', '1', '3', '2', '1', '1', '3', '1', '2', '3', '3', '2', '3', '2', '1', '2', '2', '3', '3', '2', '2', '2', '3', '3', '2', '3', '2', '1', '1', '3', '1', '3', '3', '2', '2', '3', '3', '2', '2', '1', '1', '3', '2', '1', '2', '1', '1', '1', '1', '2', '2', '3', '1', '2', '1', '3', '1', '1', '1', '1', '3', '3', '3', '2']
nums3= ['2', '3', '3', '1', '2', '2', '2', '2', '2', '1', '3', '1', '1', '1', '3', '2', '2', '1', '1', '1', '3', '2', '1', '1', '1', '3', '3', '2', '2', '3', '3', '3', '1', '2', '2', '1', '3', '2', '1', '1', '1', '3', '2', '3', '3', '3', '3', '2', '3', '1', '1', '1', '1', '1', '3', '1', '3', '2', '2', '3', '2', '3', '3', '3', '3', '2', '1', '2', '1', '3', '2', '2', '2', '2', '2', '3', '2', '1', '1', '3', '1', '2', '2', '3', '2', '1', '2', '1', '1', '2', '3', '1', '3', '1', '2', '3', '2', '1', '3', '3', '3', '2', '1', '2', '3', '3', '3', '1', '2', '3', '2', '2', '2', '1', '1', '1', '2', '1', '3', '3', '3', '1', '1', '2', '1', '1', '2', '3', '1', '2', '1', '3', '1', '3', '1', '1', '3', '2', '2', '1', '2', '3', '2', '3', '1', '2', '2', '1', '3', '2', '2', '3', '3', '3', '2', '3', '1', '3', '1']
nums4= ['1', '2', '1', '2', '3', '3', '3', '3', '3', '2', '3', '1', '3', '3', '2', '1', '2', '2', '3', '3', '2', '3', '2', '1', '1', '1', '2', '3', '2', '2', '2', '1', '2', '1', '3', '1', '1', '3', '3', '2', '1', '1', '2', '1', '1', '3', '2', '1', '2', '1', '1', '1', '1', '2', '3', '1', '3', '2', '2', '2', '1', '3', '2', '2', '2', '3', '3', '1', '3', '1', '2', '1', '3', '1', '3', '1', '3', '2', '2', '1', '1', '2', '3', '2', '1', '3', '2', '3', '3', '3', '2', '3', '1', '1', '3', '3', '1', '3', '2', '2', '2', '1', '2', '1', '2', '2', '2', '3', '2', '1', '1', '3', '2', '1', '1', '3', '1', '3', '3', '3', '2', '1', '3', '3', '1', '2', '1', '1', '2', '2', '3', '3', '2', '1', '3', '3', '3', '2', '2', '1', '1', '1', '3', '3', '2', '2', '1', '1', '1', '3', '1', '3', '2', '3', '1', '2', '2', '2', '3']
nums5= ['3', '3', '2', '1', '1', '2', '1', '1', '3', '1', '2', '2', '2', '3', '2', '1', '3', '3', '3', '1', '1', '3', '2', '1', '2', '3', '1', '2', '2', '3', '1', '3', '1', '2', '3', '2', '3', '1', '2', '1', '2', '1', '3', '2', '3', '3', '1', '1', '1', '3', '3', '3', '3', '2', '1', '1', '2', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '2', '1', '1', '1', '2', '3', '3', '3', '3', '3', '3', '3', '3', '1', '3', '1', '1', '3', '2', '3', '2', '2', '1', '3', '3', '1', '2', '1', '3', '2', '3', '2', '2', '2', '2', '3', '2', '1', '1', '2', '1', '1', '2', '2', '2', '1', '2', '1', '1', '1', '1', '3', '1', '2', '3', '1', '3', '1', '3', '3', '3', '1', '3', '2', '1', '2', '3', '2', '2', '3', '1', '1', '1', '2', '1', '2', '2', '2', '3', '1', '2', '1', '3', '2', '1', '2', '3']
nums6= ['1', '3', '2', '3', '1', '1', '3', '3', '3', '2', '3', '3', '3', '2', '2', '2', '1', '2', '1', '1', '2', '2', '1', '3', '2', '2', '1', '1', '2', '1', '3', '3', '1', '2', '2', '3', '1', '1', '1', '3', '3', '2', '2', '1', '2', '3', '2', '2', '1', '2', '2', '1', '2', '1', '3', '3', '1', '2', '3', '1', '1', '3', '3', '3', '1', '2', '3', '1', '3', '1', '3', '1', '1', '2', '1', '1', '1', '1', '1', '3', '3', '2', '1', '1', '2', '1', '3', '2', '1', '3', '2', '2', '3', '2', '2', '3', '3', '3', '3', '1', '3', '3', '2', '3', '2', '2', '2', '2', '2', '1', '3', '2', '3', '3', '1', '1', '2', '2', '3', '2', '2', '3', '3', '1', '3', '2', '2', '2', '1', '2', '2', '2', '3', '2', '1', '1', '1', '3', '3', '2', '2', '3', '2', '1', '3', '1', '2', '3', '1', '3', '3', '1', '1', '1', '3', '1', '3', '1', '1']
nums = [nums1,nums2,nums3,nums4,nums5,nums6]

#Correct locations for Change condition
#cLoc1 = ['1', '3', '3']#for testing
cLoc1 = ['1', '3', '3', '2', '1', '1', '3', '3', '2', '1', '2', '3', '1', '1', '2', '1', '3', '1', '2', '3', '2', '2', '2', '3', '2', '1', '3', '2', '1', '1', '1', '3', '3', '2', '1', '2', '3', '2', '1', '2', '1', '1', '3', '3', '2', '3', '2', '3', '3', '1', '1', '3', '4', '4', '1', '4', '4', '3', '3', '4', '3', '1', '1', '1', '4', '4', '3', '1', '4', '1', '3', '3', '4', '1', '3', '3', '4', '1', '4', '1', '1', '3', '4', '1', '4', '3', '4', '1', '4', '4', '1', '1', '3', '3', '3', '3', '2', '2', '2', '1', '2', '2', '1', '1', '1', '1', '1', '4', '1', '1', '4', '4', '2', '4', '1', '1', '4', '2', '1', '4', '2', '4', '4', '2', '1', '1', '2', '2', '4', '2', '2', '4', '2', '1', '2', '4', '4', '4', '1', '4', '1', '4', '4', '2', '3', '3', '3', '4', '4', '4', '3', '2', '4', '2', '2', '2', '4', '3', '3', '3', '4', '3', '2', '2', '4', '4', '3', '2', '2', '3', '4', '2', '2', '2', '3', '2', '4', '3', '4', '4']
cLoc2 = ['4', '2', '4', '1', '1', '4', '4', '1', '2', '4', '4', '4', '2', '4', '2', '2', '2', '1', '2', '2', '2', '1', '2', '4', '1', '2', '1', '1', '2', '1', '1', '1', '1', '2', '2', '4', '4', '4', '1', '4', '4', '1', '1', '2', '1', '2', '3', '2', '2', '2', '1', '2', '3', '3', '3', '1', '3', '3', '1', '2', '3', '3', '1', '2', '1', '2', '3', '2', '3', '1', '3', '1', '2', '1', '1', '1', '1', '3', '3', '4', '3', '4', '4', '1', '3', '1', '1', '4', '4', '3', '4', '1', '3', '3', '4', '1', '4', '1', '3', '4', '4', '1', '4', '3', '1', '1', '3', '1', '3', '4', '3', '1', '2', '2', '1', '1', '1', '2', '2', '1', '2', '1', '3', '3', '2', '3', '2', '2', '1', '1', '2', '2', '1', '1', '3', '3', '2', '1', '3', '1', '3', '3', '3', '3', '1', '1', '2', '3', '1', '3', '2', '3', '3', '3', '3', '2', '2', '2', '1']
cLoc3 = ['2', '4', '4', '1', '2', '2', '2', '2', '2', '1', '4', '1', '1', '1', '4', '2', '2', '1', '1', '1', '4', '2', '1', '1', '1', '4', '4', '2', '2', '4', '4', '4', '1', '2', '2', '1', '4', '2', '1', '1', '1', '4', '2', '4', '4', '4', '4', '2', '3', '2', '2', '2', '2', '2', '3', '2', '3', '4', '4', '3', '4', '3', '3', '3', '3', '4', '2', '4', '2', '3', '4', '4', '4', '4', '4', '3', '4', '2', '2', '3', '2', '1', '1', '2', '1', '4', '1', '4', '4', '1', '2', '4', '2', '4', '1', '2', '1', '4', '2', '2', '2', '1', '4', '1', '2', '2', '2', '4', '1', '2', '1', '1', '1', '4', '4', '4', '1', '4', '2', '2', '2', '4', '4', '2', '3', '3', '2', '1', '3', '2', '3', '1', '3', '1', '3', '3', '1', '2', '2', '3', '2', '1', '2', '1', '3', '2', '2', '3', '1', '2', '2', '1', '1', '1', '2', '1', '3', '1', '3']
cLoc4 = ['4', '1', '4', '1', '3', '3', '3', '3', '3', '1', '3', '4', '3', '3', '1', '4', '1', '1', '3', '3', '1', '3', '1', '4', '4', '4', '1', '3', '1', '1', '1', '4', '1', '4', '3', '4', '4', '3', '3', '1', '4', '4', '1', '4', '4', '3', '1', '4', '3', '2', '2', '2', '2', '3', '4', '2', '4', '3', '3', '3', '2', '4', '3', '3', '3', '4', '4', '2', '4', '2', '3', '2', '4', '2', '4', '2', '4', '3', '3', '2', '2', '3', '4', '3', '2', '4', '3', '4', '4', '4', '4', '2', '1', '1', '2', '2', '1', '2', '4', '4', '4', '1', '4', '1', '4', '4', '4', '2', '4', '1', '1', '2', '4', '1', '1', '2', '1', '2', '2', '2', '4', '1', '2', '1', '2', '3', '2', '2', '3', '3', '1', '1', '3', '2', '1', '1', '1', '3', '3', '2', '2', '2', '1', '1', '3', '3', '2', '2', '2', '1', '2', '1', '3', '1', '2', '3', '3', '3', '1']
cLoc5 = ['4', '4', '1', '3', '3', '1', '3', '3', '4', '3', '1', '1', '1', '4', '1', '3', '4', '4', '4', '3', '3', '4', '1', '3', '1', '4', '3', '1', '1', '4', '3', '4', '3', '1', '4', '1', '3', '4', '2', '4', '2', '4', '3', '2', '3', '3', '4', '4', '4', '3', '3', '3', '3', '2', '4', '4', '2', '4', '4', '4', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '2', '4', '4', '4', '2', '3', '2', '2', '2', '2', '2', '2', '2', '1', '2', '1', '1', '2', '3', '2', '3', '3', '1', '2', '2', '1', '3', '1', '2', '3', '2', '3', '3', '3', '3', '2', '3', '1', '1', '3', '1', '1', '3', '3', '3', '1', '3', '1', '1', '1', '1', '2', '1', '3', '1', '3', '1', '3', '1', '1', '1', '3', '1', '4', '3', '4', '1', '4', '4', '1', '3', '3', '3', '4', '3', '4', '4', '4', '1', '3', '4', '3', '1', '4', '3', '4', '1']
cLoc6 = ['4', '2', '3', '2', '4', '4', '2', '2', '2', '3', '2', '2', '2', '3', '3', '3', '4', '3', '4', '4', '3', '3', '4', '2', '3', '3', '4', '4', '3', '4', '2', '2', '4', '4', '4', '1', '2', '2', '2', '1', '1', '4', '4', '2', '4', '1', '4', '4', '2', '4', '4', '2', '4', '2', '1', '1', '2', '4', '1', '2', '2', '1', '1', '1', '2', '4', '1', '2', '1', '3', '4', '3', '3', '2', '3', '3', '3', '3', '3', '4', '4', '2', '3', '3', '2', '3', '4', '2', '3', '4', '2', '2', '4', '2', '2', '4', '4', '4', '4', '3', '4', '4', '2', '4', '2', '2', '2', '2', '2', '3', '4', '4', '3', '3', '1', '1', '4', '4', '3', '4', '4', '3', '3', '1', '3', '4', '4', '4', '1', '4', '4', '4', '3', '4', '1', '1', '1', '3', '3', '4', '4', '3', '4', '1', '3', '1', '4', '3', '1', '3', '3', '1', '1', '1', '3', '1', '3', '1', '1']
cLocs = [cLoc1,cLoc2,cLoc3,cLoc4,cLoc5,cLoc6]

#Correct locations for Same condition
#sLoc1 = ['3', '4', '4']#for testing
sLoc1 = ['3', '4', '4', '1', '3', '3', '4', '4', '1', '3', '1', '4', '3', '3', '1', '3', '4', '3', '1', '4', '1', '1', '1', '4', '1', '3', '4', '1', '3', '3', '3', '4', '4', '1', '3', '1', '4', '1', '3', '1', '3', '3', '4', '4', '1', '4', '1', '4', '1', '4', '4', '1', '2', '2', '4', '2', '2', '1', '1', '2', '1', '4', '4', '4', '2', '2', '1', '4', '2', '4', '1', '1', '2', '4', '1', '1', '2', '4', '2', '4', '4', '1', '2', '4', '2', '1', '2', '4', '2', '2', '4', '4', '1', '1', '1', '1', '4', '4', '4', '3', '4', '4', '3', '3', '3', '3', '3', '2', '3', '3', '2', '2', '4', '2', '3', '3', '2', '4', '3', '2', '4', '2', '2', '4', '3', '3', '4', '4', '2', '4', '4', '2', '4', '3', '4', '2', '2', '2', '3', '2', '3', '2', '2', '4', '1', '1', '1', '3', '3', '3', '1', '4', '3', '4', '4', '4', '3', '1', '1', '1', '3', '1', '4', '4', '3', '3', '1', '4', '4', '1', '3', '4', '4', '4', '1', '4', '3', '1', '3', '3']
sLoc2 = ['2', '4', '2', '1', '1', '2', '2', '1', '4', '2', '2', '2', '4', '2', '4', '4', '4', '1', '4', '4', '4', '1', '4', '2', '1', '4', '1', '1', '4', '1', '1', '1', '1', '4', '4', '2', '2', '2', '1', '2', '2', '1', '1', '3', '1', '3', '4', '3', '3', '3', '1', '3', '4', '4', '4', '1', '4', '4', '1', '3', '4', '4', '1', '3', '1', '3', '4', '3', '4', '1', '4', '1', '3', '1', '1', '2', '2', '1', '1', '4', '1', '4', '4', '2', '1', '2', '2', '4', '4', '1', '4', '2', '1', '1', '4', '2', '4', '2', '1', '4', '4', '2', '4', '1', '2', '2', '1', '2', '1', '4', '1', '4', '3', '3', '4', '4', '4', '3', '3', '4', '3', '4', '2', '2', '3', '2', '3', '3', '4', '4', '3', '3', '4', '4', '2', '2', '3', '4', '2', '4', '2', '2', '2', '2', '4', '4', '3', '2', '4', '2', '3', '2', '2', '2', '2', '3', '3', '3', '4']
sLoc3 = ['3', '4', '4', '1', '3', '3', '3', '3', '3', '1', '4', '1', '1', '1', '4', '3', '3', '1', '1', '1', '4', '3', '1', '1', '1', '4', '4', '3', '3', '4', '4', '4', '1', '3', '3', '1', '4', '3', '1', '1', '1', '4', '3', '4', '4', '4', '4', '3', '3', '2', '2', '2', '2', '2', '3', '2', '3', '4', '4', '3', '4', '3', '3', '3', '3', '4', '2', '4', '2', '3', '4', '4', '4', '4', '4', '3', '4', '2', '2', '3', '2', '1', '1', '2', '1', '4', '1', '4', '4', '1', '2', '4', '2', '4', '1', '2', '1', '4', '2', '2', '2', '1', '4', '1', '2', '2', '2', '4', '1', '2', '1', '1', '1', '4', '4', '4', '1', '4', '2', '2', '2', '4', '4', '3', '1', '1', '3', '4', '1', '3', '1', '4', '1', '4', '1', '1', '4', '3', '3', '1', '3', '4', '3', '4', '1', '3', '3', '1', '4', '3', '3', '4', '4', '4', '3', '4', '1', '4', '1']
sLoc4 = ['2', '4', '2', '4', '3', '3', '3', '3', '3', '4', '3', '2', '3', '3', '4', '2', '4', '4', '3', '3', '4', '3', '4', '2', '2', '2', '4', '3', '4', '4', '4', '2', '4', '2', '3', '2', '2', '3', '3', '4', '2', '2', '4', '2', '2', '3', '4', '2', '1', '4', '4', '4', '4', '1', '2', '4', '2', '1', '1', '1', '4', '2', '1', '1', '1', '2', '2', '4', '2', '4', '1', '4', '2', '4', '2', '4', '2', '1', '1', '4', '4', '1', '2', '1', '4', '2', '1', '2', '2', '2', '3', '4', '1', '1', '4', '4', '1', '4', '3', '3', '3', '1', '3', '1', '3', '3', '3', '4', '3', '1', '1', '4', '3', '1', '1', '4', '1', '4', '4', '4', '3', '1', '4', '3', '2', '4', '2', '2', '4', '4', '3', '3', '4', '2', '3', '3', '3', '4', '4', '2', '2', '2', '3', '3', '4', '4', '2', '2', '2', '3', '2', '3', '4', '3', '2', '4', '4', '4', '3']
sLoc5 = ['2', '2', '1', '4', '4', '1', '4', '4', '2', '4', '1', '1', '1', '2', '1', '4', '2', '2', '2', '4', '4', '2', '1', '4', '1', '2', '4', '1', '1', '2', '4', '2', '4', '1', '2', '1', '3', '2', '4', '2', '4', '2', '3', '4', '3', '3', '2', '2', '2', '3', '3', '3', '3', '4', '2', '2', '4', '2', '2', '2', '4', '4', '4', '4', '4', '4', '4', '3', '3', '3', '3', '3', '4', '2', '2', '2', '4', '3', '4', '4', '4', '4', '4', '4', '4', '1', '4', '1', '1', '4', '3', '4', '3', '3', '1', '4', '4', '1', '3', '1', '4', '3', '4', '3', '3', '3', '3', '4', '3', '1', '1', '3', '1', '1', '3', '3', '3', '1', '3', '1', '1', '1', '1', '4', '1', '3', '3', '2', '3', '2', '3', '3', '3', '2', '3', '4', '2', '4', '3', '4', '4', '3', '2', '2', '2', '4', '2', '4', '4', '4', '3', '2', '4', '2', '3', '4', '2', '4', '3']
sLoc6 = ['1', '4', '3', '4', '1', '1', '4', '4', '4', '3', '4', '4', '4', '3', '3', '3', '1', '3', '1', '1', '3', '3', '1', '4', '3', '3', '1', '1', '3', '1', '4', '4', '1', '1', '1', '2', '4', '4', '4', '2', '2', '1', '1', '4', '1', '2', '1', '1', '4', '1', '1', '4', '1', '4', '2', '2', '4', '1', '2', '4', '4', '2', '2', '2', '4', '1', '2', '4', '2', '2', '3', '2', '2', '4', '2', '2', '2', '2', '2', '3', '3', '4', '2', '2', '4', '2', '3', '4', '2', '3', '4', '4', '3', '4', '4', '3', '3', '3', '3', '2', '3', '3', '4', '3', '4', '4', '4', '4', '4', '2', '3', '1', '2', '2', '4', '4', '1', '1', '2', '1', '1', '2', '2', '4', '2', '1', '1', '1', '4', '1', '1', '1', '2', '1', '4', '4', '4', '2', '2', '1', '1', '2', '1', '4', '2', '4', '1', '2', '4', '2', '2', '4', '4', '4', '2', '4', '2', '4', '4']
sLocs = [sLoc1,sLoc2,sLoc3,sLoc4,sLoc5,sLoc6]

# Trap trial (1) or no trap (0) - applies to both conditions
#trap1 = ['0', '0', '1']#for testing
trap1 = ['0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0']
trap2 = ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0']
trap3 = ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0']
trap4 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0']
trap5 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1']
trap6 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1']
traps = [trap1,trap2,trap3,trap4,trap5,trap6]

#Strategy numbers for the same condition
#sStrat1 = ['3', '3', '3']#for testing
sStrat1 = ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3']
sStrat2 = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
sStrat3 = ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3']
sStrat4 = ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
sStrat5 = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
sStrat6 = ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
sStrats = [sStrat1,sStrat2,sStrat3,sStrat4,sStrat5,sStrat6]
cStrat = eps

setLoc = None
strat = None
sesstype = None
if sess == 1:
    setLoc = sLocs
    strat = sStrats
    sesstype = "Same"
elif sess == 2:
    setLoc = cLocs
    strat = cStrats
    sesstype = "Change"

##################
# Data recording #
##################

path = os.getcwd()
date_time=time.asctime()
dt=date_time.replace(' ','_')
dt2 = dt.replace(':','_')
# Initialize data file
datafile = file(path+'//data//'+str(category)+'_'+str(subID)+'_'+str(subNum)+'_'+str(sess)+'_'+sesstype+'_'+str(run)+'_'+dt2+'.csv','wb')
dataHeader = ["Category","SubID","SubNum","Strat","NumPres","Location","Trap", "Run", "TotalTrial","RunTrial","StratTrial","SubResp","KeyCode","Correct","Reward","RT"]
datafile.write(",".join(dataHeader)+'\n')
datafile.flush()
# Function to record data
def recData(cat,sid,snum,sts,npres,loca,ts,r,tottr,rtr,strtr,subres,keycd,cor,rw,rt):
    dat = map(str,[cat,sid,snum,sts,npres,loca,ts,r,tottr,rtr,strtr,subres,keycd,cor,rw,rt])
    datafile.write(",".join(dat)+'\n')
    datafile.flush()

####################
# Task environment #
####################

# Colors
corrCol = (-1,1,-1)#"green" #color for correct response
errCol = (1,-1,-1)#"red" #color for incorrect response
backG = (-1,-1,-1)
textCol = (1,1,1)

# Experimental window
if test == False:
	win = visual.Window(units = 'pix',color = backG, fullscr = True)
elif test == True:
    win = visual.Window(units = 'pix', color = backG)#make small window for testing purposes

# Buffer stimulus boxes, centre circle, and text stimulus (numbers)
boxSize = 120
textHeight = 100
backRect = visual.Rect(win, width=boxSize*4+10,height = boxSize+10,fillColor = textCol)
stimBox = {}
numStim = {}
posStart = -boxSize - (boxSize/2)
for i in range(4):
    stimBox[i]=visual.Rect(win,width=boxSize,height = boxSize,pos = (posStart,0), fillColor = backG,lineWidth = 10,lineColor = textCol)
    numStim[i]=visual.TextStim(win,text='0',font='Arial',height = textHeight,pos=(posStart,0))
    posStart += boxSize
circ = visual.Circle(win,radius = 8,fillColor = textCol)
# Dictionary to map keys to spatial positions
keyDict = {'j':"1",'k':"2",'l':"3",'semicolon':"4"}

#Sets
numSet = None
if subNum % 2 == 1:
    if sess == 1:
        numSet = [1,3,5]
    elif sess == 2:
        numSet = [2,4,6]
elif subNum % 2 == 0:
    if sess == 1:
        numSet = [2,4,6]
    elif sess == 2:
        numSet = [1,3,5]

# Timing
feedbackTime = .8 #display time
isi = .4
feedbackDel = .1
if test == True:
    feedbackTime = 0 #display time
    isi = 0
    feedbackDel = 0

# Function to draw stimuli
def stimDraw(n, pos = None, col = False):
    backRect.draw()
    if pos == None:
        for i in range(4):
            numStim[i].setText(n)
            stimBox[i].draw()
            numStim[i].draw()
    else:
        for i in range(4):
            stimBox[i].draw()
        numStim[pos-1].setText(n)
        numStim[pos-1].setColor(col)
        numStim[pos-1].draw()
    circ.draw()
    win.flip()
    for i in range(4):
        numStim[i].setColor(textCol)

# runs the trials
def trials(n,maps,tp,rInfo):
    stimDraw(" ")
    core.wait(isi)
    stim = numSet[int(n)-1]
    stimDraw(stim) #Draw initial stim
    #rtClock = core.Clock() #Clock to measure RTs
    RT = None
    if test == False:
    	rtClock = core.Clock()
    	keys = event.waitKeys(keyList=['j','k','l','semicolon','q','escape']) #Wait for a keypress
    	RT = rtClock.getTime()
    elif test == True:
    	rtClock = core.Clock()
    	keys = random.choice([['j'],['k'],['l'],['semicolon']])#comment above line and ucomment this one for testing
    	RT = rtClock.getTime()
    #RT = rtClock.getTime() #Get RT
    if keys[0] in ['q','escape']:
        core.quit()
    loc = keyDict[keys[0]] #Get which key has been presses
    resp = None #Participant response
    rCol = None #Feedback colour placeholder
    #Guides trap trials (Correct feedback for incorrect response, and vice versa)
    stimDraw(" ")
    core.wait(feedbackDel)
    correct = None
    fback = None
    if loc == maps:
        correct = 1
    else:
        correct = 0
    if int(tp) == 0:
        if loc == maps:
            fback = 1
            resp = stim
            rCol = corrCol
        else:
            fback = 0
            resp = "X"
            rCol = errCol
    elif int(tp) == 1:
        if loc == maps:
            fback = 0
            resp = "X"
            rCol = errCol
        else:
            fback = 1
            resp = stim
            rCol = corrCol
    tottr = 1
    rtr = 1
    strtr = 1
    stimDraw(resp,pos=int(loc),col=rCol)
    recData(rInfo[0],rInfo[1],rInfo[2],rInfo[3],rInfo[4],rInfo[5],tp,rInfo[6],rInfo[7],rInfo[8],rInfo[9],loc,keys[0],correct,fback,RT)
    #recData(category,subID,subNum,strat,num,maps,trap,run,tottr,rtr,strtr,loc,keys[0],correct,fback,RT)
    core.wait(feedbackTime)

#################################
# Instruction and break screens #
#################################

def startScreen():
    ts = visual.TextStim(win,text="Get ready...", height = 30)
    ts.draw()
    win.flip()
    if test == True:
        core.wait(2)
    else:
        key = event.waitKeys()

def breakScreen(r):
    bt = "Block "+str(r)+" of 6 completed.\nPress any key to start next block."
    if r == 6:
        bt = 'Block 6 of 6 completed.\nPlease see the RA for further instructions.'
    tt = visual.TextStim(win,text=bt,height=30)
    tt.draw()
    win.flip()
    if test == True:
        core.wait(2)
    else:
        key = event.waitKeys()

#################
# Trial Handler #
#################
startScreen()
totTrial = 1
for run in range(6):
    ep=eps[run]
    num=nums[run]
    corrLocs = setLoc[run]
    trap=traps[run]
    sts = strat[run]
    runNum = run+1
    runTrial = 1
    currEp = ep[0]
    epTrial = 1
    for trial in range(len(ep)):
        trialEp = ep[trial]
        if currEp != trialEp:
            currEp = trialEp
            epTrial = 1
        tNum = num[trial]
        cL = corrLocs[trial]
        trp = trap[trial]
        st = sts[trial]
        recInfo = [category, subID, subNum, st, tNum, cL,runNum,totTrial,runTrial,epTrial]
        trials(tNum,cL,trp,recInfo)
        totTrial += 1
        runTrial += 1
        epTrial += 1
    breakScreen(run+1)

