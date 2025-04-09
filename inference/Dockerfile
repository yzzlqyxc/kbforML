From python:3.8-slim
WORKDIR /usr/local/app

COPY a.py ./a.py
COPY requirement.txt ./requirement.txt

RUN pip install -r requirement.txt

CMD ["python", "a.py"]
