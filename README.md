# PerlinScripts

Helper batch and Python scripts used to simplify development workflows for the Perlin3D engine.

## Features

- **WinBuild.bat**
  - Converts texture files into `.ktx2` format for Vulkan texture usage.

- **JsonBuilder.py**
  - Provides a base class for JSON serialization, deserialization, and data processing.
  - Defines the common interface used by specialized JSON builders.

- **AssetJsonBuilder.py**
  - Implements asset-specific JSON processing based on `JsonBuilder`.
  - Deserializes source and destination JSON files.
  - Processes mesh texture metadata and updates the destination texture registry.
  - Serializes the updated data back into the destination JSON file.

- **main.py**
  - Entry point for the JSON processing tool.
  - Takes the source and destination JSON filenames through command-line arguments.
  - Uses `AssetJsonBuilder` to deserialize, update, and serialize asset data.

## Usage

Run the JSON processing tool from the `PerlinScripts` directory:

```bash
python main.py meshes.json textures.json
```

Here, `meshes.json` is the source JSON file containing mesh and texture metadata, while `textures.json` is the destination JSON file whose texture registry will be updated.