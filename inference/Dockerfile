From python:3.10
WORKDIR /usr/local/app

COPY inf.py ./inf.py
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "inf.py"]
