# PerlinScripts

Helper batch and Python scripts used to simplify development workflows for the Perlin3D engine.

## Features

- **Build.bat**
  - Converts texture files into `.ktx2` format for Vulkan texture usage.

- **HardcodedJsonBuilder.py**
  - Deserializes hardcoded source JSON files, processes their contents, and serializes the result into destination JSON files.
  - Currently used for generating and updating texture registry data from mesh asset metadata.

- **JsonBuilder.py**
  - Deserializes source and destination JSON files provided through command-line arguments.
  - Processes mesh texture metadata and appends generated texture entries into destination JSON registries.