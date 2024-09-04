import os

from app_utils.parse_json import parse_json
from app_utils.get_job_action_path import get_job_action_path
from app_utils.execute_script_by_action import execute_script_by_action

job_action = os.environ['JOB_ACTION_TYPE']


def main():
    print(f'Running job action: {job_action}')

    """
    Commands for each job action type:

    - 1st job - Copy s3 files to EFS: JOB_ACTION_TYPE=copy_efs python3 /app/app.py
    - 2nd job - render: JOB_ACTION_TYPE=render python3 /app/app.py
    - 2nd job - custom python render: JOB_ACTION_TYPE=custom_render_python python3 /app/app.py
    - 3rd job - Save renders from EFS to S3 & send SES Email: JOB_ACTION_TYPE=upload_render_output python3 /app/app.py

    Note: You can override ENV variables. e.g. EFS_BLENDER_OUTPUT_FOLDER_PATH=/mnt/efs/projects/FR_CYCLES_AUTO/output,
    the command will be: EFS_BLENDER_OUTPUT_FOLDER_PATH=/mnt/efs/projects/FR_CYCLES_AUTO/output JOB_ACTION_TYPE=upload_render_output python3 /app/app.py
    """

    ### JOB 2 COMMANDS - RENDER ###

    ### CYCLES AUTO RENDER CONFIG ###
    # command_container_json_str = "{\"render_config\":{\"type\":\"animation\",\"is_render_auto\":true,\"use_denoise\":false,\"engine\":\"CYCLES\",\"use_gpu\":true,\"use_compositor\":true,\"use_sequencer\":true,\"use_stamp_metadata\":false,\"active_frame\":1,\"start_frame\":1,\"end_frame\":10,\"frame_step\":1,\"fps\":24,\"render_info\":{\"scene_name\":\"Scene\",\"layer_name\":\"AXE_LAYER\",\"camera_name\":\"Camera\",\"aspect_ratio\":{\"height\":1,\"width\":1},\"resolution\":{\"height\":2000,\"width\":3500,\"percentage\":100},\"output\":{\"color\":{\"color_depth\":\"16\",\"color_mode\":\"RGB\"},\"compression\":15,\"output_format\":\"PNG\",\"project_name\":\"FR-CPU-1\"},\"cycles_config\":{\"denoise_config\":{\"algorithm\":\"OPENIMAGEDENOISE\",\"denoise_pass\":\"RGB_ALBEDO_NORMAL\",\"denoise_prefilter\":\"ACCURATE\",\"noise_threshold\":0.01},\"light_paths\":{\"caustics\":{\"filter_glossy\":1,\"reflective\":true,\"refractive\":true},\"clamping\":{\"indirect\":10,\"direct\":0},\"max_bounces\":{\"diffuse_bounces\":4,\"glossy_bounces\":4,\"total\":12,\"transmission_bounces\":12,\"transparent_max_bounces\":8,\"volume_bounces\":0}},\"samples\":50}}}}"

    ## CYCLES CUSTOM RENDER CONFIG ###
    # command_container_json_str = "{\"render_config\":{\"type\":\"animation\",\"is_render_auto\":false,\"use_denoise\":false,\"engine\":\"CYCLES\",\"use_gpu\":true,\"use_compositor\":true,\"use_sequencer\":true,\"use_stamp_metadata\":false,\"active_frame\":1,\"start_frame\":1,\"end_frame\":25,\"frame_step\":1,\"fps\":24,\"render_info\":{\"scene_name\":\"Scene\",\"layer_name\":\"ViewLayer_001\",\"camera_name\":\"Camera.002\",\"aspect_ratio\":{\"height\":1,\"width\":1},\"resolution\":{\"height\":1350,\"width\":1080,\"percentage\":100},\"output\":{\"color\":{\"color_depth\":\"8\",\"color_mode\":\"RGB\"},\"compression\":15,\"output_format\":\"PNG\",\"project_name\":\"FR-CPU-1\"},\"cycles_config\":{\"denoise_config\":{\"algorithm\":\"OPENIMAGEDENOISE\",\"denoise_pass\":\"RGB_ALBEDO_NORMAL\",\"denoise_prefilter\":\"ACCURATE\",\"noise_threshold\":0.01},\"light_paths\":{\"caustics\":{\"filter_glossy\":1,\"reflective\":true,\"refractive\":true},\"clamping\":{\"indirect\":10,\"direct\":0},\"max_bounces\":{\"diffuse_bounces\":4,\"glossy_bounces\":4,\"total\":12,\"transmission_bounces\":12,\"transparent_max_bounces\":8,\"volume_bounces\":0}},\"samples\":50}}}}"

    ## CYCLES CUSTOM ANIMATION CONFIG ###
    command_container_json_str = "{\"render_config\":{\"type\":\"animation\",\"is_render_auto\":false,\"use_denoise\":false,\"engine\":\"CYCLES\",\"use_gpu\":true,\"use_compositor\":true,\"use_sequencer\":true,\"use_stamp_metadata\":false,\"active_frame\":1,\"start_frame\":1,\"end_frame\":25,\"frame_step\":1,\"fps\":30,\"render_info\":{\"scene_name\":\"Scene\",\"layer_name\":\"View Layer\",\"camera_name\":\"Camera\",\"aspect_ratio\":{\"height\":1,\"width\":1},\"resolution\":{\"height\":1350,\"width\":1080,\"percentage\":100},\"output\":{\"color\":{\"color_depth\":\"8\",\"color_mode\":\"RGB\"},\"compression\":15,\"output_format\":\"PNG\",\"project_name\":\"FR-CPU-1\"},\"cycles_config\":{\"denoise_config\":{\"algorithm\":\"OPENIMAGEDENOISE\",\"denoise_pass\":\"RGB_ALBEDO_NORMAL\",\"denoise_prefilter\":\"ACCURATE\",\"noise_threshold\":0.01},\"light_paths\":{\"caustics\":{\"filter_glossy\":1,\"reflective\":true,\"refractive\":true},\"clamping\":{\"indirect\":10,\"direct\":0},\"max_bounces\":{\"diffuse_bounces\":4,\"glossy_bounces\":4,\"total\":12,\"transmission_bounces\":12,\"transparent_max_bounces\":8,\"volume_bounces\":0}},\"samples\":50}}}}"

    ### EEVEE AUTO RENDER CONFIG ###
    # command_container_json_str = "{\"render_config\":{\"type\":\"frame\",\"is_render_auto\":true,\"use_denoise\":false,\"engine\":\"BLENDER_EEVEE\",\"use_gpu\":true,\"use_compositor\":true,\"use_sequencer\":true,\"use_stamp_metadata\":false,\"active_frame\":1,\"start_frame\":1,\"end_frame\":25,\"frame_step\":1,\"fps\":24,\"render_info\":{\"scene_name\":\"Scene\",\"layer_name\":\"View Layer\",\"camera_name\":\"Camera\",\"aspect_ratio\":{\"height\":1,\"width\":1},\"resolution\":{\"height\":1350,\"width\":1080,\"percentage\":100},\"output\":{\"color\":{\"color_depth\":\"8\",\"color_mode\":\"RGB\"},\"compression\":15,\"output_format\":\"PNG\",\"project_name\":\"FR-CPU-1\"},\"cycles_config\":{\"denoise_config\":{\"algorithm\":\"OPENIMAGEDENOISE\",\"denoise_pass\":\"RGB_ALBEDO_NORMAL\",\"denoise_prefilter\":\"ACCURATE\",\"noise_threshold\":0.01},\"light_paths\":{\"caustics\":{\"filter_glossy\":1,\"reflective\":true,\"refractive\":true},\"clamping\":{\"indirect\":10,\"direct\":0},\"max_bounces\":{\"diffuse_bounces\":4,\"glossy_bounces\":4,\"total\":12,\"transmission_bounces\":12,\"transparent_max_bounces\":8,\"volume_bounces\":0}},\"samples\":50}}}}"

    ### EEVEE CUSTOM RENDER CONFIG ###
    # command_container_json_str = "{\"render_config\":{\"type\":\"frame\",\"is_render_auto\":false,\"use_denoise\":false,\"engine\":\"BLENDER_EEVEE\",\"use_gpu\":true,\"use_compositor\":true,\"use_sequencer\":true,\"use_stamp_metadata\":false,\"active_frame\":1,\"start_frame\":1,\"end_frame\":25,\"frame_step\":1,\"fps\":24,\"render_info\":{\"scene_name\":\"Scene\",\"layer_name\":\"View Layer\",\"camera_name\":\"Camera\",\"aspect_ratio\":{\"height\":1,\"width\":1},\"resolution\":{\"height\":1350,\"width\":1080,\"percentage\":100},\"output\":{\"color\":{\"color_depth\":\"8\",\"color_mode\":\"RGB\"},\"compression\":15,\"output_format\":\"PNG\",\"project_name\":\"FR-CPU-1\"},\"cycles_config\":{\"denoise_config\":{\"algorithm\":\"OPENIMAGEDENOISE\",\"denoise_pass\":\"RGB_ALBEDO_NORMAL\",\"denoise_prefilter\":\"ACCURATE\",\"noise_threshold\":0.01},\"light_paths\":{\"caustics\":{\"filter_glossy\":1,\"reflective\":true,\"refractive\":true},\"clamping\":{\"indirect\":10,\"direct\":0},\"max_bounces\":{\"diffuse_bounces\":4,\"glossy_bounces\":4,\"total\":12,\"transmission_bounces\":12,\"transparent_max_bounces\":8,\"volume_bounces\":0}},\"samples\":50}}}}"
    
    ### JOB 3 COMMANDS ###
    # command_container_json_str = "{\"ses\":{\"ses_active\":true,\"animation_preview\":{\"animation_preview_full_resolution\":true,\"fps\":24,\"resolution_x\":1080,\"resolution_y\":1350,\"output_quality\":\"HIGH\",\"encoding_speed\":\"GOOD\",\"autosplit\":false,\"ffmpeg_format\":\"MPEG4\"},\"render_details\":{\"project_name\":\"FR-CPU-1\",\"resolution\":\"1080x1350\",\"scene_name\":\"Scene\",\"layer_name\":\"View Layer\",\"camera_name\":\"Camera\",\"samples\":50,\"engine\":\"CYCLES\",\"render_type\":\"Animation\",\"active_frame\":1,\"frame_range\":\"1-25\",\"job_array_size\":\"0\"},\"ses_config\":{\"region\":\"us-east-1\",\"source_email\":\"test@gmail.com\",\"destination_email\":\"test@gmail.com\",\"render_ok_template_name\":\"RenderCompletedTemplate\",\"render_error_template_name\":\"RenderFailedTemplate\",\"batch_job_2_id\":\"d8ae665c-cce9-4c7b-8eef-f855f47a879c\"}}}"

    # Parse JSON from AWS Batch job command
    json_command_container = parse_json(command_container_json_str)
    print("Parsed JSON:", json_command_container)

    # Get job action path from job action type
    job_action_script_path = get_job_action_path(job_action)
    print("Job action script path:", job_action_script_path)

    # Execute script by job action type
    execute_script_by_action(json_command_container, job_action_script_path, job_action)


if __name__ == '__main__':
    main()