from django.shortcuts import render

dataList=[]
# Create your views here.
def deleteData(req,name):
	for stu in dataList:
		if(stu["name"]==name):
			dataList.remove(stu)
	student={"data":dataList}
	return render(req,"show.html",student)

def index(req):
	return render(req,"index.html")

def saveMarks(req):
	no=req.GET.get("no")
	name=req.GET.get("name")
	java=req.GET.get("java")
	py=req.GET.get("py")
	data={"no":no,"name":name,"java":java,"py":py}
	dataList.append(data)
	student={"data":dataList}
	return render(req,"show.html",student)

