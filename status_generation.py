import streamlit as st
from PIL import Image, ImageDraw, ImageFont

x1 = 570
y1 = 55
y_margin = 180
y2 = y1 + y_margin
y3 = y2 + y_margin
y4 = y3 + y_margin
y5 = y4 + y_margin
y6 = y5 + y_margin
y7 = y6 + y_margin
box_width = 50
box_height = 100
margin = 20
text_margin_x = 5
text_margin_y = 5

def generate_status_image(stats):
    # imageフォルダからstatus_template.pngをロード
    img = Image.open("image/status_template.png")
    draw = ImageDraw.Draw(img)

    # 各ステータスの位置を定義
    positions = {
        "VIT": (x1, y1),
        "STR": (x1, y2),
        "MAG": (x1, y3),
        "DEX": (x1, y4),
        "INT": (x1, y5),
        "AGI": (x1, y6),
        "LUK": (x1, y7),
    }

    # フォントをロード
    font = ImageFont.truetype("font/mitimasu.ttf", size=100) # フォントのパスとサイズは適宜調整

    # 各ステータスの四角と数値を描画
    for stat, value in stats.items():
        x, y = positions[stat]
        for i in range(value):
            # 四角を描画
            draw.rectangle([x-1, y-1, x + box_width + 1, y + box_height + 1], fill="gray")
            if(value == 10):
                draw.rectangle([x, y, x + box_width, y + box_height], fill="red")
            else:
                draw.rectangle([x, y, x + box_width, y + box_height], fill="orange")
            x += box_width + margin # 次の四角の位置
        for i in range(value + 1, 11):
            # 四角を描画
            draw.rectangle([x-1, y-1, x + box_width + 1, y + box_height + 1], fill="gray")
            draw.rectangle([x, y, x + box_width, y + box_height], fill="white")
            x += box_width + margin # 次の四角の位置

        # 数値を描画
        text_x = x + text_margin_x # 数値のX位置は調整が必要
        text_y = y + text_margin_y # 数値のY位置は調整が必要
        draw.text((text_x, text_y), str(value), font=font, fill="black") 

    return img


st.title("キャラクターステータス画像生成")
st.markdown("""
## 概要
0～10の整数を入力して下部のボタンを押すと、キャラクターステータスの画面が生成されます。\n
- このアプリで生成されたイラストは、商用・非商用を問わず自由に利用できます。
- 生成されたイラストの再配布や転載は自由ですが、アプリ自体の複製・再配布は禁止します。
- 作者：らけしでhttps://twitter.com/lakeside529
- SNS投稿時に 「#キャラステ生成機」 をつけて貰えると喜びます（必須ではないです）
""")

# ステータス入力
vit_ = st.number_input('VIT', min_value=0, max_value=10, value=0)
str_ = st.number_input('STR', min_value=0, max_value=10, value=0)
mag_ = st.number_input('MAG', min_value=0, max_value=10, value=0)
dex_ = st.number_input('DEX', min_value=0, max_value=10, value=0)
int_ = st.number_input('INT', min_value=0, max_value=10, value=0)
agi_ = st.number_input('AGI', min_value=0, max_value=10, value=0)
luk_ = st.number_input('LUK', min_value=0, max_value=10, value=0)

# 画像生成ボタン
if st.button('生成'):
    stats = {"VIT": vit_, "STR": str_, "MAG": mag_, "DEX": dex_, "INT": int_, "AGI": agi_, "LUK": luk_}
    output_image = generate_status_image(stats)
    st.image(output_image)