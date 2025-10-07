# Alfred 1.0
Alfred is a friendly bot that will help you during your work hours, or to properly organize and manage your tasks\
It runs on PC only for now.\
To run it, you must first install [Python 3.13](https://www.python.org/downloads/)\
Then git clone / unzip it to your machine\
### 1_INSTALLING PACKAGES :
On your personal computer, from Alfred's directory, please run :
```
python -m pip install -r requirements.txt
```
On your work station, if your company uses a proxy, please run : 
```
pip install -r requirements.txt --proxy http://user:password@proxy.company.com:port
```
### 2_LAUNCH :
Open your console in the project directory and run:
```
python Alfred.py YourName (optionnal)
```
### 3_ALFRED : 
At launch, you will get several options to choose from. To activate them, you can type in the designated number OR the name of the option.
```
0_EXIT => self explanatory
1_WAKEPY => keep your computer active and prevent sleep mode (does nothing for your teams status)
2_POMODORO => to-do list and 5mn breaks suggested every 25 minutes
3_WEATHER => worldwide weather API (will need a proxy set up on a work station)
4_CALCULATOR => complex calculations such as "(2*2) - 24 / 3" are viable
```
Happy coding !\
![White duck wearing a hat and dancing](https://github.com/volpito/Alfred/blob/master/duck-dance-2383412861.gif)
