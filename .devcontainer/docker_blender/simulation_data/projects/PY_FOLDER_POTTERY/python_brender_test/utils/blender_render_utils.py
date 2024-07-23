import bpy
import os
import sys

def check_output_path():
    output_path = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')

    if not output_path:
        print("Error: EFS_BLENDER_OUTPUT_FOLDER_PATH not configured.")
        sys.exit(1)
    
    print("output_path:", output_path)
    return output_path

def get_active_frame():
    # Get active frame
    active_frame = bpy.context.scene.frame_current
    bpy.context.scene.frame_set(active_frame)
    print(f"Active frame: {active_frame}")
    return active_frame

def set_render_filepath(output_path, active_frame):
    render_file_path = os.path.join(output_path, f"{active_frame:05d}.png")
    print("render_file_path:", render_file_path)
    bpy.context.scene.render.filepath = render_file_path
    return render_file_path

def render_image():
    bpy.ops.render.render(write_still=True)
    print("Renderizado completado.")
