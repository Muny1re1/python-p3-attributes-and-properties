#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Unknown", job = "Unknown"):
        self.set_name(name)
        self.set_job(job)
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"
    
    name = property(get_name, set_name)

    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if (job not in APPROVED_JOBS):
            print("Job must be in list of approved jobs.")
        else:
            self._job = job

    job = property(get_job, set_job)
