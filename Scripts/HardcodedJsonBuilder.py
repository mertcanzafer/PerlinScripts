import json

def DeserializeJsonFile(fileName):
    path = "../Assets/Config/" + fileName
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    
def SerializeJsonFile(fileName, data):
    path = "../Assets/Config/" + fileName
    try:
        jsonStr = json.dumps(data,indent=4)
        with open(path, 'w') as file:
            file.write(jsonStr)
            return 1
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None

srcFile = "meshes.json"
dstFile = "textures.json"
srcData = DeserializeJsonFile(srcFile)
dstData = DeserializeJsonFile(dstFile)

if(srcData is None):
    print("Error occured")
else:
    print(json.dumps(srcData, indent=4))

    for m in srcData["meshes"]:
        for t in m["textures"]:
            dstData["textures"].append({
                "name": t
            })

res = SerializeJsonFile("textures.json",dstData)

if(res is None):
    print("Error occured")
