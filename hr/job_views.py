from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3


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
