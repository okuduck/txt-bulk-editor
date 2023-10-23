import os
from PIL import Image

def downscale_images(input_path, output_path, scale_factor):
    # 画像を順番に読み込む
    image_files = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort()  # ファイルをソートして順番に読み込む

    for image_file in image_files:
        image_path = os.path.join(input_path, image_file)
        # print('image_path', image_path)
        downscale_image(image_path, image_path, scale_factor)

def downscale_image(input_path, output_path, scale_factor):
    # 画像を開く
    image = Image.open(input_path)

    # ダウンスケール
    # width, height = image.size
    new_width = int(scale_factor)
    new_height = int(scale_factor)
    downscaled_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # ダウンスケール後の画像を保存
    downscaled_image.save(output_path)

def upscale_images(input_path, output_path, scale_factor):
    image_files = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort()  # ファイルをソートして順番に読み込む

    for image_file in image_files:
        image_path = os.path.join(input_path, image_file)
        # print('image_path', image_path)
        upscale_image(image_path, image_path, scale_factor)
        
def upscale_image(input_path, output_path, scale_factor):
    # 画像を開く
    image = Image.open(input_path)

    # ダウンスケール
    # width, height = image.size
    new_width = int(scale_factor)
    new_height = int(scale_factor)
    downscaled_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # ダウンスケール後の画像を保存
    downscaled_image.save(output_path)