#Base Layer
FROM ubuntu:18.04


# Install dependencies with apt package manager, automatic yes to prompts
# pip to install python packages.
RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip 

# Install python packages needed for machine learning / data science
# TODO: specify dependencies in requirements.txt
RUN pip3 install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

#Copy project files over to container
COPY . /app

# Configure python installation
RUN ln -s /usr/bin/python3 /usr/bin/python

EXPOSE 8080
