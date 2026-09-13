# XUQU体 · 五字重字体家族

字体家族版本：1.3

包含极细、细体、常规、粗体、特粗五档真实字重。v1.3 合入已确认的 B 字母连接优化，并保留 v1.2 的全部字重修正。每个字重均包含 357 个 Unicode 编码字符，覆盖大小写英文、数字、常用标点、Latin-1 和 Latin Extended-A，以及部分排版／数学符号。

| 中文名称 | 英文样式 | 字重值 | 文件名前缀 |
| --- | --- | ---: | --- |
| 极细 | Thin | 100 | XUQU-Thin |
| 细体 | Light | 300 | XUQU-Light |
| 常规 | Regular | 400 | XUQU-Regular |
| 粗体 | Bold | 700 | XUQU-Bold |
| 特粗 | ExtraBold | 800 | XUQU-ExtraBold |

## 安装

选中 `fonts` 文件夹中五个 `.ttf` 文件并安装。也可以选择五个 `.otf` 文件；同一台设备安装 TTF 或 OTF 中的一套即可。如已安装旧版，请先退出设计软件并移除旧版 XUQU 字体，再安装本包完整的五个字重。这样可避免同名字体缓存导致仍显示旧版。

支持字体家族分组的软件中，搜索 **XUQU体** 并选择相应字重。部分旧软件按旧式命名显示，Thin、Light、ExtraBold 可能分别列为 **XUQU Thin**、**XUQU Light**、**XUQU ExtraBold**；Regular 与 Bold 使用常规／粗体链接。

安装时已经打开的设计软件可能需要重新打开，才能刷新字体列表。

## 文件格式

- **TTF**：桌面通用字体，每个字重一份。
- **OTF**：相同设计的 PostScript/CFF 轮廓格式，每个字重一份。
- **WOFF2**：网页字体，每个字重一份。五档静态字重不是可变字体。
- `webfont.css`：五字重网页声明。
- `XUQU-Preview.html`：建议优先打开的新版五字重试字入口。
- `preview/XUQU-Five-Weights.png`：五字重对比样张。
- `preview/XUQU-Family-Live-Preview.html`：与根目录入口相同的离线试字页，可更换文字、字号、字重和背景。直接绘制字体中的 SVG 轮廓，不依赖网页字体加载；下方始终保留五档真实字形对比。
- `preview/XUQU-Preview-Comparison.png`：由新版预览的矢量字形绘制的五档对比图。
- `preview/XUQU-Proof-*.png`：字母、数字、符号等排版检查样张。

## 设计与适用范围

保留宽字面、方形骨架、切角转折与锐利边缘。各字重是实际的字体轮廓文件。在常规体矢量基础上进行轮廓扩展／收缩，并直接绘制 A、B、&、#、e、标点等的各档笔画；重音字母继承同档基础字母，重音独立处理。检查覆盖全部编码字符，而非少量示例。

适合品牌英文、视频封面、海报与短标题。极细体优先用于大字号，以保留细线的清晰度。本版不包含中文字形，也不包含斜体。

试字时请使用英文、数字或支持的拉丁字符。输入中文时，预览页会明确提示未收录；中文不会随 XUQU体 的字重变化。若文件查看器不运行 HTML 交互脚本，可下载 HTML 后在浏览器中打开；静态五字重对比不需要脚本。

五个字重的内部版本统一为 1.300。本次仅调整五个字重的 B 轮廓，字高、字宽和排版间距保持一致；其他字符沿用 v1.2。字体家族名称统一为 XUQU体，各字重有独立 PostScript 名称。

## 源文件与重建

`source/base_regular.py` 为原常规体矢量主稿，`source/build_family.py` 为字重生成脚本，`source/b-approved-outlines.json` 保存已确认的五档 B 轮廓，`source/make_family_preview.py` 为样张生成脚本。

```sh
python -m pip install -r source/requirements.txt
python source/build_family.py
python source/make_family_preview.py
python source/make_audit_preview.py
python source/validate_family.py
python source/audit_weights.py
node source/check_vector_preview.cjs
```

构建参数与光学修正记录见 `source/family-build.json`。格式与排版验证结果见 `source/validation.json`；全部字符的逐档着墨面积、渲染检查与字腔记录见 `source/weight-audit.json`。`source/b-integration-validation.json` 记录了最终 B 与确认稿逐档一致、其他字形和间距保持不变的核对结果。

## v1.3 B 连接优化

- 上下字腔共用一条中横，消除叠合造成的中间笔画过厚。
- 右侧连接采用短平口，保留几何切角风格。
- 五个字重均采用已确认的轮廓，并保持原有字高、字宽与间距。
- 全部试字预览与样张同步更新。

## v1.2 字重修正（本版保留）

- A 的粗体和特粗在相同字高、字宽下，实际轮廓着墨面积由约 2% 的差距增至约 21%。
- 修复带重音字母的基础字形被整体缩放、导致特粗变细的问题。
- 统一圆点、引号、省略号等标点的粗细递进，修正部分符号与组合字母。
- 修正极细连接处、特粗间隙和小字腔，并清除复合字形中的多余小孔。
- 字号与字重不同：相同字号下，A 的外框大小一致是正常的；特粗应体现为更厚的笔画与相应缩小的字腔。

`preview/XUQU-Weight-Fix.png` 为修正前后对比，`preview/XUQU-All-Glyphs-*.png` 为完整字符检查样张。

## 验证范围

使用 fontTools 检查命名、字符覆盖、字重值与字体解析，使用 FreeType 栅格化全部非空白字符，并使用 HarfBuzz 检查示例排版与字距。验证运行环境未进行 Windows/macOS 字体安装窗口或 Adobe/Figma 的图形界面安装验收。

## 联系作者

作者：序曲

微信号：**w86166569**

欢迎交流字体使用、品牌设计与 AIGC 创作，可搜索微信号添加好友。
