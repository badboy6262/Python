from django.shortcuts import render

carList=[]
# Create your views here.
def index(req):
	return render(req,"index.html")


def search(req):
	carName=req.GET.get("carName")
	carColor=req.GET.get("carColor")
	carNumber=req.GET.get("carNumber")
	carList.append({
			"name":carName,
			"color":carColor,
			"number":carNumber
		})
	return render(req,"search.html")

def result(req):
	searchNumber=req.GET.get("searchNumber")

	for car in carList:
		if car.get("number") == searchNumber:
			details={
				"name":car.get("name"),
				"color":car.get("color"),
				"number":car.get("number")
			}
	return render(req,"result.html",{"details":details})