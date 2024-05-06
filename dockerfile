FROM python:3.9-slim

WORKDIR /About

COPY . /About

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "About.py"]