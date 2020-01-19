from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from django.core import serializers
from .models import Profile, Job, Question, ProfileQuestionMapping, Option


def profiles(request):
    if request.method == 'GET':
        all_profiles = Profile.objects.all()
        all_profiles_json = serializers.serialize('json', all_profiles)
        return HttpResponse(all_profiles_json, content_type='application/json')

    if request.method == 'POST':
        for values in (json.loads(request.body)).values():
            for profile_id, title in values.items():
                new_profile = Profile(profile_id=profile_id, title=title)
                new_profile.save()

        return HttpResponse("Bhar diya!!")


def jobs(request):
    if request.method == 'POST':
        profile_id = json.loads(request.body)
        profile_id = profile_id["profile_id"]
        profile = Profile.objects.get(pk=profile_id)
        new_job = profile.job_set.create()
        return HttpResponse(new_job.job_id)

    if request.method == 'GET':
        x = Job.objects.all()
        x_json = serializers.serialize('json', x)
        return HttpResponse(x_json, content_type='application/json')

    if request.method == 'PUT':
        body = json.loads(request.boy)
        parameter = body['parameter']
        job_id = body['profile_id']
        type_of_question = body['type_of_question']

        if(type_of_question == )

        MyModel.objects.filter(pk=some_value).update(field1='some value'
        profile =

    return HttpResponse("Bhar diya!!")


def questions(request):
    if request.method == 'GET':
        job_id = json.loads(request.body)
        job_id = job_id["job_id"]
        print(job_id)
        profiles_id = Job.objects.get(pk=job_id).profile
        pqms = ProfileQuestionMapping.objects.filter(profile_id=profiles_id).order_by('order')
        question_set = {}
        for i in pqms:

            question = i.question
            qoms = Option.objects.filter(question_id=question.question_id)
            options = []
            for j in qoms:
                options.append(j.title)

            question_dic = {'job_id': job_id, 'default': i.default, 'should_display': i.should_display, 'is_required': i.is_required, 'parameter': question.parameter,
                            'type of question': question.type, 'options': options}

            question_set[question.question_id] = question_dic
        question_json = json.dumps(question_set)
        return HttpResponse(question_json, content_type='application/json')

    return HttpResponse("Mujhe nahi pata!")

    #     if request.method == 'GET':
    #         # select profile_id from jobs where job_id= given
    #         job_id = json.loads(request.body)
    #         job_id = job_id["job_id"]
    #         profile_id = Job.objects.get(pk=job_id).profile
    #         pqms = ProfileQuestionMapping.objects.filter(profile_id=profile_id).order_by('order')
#         for i in pqms:
#           default = i.default
#           should_display = i.should_display
#           is_required = i.is_required
#           question_get = Question.objects.get(pk=i)
#           title = question_get.title
#           parameter = question_get.title
#           type = Question_get.type
#           options_get = Option.objects.filter(question_id = i.question.question_id)
#           options =[]
#           for j in options_get:
#               options.append(j.option_id)

#
#
#
#
#
#
#
#           print(i.question.question_id) // questions

# select question_id, default, is_required, should_display, order by order from PQM
# for each question_id in above query, select questions name, parameter, type from question
# for each question_id in above query, select whether to load question or not, then load option_id, title

#     question = models.ForeignKey(Question)
# def questions(request): if request.method == 'GET': all_questions = Question.objects.all() # order by
# ProfileQuestionMapper # this should include all the questions, should display, is_required, default, title,
# parameter, type in json format. We will select all the questions details, along with extra parameters which are there
# related to a particular profile then we will select all the options which are related to each particular question
# all_questions_jso
# def questions(request):
#     if request.method == 'GET':
#         job_id = json.loads(request.body)
#         job_id = job_id["job_id"]
#         print(job_id)
#         profiles_id = Job.objects.get(pk=job_id).profile
#         pqms = ProfileQuestionMapping.objects.filter(profile_id=profiles_id).order_by('order')
#         question_set = {}
#         for i in pqms:
#
#             question = i.question
#             qoms = Option.objects.filter(question_id=question.question_id)
#             options = []
#             for j in qoms:
#                 options.append(j.title)
#
#             question_dic = {'job_id': job_id, 'default': i.default, 'should_display': i.should_display, 'is_required': i.is_required, 'parameter': question.parameter,
#                             'type of question': question.type, 'options': options}
#
#             question_set[question.question_id] = question_dic
#         question_json = json.dumps(question_set)
#         return HttpResponse(question_json, content_type='application/json')
#
#     return HttpResponse("Mujhe nahi pata!")
#
#     #     if request.method == 'GET':
#     #         # select profile_id from jobs where job_id= given
#     #         job_id = json.loads(request.body)
#     #         job_id = job_id["job_id"]
#     #         profile_id = Job.objects.get(pk=job_id).profile
#     #         pqms = ProfileQuestionMapping.objects.filter(profile_id=profile_id).order_by('order')
# #         for i in pqms:
# #           default = i.default
# #           should_display = i.should_display
# #           is_required = i.is_required
# #           question_get = Question.objects.get(pk=i)
# #           title = question_get.title
# #           parameter = question_get.title
# #           type = Question_get.type
# #           options_get = Option.objects.filter(question_id = i.question.question_id)
# #           options =[]
# #           for j in options_get:
# #               options.append(j.option_id)
#
# #
# #
# #
# #
# #
# #
# #
# #           print(i.question.question_id) // questions
#
# # select question_id, default, is_required, should_display, order by order from PQM
# # for each question_id in above query, select questions name, parameter, type from question
# # for each question_id in above query, select whether to load question or not, then load option_id, title
#
# #     question = models.ForeignKey(Question)
# # def questions(request): if request.method == 'GET': all_questions = Question.objects.all() # order by
# # ProfileQuestionMapper # this should include all the questions, should display, is_required, default, title,
# # parameter, type in json format. We will select all the questions details, along with extra parameters which are there
# # related to a particular profile then we will select all the options which are related to each particular question
# # all_questions_json = serializers.serialize('json', all_questions return HttpResponse(all_questions,
# # content_type='application/json')n = serializers.serialize('json', all_questions return HttpResponse(all_questions,
# content_type='application/json')
