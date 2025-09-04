import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        wd = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(wd, directory))

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        if not full_path.startswith(wd + os.sep) and full_path != wd:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        results = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            size = os.path.getsize(item_path)
            results.append(f"- {item}: file_size={size} bytes, is_dir={os.path.isdir(item_path)}")
        return "\n".join(results)

    except Exception as e:
        return f"Error: {e}"

