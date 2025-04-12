From python:3.10
WORKDIR /usr/local/app

COPY templates ./templates
COPY front_end.py ./front_end.py
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "front_end.py"]
