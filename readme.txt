Food Picker

# ssh into pi

ssh pi@192.168.0.145

# cd to home directory (~): Install & Run

git clone https://github.com/kevmck451/Food_Picker

cd Food_Picker

# start program indefinitely

nohup python3 main.py &




Ending Process to Update:

ps aux | grep "python3" | grep "main.py" | grep -v grep

# get PID number and End Program

kill 1295

# Remove old program:

sudo rm -rf Food_Picker

# install from git and run again
