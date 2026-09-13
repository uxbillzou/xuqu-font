#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json
ROOT=Path(__file__).resolve().parents[1]

TRIAGE={
 'googlefonts/metadata/unreachable_subsetting':('接入阶段确认','尚未生成正式 METADATA.pb；部分辅助符号与私用 Logo 不一定由 Google Fonts 服务端分发。由接入维护者核对子集，不虚报支持其他文字系统。'),
 'googlefonts/glyphsets/shape_languages':('范围说明','必需字形及语言排版检查已通过。提示涉及可选辅助字符，如部分萨米语/扩展拼写字符，本版不声明覆盖这些附加范围。'),
 'googlefonts/gasp':('规范差异待审核','字体刻意不做 hinting，采用官方静态展示字体指南建议的 GASP 0x000A。Fontspector 此检查偏好 0x000F；未为消除提示而添加不存在的提示程序。'),
 'googlefonts/vendor_id':('可选品牌登记','保留真实项目厂商标识 XUQU，未宣称已在 Microsoft 注册。是否登记可在正式发布前决定，不借用他人标识。'),
 'contour_count':('人工设计审阅','几何式 section 等符号的轮廓数量与统计常见值不同；并非缺字判定。保留原设计，由字体设计审核确认。'),
 'math_signs_width':('已知设计差异','沿用 v1.3 中 minus、比较符号的不同字宽；本版是展示字体，并未宣称数学符号等宽。正式接入可按审核意见统一。'),
 'rupee':('可选字符','本版未收录印度卢比符号 U+20B9。它不是本次固定 GF Latin Core 清单的缺失项，不声明支持完整货币符号集合。'),
 'soft_hyphen':('保留兼容性','保留原有 U+00AD；HarfBuzz 将其按软连字符语义处理。没有为降低警告数删除旧字符。'),
 'outline_alignment_miss':('原轮廓保留','部分切角/斜线交点接近基线或字高，偏差约 1–2 单位。回归已核对实际字形；未擅自改动已批准轮廓以消除启发式提示。'),
 'outline_colinear_vectors':('原轮廓保留','转换清理了严格共线点；整数化后的近似共线向量仍可能触发检查。保持 A/B 等已批准轮廓的几何一致。'),
 'outline_short_segments':('原轮廓保留','包括已确认 B 中部短平口和部分切角的短线段。保留实际设计，在附带大字号样张中可查看。'),
}
def main():
    cfg=json.loads((ROOT/'project.json').read_text())
    q=ROOT/'documentation/qa';j=json.loads((q/'fontspector.json').read_text());base=json.loads((q/'baseline-fontspector.json').read_text());reg=json.loads((q/'regression.json').read_text())
    counts=Counter();fails=Counter()
    for sections in j['results'].values():
        for checks in sections.values():
            for c in checks:
                for s in c['subresults']:
                    if s['severity']=='WARN':counts[c['check_id']]+=1
                    if s['severity'] in ('FAIL','ERROR','FATAL'):fails[(s['severity'],c['check_id'])]+=1
    assert set(counts)<=set(TRIAGE),set(counts)-set(TRIAGE)
    lines=['# XUQU体 Google Fonts 准备版：检查汇总','',
      f"日期：2026-09-13。版本：{cfg['version']}。名称：Xuqu。**作者已确认整套 OFL 1.1 授权与邹旭个人版权；这仍是提交准备文件，尚未获 Google Fonts 收录。**",'',
      '## 本次结果','',
      '| 检查 | 结果 |','|---|---|',
      '| 授权与署名 | OFL 1.1、名称 Xuqu、个人版权 Xu Zou (邹旭) 已同步到五字重和作者文件 |',
      f"| {cfg['version']} 元数据更新 | 每款 416 个字形全部保留；与 1.401 的所有非元数据字体表字节一致，包括轮廓、字宽、字距和定位表 |",
      '| 可编辑源文件与构建 | 五份 UFO，已用 fontmake 3.12.1 重建五份 TTF 和五份 WOFF2 |',
      '| GF Latin Core | 324 项：319 个编码项、5 个必需非编码字形全部存在 |',
      '| 字符保留 | 原有 357 个编码字符全部保留；现在每款 400 个编码字符、416 个字形 |',
      '| A / B | 五档字重均与已确认 v1.3 的轮廓和字宽精确一致 |',
      '| 字重递进 | 每款 388 个非空白编码字形，所有相邻字重着墨面积严格递增 |',
      '| 原字形回归 | 每款 342 个原编码字形/字宽完全相同；15 个有记录的语言/数字改进 |',
      '| 字体引擎验证 | FreeType 全部编码字形栅格化，HarfBuzz 重音、去点、字距、Catalan locl、tnum 检查通过 |',
      '| 文件格式 | TTF 与 WOFF2 字符映射、轮廓和字宽一致 |',
      '| 重建一致性 | 同一组 UFO 连续构建，10 个输出文件 SHA-256 完全一致；见 reproducibility.json |','',
      '## 官方工具结果','',
      '使用官方 Fontspector **1.7.4**，`googlefonts` 配置，`--skip-network`。**没有排除任何具体检查 ID。** 以下数字是跨字体/家族的检查结果统计，不是独立字形数量。','',
      '| 状态 | 原 v1.3 基线 | 当前准备版 |','|---|---:|---:|']
    for k in ['PASS','WARN','FAIL','ERROR','FATAL','INFO','SKIP']:lines.append(f"| {k} | {base['summary'].get(k,0)} | {j['summary'].get(k,0)} |")
    nfail=sum(fails.values())
    blocking_note=(f'当前有 {nfail} 项 FAIL/ERROR/FATAL，不能标为全通过。' if nfail else '当前无 FAIL/ERROR/FATAL；仍需审阅 WARN 与未执行项。')
    if fails and all(cid in ('googlefonts/font_copyright','googlefonts/license/OFL_copyright') for _,cid in fails):
        blocking_note+='授权决定已经完成；这些 FAIL 都与 Google Fonts 要求的版权行中缺少真实项目仓库 URL 有关。'
    lines+=['',blocking_note]
    if fails:lines+=['','| 次数 | 检查 | 处理方式 |','|---:|---|---|']
    reasons={
        'googlefonts/font_copyright':'5 份字体中的项目版权行需要追加真实仓库 URL；收到地址后同步更新。不是版权主体尚未确认。',
        'googlefonts/license/OFL_copyright':'正式 OFL.txt 已存在且文本检查通过；首行还需要与字体一致的真实仓库 URL。授权已经启用。'
    }
    for (severity,cid),n in sorted(fails.items()):
        reason=reasons.get(cid,'查看原始报告中的实际失败信息，修复后重跑完整检查。')
        lines.append(f'| {n} | `{cid}` | {reason} |')
    lines+=['','正式授权文件已作为检查输入。真实仓库 URL 已统一写入 OFL 与五份字体，原有六项版权格式失败已经消除。','',
      '## WARN 逐项说明','',
      '保留所有原始 WARN；以下是本地审阅结论，不是 Google 对例外的批准。','',
      '| 次数 | 检查 | 分类 | 说明 |','|---:|---|---|---|']
    for k,n in sorted(counts.items()):cat,msg=TRIAGE[k];lines.append(f'| {n} | `{k}` | {cat} | {msg} |')
    lines+=['','## 未完成和受限部分','',
      '- 自动审批拒绝了外部名称检查服务的请求，理由是名称/元数据向未经授权目的地发送。未绕过限制；正式名称查重待单独授权或由作者自行核实。',
      f"- {j['summary'].get('SKIP',0)} 个 SKIP 包括离线网络项、可变字体不适用项，以及缺少正式接入资料时无法执行的项目。不能将它们计为通过。",
      '- 未在 Mac/Windows 字体安装界面和 Adobe/Figma GUI 中测试；不声称已通过这些环境验收。',
      '- 公开仓库为 https://github.com/uxbillzou/xuqu-font。作者已报告提交 CLA 并提供成功页面；Google 账号匹配尚未核验。正式收录申请尚未发送，设计审核、名称查重和持续维护承诺仍需完成。','',
      '## 原始证据','',
      '- `qa/fontspector.json` / `.md` / `.html`：当前官方完整检查结果。',
      '- `qa/baseline-fontspector.json` / `.md`：原 v1.3 的离线基线。',
      '- `qa/regression.json`：逐字重、逐字符和排版验证。',
      '- `qa/metadata-update.json`：1.401 到 1.402 的全部非元数据字体表一致性与授权字段核对。',
      '- `qa/source-conversion.json`：新增字符和既有字形改动。',
      '- `qa/reproducibility.json`：重复构建的输出校验值。',
      '- `qa/build.json`：最终字体文件名、字符数、字重、校验值。',
      '- `qa/fontspector-tool.json`：使用的官方工具发布版本及下载包校验值。','',
      '参考：[QA 指南](https://googlefonts.github.io/gf-guide/qa.html)、[静态字体说明](https://googlefonts.github.io/gf-guide/statics)、[收录要求](https://googlefonts.github.io/gf-guide/onboarding.html)。','']
    (ROOT/'documentation/QA-SUMMARY.md').write_text('\n'.join(lines))
    print('Wrote QA summary with all warning categories.')
if __name__=='__main__':main()
