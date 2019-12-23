from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
from .forms import JobForm


def list_jobs(request):
    try:
        with sqlite3.connect(r"e:\classroom\python\nov11\hr.db") as con:
            cur = con.cursor()
            cur.execute("select * from jobs")
            jobs = cur.fetchall()
            return render(request, 'list_jobs.html', {'jobs': jobs})
    except Exception as ex:
        print(ex)
        return render(request, 'error.html')


def add_job(request):
    if request.method == "GET":
        return render(request, 'add_job.html')
    else:  # POST
        # process data sent from form
        title = request.POST['title']
        location = request.POST['location']
        minsal = request.POST['minsalary']
        # insert into JOBS table
        try:
            with sqlite3.connect(r"e:\classroom\python\nov11\hr.db") as con:
                cur = con.cursor()
                cur.execute("insert into jobs(title,location,minsal) values (?,?,?)",
                            (title, location, minsal))
                return redirect("/hr/jobs")
        except Exception as ex:
            print(ex)
            return render(request, 'error.html')


def add_job2(request):
    if request.method == "GET":
        f = JobForm()  # Unbound form
        return render(request, 'add_job2.html', {'form': f})
    else:  # POST
        # get data sent from form
        f = JobForm(request.POST)
        # If validation fails, redisplay form with data
        if not f.is_valid():
            return render(request, 'add_job2.html', {'form': f})

        # Take data from cleaned_data
        title = f.cleaned_data['title']
        location = f.cleaned_data['location']
        minsal = f.cleaned_data['minsal']
        # insert into JOBS table
        try:
            with sqlite3.connect(r"e:\classroom\python\nov11\hr.db") as con:
                cur = con.cursor()
                cur.execute("insert into job(title,location,minsal) values (?,?,?)",
                            (title, location, minsal))
                return redirect("/hr/jobs")
        except Exception as ex:
            # print(ex)
            return render(request, 'add_job2.html',
                          {'form': f, 'error': str(ex)})
