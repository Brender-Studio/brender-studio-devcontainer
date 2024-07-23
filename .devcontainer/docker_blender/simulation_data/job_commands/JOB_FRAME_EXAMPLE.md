# AWS Batch command overrides for the FRAME job type

## Description

This file contains the AWS Batch command overrides for the FRAME job type. The FRAME job type is used to render a single frame of a Blender project.

### 1st Job: Copy s3 files to EFS

This job only requires ENV variables to be set. 

#### ENV

| Name            | Value                    |
| --------------- | ------------------------ |
| BUCKET_NAME     | brender-bucket-s3-uuid   |
| BUCKET_KEY      | FR-CPU-1                 |
| JOB_ACTION_TYPE | copy_efs                 |



### 2nd Job: Render Frame

This job requires ENV variables to be set.

#### ENV

| Name                           | Value                                              |
| ------------------------------ | -------------------------------------------------- |
| EFS_BLENDER_FILE_PATH          | /mnt/efs/projects/FR-CPU-1/pottery-animation.blend |
| EFS_BLENDER_OUTPUT_FOLDER_PATH | /mnt/efs/projects/FR-CPU-1/output                  |
| JOB_ACTION_TYPE                | render                                             |


### Command Overrides (AWS Batch Format)

This command overrides the default command for the FRAME job type. This will be used inside AWS Batch container.

```bash
["{\"render_config\":{\"type\":\"frame\",\"is_render_auto\":true,\"use_denoise\":false,\"engine\":\"CYCLES\",\"use_gpu\":true,\"use_compositor\":true,\"use_sequencer\":true,\"use_stamp_metadata\":false,\"active_frame\":1,\"start_frame\":1,\"end_frame\":25,\"frame_step\":1,\"fps\":24,\"render_info\":{\"scene_name\":\"Scene\",\"layer_name\":\"View Layer\",\"camera_name\":\"Camera\",\"aspect_ratio\":{\"height\":1,\"width\":1},\"resolution\":{\"height\":1350,\"width\":1080,\"percentage\":100},\"output\":{\"color\":{\"color_depth\":\"8\",\"color_mode\":\"RGB\"},\"compression\":15,\"output_format\":\"PNG\",\"project_name\":\"FR-CPU-1\"},\"cycles_config\":{\"denoise_config\":{\"algorithm\":\"OPENIMAGEDENOISE\",\"denoise_pass\":\"RGB_ALBEDO_NORMAL\",\"denoise_prefilter\":\"ACCURATE\",\"noise_threshold\":0.01},\"light_paths\":{\"caustics\":{\"filter_glossy\":1,\"reflective\":true,\"refractive\":true},\"clamping\":{\"indirect\":10,\"direct\":0},\"max_bounces\":{\"diffuse_bounces\":4,\"glossy_bounces\":4,\"total\":12,\"transmission_bounces\":12,\"transparent_max_bounces\":8,\"volume_bounces\":0}},\"samples\":50}}}}"]
```

#### JSON FORMAT

```json
{
  "render_config": {
    "type": "frame",
    "is_render_auto": true,
    "use_denoise": false,
    "engine": "CYCLES",
    "use_gpu": true,
    "use_compositor": true,
    "use_sequencer": true,
    "use_stamp_metadata": false,
    "active_frame": 1,
    "start_frame": 1,
    "end_frame": 25,
    "frame_step": 1,
    "fps": 24,
    "render_info": {
      "scene_name": "Scene",
      "layer_name": "View Layer",
      "camera_name": "Camera",
      "aspect_ratio": {
        "height": 1,
        "width": 1
      },
      "resolution": {
        "height": 1350,
        "width": 1080,
        "percentage": 100
      },
      "output": {
        "color": {
          "color_depth": "8",
          "color_mode": "RGB"
        },
        "compression": 15,
        "output_format": "PNG",
        "project_name": "FR-CPU-1"
      },
      "cycles_config": {
        "denoise_config": {
          "algorithm": "OPENIMAGEDENOISE",
          "denoise_pass": "RGB_ALBEDO_NORMAL",
          "denoise_prefilter": "ACCURATE",
          "noise_threshold": 0.01
        },
        "light_paths": {
          "caustics": {
            "filter_glossy": 1,
            "reflective": true,
            "refractive": true
          },
          "clamping": {
            "indirect": 10,
            "direct": 0
          },
          "max_bounces": {
            "diffuse_bounces": 4,
            "glossy_bounces": 4,
            "total": 12,
            "transmission_bounces": 12,
            "transparent_max_bounces": 8,
            "volume_bounces": 0
          }
        },
        "samples": 50
      }
    }
  }
}
```

### 3rd Job: Copy EFS files to S3

This job requires ENV variables to be set.

#### ENV

| Name            | Value                  |
| --------------- | ---------------------- |
| BUCKET_NAME     | brender-bucket-s3-uuid |
| BUCKET_KEY      | FR-CPU-1               |
| JOB_ACTION_TYPE | upload_render_output   |


#### Command Overrides (AWS Batch Format)

```bash
["{\"ses\":{\"ses_active\":true,\"animation_preview\":{\"animation_preview_full_resolution\":true,\"fps\":24,\"resolution_x\":1080,\"resolution_y\":1350,\"output_quality\":\"HIGH\",\"encoding_speed\":\"GOOD\",\"autosplit\":false,\"ffmpeg_format\":\"MPEG4\"},\"render_details\":{\"project_name\":\"FR-CPU-1\",\"resolution\":\"1080x1350\",\"scene_name\":\"Scene\",\"layer_name\":\"View Layer\",\"camera_name\":\"Camera\",\"samples\":50,\"engine\":\"CYCLES\",\"render_type\":\"Still\",\"active_frame\":1,\"frame_range\":\"1-25\",\"job_array_size\":\"0\"},\"ses_config\":{\"region\":\"us-east-1\",\"source_email\":\"your_email@gmail.com\",\"destination_email\":\"your_email@gmail.com\",\"render_ok_template_name\":\"RenderCompletedTemplate\",\"render_error_template_name\":\"RenderFailedTemplate\",\"batch_job_2_id\":\"d8ae665c-cce9-4c7b-8eef-f855f47a879c\"}}}"]
```

#### JSON FORMAT

```json
{
  "ses": {
    "ses_active": true,
    "animation_preview": {
      "animation_preview_full_resolution": true,
      "fps": 24,
      "resolution_x": 1080,
      "resolution_y": 1350,
      "output_quality": "HIGH",
      "encoding_speed": "GOOD",
      "autosplit": false,
      "ffmpeg_format": "MPEG4"
    },
    "render_details": {
      "project_name": "FR-CPU-1",
      "resolution": "1080x1350",
      "scene_name": "Scene",
      "layer_name": "View Layer",
      "camera_name": "Camera",
      "samples": 50,
      "engine": "CYCLES",
      "render_type": "Still",
      "active_frame": 1,
      "frame_range": "1-25",
      "job_array_size": "0"
    },
    "ses_config": {
      "region": "us-east-1",
      "source_email": "your_email@gmail.com",
      "destination_email": "your_email@gmail.com",
      "render_ok_template_name": "RenderCompletedTemplate",
      "render_error_template_name": "RenderFailedTemplate",
      "batch_job_2_id": "d8ae665c-cce9-4c7b-8eef-f855f47a879c"
    }
  }
}
```