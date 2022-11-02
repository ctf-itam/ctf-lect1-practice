FROM python:3.11.0-slim

# Set Docker mode to true
ENV DOCKER_MODE=true

# Set current working directory
WORKDIR /app

# Copy dependency list and install the packages
COPY ./src/requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Copy source files
COPY ./src/main.py ./

# Copy the flag
#COPY ./src/flag.txt /

# Run the app
CMD ["uvicorn", "pwn:app", "--host", "0.0.0.0", "--port", "80"]

