import os
import json

# 指定 "character" 目录的路径
character_folder_path = "character"

# 获取目录中的所有文件名
file_names = [file for file in os.listdir(character_folder_path) if os.path.isfile(os.path.join(character_folder_path, file))]

# 构建包含文件名的JSON数组
file_name_array = {
    "files": file_names
}

# 指定要保存的JSON文件名
json_file_name = "character_files.json"

# 将JSON数组写入文件
with open(json_file_name, "w") as json_file:
    json.dump(file_name_array, json_file)

print(f"文件名已保存到 {json_file_name}")
