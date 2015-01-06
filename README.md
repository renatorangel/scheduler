Scheduling courses using a CSP solver
========

**Library used:**

Python Constraint Solver (http://labix.org/python-constraint)

**Files**

**Problem:**

- Schedule all classes in the department for a given semester.

- The same instructor can't teach two different classes at the same time.

- Two classes should not be scheduled at the same time if they are likely to be taken concurrently.

- The instructor can select the preferable time to teach.

- No instructor should have consecutive classes in different buildings.

**Problem in CSP:**

- variables:courses
- domains: possible rooms 
- constraints: the requirements we mentioned above

