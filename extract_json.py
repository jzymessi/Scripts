import json

with open('/data/dataset/data/weice_data/annotations/aoi_20230707/val_labels.json') as f:
    data = json.load(f)
    file_names = [image["file_name"] for image in data["images"]]
    ids = [image["id"] for image in data["images"]]

with open("/data/dataset/data/weice_data/annotations/aoi_20230707/accuracy_det_list.txt", "w") as file:
    for file_name, image_id in zip(file_names, ids):
        file.write(f"/data/dataset/data/weice_data/det/aoi_2023_07_07/{file_name} {image_id}\n")
