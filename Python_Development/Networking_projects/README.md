Setting Up Python3
type python in cmd if verson is below 3.1 then update first using the command: 
-> sudo apt-get upgrade python3

command for setting up environment:
-> sudo apt-get install python3-venv
-> mkdir bhp
-> cd bhp
-> python3 -m venv venv3
-> source venv3/bin/activate
-> python

install necessary modules
-> pip install lxml
-> python
confirm the package is installed:
-> from lxml import etree
-> exit()

intall an IDE (recommend vs code)
-> apt-get install code
-> apt-get install -f ./code_[current_version].deb

