import json

# 你可以在这里修改输入和输出文件路径
input_path = r'C:\Users\LTY\Desktop\（TEST）\response data\Writing\writing-1k(0-129).json'
output_path = r'C:\Users\LTY\Desktop\test\writing-1k(0-129).json'

def remove_label_field(input_path, output_path):
    # 读取原始 JSON 文件
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 删除每条记录中的 "label" 字段
    for item in data:
        if 'label' in item:
            del item['label']

    # 写入新的 JSON 文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"已处理完毕，结果保存为：{output_path}")

if __name__ == '__main__':
    remove_label_field(input_path, output_path)
