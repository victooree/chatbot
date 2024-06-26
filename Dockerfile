FROM python:3.11-bullseye


COPY app /app
COPY ./static /static
COPY requirements.txt /

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get install -y --no-install-recommends ssh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update -y \
    && apt-get upgrade -y


RUN pip install -r requirements.txt
RUN pip install python-jose[cryptography]

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
