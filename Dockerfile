# base image
FROM python:3.9
LABEL maintainer="kakaocall.com"

# Set env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GOOGLE_CLOUD_PROJECT kakaocall-0929
ENV USE_CLOUD_SQL_AUTH_PROXY false
ENV USE_LOCAL_POSTGRESQL true
#ENV USE_GCLOUD_SQL true

COPY ./requirements.txt /requirements.txt
COPY ./serviceAccountKey.json /serviceAccountKey.json

COPY ./app /app
WORKDIR /app


#RUN ehco "########## $PATH" >> /Users/jong-yeollee/Projects/Delivery_App/Web/Django/temp
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"
ENV GOOGLE_APPLICATION_CREDENTIALS="/serviceAccountKey.json"

#ENV DATABASE_URL=postgresql://root:password@localhost:5432/django_test
#RUN source /Users/jong-yeollee/Projects/Delivery_App/Web/GoogleCloud/venv/bin/activate
#ENV PATH="/Users/jong-yeollee/Projects/Delivery_App/Web/GoogleCloud/venv/bin:$PATH"
USER django-user

