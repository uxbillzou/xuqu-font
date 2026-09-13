# Xuqu / XUQU体

**1.402 · 五个字重 · SIL OFL 1.1 · 版权归邹旭（Xu Zou）个人**

Xuqu 是从序曲科技英文字标发展而来的拉丁展示字体，采用宽字面、几何骨架、切角转折与锐利边缘，适合品牌英文、海报和视频标题。极细与细体更适合较大字号。

[项目仓库](https://github.com/uxbillzou/xuqu-font) · [检查报告](documentation/QA-SUMMARY.md) · [制作来源](documentation/PROVENANCE.md)

## 文件与使用

| 内容 | 位置 |
|---|---|
| 极细 100、细体 300、常规 400、粗体 700、特粗 800 | fonts/ttf/ |
| 五款 WOFF2 网页字体 | fonts/webfonts/ |
| 五份可编辑 UFO 源文件 | sources/Xuqu-*.ufo/ |
| 构建与专项验证 | scripts/build.py、scripts/validate.py |
| 正式授权与作者 | OFL.txt、AUTHORS.txt、CONTRIBUTORS.txt |
| 实际字体渲染的样张 | documentation/specimens/ |
| 中英文 Google Fonts 提交稿 | review/SUBMISSION.en.md、SUBMISSION.zh-CN.md |

安装 TTF 后，在字体菜单选择 **Xuqu**。网页使用可引入 webfont.css，各档对应真实字体文件。每款含 **400 个编码字符、416 个字形**，补齐固定 GF Latin Core 清单；支持大小写、数字、标点、拉丁重音及组合重音。不含中文、斜体或可变字体。

已批准的 A/B 字形保持一致。1.402 只补充真实仓库 URL 和版本信息；与 1.401 的全部轮廓、字宽、字距和排版表一致。默认数字为比例间距，`tnum` 可启用等宽数字。

## 重建

在仓库根目录运行，已验证 Python 3.12：

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/validate.py
```

Windows 激活命令为 `.venv\Scripts\activate`。安装 Fontspector 1.7.4 后运行：

```sh
python scripts/run_qa.py --fontspector fontspector
```

本次完整离线结果：**467 PASS、51 WARN、0 FAIL、0 ERROR/FATAL、32 INFO、303 SKIP**。未排除检查 ID；警告与未执行项见报告，不能将离线检查等同于 Google 收录。十个字体输出文件的重复构建 SHA-256 一致。

日常修改 UFO 后运行构建即可。`export_sources.py --overwrite` 会覆盖后续字形编辑，仅用于重做初始转换。

## 授权与当前进度

你已授权整套家族已有及未来样式采用 **SIL OFL 1.1**，名称为 **Xuqu**，个人版权主体为 **邹旭 / Xu Zou**。OFL 与五款字体内嵌版权声明已统一写入真实项目仓库地址。

你已确认完成 Google Individual CLA，并提供了提交成功页面。当前记录为“作者已提交”，Google 的账号关联核验仍以后续贡献流程结果为准。仓库不包含这张签署截图。

2026-09-13 已在 namecheck.fontdata.com 查询 Xuqu，未发现完全同名字体；持续维护与公开提交均已获得作者确认。**[Add Xuqu #10962](https://github.com/google/fonts/issues/10962) 已由 uxbillzou 于 2026-09-13 提交**，核实时状态为 Open、暂无评论或审核反馈。申请正文与定稿一致；详细记录见 [申请状态](review/SUBMIT-TO-GOOGLE-FONTS.md)。Google 的设计审核与正式收录仍待进行；未做 Mac/Windows、Adobe/Figma 图形界面安装验收。详细状态见 [清单](review/OWNER-CHECKLIST.md)。

## 联系方式

序曲 / 邹旭 · 南京序曲科技  
邮箱：**zouxu@xuqutech.com**  
微信号：**w86166569**  
GitHub：**uxbillzou**

公开邮箱取自你现有官网源码中的联系栏；本项目不含微信二维码。
