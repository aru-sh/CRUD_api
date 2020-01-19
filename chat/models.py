from django.db import models


# Create your models here.
# Comment is for next line
class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


# Specific instance of a Profile, an employer can post many jobs of same profile
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    comp_name = models.CharField(max_length=50)
    exp = models.CharField(max_length=30)

    def __str__(self):
        return str(self.job_id)


# Skills is only there to PUT, not for GET
class Skills(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    sid = models.CharField(max_length=100)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Questions is GET from Question based on Profile id, ProfileQuestionMapping
class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    profile = models.ManyToManyField(Profile, through='ProfileQuestionMapping')
    question_name = models.CharField(max_length=200)
    # It is there to tell to which column to add this question's answer in Job table
    parameter = models.CharField(max_length=40)
    # Type is the type of options which needs to be populated'
    # 0 - Radiobutton, 1 - Checkbox, 2 - TextBox
    type = models.IntegerField()

    def __str__(self):
        return self.question_name


class ProfileQuestionMapping(models.Model):
    profile_id = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    # Order is the specific order in which questions will come
    order = models.IntegerField()
    # Default is the default value of question
    default = models.CharField(max_length=30)
    # Confusion between should display and is_required
    # should display shows whether to include this in the
    should_display = models.BooleanField()
    is_required = models.BooleanField()
    default = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Option(models.Model):
    option_id = models.IntegerField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=True)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
