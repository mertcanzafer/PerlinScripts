from JsonBuilder import JsonBuilder
import json


class AssetJsonBuilder(JsonBuilder):

    def DeserializeJsonFile(self, fileName):
        path = "../Assets/Config/" + fileName

        try:
            with open(path, 'r') as file:
                data = json.load(file)
                return data

        except FileNotFoundError:
            print("Error: The file was not found.")
            return None

    def SerializeJsonFile(self, fileName, data):
        path = "../Assets/Config/" + fileName

        try:
            jsonStr = json.dumps(data, indent=4)

            with open(path, 'w') as file:
                file.write(jsonStr)

            return 1

        except FileNotFoundError:
            print("Error: The file was not found.")
            return None

    def UpdateJsonData(self, srcData, dstData):
        if srcData is None or dstData is None:
            print("Error occurred")
            return None

        print(json.dumps(srcData, indent=4))

        for m in srcData["meshes"]:
            for t in m["textures"]:
                dstData["textures"].append({
                    "name": t
                })

        return dstData