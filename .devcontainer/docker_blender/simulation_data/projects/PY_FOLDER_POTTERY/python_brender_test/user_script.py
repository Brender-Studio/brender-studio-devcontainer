import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

if script_dir not in sys.path:
    sys.path.append(script_dir)
    
from utils.blender_render_utils import check_output_path, get_active_frame, set_render_filepath, render_image


def main():

    main_folder = sys.path[0]
    print(f'Script location: {main_folder}')

    
    # Verify the output path
    output_path = check_output_path()
    print(f'Output path: {output_path}')
    
    
    # Get the active frame
    active_frame = get_active_frame()
    print(f'Active frame: {active_frame}')
    
    # Set the render filepath
    render_file_path = set_render_filepath(output_path, active_frame)
    print(f'Configurando el filepath para el renderizado: {render_file_path}')
    
    
    # Render the image
    render_image()

if __name__ == "__main__":
    main()
