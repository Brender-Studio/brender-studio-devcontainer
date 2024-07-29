import bpy
import os

output_path = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')
array_size = os.environ.get('AWS_BATCH_JOB_ARRAY_SIZE', '1')  
job_index = os.environ.get('AWS_BATCH_JOB_ARRAY_INDEX', '0')

def calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step):
    start_frame = int(start_frame)
    end_frame = int(end_frame)
    frame_step = int(frame_step)
    array_size = int(array_size)
    job_index = int(job_index)
    
    if array_size == 1:
        # If not running as an array job, render all frames
        return start_frame, end_frame, frame_step
    
    total_frames = end_frame - start_frame + 1
    frames_per_chunk = total_frames // array_size
    extra_frames = total_frames % array_size
    
    chunk_start = start_frame + job_index * frames_per_chunk + min(job_index, extra_frames)
    chunk_end = chunk_start + frames_per_chunk + (1 if job_index < extra_frames else 0) - 1 
    
    return chunk_start, chunk_end, frame_step

def render_animation(start_frame, end_frame, frame_step):
    start_frame, end_frame, frame_step = calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step)
    for frame in range(int(start_frame), int(end_frame) + 1, int(frame_step)): 
        bpy.context.scene.frame_set(frame)
        render_file_path = os.path.join(output_path, f"{frame:05d}")
        bpy.context.scene.render.filepath = render_file_path
        bpy.ops.render.render(write_still=True)

def render_animation_without_compositor(scene_name, layer_name, start_frame, end_frame, frame_step):
    # Asegúrate de que estamos usando la escena correcta
    if scene_name in bpy.data.scenes:
        scene = bpy.data.scenes[scene_name]
        bpy.context.window.scene = scene
    else:
        print(f"Error: La escena '{scene_name}' no existe.")
        return

    # Desactiva todas las capas excepto la que queremos renderizar
    for layer in scene.view_layers:
        layer.use = (layer.name == layer_name)

    # Configura el nodo Render Layers para usar la capa específica
    scene.use_nodes = True
    render_layer_node = scene.node_tree.nodes.get("Render Layers")
    if render_layer_node:
        render_layer_node.layer = layer_name
    else:
        print("Error: No se encontró el nodo Render Layers en el árbol de nodos.")
        return

    # Configura la ruta de salida para la animación
    base_output_path = os.path.join(output_path, f"{layer_name}")
    if not os.path.exists(base_output_path):
        os.makedirs(base_output_path)

    # Renderiza cada fotograma dentro del rango especificado
    for frame in range(int(start_frame), int(end_frame) + 1, int(frame_step)):
        scene.frame_set(frame)
        render_file_path = os.path.join(base_output_path, f"{frame:05d}")
        scene.render.filepath = render_file_path
        bpy.ops.render.render(write_still=True)
        print(f"Renderizado el fotograma {frame} de la capa '{layer_name}' de la escena '{scene_name}' en {render_file_path}")
