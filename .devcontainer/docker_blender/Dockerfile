# FROM public.ecr.aws/genophore/nvidia/cuda:12.3.1-runtime-ubuntu22.04
FROM public.ecr.aws/k6z4i1r5/nvidia-cuda:12.3.1-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'tzdata tzdata/Areas select Etc' | debconf-set-selections
RUN echo 'tzdata tzdata/Zones/Etc select UTC' | debconf-set-selections

ENV BLENDER_VERSION 4.2
ENV BLENDER_VERSION_MAJOR 4.2.0

# ARG BLENDER_VERSION=${BLENDER_VERSION}
# ARG BLENDER_VERSION_MAJOR=${BLENDER_VERSION_MAJOR}
ENV BLENDER_URL https://mirror.clarkson.edu/blender/release/Blender${BLENDER_VERSION}/blender-${BLENDER_VERSION_MAJOR}-linux-x64.tar.xz

# Install dependencies
RUN apt-get update -y && \
    apt-get install -y \
    sudo \
    curl \
    ca-certificates \
    zip \
    xz-utils \
    imagemagick \
    python3 \
    python3-pip \
    python3-pil \
    python3-pil.imagetk \
    xvfb \
    libnvidia-gl-515 \
    tree \
    libx11-dev \
    libxi-dev \
    libxxf86vm-dev \
    libfontconfig1 \
    libxrender1 \
    libgl1-mesa-glx \
    libxkbcommon-x11-0 \
    libsm6 \
    libwayland-client0 \
    libwayland-server0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and install Blender
RUN curl "${BLENDER_URL}" -o "blender.tar.xz" && \
    tar -xvf blender.tar.xz --strip-components=1 -C /bin && \
    rm -rf blender.tar.xz && \
    rm -rf blender

RUN pip3 install boto3 requests Wand

# AWS BATCH TEST ENV
ENV AWS_BATCH_JOB_ARRAY_INDEX=0
ENV AWS_BATCH_JOB_ARRAY_SIZE=10
ENV AWS_BATCH_JOB_ID=1234

ENV BUCKET_NAME=brender-bucket-s3-<uuid>
ENV BUCKET_KEY=PY_SINGLE_POTTERY

# AWS CREDENTIALS
ENV AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
ENV AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
ENV AWS_REGION=us-east-1
ENV AWS_DEFAULT_REGION=us-east-1



# EFS ENV
ENV EFS_BLENDER_FOLDER_PATH=/mnt/efs/projects
ENV EFS_BLENDER_OUTPUT_FOLDER_PATH=/mnt/efs/projects/PY_SINGLE_POTTERY/output
ENV EFS_BLENDER_FILE_PATH=/mnt/efs/projects/PY_SINGLE_POTTERY/pottery-animation.blend

# PYTHON TESTING - Main Script Path

## Folder
# ENV EFS_MAIN_SCRIPT_PATH=/mnt/efs/projects/PY_FOLDER_POTTERY/python_brender_test/user_script.py

## File
ENV EFS_MAIN_SCRIPT_PATH=/mnt/efs/projects/PY_SINGLE_POTTERY/user_script.py


ENV USE_EEVEE=False

# Blender ENV
ENV BLENDER_EXECUTABLE=/usr/bin/blender

# Job Action type (copy_efs, render, custom_render_python, upload_render_output, remove_efs)
ENV JOB_ACTION_TYPE=custom_render_python


# Copy specific folders and their contents
COPY ./app /app
COPY ./simulation_data/projects /mnt/efs/projects

# Give execute permissions to the script
RUN chmod +x /app
RUN chmod +x /mnt/efs/projects

WORKDIR /app

# Set the PYTHONPATH
ENV PYTHONPATH=/app:/mnt/efs/projects:$PYTHONPATH

ENTRYPOINT ["python3", "/app/app.py"]
 