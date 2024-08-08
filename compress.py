from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    """
    压缩图片，同时尽可能保留质量。
    
    :param input_path: 原始图片路径
    :param output_path: 压缩后图片保存路径
    :param quality: 压缩质量，取值范围是 0 到 100，100 代表最高质量
    """
    # 打开图片
    with Image.open(input_path) as img:
        # 确保图片是 RGB 模式
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # 保存压缩后的图片
        img.save(output_path, "JPEG", quality=quality, optimize=True)


# 示例用法
input_image_path = "/Users/bohao/Desktop/training_convergence.jpg"
output_image_path = "/Users/bohao/Desktop/PBH/pbihao.github.io/projects/controlnext/figs/training_convergence.jpg"
compress_image(input_image_path, output_image_path, quality=50)

