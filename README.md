# CapX_Task2
# Assist Capacity Exchange Development - Task 2

This task is a continuation of Task 1
## Objective of the task: Structure a SQLite database and create a django model for the Bug app.

Steps:
* Read the second part of the Writing your first Django app tutorial.
* Create a Bug model with the following fields: "description", "bug_type", "report_date", "status", representing, respectively, the textual description of the bug, the type of the bug (e.g. error, new feature etc), the date in which the bug is being registered and the status of resolution of the bug (e.g. to do, in progress, done, etc).
* Structure the database as described in the tutorial and create at least one bug through Django Admin.

# Observations in Contribution
1. I was able to create the home page of my bug app report site;

![Image](https://github.com/PaulaGweke/Outreachy_Contributions/blob/main/T347253/django_task2a.png)

3. Since the tutorial was using a different app type. I found it difficult to mimic the API shell as this is my introduction to django (which uses Python environment that I am familiar with).
4. In the shell however, a created a variable q from `Bug.objects.all()` and got a `QuerySet [<Bug: ERROR>]>` using `q = Bug(title="BUG_TYPES", report_date=datetime.date.today())`
   Since all my bug types are in title (see Bug/models.py), the bug can be selected from the drop down box of bug types created from q in the site. Hopefully, this was a good choice. I am hopeful to use this internship to learn how to optimize this step.

![Image](https://github.com/PaulaGweke/Outreachy_Contributions/blob/main/T347253/django_task2b.png)

![Image](https://github.com/PaulaGweke/Outreachy_Contributions/blob/main/T347253/django_task2c.png)

![Image](https://github.com/PaulaGweke/Outreachy_Contributions/blob/main/T347253/django_task2d.png)
   
5. I was able to launch the site to view the defined bugs using the shell command. I ran this project twice (the second attempt I submitted via pull commits). In my previous post, I complained about not able to view the admin tab forgetting that I was in the admin view upon login.
