From pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime
WORKDIR /usr/local/app

COPY train.py ./train.py
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "train.py"]
