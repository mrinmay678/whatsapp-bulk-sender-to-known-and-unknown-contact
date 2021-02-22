from django.shortcuts import render
from .forms import PNCSVModelForm
from .models import PhoneNumberCSV, PhoneNumber
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import webbrowser as web
import pyautogui as pg
import time


def upload_csv_here(request):
    form = PNCSVModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = PNCSVModelForm()
        obj = PhoneNumberCSV.objects.get(used=False)
        obj.used = True
        obj.save()
        driver = webdriver.Edge(
            "C:/Users/mrinm/Downloads/edgedriver_win64/msedgedriver.exe")
        driver.get("http://web.whatsapp.com/")
        wait = WebDriverWait(driver, 1000)
        with open(obj.file_name.path, 'r') as f:
            read = csv.reader(f)
            for i, row in enumerate(read):
                name = "+"+row[0]
                print(name)
                search_box = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
                search_box.send_keys(name+Keys.ENTER)

                input_box = driver.find_element_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                input_box.send_keys(row[1]+Keys.ENTER)

    return render(request, 'index.html', {'form': form})


def upload_unknown_csv_here(request):
    form = PNCSVModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = PNCSVModelForm()
        obj = PhoneNumberCSV.objects.get(used=False)
        obj.used = True
        obj.save()
        with open(obj.file_name.path, 'r') as f:
            read = csv.reader(f)
            for i, row in enumerate(read):
                name = "+"+row[0]
                print(name)
                web.open("https://web.whatsapp.com/send?phone=" +
                         str(name)+"&text="+row[1])
                time.sleep(5)
                width, height = pg.size()
                pg.click(width/2, height/2)
                time.sleep(5)
                pg.press('enter')
                time.sleep(5)
                pg.hotkey('ctrl', 'w')
                time.sleep(5)

    return render(request, 'index.html', {'form': form})
