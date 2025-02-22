# PiHut Maker Advent Calender

## Virtual Envrionment Setup        
    # Create Virtual Environment
    $ python -m venv ~/.venv/<env>      
    
    # Activate Virtual Environment
    $ source ~/.venv/<env>/bin/activate` 

## rshell Setup                        
    # Install rshell
    $ python -m pip install rshell             

## Uploading Program
    # Connect to Raspberry Pi Pico
    $ rshell -p /dev/<board> --buffer-size 512
    
    # Copy Program to Raspberry Pi Pico
    $ cp <program>.py /pyboard/main.py
    
## Running Program
    # Enter REPL
    $ repl
    
    # Soft Reset Board
    CTRL-D
    -OR-
    machine.soft_reset()
