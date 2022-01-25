from pptx import Presentation
from pptx.util import Inches
from pptx.chart.data import ChartData, CategoryChartData, XyChartData, BubbleChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.enum.text import PP_ALIGN
from pptx.util import Cm, Pt

prs = Presentation()

# レイアウトの決定
slide_layout = prs.slide_layouts[0]

# スライド作成(Slide)
slide = prs.slides.add_slide(slide_layout)
## テキストの設定(placeholders)
slide.shapes.title.text = "テスト1"
slide.placeholders[1].text = "テスト2"


lide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes
shape = shapes.add_textbox(Cm(0), Cm(0), Cm(10), Cm(2))

shape.text = "テスト３"


# スライドの保存
prs.save('python.pptx')


