FROM python:3.8.10-alpine

# Copy the requirements file into the image
COPY requirements.txt /app/

# Switch working directory 
WORKDIR /app/

# Install all the dependencies
RUN pip install -r requirements.txt

# Copy all the content from the local file to the image
COPY . /app/

EXPOSE 8080

CMD [ "python", "run.py" ]