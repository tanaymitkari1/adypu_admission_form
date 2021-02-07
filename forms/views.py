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
        gd = request.POST
        rf = request.FILES
        first_name = gd["first_name"]
        last_name = gd["last_name"]
        father_name = gd["father_name"]
        mother_name = gd["mother_name"]
        number = gd["contact"]
        email=gd["email"]
        father_no = gd["father_contact"]
        mother_no = gd["mother_contact"]
        address = gd["address"]
        city=gd["city"]
        pin_code = gd["pin"]
        state=gd["state"]
        country = gd["country"]
        present_address = gd["padress"]
        present_city = gd["pcity"]
        p_pin = gd["ppin"]
        present_state = gd["pstate"]
        present_country = gd["pcountry"]
        birthdate = gd["dob"]
        place = gd["pob"]
        gender = gd["radio1"]
        category = gd["category"]
        aadhar = gd["aadhar"]
        status = gd["radio2"]
        blood_group = gd["blood_grp"]
        course = gd["degree"]
        program = gd["program"]
        year1 = gd["year1"]
        nos1 = gd["nos1"]
        board1 = gd["board1"]
        mm1 = gd["mm1"]
        mo1 = gd["mo1"]
        p1 = gd["p1"]
        year2 = gd["year2"]
        nos2 = gd["nos2"]
        board2= gd["board2"]
        mm2 = gd["mm2"]
        mo2 = gd["mo2"]
        p2 = gd["p2"]
        name_of_degree=gd["name_of_degree"]
        gy1 = gd["gy1"]
        collegename1 = gd["collegename1"]
        uni1 = gd["uni1"]
        gmm1 = gd["gmm1"]
        gmo1 = gd["gmo1"]
        cgpa1 = gd["cgpa1"]
        gy2 = gd["gy2"]
        collegename2 = gd["collegename2"]
        uni2 = gd["uni2"]
        gmm2 = gd["gmm2"]
        gmo2 = gd["gmo2"]
        cgpa2 = gd["cgpa2"]
        gy3 = gd["gy3"]
        collegename3 = gd["collegename3"]
        uni3 = gd["uni3"]
        gmm3 = gd["gmm3"]
        gmo3 = gd["gmo3"]
        cgpa3 = gd["cgpa3"]
        gy4 = gd["gy1"]
        collegename4 = gd["collegename4"]
        uni4 = gd["uni4"]
        gmm4 = gd["gmm4"]
        gmo4 = gd["gmo4"]
        cgpa4 = gd["cgpa4"]
        org_name1 = gd["org_name1"]
        des1 = gd["des1"]
        peroid1 = gd["period1"]
        nature_work1 = gd["nature_work1"]
        salary1 = gd["salary1"]
        org_name2 = gd["org_name2"]
        des2 = gd["des2"]
        peroid2 = gd["period2"]
        nature_work2 = gd["nature_work2"]
        salary2 = gd["salary2"]
        total_exp = gd["total_exp"]
        year1 = gd["year1"]
        award_name1 = gd["award_name1"]
        institute1 = gd["institute1"]
        level1 = gd["level1"]
        remark1 = gd["remark1"]
        year12= gd["year2"]
        award_name2 = gd["award_name2"]
        institute2 = gd["institute2"]
        level2 = gd["level2"]
        remark2 = gd["remark2"]
        father_education = gd["father_education"]
        father_occupation = gd["father_occupation"]
        father_income = gd["father_income"]
        mother_education = gd["mother_education"]
        mother_occupation = gd["mother_occupation"]
        mother_income = gd["mother_income"]
        why_study = gd=["why_study"]
       
        data = data_form(first_name=first_name, last_name=last_name, father_name=father_name, mother_name=mother_name,
        contact=number, email=email, father_contact=father_no, mother_contact=mother_no, address=address, city=city, pin=pin_code,
        state=state, country=country, present_address=present_address, present_city=present_city, ppin=p_pin, pstate=present_state,
        pcountry=present_country, dob=birthdate, pob=place, gender=gender, category=category, aadhar=aadhar, blood_group=blood_group,
        maratial_status=status, course=course, program=program, secondary_year=year1, nos1=nos1, board1=board1, max_marks1=mm1,
        marks1=mo1, percent1=p1, sr_secondary_year=year2, nos2=nos2, board2=board2, max_marks2=mm2, marks2=mo2, percent2=p2,
        name_of_degree=name_of_degree, graduation_year1=gy1, college1=collegename1, uni1=uni1, mmarks1=gmm1, mo1=gmo1, cgpa1=cgpa1,
        graduation_year2=gy2, college2=collegename2, uni2=uni2, mmarks2=gmm2, mo2=gmo2, cgpa2=cgpa2, 
        graduation_year3=gy3, college3=collegename3, uni3=uni3, mmarks3=gmm3, mo3=gmo3, cgpa3=cgpa3,
        graduation_year4=gy4, college4=collegename4, uni4=uni4, mmarks4=gmm4, mo4=gmo4, cgpa4=cgpa4,
        org_name1=org_name1, des1=des1, peroid1=peroid1, nature_work1=nature_work1, salary1=salary1, 
        org_name2=org_name2, des2=des2, period2=peroid2, nature_work2=nature_work2, salary2=salary2,
        total_exp=total_exp, year1=year1, award_name1=award_name1, institute1=institute1, level1=level1, remark1=remark1,
        year2=year2, award_name2=award_name2, institute2=institute2, level2=level2, remark2=remark2, why_study= why_study,
        fater_education=father_education, mother_education=mother_education, father_occupation=father_occupation, mother_occupation=mother_occupation,
        father_income=father_income, mother_income=mother_income)
        data.save()
        return HttpResponseRedirect(reverse('pdf_form'))

"""
def input_form(request):
    if request.method == "GET":
        return render(request, 'form.html')
    if request.method == "POST":
        data = request.POST
        form_data = data_form(first_name=data['first_name'], middle_name=data['middle_name'],
        last_name=data['last_name'], dob=data['dob'], contact=data['contact'], blood_group=data['blood_grp'], 
        gender=data['radio1'], disability=data['checkbox'], muslim_minority=data['muslim'], other_minority=data['other_minority'],
        category=data['category'], maratial_status=data['radio2'], nationality=data['nationality'], address=data['adress'],
        city=data['city'], state=data['state'], aadhar=data['aadhar'], mother_name=data['mother_name'], father_name=data['father_name'],
        parent_email=data['parent_email'], parent_contact=data['parent_contact'], local_guardian=data['guardian_name'], 
        emergency_number=data['emergency'], urn=data['urn'], year_of_study=data['study'], semister=data['sem'], degree=data['degree'],
        program=data['program'], education_loan=data['checkbox_edu'], scholarship=data['checkbox_scholar'], last_year_amount=data['amount_transferred'],
        last_year_payment_mode=data['payment_mode'], last_year_transaction_id=data['transaction_id'], last_year_date=data['dop'],
        current_year_amount_transferred=data['amount_ay'], current_year_payment_mode=data['payment_ay'], current_year_transaction_id=data['transaction_ay'],
        current_year_date=data['dop_ay'])
        form_data.save()
        return HttpResponseRedirect(reverse('pdf_form'))

"""