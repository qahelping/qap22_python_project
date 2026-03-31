FROM python:3.12-slim
LABEL authors="elenayanushevskaya"
ENV APP=prod
WORKDIR /app

#/app/app.py
COPY app.py .

#RUN pip install -r requrements.txt
RUN apt-get update && apt-get install -y curl


ENTRYPOINT ["python"]
CMD ["app.py"]





