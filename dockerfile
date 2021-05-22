FROM python:3.8-slim
COPY $PWD /home/app/
WORKDIR /home/app/
RUN pip install -r requirements.txt
CMD python main.py