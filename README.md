# Brender Studio DevContainer

## Description

This repository contains a Docker-based development environment for Brender Studio, a cloud-based rendering solution. It replicates the Docker image used in AWS Batch jobs, allowing developers to test and iterate on Blender scripts and rendering workflows locally before deploying to the cloud.

## Purpose

The main goals of this devcontainer are:
- To provide a local development environment that mirrors the AWS Batch execution environment
- To allow testing of Blender scripts and job logic without needing to deploy to AWS
- To facilitate faster iteration and debugging of rendering workflows

## Key Concepts

### Job Types

The container supports multiple job types, controlled by the `JOB_ACTION_TYPE` environment variable:

1. Copy S3 files to EFS: `JOB_ACTION_TYPE=copy_efs`
2. Render: `JOB_ACTION_TYPE=render`
3. Custom Python render: `JOB_ACTION_TYPE=custom_render_python`
4. Save renders from EFS to S3 & send SES Email: `JOB_ACTION_TYPE=upload_render_output`

### Execution Flow

The `app.py` entrypoint script determines the job type and executes the appropriate logic based on the `JOB_ACTION_TYPE`.

## Local Setup and Usage

This project is configured to use Visual Studio Code with the Dev Containers extension. To get started:

1. Ensure Docker is installed on your system.

2. Install Visual Studio Code if you haven't already.

3. Install the "Remote - Containers" extension by Microsoft (ID: ms-vscode-remote.remote-containers) in VS Code.

4. Clone this repository to your local machine:
   ```
   git clone https://github.com/Brender-Studio/brender-studio-devcontainer.git
   ```

5. Open the project folder in VS Code.

6. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the command palette.

7. Type "Dev Containers: Reopen in Container" and select this option.

VS Code will build the Docker container based on the `.devcontainer/devcontainer.json` and `Dockerfile` configurations, then reopen the project inside the container.

### Running Jobs

Once inside the container, you can run different job types directly from the integrated VS Code terminal. Use the following command format:

```bash
JOB_ACTION_TYPE=<job_type> python3 /app/app.py
```

For example:

```bash
JOB_ACTION_TYPE=render python3 /app/app.py
```

Other example commands:

```bash
JOB_ACTION_TYPE=copy_efs python3 /app/app.py
JOB_ACTION_TYPE=custom_render_python python3 /app/app.py
JOB_ACTION_TYPE=upload_render_output python3 /app/app.py
```

### Exiting the Container

To exit the container environment, you can either close the VS Code window or use the "Remote-Containers: Reopen Folder Locally" command from the command palette.

## Test Scene and Custom Projects

For testing purposes, this repository includes a sample Blender scene. The scene is a pottery animation, which you can find in the `simulation_data/projects` directory. This scene is sourced from [BlendSwap](https://blendswap.com/blend/28661) (by Prokster) and is used as a default test project.

If you want to use your own Blender scenes or create custom projects:

1. Place your .blend files and any associated assets in the `simulation_data/projects` directory.
2. You can either create a new folder for your project or use an existing one.
3. Update the relevant environment variables in the Dockerfile or when running commands to point to your new files. For example:

```bash
EFS_BLENDER_FILE_PATH=/mnt/efs/projects/YOUR_PROJECT_FOLDER/your_scene.blend
EFS_BLENDER_OUTPUT_FOLDER_PATH=/mnt/efs/projects/YOUR_PROJECT_FOLDER/output
```

Remember to adjust other environment variables as needed to match your project structure and requirements.


## Project Structure

```
.
├── Dockerfile
├── app/
│   ├── app.py
│   ├── app_utils/
│   ├── render/
│   ├── render_python/
│   └── storage_actions/
│       ├── job_1/
│       ├── job_3/
│       └── job_4/
└── simulation_data/
└─── projects/
├──── AN_POTTERY/
├──── PY_FOLDER_POTTERY/
└──── PY_SINGLE_POTTERY/
```

## Dockerfile

The included Dockerfile sets up the environment with:
- Ubuntu 22.04 with CUDA support
- Blender 4.2
- Python 3 with necessary libraries
- AWS CLI and required environment variables

## Differences from Production

While this devcontainer closely mimics the production environment, there are some differences:
- Some AWS-specific features may not be fully functional locally
- Recent data may require running actual AWS Batch jobs

## Related Repositories

- [Brender Studio CDK](https://github.com/Brender-Studio/brender-studio-cdk) - The full AWS CDK deployment for Brender Studio

## Resources

- [Docker](https://docker.com/)
- [Visual Studio Code Remote Containers](https://code.visualstudio.com/docs/remote/containers)
- [AWS Batch Documentation](https://docs.aws.amazon.com/batch/)