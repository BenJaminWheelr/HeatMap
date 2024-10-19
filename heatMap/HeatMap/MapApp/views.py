from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd
import csv

fileToParse = "MapApp/output.csv"
fileToParseLabel = "ALL Accidents, may take a second to load."
maxIntensity = 200

def index(request):
    return  render(request, "MapApp/index.html", {'dataFile': f"{fileToParseLabel}"})

def readOutput(request):
    output = []
    with open(fileToParse, mode='r') as file:
        data = csv.reader(file)
        for row in data:
            output.append(row)
    return JsonResponse(output, safe=False)

def changeDataToDefault(request):
    global fileToParse 
    global fileToParseLabel
    fileToParse = "MapApp/output.csv"
    fileToParseLabel = "ALL Accidents, may take a second to load."
    return redirect("/")

def changeDataToDui(request):
    global fileToParse 
    global fileToParseLabel
    fileToParse = "MapApp/outputDUI.csv"
    fileToParseLabel = "DUI Accidents"

    return redirect("/")

def changeDataToWildAnimal(request):
    global fileToParse 
    global fileToParseLabel
    fileToParse = "MapApp/outputWILDANIMAL.csv"
    fileToParseLabel = "WILDLIFE Accidents"
    return redirect("/")

def changeDataToPedestrian(request):
    global fileToParse 
    global fileToParseLabel
    fileToParse = "MapApp/outputPEDESTRIAN.csv"
    fileToParseLabel = "PEDESTRIAN Accidents"
    return redirect("/")

def changeDataToBicyclist(request):
    global fileToParse 
    global fileToParseLabel
    fileToParse = "MapApp/outputBICYCLIST.csv"
    fileToParseLabel = "BICYCLIST Accidents"
    return redirect("/")

def changeDataToMotorcycle(request):
    global fileToParse 
    global fileToParseLabel
    fileToParse = "MapApp/outputMOTORCYCLE.csv"
    fileToParseLabel = "MOTORCYCLE Accidents"
    return redirect("/")
