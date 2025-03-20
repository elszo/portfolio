from django.shortcuts import render
from glob import glob

from main.models import Education, Experience, Project, Skill, Detailproject


def index(request):
    data_education = Education.objects.all()
    data_experience = Experience.objects.all()
    data_project = Project.objects.all()
    data_skill = Skill.objects.all()
    return render(request, 'main/index.html', context={'educations': data_education, 'experiences': data_experience,
                                                       'projects': data_project, "skills": data_skill})


def details(request, idprojet):

    item = Project.objects.get(id=idprojet)
    details_project = Detailproject.objects.get(projet=item)
    projets = Project.objects.all()

    images  = glob(f"main/static/{details_project.dossier_images}/*.png") + glob(f"main/static/{details_project.dossier_images}/*.jpg")
    images = [el.split("/")[-1] for el in images]
    images.sort()

    imgbase = ''
    if '4imagebase.png' in images:
        imgbase = '4imagebase.png'
        images.remove(imgbase)

    return render(request, f'main/details.html', context={'item': item, 'projets': projets[1:], 'details_project': details_project,
                                                          'images': images, 'imgbase': imgbase})
