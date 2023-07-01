Food Picker

# ssh into pi
# use current pi IP address - should be static now

ssh pi@192.168.0.139

# message might come up about unknown host. enter yes
# password is drpepper

# cd to home directory (~)

git clone https://github.com/kevmck451/Food_Picker

cd Food_Picker

# start program indefinitely

nohup python3 main.py &




Ending Process to Update:

ps aux | grep "python3" | grep "main.py" | grep -v grep

# End Program

kill 1295

# Remove old program:

sudo rm -rf Food_Picker

# update and run again

