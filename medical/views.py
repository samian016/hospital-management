from django.shortcuts import render, redirect
from django.contrib import messages
from medical.models import Patient


def medical(request):
    return render(request, 'medical/medical.html')


def add(request):
    if request.method == 'GET':
        return render(request, 'medical/addp.html')
    elif request.method == 'POST':
        date = request.POST['date']
        first_name = request.POST['first']
        second_name = request.POST['second']
        dob = request.POST['dob']
        sex = request.POST['sex']
        maritals = request.POST['maritalS']
        children = request.POST['children']
        residence = request.POST['residence']
        nationality = request.POST['nationality']
        occupation = request.POST['occupation']
        religion = request.POST['religion']
        gfn = request.POST['g_first_name']
        gsn = request.POST['g_second_name']
        telephone = request.POST['telephone']
        disease = request.POST['disease']
        ward = request.POST['ward']
        bed = request.POST['bed']
        care_note = request.POST['care_note']
        transfer_from = request.POST['transfer_from']
        pulse = request.POST['pulse']
        bloodp = request.POST['bloodP']
        respiration = request.POST['respiration']
        temperature = request.POST['temperature']
        physical_con = request.POST['physical_con']
        patient = Patient.objects.create(date=date, status="Admitted", first_name=first_name, second_name=second_name, date_of_birth=dob, sex=sex, maritalS=maritals, childrenN=children, residence=residence, nationality=nationality, occupation=occupation, religion=religion, guardian_first_name=gfn, guardian_second_name=gsn, telephone=telephone, disease=disease, ward=ward, bed=bed, care_note=care_note, transfer_from=transfer_from, pulse=pulse, bloodP=bloodp, respiration=respiration, tempe=temperature, physical_con=physical_con)

        messages.info(request, "Patient profile Created...")
        return redirect('/medical/m')


def death(request):
    return render(request, 'medical/death.html')


def list(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            patients = Patient.objects.all()
            context = {
                'patients': patients
            }
            return render(request, 'medical/patients.html', context)
    else:
        messages.info(request, "You have to login first...")
        return redirect('/login')


def profile(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            patient = Patient.objects.get(id=id)
        context = {
            'patient': patient
        }
        return render(request, 'medical/profile.html', context)
    else:
        messages.info(request, "You have to login first...")
        return redirect('/login')


def update(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        'patient': patient
    }
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'medical/update.html', context)
        elif request.method == "POST":
            gfn = request.POST["g_first_n"]
            gsn = request.POST["g_second_n"]
            telephone = request.POST["telephone"]
            disease = request.POST["disease"]
            ward = request.POST["ward"]
            bed = request.POST["bed"]
            care = request.POST["care"]
            physicalc = request.POST["physical"]
            patient.guardian_first_name = gfn
            patient.guardian_second_name = gsn
            patient.telephone = telephone
            patient.disease = disease
            patient.ward = ward
            patient.bed = bed
            patient.care_note = care
            patient.physical_con = physicalc
            patient.save()
            messages.info(request, "Profile update complete...")
            return redirect('/medical/m')
    else:
        messages.info(request, "You have to login first")
        return redirect('/login')


def delete(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        'patient': patient
    }
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "medical/delete.html", context)
        elif request.method == "POST":
            patient.delete()
            return redirect('/medical/m')
    else:
        messages.info(request, "You have to login first...")


def release(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        'patient': patient
    }
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'medical/release.html', context)
        elif request.method == "POST":
            release_date = request.POST["release"]
            status = request.POST["status"]
            patient.release_date = release_date
            patient.status = status
            patient.save()
            messages.info(request, "Patient release complete...")
            return redirect('/medical/m')
    else:
        messages.info(request, "You have to login first")
        return redirect('/login')


def summary(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        'patient': patient
    }
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'medical/Case summary.html', context)
        elif request.method == "POST":
            case = request.POST['case']
            patient.case_summary = case
            patient.save()
            return render(request, 'medical/show.html',context)
    else:
        messages.info(request, "You have to login first")
        return redirect('/login')


def death(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        'patient': patient
    }
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'medical/death.html', context)
        elif request.method == "POST":
            dide = "Death"
            status = "Released"
            cause = request.POST["cause"]
            de_date = request.POST["de_date"]
            patient.physical_con = dide
            patient.release_date = de_date
            patient.status = status
            patient.death_date = de_date
            patient.disease = cause
            patient.save()
            return render(request, 'medical/certificate.html', context)
    else:
        messages.info(request, "You have to login first")
        return redirect('/login')