import bpy
import os

output_path = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')

# Verify if the output path exists, if not, create it
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Carpeta de salida {output_path} creada correctamente.")
else:
    print(f"La carpeta de salida {output_path} ya existe.")


def render_still(active_frame):
    # Set the active frame 
    bpy.context.scene.frame_set(active_frame)

    print("Valor de output_path:", output_path)

    # Set the render file path for the frame
    render_file_path = os.path.join(output_path, f"{active_frame:05d}")
    
    print("Valor de render_file_path:", render_file_path)

    # Set the render file path in the scene
    bpy.context.scene.render.filepath = render_file_path

    # Render the frame
    bpy.ops.render.render(write_still=True)

# def render_still(scene_name, layer_name, active_frame):
#     # Asegúrate de que estamos usando la escena correcta
#     if scene_name in bpy.data.scenes:
#         bpy.context.window.scene = bpy.data.scenes[scene_name]
#     else:
#         print(f"Error: La escena '{scene_name}' no existe.")
#         return
    
#     # Configura el nodo Render Layers para usar la capa específica
#     bpy.context.scene.use_nodes = True
#     render_layer_node = bpy.context.scene.node_tree.nodes.get("Render Layers")
#     if render_layer_node:
#         render_layer_node.layer = layer_name
#     else:
#         print("Error: No se encontró el nodo Render Layers en el árbol de nodos.")
#         return

#     # Set the active frame 
#     bpy.context.scene.frame_set(active_frame)

#     print("Valor de output_path:", output_path)

#     # Configura la ruta de salida
#     output_file = os.path.join(output_path, f"{layer_name}_{active_frame:05d}")
#     bpy.context.scene.render.filepath = output_file

#     # Renderiza y guarda
#     bpy.ops.render.render(write_still=True)

#     print(f"Renderizada y guardada la capa '{layer_name}' de la escena '{scene_name}' en {output_file}")


def render_still_without_compositor(scene_name, layer_name, active_frame):
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

    # Set the active frame 
    scene.frame_set(active_frame)

    print("Valor de output_path:", output_path)

    # Configura la ruta de salida
    output_file = os.path.join(output_path, f"{layer_name}_{active_frame:05d}")
    scene.render.filepath = output_file

    # Renderiza y guarda
    bpy.ops.render.render(write_still=True)

    print(f"Renderizada y guardada la capa '{layer_name}' de la escena '{scene_name}' en {output_file}")

