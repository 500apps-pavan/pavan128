from behave import *
@given ('I reach office at "{time}" shift')
def step_implay(context,time):
      print("shift is :{}",format(time))