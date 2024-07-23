import os
import bpy


# Get the values of environment variables or assign default values
output_path = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH', '/output')
bucket_name = os.environ.get('BUCKET_NAME', 'default-bucket-name')
bucket_key = os.environ.get('BUCKET_KEY', 'default-bucket-key')


# Function to render a specific frame in Blender
def render_still(active_frame):
    # Set the frame to render    
    bpy.context.scene.frame_set(active_frame)

    # Print the value of output_path
    print("Value of output_path:", output_path)

    # Set the output path for rendering according to the render type
    render_file_path = os.path.join(output_path, f"{active_frame:05d}")
    
    # Print the value of render_file_path
    print("Value of render_file_path:", render_file_path)

    # Set the filepath for rendering
    bpy.context.scene.render.filepath = render_file_path

    # Render the image
    bpy.ops.render.render(write_still=True)

# Call the rendering function with a specific frame
render_still(10)