import os
import json
from PIL import Image, ImageDraw, ImageFont

with open('ans.json', 'r', encoding='utf-8') as f:
    data_list = json.load(f)

if not os.path.exists('ans_imgs'):
    os.makedirs('ans_imgs')

for i in os.listdir('src_imgs'):
    if i.endswith('.png'):
        for data in data_list:
            tid = data['tid']
            ans_list = data['ans']
            episode = data['episode']

            # match needed file: tid_{tid}.png
            if i == f'tid_{tid}.png':
                print(f"match file: {i}")
                img_path = os.path.join('src_imgs', i)
                img = Image.open(img_path)
                draw = ImageDraw.Draw(img)

                # color: Red
                font = ImageFont.truetype("arial.ttf", 36)
                text_color = (255, 0, 0)

                ans_text = ' '.join(ans_list)

                # pos of text
                img_width, img_height = img.size
                text_y = img_height - 20

                # cal text w and h
                bbox = draw.textbbox((0, 0), ans_text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                text_x = (img_width - text_width) / 2
                text_y -= text_height + 10  # 每个文本之间留一点间距

                # Draw Text
                draw.text((text_x, text_y), ans_text, font=font, fill=text_color)

                # format: tid_{tid}_{episode}.png
                new_filename = f'tid_{tid}_{episode}.png'
                nip = os.path.join('ans_imgs', new_filename)
                img.save(nip)
                print(f"Save to New IMGS: {nip}")
                break

print("ALL DONE!")
