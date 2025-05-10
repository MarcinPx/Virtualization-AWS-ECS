FROM python:3.9.0
ADD simplewebv1.py .




RUN apt-get update



RUN pip install flask mysql mysql-connector-python



CMD [ "python3", "simplewebv1.py" , "-m", "flask", "run"]