#!/usr/bin/python2.7
# encoding:utf-8
# pip install GitPython

import Deadline.DeadlineConnect as Connect
connectionObject = Connect.DeadlineCon('WebServiceName', 8082)
print connectionObject.Groups.GetGroupNames()
#["group1","group2","group3"]
#jobId = ...(valid job ID)
#print connectionObject.Jobs.SuspendJob(jobId)

