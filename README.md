# dashboard-streamlit

1. deploy virtual machine
2. update virtual machine
  - ``` sudo apt-get update```
6. install pip3
  - ```sudo apt install pyhton3-pip```
8. install streamlit
  - ``pip3 install streamlit```
  - ```nano ~/.bashrc```
  - insert ``export PATH='$HOME/.local/bin:$PATH`` into file
  - restart terminal with ```source ~/.bashrc```
  - update jinja2 with ```pip3 install jinja2 --upgrade```
10. create new .py file
  - to create new .py file use ``` touch app.py ```
  - write script
  or
  - git clone a repository that holds a .py script
11. deploy dashboard app
  - ```streamlit run apr.py -- server.port 80 ```
