from django.shortcuts import render

# Create your views here.

lstmarks=[]
def index(req):
	return render(req, "index.html")

def savemarks(req):
		marks=req.GET.get("txtMarks")
		lstmarks.append(marks)
		print(lstmarks)
		Dicdata={'marks':lstmarks}
		return render(req,"showmarks.html", Dicdata)

def info(req):
	return render(req, "info.html")

	def details(req):
		enrollment=req.GET.get("enroll")
		name=req.GET.get("name1")
		marks



