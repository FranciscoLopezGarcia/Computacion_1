FROM python:3
RUN git clone https://github.com/FranciscoLopezGarcia/4-In-Line-Docker.git
WORKDIR /4-In-Line-Docker/tree/main
RUN pip install -r requirements.txt
CMD ["python3",  "-m", "unittest"]
