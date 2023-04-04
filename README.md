# test_kamtor
Test task for Kamtor

## Task: 

Напишите код программы на Python, которая будет в реальном времени (с максимально возможной скоростью) считывать текущую цену фьючерса XRP/USDT на бирже Binance. 
В случае, если цена упала на 1% от максимальной цены за последний час, программа должна вывести сообщение в консоль. 
При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.


## How to install:
### 1) Clone repository
```
git clone https://github.com/R1Sen007/test_kamtor.git
cd test_kamtor
```
### 2) Create & activate virtual environment 
```
python -m venv venv
```
If your platform is Windows:
```
Set-ExecutionPolicy Unrestricted
venv/Scripts/activate.ps1
```
If you have Unix/Linux:
```
sourse venv/bin/activate
```
### 3) Clone important libraries 
```
pip install -r requirements.txt
```
## How to run:
```
python main.py
```
