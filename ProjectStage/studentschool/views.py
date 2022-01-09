from django.shortcuts import render
from studentschool import models,forms


def Search(request):
    form_data = forms.StudentSearch(request.POST or None)
    msg = ''
    if form_data.is_valid():
        student_name = form_data.cleaned_data['name'].upper()
        if models.StudentStage.objects.filter(name=student_name):

            student = list(models.StudentStage.objects.filter(name=student_name))
            if student[0].image.find('data:image')>=0:
                #student[0].image = "{% static 'studentschool/images/photo-profil.jpg' %}"
                student[0].image = "https://upload.wikimedia.org/wikipedia/commons/e/e9/Linkedin_icon.svg"
            #msg = '<div class="card" style="width: 18rem;"><img src=".\images\serieux.jpg" class="card-img-top" alt="..."><div class="card-body"><h5 class="card-title">sérieux</h5><div  class="card-footer text-center txt"><h3>{}</h3></div>'.format(student[0].school)
            msg = '<div class="card mb-3" style="max-width: 540px;"><div class="row no-gutters"><div class="col-md-4"><img src="{}" class="card-img" alt="student_photo"></div><div class="col-md-8"><div class="card-body"><h5 class="card-title"><b>{}</b></h5><p class="card-text">{}</p><p class="card-text"><small class="text-muted">informations got from Linkedin</small></p></div></div></div></div>'.format(student[0].image,student_name,student[0].school)
            if student[0].school == "None":
                msg = "Student account found but it seems like if <b>{}</b> dosen't enter his studies informations to Linkedin ".format(student[0].name)
            if student[0].school == "account not found":
                mg = "We are using Linkedin accound to find students school but it seems that <strong>{}</strong> hasn't a Linkedin account".format(student_name)
                msg ='<div class="card mb-3 p-3 mb-2 bg-primary text-white" style="max-width: 540px;color:blue"><b>{}</b></div>'.format(mg)  
        else:
            mg = "Student doesn't figure in the list or try to enter 'family_name + name' Ex : KOUHOU MOHAMED  "
            #msg='<div><strong>{}</strong></div>'.format(mg)
            msg ='<div class="card mb-3 p-3 mb-2 bg-danger text-white" style="max-width: 540px;color:red"><b>{}</b></div>'.format(mg) 
            #msg = '<div class="alert alert-warning alert-dismissible fade show" role="alert"><strong>Holy guacamole!</strong> "Student doesnt figure in the list or try to enter family_name + name Ex : KOUHOU MOHAMED  "<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
    context = {'search':form_data,
               'msg':msg}
    return render(request, 'look.html', context)
