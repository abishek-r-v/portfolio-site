from django.db import models


class TechStack(models.Model):
    class Meta:
        db_table = 'tech_stack'  # table_name

    CATEGORY = [
        ('PL', 'Programming Language'),
        ('DB', 'Database'),
        ('FE', 'Front-end'),
        ('TS', 'Tools or Software'),
    ]

    stack_name = models.CharField(max_length=50, primary_key=True)
    category = models.CharField(max_length=2, choices=CATEGORY)

    def __str__(self):
        return self.stack_name  # name displayed during dbshell


class Package(models.Model):
    class Meta:
        db_table = 'package'  # table_name

    PKG_TYPE = [
        ('EX', 'External package'),
        ('IN', 'Builtin package'),
    ]
    pkg_name = models.CharField(max_length=50)
    stack_name = models.ForeignKey(TechStack, on_delete=models.CASCADE)
    pkg_type = models.CharField(max_length=2, choices=PKG_TYPE)

    def __str__(self):
        return self.pkg_name  # name displayed during dbshell


class Framework(models.Model):
    class Meta:
        db_table = 'framework'  # table_name

    framework_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.framework_name  # name displayed during dbshell


class Project(models.Model):
    class Meta:
        db_table = 'project'  # table_name

    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    tech_stacks = models.ManyToManyField(TechStack)
    frameworks = models.ManyToManyField(Framework, blank=True)
    packages = models.ManyToManyField(Package, blank=True)
    entry_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.project_name  # name displayed during dbshell


class Image(models.Model):
    class Meta:
        db_table = 'image'  # table_name

    file_name = models.CharField(max_length=200)
    caption = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name  # name displayed during dbshell
