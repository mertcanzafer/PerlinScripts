import AssetJsonBuilder
import sys


def main():
    _srcFile = sys.argv[1]
    _dstFile = sys.argv[2]

    _assetInstance = AssetJsonBuilder.AssetJsonBuilder()

    _srcData = _assetInstance.DeserializeJsonFile(_srcFile)
    _dstData = _assetInstance.DeserializeJsonFile(_dstFile)

    _dstData = _assetInstance.UpdateJsonData(_srcData, _dstData)

    if _dstData is not None:
        print("Data updated!")

        _res = _assetInstance.SerializeJsonFile(_dstFile, _dstData)

        if _res is None:
            return
        else:
            print("Serialization success!")


if __name__ == "__main__":
    main()