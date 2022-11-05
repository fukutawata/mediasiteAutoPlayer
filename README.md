# mediasiteAutoPlayer
This program can sign in to manaba and mediasite, and start watching live automatically at the appropriate time.

## Requirements
- MacOS>=12
- Python>=3.7
- Command Line Developer Tools

The following will be installed automatically when you run the program.
- chromedriver-binary==106.0.5249.61.0
- schedule for Python3
- selenium for Python3

## Download


## How to use the program
https://qiita.com/trombone0717960/private/9a04d7213f1ccdb64afd

## Usage of function
```python:main.py
work_?(start_time,duration,lesson_url)
```

- "?" indicates what day of the week the function is to be executed.

```python:main.py
##Monday
work_1(start_time,duration,lesson_url) 
##Tuesday
work_2(start_time,duration,lesson_url) 
##Wednesday
work_3(start_time,duration,lesson_url) 
##Thursday
work_4(start_time,duration,lesson_url) 
##Friday
work_5(start_time,duration,lesson_url) 
```
- start_time indicates the start time of the function. 
It takes about 30 seconds for the live viewing to start, so if the class starts at 12:15, it is recommended to  substitute 12:13, two minutes earlier.

- duration indicates the length of time to run a program. The unit is seconds.
If you only have one class period in the URL, just substitute 5100. If there are two classes in a row, substitute 10500.

- lesson_url is the URL of the class.

From the above, for example, if there were three consecutive classes on Tuesday from the third to the fifth period, the required functions would be as follows.
```python:main.py
work_2("12:13",10500,"https://xxxxxxxxxxxxxxxx")
work_2("15:13",5100,"https://xxxxxxxxxxxxxxxx")
```

It is also recommended that the IF function and the dametime library be used so that the program will work no matter when it is executed.
For example, it could be written as follows.
```main.py
if (now > datetime.datetime(2022,11,9,10, 8, 1) and now < datetime.datetime(2022,11,9,12, 13, 0)):
    work_3("12:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")


if (now > datetime.datetime(2022,11,9,12, 13, 1) and now < datetime.datetime(2022,11,11,10, 8, 0)):
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")

if (now > datetime.datetime(2022,11,11,10, 8, 1) and now < datetime.datetime(2022,11,11,12, 13, 0)):
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")
```
