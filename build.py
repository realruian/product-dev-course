"""组装产品开发全流程课件 deck.html
基于 _skeleton.html（拷自上一份课件，含所有 CSS 微调：左对齐规则、reveal 动效、复制按钮等）
替换 title / toc / slides 三块，生成新课件。
"""
from pathlib import Path
import re

ROOT = Path(__file__).parent
SKEL = (ROOT / "_skeleton.html").read_text(encoding="utf-8")
DECK_TITLE = "产品开发全流程"


# ============================================================
# 26 项目录
# ============================================================
TOC = [
    (0,  "封面",                       "ch"),
    (1,  "CH00 为什么这么完整地走",    "ch"),
    (2,  "和以前不一样在哪",            "sub"),
    (3,  "为什么要完整走（快≠对）",    "sub"),
    (4,  "真实做法：一个人+工具",       "sub"),
    (5,  "五步全流程",                  "sub"),
    (6,  "传统 vs 现在",                "sub"),
    (7,  "五步在本案例的落地",          "sub"),
    (8,  "与糊一个 demo 的区别",        "sub"),
    (9,  "CH01 发现市场机会",          "ch"),
    (10, "做之前要问的三个问题",        "sub"),
    (11, "CH02 定义产品需求",          "ch"),
    (12, "四份文档：四件套",            "sub"),
    (13, "MRD 是什么",                  "sub"),
    (14, "MRD 示例 · 减脂健身",         "sub"),
    (15, "BRD 是什么",                  "sub"),
    (16, "BRD 示例 · 共享充电宝",       "sub"),
    (17, "PRD 是什么",                  "sub"),
    (18, "PRD 示例 · 待办清单",         "sub"),
    (19, "为什么三份要串行",            "sub"),
    (20, "CH03 先搞懂三个词",          "ch"),
    (21, "前端 = 餐厅大堂",             "sub"),
    (22, "后端 = 餐厅后厨",             "sub"),
    (23, "数据库 = 仓库冰箱",           "sub"),
    (24, "一次完整交互 · 三层结构",     "sub"),
    (25, "结尾 · 接下来跟我实操",       "ch"),
]


# ============================================================
# 26 张 slide
# ============================================================
SLIDES = []

# 00 · 封面
SLIDES.append("""<section class="slide active">
  <div class="eyebrow">产品开发全流程 · 方法论</div>
  <h1 class="display h-xxl">人 × AI<br>产品落地全流程</h1>
  <p class="body-xl mt-l">一个真实案例，把"在公司里开发一个产品"完整跑一遍</p>
  <p style="position:absolute;bottom:110px;left:290px;font-size:22px;letter-spacing:2px;color:var(--text-secondary);font-weight:500">前期方法论篇 · 后续跟我实操</p>
</section>""")

# 01 · CH00 章节页
SLIDES.append("""<section class="slide">
  <div class="slide-header"><span>Chapter 00</span><span>Why This Way</span></div>
  <div class="chapter-watermark">00</div>
  <div class="chapter">
    <span class="num">Chapter 00</span>
    <h2 class="title">为什么要这么<br>完整地走一遍</h2>
    <div class="sub">"快"不等于"好"——做得对，比做得快更重要。</div>
  </div>
</section>""")

# 02 · 这次和以前不一样在哪
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>这次和以前不一样</span></div>
  <div class="top-title">不是做小东西，是一个真实产品 · 完整跑通</div>
  <div style="width:100%;max-width:1620px">
    <div class="card" style="padding:42px 52px">
      <div class="card-label">这次的不一样</div>
      <ul class="bullet-list" style="font-size:30px;margin-top:14px">
        <li>是一个<strong>真实案例</strong>，从头到尾走一遍"在公司里开发产品"的全过程</li>
        <li>一直走到<strong>落地、部署、上线</strong>——结束后你拿到一个能发给别人用的<strong>真实链接</strong></li>
        <li>把完整产品的所有技术全串到——<strong>前端 / 后端 / 数据库</strong>，一个不落</li>
      </ul>
    </div>
  </div>
</section>""")

# 03 · 为什么完整走（快 ≠ 对）
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>快 ≠ 好</span></div>
  <div class="top-title">"快"不等于"好"</div>
  <div style="width:100%;max-width:1620px">
    <p class="body-l" style="text-align:center;color:var(--text-secondary);margin-bottom:24px">用 AI 做应用确实<strong>太方便、太快了</strong>。但快出来的东西——</p>
    <div class="two-col">
      <div class="card" style="padding:38px 44px">
        <div class="card-label">三个真正的问题</div>
        <ul class="bullet-list" style="font-size:26px;margin-top:14px">
          <li>是不是真的<strong>有用</strong>？</li>
          <li>是不是真的<strong>有价值</strong>？</li>
          <li>能不能被<strong>市场认可</strong>？放进简历能不能让面试官认可？</li>
        </ul>
      </div>
      <div class="card" style="padding:38px 44px;border-color:var(--text)">
        <div class="card-label" style="color:var(--accent)">这套流程要解决的</div>
        <div class="body-l mt-m" style="color:var(--text);line-height:1.6">"做得快"之外的<strong>那半句</strong>——<br><span style="font-size:48px;font-weight:700">做得对。</span></div>
      </div>
    </div>
  </div>
</section>""")

# 04 · 真实做法（公式金句）
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>企业里的真实做法</span></div>
  <div class="top-title">现在企业里真实的做法</div>
  <div style="display:inline-block">
    <div class="formula" style="font-size:66px">
      一个人 &nbsp;+&nbsp; <span class="hl">Claude Code · Agent Skills · MCP</span>
    </div>
  </div>
  <p class="body-xl mt-xl" style="max-width:1500px;text-align:center">一套工具组合，把过去一支团队的活，<strong>一个人就能跑完</strong>。</p>
</section>""")

# 05 · 五步全流程（reveal）
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>五步全流程</span></div>
  <div class="top-title">一套完整的产品开发流程 · 就五步</div>
  <div style="width:100%;max-width:1620px" data-step-reveal>
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px">
      <div class="step-card reveal-step" data-step="0" style="padding:28px 22px">
        <div class="step-num">Step 01</div>
        <div style="font-size:26px;font-weight:700;margin-top:10px;line-height:1.3">发现<br>市场机会</div>
      </div>
      <div class="step-card reveal-step" data-step="1" style="padding:28px 22px">
        <div class="step-num">Step 02</div>
        <div style="font-size:26px;font-weight:700;margin-top:10px;line-height:1.3">定义<br>产品需求</div>
      </div>
      <div class="step-card reveal-step" data-step="2" style="padding:28px 22px">
        <div class="step-num">Step 03</div>
        <div style="font-size:26px;font-weight:700;margin-top:10px;line-height:1.3">设计<br>产品原型</div>
      </div>
      <div class="step-card reveal-step" data-step="3" style="padding:28px 22px">
        <div class="step-num">Step 04</div>
        <div style="font-size:26px;font-weight:700;margin-top:10px;line-height:1.3">快速<br>开发实现</div>
      </div>
      <div class="step-card reveal-step" data-step="4" style="padding:28px 22px;border-color:var(--text)">
        <div class="step-num" style="color:var(--accent)">Step 05</div>
        <div style="font-size:26px;font-weight:700;margin-top:10px;line-height:1.3">完成<br>产品上线</div>
      </div>
    </div>
    <p class="body-l reveal-final mt-xl" style="color:var(--text-secondary);text-align:center">注意：这五步和传统做产品<strong>没有任何区别</strong>。唯一的区别是——传统是一堆人分角色按部就班；我们是<strong>一个人，用 AI</strong> 把这五步跑完。</p>
    <div class="reveal-hint" style="position:absolute;bottom:96px;left:50%;transform:translateX(-50%);font-family:'JetBrains Mono',monospace;font-size:14px;letter-spacing:2px;color:var(--text-meta);text-transform:uppercase">按 → 依次点亮 · <span class="reveal-counter">0</span>/5</div>
  </div>
</section>""")

# 06 · 传统 vs 现在（大数据对比）
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>代价差多少</span></div>
  <div class="top-title">代价差多少 · 传统 vs 现在</div>
  <div style="width:100%;max-width:1500px">
    <div class="two-col">
      <div class="card" style="padding:48px 52px">
        <div class="card-label">传统方式</div>
        <div style="font-size:80px;font-weight:700;line-height:1.05;color:var(--text-secondary);letter-spacing:-0.03em;margin-top:18px">¥ 300<span style="font-size:36px;font-weight:600;margin-left:6px">万 +</span></div>
        <div style="font-size:80px;font-weight:700;line-height:1.05;color:var(--text-secondary);letter-spacing:-0.03em;margin-top:8px">7<span style="font-size:36px;font-weight:600;margin-left:6px">个月</span></div>
        <div class="body-m mt-l" style="color:var(--text-secondary)">一支团队 · 分角色按部就班</div>
      </div>
      <div class="card" style="padding:48px 52px;border-color:var(--text)">
        <div class="card-label" style="color:var(--accent)">现在 · 一个人 + AI</div>
        <div style="font-size:80px;font-weight:700;line-height:1.05;color:var(--accent);letter-spacing:-0.03em;margin-top:18px">2<span style="font-size:36px;font-weight:600;margin-left:6px;color:var(--text)">周</span></div>
        <div style="font-size:80px;font-weight:700;line-height:1.05;color:var(--text);letter-spacing:-0.03em;margin-top:8px">1<span style="font-size:36px;font-weight:600;margin-left:6px;color:var(--text-secondary)">个人</span></div>
        <div class="body-m mt-l" style="color:var(--text)">Claude Code + Agent Skills + MCP</div>
      </div>
    </div>
  </div>
</section>""")

# 07 · 五步在本案例的落地
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>本案例的落地</span></div>
  <div class="top-title">五步在本案例里 · 具体这样落地</div>
  <div style="width:100%;max-width:1700px">
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px;align-items:stretch">
      <div class="card" style="padding:22px 16px;text-align:center"><div class="card-label" style="font-size:13px">Step 01</div><div style="font-size:22px;font-weight:700;margin-top:8px;line-height:1.3">爬真实<br>用户评论</div></div>
      <div class="card" style="padding:22px 16px;text-align:center"><div class="card-label" style="font-size:13px">Step 02</div><div style="font-size:22px;font-weight:700;margin-top:8px;line-height:1.3">串行 MRD<br>→ BRD → PRD</div></div>
      <div class="card" style="padding:22px 16px;text-align:center"><div class="card-label" style="font-size:13px">Step 03</div><div style="font-size:22px;font-weight:700;margin-top:8px;line-height:1.3">技术选型<br>+ 界面设计</div></div>
      <div class="card" style="padding:22px 16px;text-align:center"><div class="card-label" style="font-size:13px">Step 04</div><div style="font-size:22px;font-weight:700;margin-top:8px;line-height:1.3">开发<br>跑起来</div></div>
      <div class="card" style="padding:22px 16px;text-align:center;border-color:var(--text)"><div class="card-label" style="font-size:13px;color:var(--accent)">Step 05</div><div style="font-size:22px;font-weight:700;margin-top:8px;line-height:1.3">推送<br>上线</div></div>
    </div>
    <div class="card mt-xl" style="padding:32px 44px;background:var(--bg-soft);border:none">
      <div class="body-l" style="color:var(--text)">三份文档<strong>一份接一份</strong>——上一份的结论自动传给下一份，<span class="hl">中间不丢信息</span>。</div>
    </div>
  </div>
</section>""")

# 08 · 四条核心区别（reveal）
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>核心区别</span></div>
  <div class="top-title">和"随手用 AI 糊一个 demo"的四条核心区别</div>
  <div style="width:100%;max-width:1620px" data-step-reveal>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px">
      <div class="step-card reveal-step" data-step="0" style="border-color:var(--text)">
        <div class="step-num" style="color:var(--accent)">01</div>
        <div class="step-title" style="font-size:38px">数据先行，不拍脑袋</div>
        <div class="step-desc">所有需求都从<strong>真实评论</strong>里提炼，数据里找不到支撑的就不写——宁可少做，不做错。</div>
      </div>
      <div class="step-card reveal-step" data-step="1">
        <div class="step-num">02</div>
        <div class="step-title" style="font-size:38px">串行传递，零丢失</div>
        <div class="step-desc">MRD → BRD → PRD 像<strong>接力棒</strong>，信息一棒一棒往下递，不重复提问、不丢结论。</div>
      </div>
      <div class="step-card reveal-step" data-step="2">
        <div class="step-num">03</div>
        <div class="step-title" style="font-size:38px">判断权始终在人</div>
        <div class="step-desc">AI 干<strong>执行</strong>，你干<strong>判断</strong>——也正是如今最值钱的那部分能力。</div>
      </div>
      <div class="step-card reveal-step" data-step="3">
        <div class="step-num">04</div>
        <div class="step-title" style="font-size:38px">成本断崖式下降</div>
        <div class="step-desc">一个人很短时间就能走一遍，不行就换一个，<strong>试错几乎零成本</strong>。</div>
      </div>
    </div>
    <div class="reveal-hint" style="position:absolute;bottom:96px;left:50%;transform:translateX(-50%);font-family:'JetBrains Mono',monospace;font-size:14px;letter-spacing:2px;color:var(--text-meta);text-transform:uppercase">按 → 依次展开 · <span class="reveal-counter">0</span>/4</div>
  </div>
</section>""")

# 09 · CH01 章节页
SLIDES.append("""<section class="slide">
  <div class="slide-header"><span>Chapter 01</span><span>Discover Market</span></div>
  <div class="chapter-watermark">01</div>
  <div class="chapter">
    <span class="num">Chapter 01</span>
    <h2 class="title">用 AI<br>发现市场机会</h2>
    <div class="sub">做产品之前，先问自己三个问题。</div>
  </div>
</section>""")

# 10 · 三个问题
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>三个问题</span></div>
  <div class="top-title">做之前，起码要问自己三个问题</div>
  <div style="width:100%;max-width:1620px">
    <div class="three-col">
      <div class="step-card">
        <div class="step-num">问题 01</div>
        <div class="step-title" style="font-size:46px;line-height:1.2">市场<br>真的存在吗？</div>
        <div class="step-desc mt-m">这个方向到底有多少人在为同一件事犯愁？</div>
      </div>
      <div class="step-card">
        <div class="step-num">问题 02</div>
        <div class="step-title" style="font-size:46px;line-height:1.2">用户<br>真的需要吗？</div>
        <div class="step-desc mt-m">他们正在用什么凑合？愿意为更好的方案付出什么？</div>
      </div>
      <div class="step-card" style="border-color:var(--text)">
        <div class="step-num" style="color:var(--accent)">问题 03</div>
        <div class="step-title" style="font-size:46px;line-height:1.2">机会<br>真的可做吗？</div>
        <div class="step-desc mt-m">现有玩家是谁？哪里没做好？我们能切进去的缝在哪？</div>
      </div>
    </div>
  </div>
</section>""")

# 11 · CH02 章节页
SLIDES.append("""<section class="slide">
  <div class="slide-header"><span>Chapter 02</span><span>Define Product</span></div>
  <div class="chapter-watermark">02</div>
  <div class="chapter">
    <span class="num">Chapter 02</span>
    <h2 class="title">用 AI<br>定义产品需求</h2>
    <div class="sub">回答两个问题：怎么赚钱、做什么功能。</div>
  </div>
</section>""")

# 12 · 四份文档（4 件套）
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>四份文档闭环</span></div>
  <div class="top-title">标准流程 · 四份文档</div>
  <div style="font-family:'JetBrains Mono',monospace;font-size:22px;letter-spacing:3px;color:var(--text-meta);text-transform:uppercase;text-align:center;margin-bottom:24px">Market &nbsp;/&nbsp; Business &nbsp;/&nbsp; Product &nbsp;/&nbsp; MVP</div>
  <div style="width:100%;max-width:1700px">
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">
      <div class="step-card" style="padding:30px 24px"><div class="step-num">DOC 01</div><div style="font-size:34px;font-weight:700;margin-top:12px">MRD</div><div class="body-m mt-m">市场需求<br><strong>用户要什么</strong></div></div>
      <div class="step-card" style="padding:30px 24px"><div class="step-num">DOC 02</div><div style="font-size:34px;font-weight:700;margin-top:12px">BRD</div><div class="body-m mt-m">商业需求<br><strong>值不值得做</strong></div></div>
      <div class="step-card" style="padding:30px 24px"><div class="step-num">DOC 03</div><div style="font-size:34px;font-weight:700;margin-top:12px">PRD</div><div class="body-m mt-m">产品需求<br><strong>具体做什么</strong></div></div>
      <div class="step-card" style="padding:30px 24px;border-color:var(--text)"><div class="step-num" style="color:var(--accent)">DOC 04</div><div style="font-size:34px;font-weight:700;margin-top:12px">MVP</div><div class="body-m mt-m">第一版清单<br><strong>先做哪几件</strong></div></div>
    </div>
    <div class="card mt-l" style="padding:24px 36px;background:var(--bg-soft);border:none">
      <div class="body-m" style="color:var(--text);text-align:center">四份文档 · 四个迭代 · <span class="hl">一个完整闭环</span></div>
    </div>
  </div>
</section>""")

# 13 · MRD 是什么
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>MRD · 市场需求文档</span></div>
  <div class="top-title">
    <div style="font-family:'JetBrains Mono',monospace;font-size:18px;letter-spacing:3px;color:var(--text-meta);text-transform:uppercase;font-weight:600;margin-bottom:10px">Market Requirements Document</div>
    MRD —— 用户到底要什么
  </div>
  <p class="body-l" style="max-width:1560px;text-align:center;color:var(--text-secondary);margin-top:20px">MRD <strong>只关注市场与用户</strong>，暂不涉及怎么做、能否盈利。一份 MRD 通常包含 <strong>4 块</strong>：</p>
  <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px;width:100%;max-width:1500px;margin-top:24px">
    <div class="step-card"><div class="step-num">Block 01</div><div class="step-title" style="font-size:42px">数据质量评估</div><div class="step-desc">先说清这批数据<strong>能分析什么、不能分析什么</strong>。后续结论才不会失真。</div></div>
    <div class="step-card"><div class="step-num">Block 02</div><div class="step-title" style="font-size:42px">痛点聚类</div><div class="step-desc">从几千条评论归纳出 <strong>3-5 个主要方向</strong>，每类配真实原声佐证。</div></div>
    <div class="step-card"><div class="step-num">Block 03</div><div class="step-title" style="font-size:42px">需求优先级</div><div class="step-desc"><strong>P0 / P1 / P2</strong> 标注，按频率、情绪强度、是否影响留存判断。</div></div>
    <div class="step-card"><div class="step-num">Block 04</div><div class="step-title" style="font-size:42px">竞品格局</div><div class="step-desc">用户在抱怨现有方案<strong>哪里不好</strong>，我们的机会窗口在哪。</div></div>
  </div>
</section>""")

# 14 · MRD 示例 · 减脂健身 App
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>示例</span></div>
  <div class="top-title">MRD 示例 · 减脂健身 App</div>
  <div style="width:100%;max-width:1560px">
    <p class="body-l" style="color:var(--text-secondary);margin-bottom:20px">爬取数千条 Keep、薄荷健康的真实评论后，<strong>可能聚出三类痛点</strong>：</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
      <div class="card" style="padding:38px 36px;border-color:var(--text)"><div class="card-label" style="color:var(--accent)">P0 必须做</div><div style="font-size:36px;font-weight:700;margin:14px 0 10px">坚持不下来</div><div class="body-m">评论最多 · 情绪最强 · 直接影响留存</div></div>
      <div class="card" style="padding:38px 36px"><div class="card-label">P1 很想要</div><div style="font-size:36px;font-weight:700;margin:14px 0 10px">不知道该吃什么</div><div class="body-m">很想要但非必需</div></div>
      <div class="card" style="padding:38px 36px"><div class="card-label">P2 锦上添花</div><div style="font-size:36px;font-weight:700;margin:14px 0 10px">在家练怕动作不标准</div><div class="body-m">提及较少</div></div>
    </div>
    <div class="card mt-l" style="padding:36px 44px;background:var(--bg-soft);border:none">
      <div class="card-label">竞品格局 · Keep</div>
      <div class="body-l mt-m" style="color:var(--text)"><strong>"跟练"做得很好</strong>，但用户抱怨"什么都要会员""课程太多挑花眼"。</div>
      <div class="body-l mt-m">机会窗口 → <span class="hl">轻、不挑花眼、专注帮用户坚持</span></div>
    </div>
  </div>
</section>""")

# 15 · BRD 是什么
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>BRD · 商业需求文档</span></div>
  <div class="top-title">
    <div style="font-family:'JetBrains Mono',monospace;font-size:18px;letter-spacing:3px;color:var(--text-meta);text-transform:uppercase;font-weight:600;margin-bottom:10px">Business Requirements Document</div>
    BRD —— 这事值不值得做
  </div>
  <p class="body-l" style="max-width:1560px;text-align:center;color:var(--text-secondary);margin-top:20px"><strong>有需求不等于值得做</strong>。BRD 负责<strong>算账与决策</strong>，通常包含 <strong>4 块</strong>：</p>
  <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px;width:100%;max-width:1500px;margin-top:24px">
    <div class="step-card"><div class="step-num">Block 01</div><div class="step-title" style="font-size:42px">继承 MRD</div><div class="step-desc">直接读取 MRD 的市场结论往下接，<strong>不重复分析、不重复提问</strong>。</div></div>
    <div class="step-card"><div class="step-num">Block 02</div><div class="step-title" style="font-size:42px">商业可行性</div><div class="step-desc">谁付费 · 怎么定价 · 成本结构 · 最小闭环（粗算单位经济）。</div></div>
    <div class="step-card"><div class="step-num">Block 03</div><div class="step-title" style="font-size:42px">明确结论</div><div class="step-desc"><strong>值得做 / 有条件地做 / 建议暂缓</strong> 三选一，必须明确表态，不和稀泥。</div></div>
    <div class="step-card"><div class="step-num">Block 04</div><div class="step-title" style="font-size:42px">关键风险</div><div class="step-desc">列出依赖的关键假设，指出<strong>哪个一旦不成立结论就翻转</strong>。</div></div>
  </div>
</section>""")

# 16 · BRD 示例 · 共享充电宝
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>示例</span></div>
  <div class="top-title">BRD 示例 · 共享充电宝</div>
  <div style="width:100%;max-width:1560px">
    <p class="body-l" style="color:var(--text-secondary);margin-bottom:20px">付费者 = 临时手机没电又离不开手机的人；定价如每小时三元；成本含机柜、商家分成、运维补货。<strong>这门生意成立与否，卡在"单台日均借用次数"这个数字上</strong>：</p>
    <div class="card" style="padding:42px 52px">
      <div class="card-label">单台测算</div>
      <div class="body-l mt-m" style="color:var(--text)">平均每次借用收 <strong>5 元</strong>，每天借 <strong>8 次 = 40 元</strong>，扣除分成与折旧 → 约数月回本。</div>
      <div class="body-l mt-m">但若每天仅借 <strong>2 次</strong> → <span style="color:var(--warn);font-weight:600">永远无法回本</span>。</div>
    </div>
    <div class="two-col mt-l">
      <div class="card" style="padding:36px 44px;border-color:var(--text)">
        <div class="card-label" style="color:var(--accent)">明确结论</div>
        <div style="font-size:32px;font-weight:600;margin-top:14px;line-height:1.4">值得做，<span class="hl">但有条件</span>：仅在<strong>日均借用高于阈值</strong>的点位铺设。</div>
      </div>
      <div class="card" style="padding:36px 44px">
        <div class="card-label">关键风险</div>
        <div class="body-m mt-m" style="color:var(--text-secondary)">电池续航普遍提升、用户自带充电宝增多 → 整体借用率下滑，<strong>根基便动摇</strong>。</div>
      </div>
    </div>
  </div>
</section>""")

# 17 · PRD 是什么
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>PRD · 产品需求文档</span></div>
  <div class="top-title">
    <div style="font-family:'JetBrains Mono',monospace;font-size:18px;letter-spacing:3px;color:var(--text-meta);text-transform:uppercase;font-weight:600;margin-bottom:10px">Product Requirements Document</div>
    PRD —— 具体做什么、怎么做
  </div>
  <p class="body-l" style="max-width:1560px;text-align:center;color:var(--text-secondary);margin-top:20px">方向确定、值得做之后，<strong>才进入产品本身</strong>。PRD 要细到<strong>能直接交给 AI 编码</strong>，通常包含 <strong>4 块</strong>：</p>
  <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px;width:100%;max-width:1500px;margin-top:24px">
    <div class="step-card"><div class="step-num">Block 01</div><div class="step-title" style="font-size:42px">继承 BRD</div><div class="step-desc">读取 BRD 的商业判断与 P0/P1 功能列表往下接。</div></div>
    <div class="step-card"><div class="step-num">Block 02</div><div class="step-title" style="font-size:42px">MVP 范围</div><div class="step-desc">V1 最多 <strong>3 个核心功能</strong>；附"不做清单"，且<strong>不做清单比要做的更长更显眼</strong>。</div></div>
    <div class="step-card"><div class="step-num">Block 03</div><div class="step-title" style="font-size:42px">页面 & 组件</div><div class="step-desc">每页有什么、每个组件做什么（交互、状态、边界），写到<strong>可直接执行</strong>。</div></div>
    <div class="step-card"><div class="step-num">Block 04</div><div class="step-title" style="font-size:42px">设计交接</div><div class="step-desc">产品调性、色彩方向、参考竞品，供设计与开发使用。</div></div>
  </div>
</section>""")

# 18 · PRD 示例 · 待办清单 App
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>示例</span></div>
  <div class="top-title">PRD 示例 · 待办清单 App</div>
  <div style="width:100%;max-width:1560px">
    <p class="body-l" style="color:var(--text-secondary);margin-bottom:20px">这类产品<strong>最易陷入"什么都想加"</strong>。PRD 会把第一版收敛为三件事，并写一份更长的"不做清单"：</p>
    <div class="two-col">
      <div class="card" style="padding:42px 48px;border-color:var(--text)">
        <div class="card-label" style="color:var(--accent)">要做 · 三件事</div>
        <ul class="bullet-list mt-m"><li>新增任务</li><li>标记完成</li><li>删除任务</li></ul>
      </div>
      <div class="card" style="padding:42px 48px">
        <div class="card-label">不做清单（更长更显眼）</div>
        <ul class="bullet-list mt-m" style="font-size:24px"><li>不做提醒</li><li>不做多人协作</li><li>不做标签</li><li>不做日历</li><li>不做云同步</li><li>不做撤销</li></ul>
      </div>
    </div>
    <div class="card mt-l" style="padding:32px 44px;background:var(--bg-soft);border:none">
      <div class="card-label">组件示例 · 任务行</div>
      <div class="body-m mt-m" style="color:var(--text)">左侧<strong>空心圆圈</strong>点击后变打勾、文字加删除线置灰；列表为空显示<strong>引导文案</strong>而非白屏；右侧删除按钮直接删除（本版不做撤销）。</div>
    </div>
  </div>
</section>""")

# 19 · 为什么串行
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>串行 vs 一次生成</span></div>
  <div class="top-title">为什么三份文档要串行</div>
  <div style="display:inline-block">
    <div class="formula" style="font-size:60px">看市场 → 决定做不做 → <span class="hl">才定怎么做</span></div>
  </div>
  <div class="three-col mt-xl" style="max-width:1620px">
    <div class="card" style="padding:36px 40px"><div class="card-label">判断点清晰</div><div class="body-m mt-m">MRD 让你看清市场，BRD 让你决定做不做，PRD 才开始定怎么做。跳过任何一步都可能整体跑偏。</div></div>
    <div class="card" style="padding:36px 40px"><div class="card-label">接力棒交接</div><div class="body-m mt-m">每份文档末尾有结构化<strong>交接区</strong>，下一份自动读取，不重复提问、不丢信息。</div></div>
    <div class="card" style="padding:36px 40px;border-color:var(--text)"><div class="card-label" style="color:var(--accent)">人始终拍板</div><div class="body-m mt-m">AI 干执行（爬数据、做分析、写文档、写代码）；<strong>判断永远由人来定</strong>。</div></div>
  </div>
</section>""")

# 20 · CH03 章节页
SLIDES.append("""<section class="slide">
  <div class="slide-header"><span>Chapter 03</span><span>Three Layers</span></div>
  <div class="chapter-watermark">03</div>
  <div class="chapter">
    <span class="num">Chapter 03</span>
    <h2 class="title">先搞懂<br>三个词</h2>
    <div class="sub">前端 · 后端 · 数据库——经典三层结构。</div>
  </div>
</section>""")

# 21 · 前端
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>前端 = 餐厅大堂</span></div>
  <div class="top-title">前端 —— 运行在用户浏览器里的代码</div>
  <div style="width:100%;max-width:1560px">
    <div class="card" style="padding:42px 52px">
      <div class="card-label">职责</div>
      <div class="body-xl mt-m" style="color:var(--text)">把界面画出来（渲染 UI）· 响应点击和输入 · 把请求发给后端。</div>
    </div>
    <div class="two-col mt-l">
      <div class="card" style="padding:38px 44px;background:var(--bg-soft);border:none">
        <div class="card-label">餐厅比喻</div>
        <div style="font-size:36px;font-weight:700;margin-top:14px">大堂</div>
        <div class="body-m mt-m">桌椅、菜单、点菜的地方——客人看得见的那部分。<br>本项目里 = 登录页、聊天界面、记忆档案页。</div>
      </div>
      <div class="card" style="padding:38px 44px;border-color:var(--text)">
        <div class="card-label" style="color:var(--accent)">技术栈</div>
        <div style="font-size:36px;font-weight:700;margin-top:14px">React + Tailwind + <span class="hl">Next.js</span></div>
        <div class="body-m mt-m">React 写界面、Tailwind 调样式，整个项目跑在 Next.js 框架上。</div>
      </div>
    </div>
  </div>
</section>""")

# 22 · 后端
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>后端 = 餐厅后厨</span></div>
  <div class="top-title">后端 —— 运行在服务器上的代码</div>
  <div style="width:100%;max-width:1560px">
    <div class="card" style="padding:42px 52px">
      <div class="card-label">职责</div>
      <div class="body-xl mt-m" style="color:var(--text)">业务逻辑 · 身份验证 · 调用第三方服务（大模型 API）· 读写数据库。前后端靠<strong>接口（API）</strong>通信。</div>
    </div>
    <div class="two-col mt-l">
      <div class="card" style="padding:36px 44px;background:var(--bg-soft);border:none">
        <div class="card-label">餐厅比喻</div>
        <div style="font-size:34px;font-weight:700;margin-top:14px">后厨</div>
        <div class="body-m mt-m">客人看不到、活儿都在这儿干。你发一句话 → 后端拼"人设+记忆" → 送给大模型 → 拿回复传回前端。</div>
      </div>
      <div class="card" style="padding:36px 44px;border-color:var(--warn)">
        <div class="card-label" style="color:var(--warn)">为什么必须有</div>
        <div class="body-m mt-m" style="color:var(--text)"><strong style="color:var(--warn)">大模型密钥只能放服务器端</strong>，绝不能写进前端——前端代码用户能看到，等于把钥匙挂门口。</div>
      </div>
    </div>
  </div>
</section>""")

# 23 · 数据库
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>数据库 = 仓库冰箱</span></div>
  <div class="top-title">数据库 —— 数据的持久化存储</div>
  <div style="width:100%;max-width:1560px">
    <div class="card" style="padding:42px 52px">
      <div class="card-label">职责</div>
      <div class="body-xl mt-m" style="color:var(--text)">不存进去，内存里的东西一刷新就没了。<strong>关系型数据库</strong>按"表"存：一行一条记录、一列一个字段，用 <strong>SQL</strong> 增删改查。</div>
    </div>
    <div class="two-col mt-l">
      <div class="card" style="padding:36px 44px;background:var(--bg-soft);border:none">
        <div class="card-label">餐厅比喻</div>
        <div style="font-size:34px;font-weight:700;margin-top:14px">仓库和冰箱</div>
        <div class="body-m mt-m">食材、账本存这儿，关了门也不丢。本项目里 = 账号、聊天记录、长期记忆。</div>
      </div>
      <div class="card" style="padding:36px 44px;border-color:var(--text)">
        <div class="card-label" style="color:var(--accent)">技术栈</div>
        <div style="font-size:34px;font-weight:700;margin-top:14px"><span class="hl">Supabase</span>（底层 PostgreSQL）</div>
        <div class="body-m mt-m">业界主流的关系型数据库，<strong>顺手把登录注册</strong>也一起做了。</div>
      </div>
    </div>
  </div>
</section>""")

# 24 · 一次完整交互 + 三层结构
SLIDES.append("""<section class="slide center">
  <div class="slide-header"><span></span><span>一次完整交互</span></div>
  <div class="top-title">三层结构 · 一次完整交互</div>
  <div style="width:100%;max-width:1700px">
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;align-items:stretch">
      <div class="card" style="padding:26px 20px;text-align:center"><div class="card-label">前端</div><div style="font-size:24px;font-weight:700;margin-top:10px">点一下</div></div>
      <div class="card" style="padding:26px 20px;text-align:center;background:var(--bg-soft);border:none"><div class="card-label">API</div><div style="font-size:24px;font-weight:700;margin-top:10px">请求 →</div></div>
      <div class="card" style="padding:26px 20px;text-align:center;border-color:var(--text)"><div class="card-label" style="color:var(--accent)">后端</div><div style="font-size:24px;font-weight:700;margin-top:10px">处理</div></div>
      <div class="card" style="padding:26px 20px;text-align:center"><div class="card-label">数据库</div><div style="font-size:24px;font-weight:700;margin-top:10px">读/写</div></div>
      <div class="card" style="padding:26px 20px;text-align:center"><div class="card-label">前端</div><div style="font-size:24px;font-weight:700;margin-top:10px">渲染</div></div>
    </div>
    <div class="card mt-xl" style="padding:36px 48px">
      <div class="card-label">最后一步</div>
      <div class="body-l mt-m" style="color:var(--text)">用 <strong>Vercel</strong> 把整个产品部署到网上，别人就能通过网址打开。</div>
    </div>
    <p class="body-m mt-l" style="color:var(--text-meta);text-align:center">具体框架、版本以第 5 步"技术选型"联网确认的为准——这里先把概念和它们怎么配合搞清楚。</p>
  </div>
</section>""")

# 25 · 结尾
SLIDES.append("""<section class="slide">
  <div class="slide-header"><span>End of Lecture</span><span>Let's Build</span></div>
  <h2 class="display h-m" style="max-width:1500px">
    方法论讲完<br>接下来 · <span class="hl">跟我实操</span>
  </h2>
  <p class="body-xl mt-xl" style="max-width:1500px">
    爬真实评论 → 三份文档 → 技术选型 → 开发跑起来 → 推送上线。<br>
    <strong>一个人，两周，一个真正能发给别人用的产品。</strong>
  </p>
  <p style="position:absolute;bottom:110px;left:290px;font-size:22px;letter-spacing:2px;color:var(--text-secondary);font-weight:500">产品开发全流程 · 前期方法论 · 完</p>
</section>""")


# ============================================================
# 渲染 toc
# ============================================================
def render_toc() -> str:
    return "\n".join(
        f'    <a class="toc-item {kind}" data-idx="{idx}">{label}</a>'
        for idx, label, kind in TOC
    )


# ============================================================
# 装配
# ============================================================
def assemble() -> str:
    html = SKEL
    # 改 title
    html = re.sub(r"<title>.*?</title>",
                  f"<title>{DECK_TITLE}</title>",
                  html, count=1)
    # 替换 toc 块（<nav class="toc"> ... </nav>）
    html = re.sub(
        r'<nav class="toc">.*?</nav>',
        f'<nav class="toc">\n{render_toc()}\n  </nav>',
        html, count=1, flags=re.DOTALL,
    )
    # 替换 slide 块
    html = re.sub(
        r'<!-- ⬇️ slide 开始 ⬇️ -->.*?<!-- ⬆️ slide 结束 ⬆️ -->',
        "<!-- ⬇️ slide 开始 ⬇️ -->\n\n" + "\n\n".join(SLIDES) + "\n\n<!-- ⬆️ slide 结束 ⬆️ -->",
        html, count=1, flags=re.DOTALL,
    )
    return html


if __name__ == "__main__":
    out = ROOT / "deck.html"
    out.write_text(assemble(), encoding="utf-8")
    print(f"✓ 生成 {out}")
    print(f"  共 {len(SLIDES)} 页 · 目录 {len(TOC)} 条")
    assert len(SLIDES) == len(TOC), "slide 数与目录条目数不符"
