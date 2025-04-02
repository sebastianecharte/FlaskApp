# our base image
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip \
    && pip install --upgrade pip \
    && rm -rf /var/cache/apk/*

# install Python modules needed by the Python app
COPY requirements.txt /home/miname/FlaskApp/
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r /home/miname/FlaskApp/requirements.txt

# copy files required for the app to run
COPY app.py /home/miname/FlaskApp/
COPY templates/index.html /home/miname/FlaskApp/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/home/miname/FlaskApp/app.py"]







