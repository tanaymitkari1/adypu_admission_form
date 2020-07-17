from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import View
from . models import data_form
from django.urls import reverse
from .utils import render_to_pdf #created in step 4

# Create your views here.
def input_form(request):
    if request.method == "GET":
        return render(request, 'form.html')
    if request.method=="POST":
        first_name = request.POST["first_name"]
        middle_name = request.POST["middle_name"]
        last_name = request.POST["last_name"]
        birthdate = request.POST["dob"]
        contact = request.POST["contact"]
        blood_group = request.POST["blood_grp"]
        gender = request.POST["radio1"]
        disability = request.POST["checkbox"]
        muslim = request.POST["muslim"]
        other = request.POST["other_minority"]
        category = request.POST["category"]
        status = request.POST["category"]
        nation = request.POST["nationality"]
        adress = request.POST["adress"]
        city = request.POST["city"]
        state = request.POST["state"]
        aadhar = request.POST["aadhar"]
        program = request.POST["program"]
        yearofstudy = request.POST["study"]
        mother_name = request.POST["mother_name"]
        father_name = request.POST["father_name"]
        email = request.POST["parent_email"]
        pcontact = request.POST["parent_contact"]
        guardian_name = request.POST["guardian_name"]
        emergency = request.POST["emergency"]
        edu_loan = request.POST["checkbox_edu"]
        scholarship = request.POST["checkbox_scholar"]
        fees_transfer = request.POST["amount_transferred"]
        mode = request.POST["payment_mode"]
        id_trans = request.POST["transaction_id"]
        dop = request.POST["dop"]
        fees_ay = request.POST["amount_ay"]
        mode_ay = request.POST["payment_ay"]
        id_ay = request.POST["transaction_ay"]
        dop_ay = request.POST["dop_ay"]
        ragging = request.FILE["antiragging"]
        fees_under = request.FILE["accept_form"]
        ac_form = request.FILE["ac_form"]
        photo = request.FILE["photo"]
        degree = request.POST["degree"]
        semister = request.POST["sem"]
        urn = request.POST["urn"]
        data = data_form(first_name=first_name, middle_name=middle_name, last_name=last_name, 
        dob=birthdate, contact=contact, blood_group=blood_group, gender=gender, disability=disability,
        muslim_minority=muslim, other_minority=other, category=category, maratial_status=status,
        nationality=nation, adress=adress, city=city, state=state, aadhar=aadhar, program=program,
        year_of_study=yearofstudy, mother_name=mother_name, father_name=father_name, parent_email=email,
        parent_contact=pcontact, local_guardian=guardian_name, emergency_number=emergency,
        education_loan=edu_loan, scholarship=scholarship, last_year_amount=fees_transfer,
        last_year_payment_mode=mode, last_year_transaction_id=id_trans, last_year_date=dop,
        current_year_amount_transferred=fees_ay, current_year_payment_mode=mode_ay,
        current_year_transaction_id=id_ay, current_year_date=dop_ay, anti_ragging=ragging, readmission_fee_undertaking=fees_under,
        readmisson_acceptance_form=ac_form, photograph=photo, degree=degree, semister=semister, urn=urn)
        data.save()
        return HttpResponseRedirect(reverse('pdf_form'))
