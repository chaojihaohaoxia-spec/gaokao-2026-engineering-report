from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "index.html"

STUDENT_RANK = 18162

SOURCES = {
    "重庆2026一分一段": "https://www.dxsbb.com/news/100977.html",
    "重庆2026志愿规则": "https://www.cq.gov.cn/zwgk/zfxxgkml/zcwd/cqs2026nptgdxxzsgzssbf/202606/t20260601_15716828.html",
    "重邮历年录取": "https://www.dxsbb.com/news/33445.html",
    "重邮软科": "https://www.shanghairanking.cn/institution/chongqing-university-of-posts-and-telecommunications",
    "重邮学科评估": "https://www.dxsbb.com/news/73477.html",
    "西安邮电重庆投档": "https://www.hzgrys.net/score/50/2025/2538.html",
    "北京信息科技重庆投档": "https://www.hzgrys.net/score/50/2025/51.html",
    "天津工业重庆投档": "https://www.hzgrys.net/score/50/2025/96.html",
    "天津理工重庆投档": "https://www.hzgrys.net/score/50/2025/98.html",
    "杭州电子科技重庆投档": "https://www.hzgrys.net/score/50/2025/904.html",
    "广州大学重庆投档": "https://www.hzgrys.net/score/50/2025/1910.html",
    "南京工程重庆投档": "https://www.hzgrys.net/score/50/2025/773.html",
    "太原理工重庆投档": "https://www.hzgrys.net/score/50/2025/277.html",
    "中国矿业重庆投档": "https://www.hzgrys.net/score/50/2025/742.html",
    "合肥工业重庆投档": "https://www.hzgrys.net/score/50/2025/1014.html",
    "大连海事重庆投档": "https://www.hzgrys.net/score/50/2025/424.html",
    "大连海事大考100": "https://www.dakao100.com/article_81712418759.html",
    "东北秦官方历年": "https://zs.neuq.edu.cn/bkzn/lnfs.htm",
    "成都信息工程2026计划": "https://zs.cuit.edu.cn/info/1096/1688.htm",
    "成都信息工程历年录取": "https://zssj.cuit.edu.cn/sjTj.asp?sf=%D6%D8%C7%EC&kl=%CE%EF%C0%ED%2B%BB%AF%D1%A7",
    "浙江工业录取入口": "https://zs.zjut.edu.cn/jsp/lnzssearch.jsp",
    "江苏大学2025录取": "https://zb.ujs.edu.cn/info/1138/15458.htm",
    "江苏大学2024录取": "https://zb.ujs.edu.cn/info/1138/13668.htm",
    "西南石油重庆录取": "https://www.dakao100.com/article_94823909058.html",
    "中国计量官方录取": "https://zs.cjlu.edu.cn/zsxx/lnfs.htm",
    "重庆理工历年录取": "https://www.dxsbb.com/news/33519.html",
    "CNUR计算机类": "https://www.cnur.com/major/2701.html",
    "CNUR通信工程": "https://www.cnur.com/major/3127.html",
    "CNUR网络工程": "https://www.cnur.com/major/3148.html",
    "CNUR网络空间安全": "https://www.cnur.com/major/3129.html",
    "CNUR电气工程": "https://www.cnur.com/major/2543.html",
    "CNUR机械电子工程": "https://www.cnur.com/major/2740.html",
    "CNUR机器人工程": "https://www.cnur.com/major/3086.html",
    "CNUR智能制造工程": "https://www.cnur.com/major/3087.html",
    "CNUR物联网工程": "https://www.cnur.com/major/3130.html",
    "CNUR车辆工程": "https://www.cnur.com/major/2734.html",
}


@dataclass(frozen=True)
class Choice:
    no: int
    tier: str
    region: str
    city: str
    school: str
    campus: str
    major: str
    priority: str
    ranks: str
    plan: str
    rating: str
    score: int
    action: str
    reason: str
    risk: str
    sources: tuple[str, ...]


PRESTIGE_CHOICES = [
    Choice(0, "冲刺", "京津", "秦皇岛", "东北大学秦皇岛分校（985/211）", "秦皇岛校区", "物联网/自动化/机械电子备选池", "第一优先", "2025:专业组最低约15562/13848；分专业待核", "2026计划待核", "985分校；信息类和控制类方向有985平台背书", 83, "名校试冲池", "这是给前段加入985层级的合理入口，但必须等系统开放后拆成具体专业。", "不能直接按专业组填报；若只能落到经管/外语/不喜欢专业，立即剔除。", ("东北秦官方历年",)),
    Choice(0, "冲刺", "华中", "武汉/徐州", "武汉理工/中国矿业等211", "以系统为准", "强211目标专业备选池", "第一优先", "多数目标专业约10000-14500位；部分低位专业偏材料/交通/矿业", "2026计划待核", "211强工科，但可接受专业要逐项筛", 82, "名校试冲池", "满足前段放少量211的诉求，但只从可接受专业里挑。", "不能把材料、交通、矿业、土木当作核心冲刺；具体专业未核前不单独排序。", ("中国矿业重庆投档",)),
    Choice(0, "冲刺", "华北", "太原", "太原理工大学（211）", "明向校区等待核", "网络空间安全", "第一优先", "2025:10859；2024/2023待核", "2026计划待核", "网络空间安全B及以上池；211", 80, "极少量远冲", "专业方向好，学校是211，适合放在前段满足名校冲刺。", "与18162差距约7300位，成功率低；不能挤占核心稳妥位。", ("太原理工重庆投档", "CNUR网络空间安全")),
    Choice(0, "冲刺", "青岛大连", "大连", "大连海事大学（211）", "校本部", "机械设计制造及其自动化", "第二优先", "2025:25204；2024/2023待核", "2026计划待核", "211；机械方向可接受，但不是学校最强信息类", 79, "可作为名校保底式冲刺", "这是少数位次安全、学校层级高、专业仍能接受的211工科。", "专业不是第一优先；需确认是否普通本科批、非中外合作。", ("大连海事大考100", "大连海事重庆投档", "CNUR机械电子工程")),
    Choice(0, "冲刺", "长三角", "合肥", "合肥工业大学（211）", "合肥校区", "测控技术与仪器", "第二优先", "2025:9189；2024/2023待核", "2026计划待核", "211强工科；测控/仪器方向B及以上池", 77, "象征性远冲", "合肥工科和新能源汽车/智能制造资源不错，学校牌子强。", "位次差距过大，目标专业基本不现实；只放1个远冲即可。", ("合肥工业重庆投档",)),
    Choice(0, "冲刺", "华中", "徐州", "中国矿业大学（211）", "南湖校区等待核", "机器人工程", "第一优先", "2025:9740；2024/2023待核", "2026计划待核", "211；机器人工程方向好", 77, "象征性远冲", "专业方向符合第一优先级，学校工科底盘强。", "差距约8400位，实际成功率很低；矿业相关低位专业不建议替代。", ("中国矿业重庆投档", "CNUR机器人工程")),
]


BASE_CHOICES = [
    Choice(1, "冲刺", "成渝", "重庆", "重庆邮电大学", "南岸校本部", "通信与信息类", "第一优先", "2025:13949；2024:15413；2023:15839", "2025约281人；2026分专业计划待系统核", "通信工程A、电子信息工程A；信息通信为强势底盘", 91, "放前段冲", "学校强项和专业方向完全一致，比冲冷门211更值。", "热门大类，位次仍高于18162约4200位；需核大类分流。", ("重邮历年录取", "重邮软科", "CNUR通信工程")),
    Choice(2, "冲刺", "西北", "西安", "西安邮电大学", "长安/雁塔校区待核", "通信工程", "第一优先", "2025:14293；2024:15799；2023:18368", "2026计划待重庆系统核", "信息通信特色院校；通信/电子信息方向按B及以上池处理", 89, "放前段冲", "西安通信、军工电子、运营商和ICT就业逻辑清楚。", "2025上涨明显；校区与计划数要最终核。", ("西安邮电重庆投档", "CNUR通信工程")),
    Choice(3, "冲刺", "长三角", "杭州", "浙江工业大学", "朝晖校区", "机器人工程", "第一优先", "2025:13602；2024:16864；2023:19711", "2025录取约5人；2026待核", "机器人工程A；工科底盘较强", 86, "少量冲", "杭州产业资源好，机器人/自动化方向质量高。", "小计划波动大，2025位次很高，不能按2023低位乐观。", ("浙江工业录取入口", "CNUR机器人工程")),
    Choice(4, "冲刺", "京津", "天津", "天津工业大学", "天津校区", "网络空间安全", "第一优先", "2025:14293；2024:14043；2023:15520", "2026计划待核", "网安方向B及以上待核；学校计算机相关专业近年热度高", 84, "高风险冲", "天津直辖市，网安方向就业口径清楚。", "近三年均明显高于18162，成功率不高。", ("天津工业重庆投档", "CNUR网络空间安全")),
    Choice(5, "冲刺", "长三角", "南京", "南京工业大学", "江浦校区", "计算机科学与技术", "第一优先", "2025:14652；2024:16151；2023:未查到同名可靠数据", "参考计划2人；最终以系统为准", "计算机科学与技术B+池", 84, "少量冲", "南京城市资源强，专业方向符合第一优先级。", "计划太少，且学校传统强项并非计算机。", ("CNUR计算机类",)),
    Choice(6, "冲刺", "珠三角", "广州", "广州大学", "大学城校区", "计算机科学与技术", "第一优先", "2025:12651；2024:13384；2023:14664", "2026计划待核", "计算机类B+池；广州产业资源强", 83, "极少量远冲", "广州城市和计算机方向都好，适合作为城市型远冲。", "位次差距过大，成功率低；不应占太多前排。", ("广州大学重庆投档", "CNUR计算机类")),
    Choice(7, "冲刺", "京津", "北京", "北京信息科技大学", "北京校区", "光电信息科学与工程", "第二优先", "2025:16764；2024:17238；2023:19358", "2026计划待核", "信息类院校，光电/电子信息方向需最终核B以上", 82, "冲稳边界", "北京信息产业资源强，2023-2024有接近18162的机会。", "评级需在最终版榜单复核；2025已上行。", ("北京信息科技重庆投档",)),
    Choice(8, "冲刺", "华中", "长沙", "长沙理工大学", "长沙校区", "通信工程", "第一优先", "2025:14652；2024:15413；2023:17056", "参考计划2人；最终以系统为准", "通信工程B及以上池", 82, "少量冲", "长沙城市资源尚可，通信方向比材料/土木更贴合。", "小计划，且2025位次较高。", ("CNUR通信工程",)),
    Choice(9, "冲刺", "长三角", "镇江", "江苏大学", "校本部", "机械电子工程", "第二优先", "2025:15346；2024:18320；2023:未查到同名可靠数据", "2025录取3人", "机械电子工程A；机械工程学科B+", 82, "冲稳边界", "若接受智能制造/机电控制，这是强专业逻辑。", "镇江城市弱于南京/苏州；招生3人波动大。", ("江苏大学2025录取", "江苏大学2024录取", "CNUR机械电子工程")),
    Choice(10, "冲刺", "成渝", "成都", "西南石油大学", "成都校区", "电气工程及其自动化", "第一优先", "2025:14652；2024:16151；2023:17392", "参考计划14人；最终以系统为准", "电气工程B及以上池", 82, "少量冲", "成都资源好，电气就业口径清楚。", "学校行业底色偏能源，不等于传统电力强校。", ("西南石油重庆录取", "CNUR电气工程")),
    Choice(11, "冲刺", "京津", "天津", "天津理工大学", "天津校区", "计算机科学与技术", "第一优先", "2025:13949；2024:14392；2023:15216", "2026计划待核", "计算机类B+池", 80, "极少量冲", "天津城市和计算机方向可以看。", "三年均明显高于18162，录取概率偏低。", ("天津理工重庆投档", "CNUR计算机类")),
    Choice(12, "冲刺", "珠三角", "广州", "广州大学", "大学城校区", "集成电路设计与集成系统", "第一优先", "2025:17147；2024:17238；2023:同名暂未查到", "2026计划待核", "集成电路评级需最终核；先列冲刺待核", 79, "待核后再排", "珠三角芯片和电子信息产业资源好。", "评级和2026计划未完全核清，不能排在重邮/西邮前。", ("广州大学重庆投档",)),
    Choice(13, "稳妥", "成渝", "重庆", "重庆邮电大学", "南岸校本部", "电子工程类", "第一优先", "2025:18260；2024:18694；2023:20706", "2025约252人；2026待核", "电子信息工程A；重邮核心工科", 92, "核心稳妥", "几乎贴合18162，是本方案最核心专业之一。", "核清大类包含专业和分流规则。", ("重邮历年录取", "重邮软科")),
    Choice(14, "稳妥", "成渝", "重庆", "重庆邮电大学", "南岸校本部", "软件工程", "第一优先", "2025:19815；2024:20262；2023:20706", "2025约193人；2026待核", "软件工程A；就业方向清楚", 91, "核心稳妥", "考生位次优于近三年最低位次，专业质量和就业逻辑都强。", "学费、培养模式和学习强度要提前接受。", ("重邮历年录取", "重邮软科")),
    Choice(15, "稳妥", "西北", "西安", "西安邮电大学", "校区待核", "电气工程及其自动化", "第一优先", "2025:18260；2024:未查到；2023:未查到", "2026计划待核", "电气工程B及以上池待核", 86, "重点放", "位次贴合，西安工科就业半径可接受。", "缺2024/2023同名数据，需系统复核。", ("西安邮电重庆投档", "CNUR电气工程")),
    Choice(16, "稳妥", "西北", "西安", "西安邮电大学", "校区待核", "电子科学与技术", "第一优先", "2025:18260；2024:19109；2023:21046", "2026计划待核", "电子信息方向B及以上池", 86, "重点放", "贴近考生位次，方向比冷门工科更匹配。", "需核课程方向是否偏器件/材料。", ("西安邮电重庆投档",)),
    Choice(17, "稳妥", "西北", "西安", "西安邮电大学", "校区待核", "信息安全", "第一优先", "2025:18260；2024:未查到；2023:未查到", "2026计划待核", "网安/信息安全B及以上池待核", 85, "重点放", "专业方向明确，和通信/网络平台相互支撑。", "近三年可比数据不足，不能放得过于靠前。", ("西安邮电重庆投档", "CNUR网络空间安全")),
    Choice(18, "稳妥", "京津", "天津", "天津工业大学", "天津校区", "智能制造工程", "第二优先", "2025:16401；2024:17944；2023:18673", "2026计划待核", "智能制造工程B+池", 85, "稳妥前段", "2024-2023贴近18162，天津制造业和自动化场景可承接。", "2025上行，且不是第一优先的信息类。", ("天津工业重庆投档", "CNUR智能制造工程")),
    Choice(19, "稳妥", "长三角", "杭州", "浙江理工大学", "下沙校区", "机械电子工程", "第二优先", "2025:18260；2024:19881；2023:20043", "参考计划3人；2026待核", "机械电子工程A", 85, "重点放", "杭州城市+机电方向，性价比很好。", "不是计算机/通信主线；计划小。", ("CNUR机械电子工程",)),
    Choice(20, "稳妥", "成渝", "重庆", "重庆邮电大学", "南岸校本部", "机器人工程", "第一优先", "2025:19441；2024:19519；2023:20043", "2025约57人；2026待核", "机器人工程B+", 85, "重点放", "录取匹配好，方向可接自动化/嵌入式/机器人应用。", "本科口径偏宽，需靠项目和实践拉开差距。", ("重邮历年录取", "CNUR机器人工程")),
    Choice(21, "稳妥", "成渝", "重庆", "重庆邮电大学", "南岸校本部", "集成电路类", "第一优先", "2025:17490；2024:19109；2023:20706", "2025约161人；2026待核", "微电子/集成电路方向需核具体评级；电子信息平台强", 84, "稳妥前段", "方向符合芯片/电子第一优先级，且重庆本地产业有承接。", "需核大类分流；若评级不能确认B以上则下调。", ("重邮历年录取", "重邮软科")),
    Choice(22, "稳妥", "成渝", "成都", "成都信息工程大学", "航空港校区", "计算机科学与技术", "第一优先", "2025:15673；2024:16151；2023:16442", "2026重庆计划7人", "计算机方向B+池", 84, "冲稳边界", "成都软件和电子信息就业资源好。", "位次高于18162较多，计划7人波动大。", ("成都信息工程2026计划", "成都信息工程历年录取", "CNUR计算机类")),
    Choice(23, "稳妥", "华中", "武汉", "湖北工业大学", "武汉校区", "电气工程及其自动化", "第一优先", "2025:19815；2024:21039；2023:22909", "参考计划5人；2026待核", "电气工程B+池", 84, "重点放", "武汉城市资源好，电气就业口径清楚。", "学校层级不如重邮/西邮，计划仍要核。", ("CNUR电气工程",)),
    Choice(24, "稳妥", "成渝", "成都", "成都信息工程大学", "航空港校区", "电子信息工程", "第一优先", "2025:19441；2024:19519；2023:20043", "2026重庆计划7人", "电子信息工程A/B+池", 84, "重点放", "成都城市+电子信息方向，适合作为稳妥主力。", "计划小，须核2026是否扩缩。", ("成都信息工程2026计划", "成都信息工程历年录取")),
    Choice(25, "稳妥", "长三角", "杭州", "中国计量大学", "杭州校区", "通信工程", "第一优先", "2025:19815；2024:未查到；2023:19711", "2025官方最低分577；2026待核", "通信工程B", 83, "可放", "杭州资源好，学校仪器/计量/电子信息特色清楚。", "近三年专业位次不完整；要核2026计划。", ("中国计量官方录取", "CNUR通信工程")),
    Choice(26, "稳妥", "长三角", "杭州", "中国计量大学", "杭州校区", "电子信息工程", "第一优先", "2025:约19056；2024/2023待核", "2025官方最低分579；2026待核", "电子信息方向B及以上池待核", 83, "可放", "杭州+电子信息，方向匹配。", "位次由分数换算/第三方交叉，最终用重庆系统核。", ("中国计量官方录取",)),
    Choice(27, "稳妥", "长三角", "杭州", "中国计量大学", "杭州校区", "测控技术与仪器", "第二优先", "2025:约19056；2024/2023待核", "2025官方最低分579；2026待核", "仪器/测控为学校特色，B及以上池", 82, "可放", "学校行业特色强，适合仪器、智能感知、检测认证方向。", "比电子信息/软件就业面窄，最好能接受考研。", ("中国计量官方录取",)),
    Choice(28, "稳妥", "成渝", "成都", "西南石油大学", "成都校区", "机器人工程", "第一优先", "2025:17490；2024:19109；2023:19711", "参考计划4人；2026待核", "机器人工程B+", 82, "可放", "成都+机器人方向可接受，避开石油冷门专业。", "计划4人波动大。", ("西南石油重庆录取", "CNUR机器人工程")),
    Choice(29, "稳妥", "成渝", "成都", "西南石油大学", "成都校区", "自动化", "第一优先", "2025:16058；2024:17588；2023:18368", "参考计划6人；2026待核", "自动化B及以上池", 82, "冲稳边界", "自动化就业面较宽，成都资源好。", "2025位次偏高；学校标签偏能源。", ("西南石油重庆录取",)),
    Choice(30, "稳妥", "长三角", "上海", "上海海事大学", "临港校区", "机械电子工程", "第二优先", "2025:20633；2024:21039；2023:未查到", "参考计划2人；2026待核", "机械电子工程B+", 81, "可放", "上海临港制造、航运装备、智能制造场景较好。", "计划2人，且学校行业偏航运。", ("CNUR机械电子工程",)),
    Choice(31, "稳妥", "西北", "西安", "西安邮电大学", "校区待核", "人工智能", "第一优先", "2025:19441；2024/2023待核", "2026计划待核", "人工智能B及以上池待核", 81, "可放", "专业方向热门，依托西邮信息类平台。", "新专业/口径变化风险，需核评级和课程。", ("西安邮电重庆投档",)),
    Choice(32, "稳妥", "西北", "西安", "西安邮电大学", "校区待核", "网络工程", "第一优先", "2025:20633；2024:20262；2023:22148", "2026计划待核", "网络工程B+", 81, "可放", "比经管包装数据类更工科，就业方向清楚。", "岗位竞争需要项目和证书，不能只靠专业名。", ("西安邮电重庆投档", "CNUR网络工程")),
    Choice(33, "稳妥", "长三角", "镇江", "江苏大学", "校本部", "机械设计制造及其自动化", "第二优先", "2025:14988；2024:16513；2023:18037", "2025录取5人", "机械工程B+；机械设计A+池", 80, "可放", "强机械专业，适合智能制造/装备路线。", "不是第一优先，城市弱于南京/杭州。", ("江苏大学2025录取", "江苏大学2024录取")),
    Choice(34, "稳妥", "华中", "武汉", "武汉科技大学", "黄家湖校区", "机械类", "第二优先", "2025:19056；2024:20676；2023:21046", "参考计划5人；2026待核", "机械类B及以上池待核", 79, "候补可放", "武汉城市资源和制造业基础可以。", "大类含工业工程等方向，需核分流。", ("CNUR机械电子工程",)),
    Choice(35, "稳妥", "青岛大连", "青岛", "山东科技大学", "青岛校区", "电子信息工程", "第一优先", "2025:20633；2024:20676；2023:21046", "参考计划4人；2026待核", "电子信息工程B+池", 79, "候补可放", "青岛城市不错，电子信息方向清楚。", "学校行业底色偏矿业/工科综合，不如重邮/西邮聚焦。", ("CNUR通信工程",)),
    Choice(36, "稳妥", "华中", "长沙", "长沙理工大学", "长沙校区", "储能科学与工程", "第二优先", "2025:18678；2024:23029；2023:24750", "参考计划2人；2026待核", "储能方向B及以上池待核", 78, "候补", "能源电力背景和长沙产业可承接。", "专业新、行业周期明显，不宜排太前。", ("CNUR电气工程",)),
    Choice(37, "保底", "成渝", "成都", "成都信息工程大学", "航空港校区", "网络工程", "第一优先", "2025:21426；2024:21039；2023:21046", "2026重庆计划4人", "网络工程A/B+池", 84, "保底前段", "成都+网络工程，安全性和专业质量都较好。", "计划4人，不要当绝对保底。", ("成都信息工程2026计划", "成都信息工程历年录取", "CNUR网络工程")),
    Choice(38, "保底", "京津", "天津", "天津理工大学", "天津校区", "人工智能", "第一优先", "2025:21426；2024:21039；2023:22909", "2026计划待核", "计算机类B+池；专业评级待核", 82, "可保底", "天津城市资源不错，位次安全性较好。", "若最终评级未达B，应下调或剔除。", ("天津理工重庆投档", "CNUR计算机类")),
    Choice(39, "保底", "长三角", "南京", "南京工程学院", "南京校区", "电子信息工程", "第一优先", "2025:23142；2024:23888；2023:28266", "2026计划待核", "电气特色强校；电子信息评级需核B以上", 81, "候补保底", "南京城市好，分数安全。", "不是学校最强电气方向，评级未完全核清。", ("南京工程重庆投档",)),
    Choice(40, "保底", "长三角", "南通", "南通大学", "启东/啬园校区", "通信工程", "第一优先", "2025:20633；2024:21845；2023:未查到", "参考计划3人；2026待核", "通信工程B", 80, "可保底", "长三角就业半径尚可，专业方向明确。", "大一启东校区，城市资源弱于南京/杭州。", ("CNUR通信工程",)),
    Choice(41, "保底", "京津", "北京", "北京联合大学", "北四环校区", "计算机科学与技术", "第一优先", "2025:21426；2024:20262；2023:23650", "参考计划3人；2026待核", "计算机类B", 79, "候补保底", "北京城市资源好，位次有安全垫。", "学校层级一般，不宜压过重邮/西邮/成信。", ("CNUR计算机类",)),
    Choice(42, "保底", "成渝", "重庆", "重庆理工大学", "花溪校区", "电气工程及其自动化", "第一优先", "2025:24396；2024:26509；2023:28698", "2025约108人；2026待核", "电气工程B+", 86, "高质量保底", "本地制造、电力设备、汽车电子能承接。", "国家电网核心岗位需考研/提升背景。", ("重庆理工历年录取", "CNUR电气工程")),
    Choice(43, "保底", "成渝", "重庆", "重庆理工大学", "两江校区", "计算机科学与技术", "第一优先", "2025:26280；2024:26935；2023:27853", "2025约180人；2026待核", "计算机类B", 85, "高质量保底", "方向接受度高，安全垫大。", "学校计算机平台不如重邮，不要当重邮替代。", ("重庆理工历年录取", "CNUR计算机类")),
    Choice(44, "保底", "成渝", "重庆", "重庆理工大学", "两江校区", "车辆工程", "第二优先", "2025:28271；2024:30664；2023:31976", "2025约122人；2026待核", "车辆工程B+", 83, "高质量保底", "重庆智能网联汽车产业链强，学校车辆背景清楚。", "如果排斥汽车行业，不要作为核心保底。", ("重庆理工历年录取", "CNUR车辆工程")),
    Choice(45, "保底", "成渝", "重庆", "重庆理工大学", "两江校区", "物联网工程", "第一优先", "2025:28751；2024:29235；2023:30304", "2025约31人；2026待核", "物联网工程B", 82, "保底", "嵌入式、传感、网络和应用开发方向可接受。", "专业平台弱于重邮，需靠项目能力。", ("重庆理工历年录取", "CNUR物联网工程")),
    Choice(46, "保底", "长三角", "南通", "南通大学", "启东/啬园校区", "物联网工程", "第一优先", "2025:23571；2024:23888；2023:26287", "参考计划2人；2026待核", "物联网工程B+", 80, "可保底", "长三角+物联网，安全性较好。", "计划2人；校区切换要接受。", ("CNUR物联网工程",)),
    Choice(47, "保底", "京津", "天津", "天津理工大学", "天津校区", "智能制造工程", "第二优先", "2025:24004；2024:23888；2023:27447", "2026计划待核", "智能制造工程B及以上池待核", 78, "候补保底", "城市不错，录取安全性较高。", "若评级核不到B，剔除。", ("天津理工重庆投档", "CNUR智能制造工程")),
    Choice(48, "保底", "成渝", "重庆", "重庆交通大学", "科学城校区", "机械设计制造及其自动化", "第二优先", "2025:29255；2024:34042；2023:36007", "参考计划46人；2026待核", "机械设计B", 77, "最后保底", "本地保底安全，专业仍是可接受工科。", "学校强项偏交通土木，排序要在重庆理工之后。", ("CNUR机械电子工程",)),
]


CHOICES = [
    Choice(
        i,
        item.tier,
        item.region,
        item.city,
        item.school,
        item.campus,
        item.major,
        item.priority,
        item.ranks,
        item.plan,
        item.rating,
        item.score,
        item.action,
        item.reason,
        item.risk,
        item.sources,
    )
    for i, item in enumerate(PRESTIGE_CHOICES + BASE_CHOICES, start=1)
]


PENDING = [
    ("深圳技术大学", "深圳", "计算机/自动化/电子信息", "城市极强，专业名匹配", "官方附件暂未顺利解析到重庆分专业位次；核清前不进主表"),
    ("广东工业大学", "广州/揭阳", "人工智能、电子信息、自动化", "珠三角工科强校", "重庆2025分专业数据未完整核到，且揭阳校区要单独评估"),
    ("南京信息工程大学", "南京", "计算机、信息安全、电子信息", "信息类强、城市好", "2025多数目标专业位次约9000-13000，明显高于18162，性价比低"),
    ("杭州电子科技大学", "杭州", "计算机、电子信息、自动化", "专业很强", "目标专业多数在7000-11000位，车辆工程可冲但不是第一优先"),
    ("上海电力大学", "上海", "电气、自动化、测控", "电力行业背景好", "电气通常过高；测控评级和匹配度不足，暂不主推"),
]

AVOID = [
    ("河海大学", "交通工程", "211和A类专业看着好", "交通工程不是本次第一/第二优先；计划少且校区流转，不能为校名牺牲专业。"),
    ("中国石油大学(北京)", "过程装备与控制工程", "211、B+、北京", "行业偏石化装备，路径窄，不适合电子信息/计算机/智能制造主线。"),
    ("南京工业大学/西南大学等", "材料、无机非金属、化工类", "学校或评级不错", "家庭已明确谨慎材料化工，不能包装成新能源就放进主表。"),
    ("医学类院校", "医学信息工程", "专业名含信息", "平台偏医学，工程训练和岗位口径不如计算机/软件/电子明确。"),
    ("财经/经贸类院校", "数据科学与大数据技术", "名字热门", "容易偏经管包装，不符合纯工科强专业优先。"),
    ("数字媒体技术", "数字媒体/内容技术方向", "看起来像计算机", "更偏内容、交互、媒体技术，不是本次优先的硬工科/信息类主线。"),
]


def source_links(keys: tuple[str, ...]) -> str:
    parts = []
    for key in keys:
        url = SOURCES.get(key)
        if url:
            parts.append(f'<a href="{escape(url)}" target="_blank" rel="noopener">{escape(key)}</a>')
        else:
            parts.append(escape(key))
    return "、".join(parts)


def rank_hint(choice: Choice) -> str:
    match = re.search(r"2025[:：]约?(\d{4,5})", choice.ranks)
    if not match:
        return "待核"
    try:
        rank = int(match.group(1))
    except ValueError:
        return "待核"
    gap = rank - STUDENT_RANK
    if gap > 3500:
        return "安全"
    if gap >= -1200:
        return "贴近"
    return "偏难"


def render_choice_row(choice: Choice) -> str:
    return f"""
      <tr class="choice-row" data-tier="{escape(choice.tier)}" data-region="{escape(choice.region)}" data-priority="{escape(choice.priority)}" data-search="{escape((choice.school + choice.city + choice.major + choice.rating).lower())}">
        <td class="no">{choice.no}</td>
        <td><span class="badge {escape(choice.tier)}">{escape(choice.tier)}</span><br><span class="mini">{escape(rank_hint(choice))}</span></td>
        <td><b>{escape(choice.school)}</b><br><span class="mini">{escape(choice.city)}｜{escape(choice.campus)}</span></td>
        <td><b>{escape(choice.major)}</b><br><span class="mini">{escape(choice.priority)}</span></td>
        <td>{escape(choice.ranks)}</td>
        <td>{escape(choice.plan)}</td>
        <td>{escape(choice.rating)}<br><span class="mini">{source_links(choice.sources)}</span></td>
        <td class="score">{choice.score}</td>
        <td>{escape(choice.action)}<br><span class="mini">风险：{escape(choice.risk)}</span></td>
      </tr>
    """


def render_choice_card(choice: Choice) -> str:
    return f"""
      <article class="choice-card" data-tier="{escape(choice.tier)}" data-region="{escape(choice.region)}" data-priority="{escape(choice.priority)}" data-search="{escape((choice.school + choice.city + choice.major + choice.rating).lower())}">
        <div class="card-head">
          <span class="badge {escape(choice.tier)}">{choice.no}. {escape(choice.tier)}</span>
          <strong>{choice.score}</strong>
        </div>
        <h3>{escape(choice.school)}｜{escape(choice.major)}</h3>
        <p class="meta">{escape(choice.city)}｜{escape(choice.campus)}｜{escape(choice.priority)}</p>
        <dl>
          <dt>位次</dt><dd>{escape(choice.ranks)}</dd>
          <dt>评级</dt><dd>{escape(choice.rating)}</dd>
          <dt>建议</dt><dd>{escape(choice.action)}</dd>
          <dt>风险</dt><dd>{escape(choice.risk)}</dd>
        </dl>
      </article>
    """


def grouped_counts() -> dict[str, int]:
    data: dict[str, int] = {}
    for item in CHOICES:
        data[item.region] = data.get(item.region, 0) + 1
    return data


def render() -> str:
    tier_buttons = ["全部", "冲刺", "稳妥", "保底"]
    region_buttons = ["全部", "成渝", "长三角", "珠三角", "京津", "华中", "华北", "西北", "青岛大连"]
    priority_buttons = ["全部", "第一优先", "第二优先"]

    rows = "".join(render_choice_row(item) for item in CHOICES)
    cards = "".join(render_choice_card(item) for item in CHOICES)
    counts = grouped_counts()
    city_cards = "".join(
        f'<div class="city-card"><strong>{escape(region)}</strong><span>{count} 条</span></div>'
        for region, count in sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    )
    pending_rows = "".join(
        f"<tr><td>{escape(s)}</td><td>{escape(c)}</td><td>{escape(m)}</td><td>{escape(v)}</td><td>{escape(r)}</td></tr>"
        for s, c, m, v, r in PENDING
    )
    avoid_rows = "".join(
        f"<tr><td>{escape(s)}</td><td>{escape(m)}</td><td>{escape(g)}</td><td>{escape(p)}</td></tr>"
        for s, m, g, p in AVOID
    )
    source_items = "".join(
        f'<li><a href="{escape(url)}" target="_blank" rel="noopener">{escape(name)}</a></li>'
        for name, url in SOURCES.items()
    )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,">
  <title>重庆2026物理类586分工科志愿清单</title>
  <style>
    :root {{
      --ink:#17202a; --muted:#667085; --line:#d9e1ec; --paper:#fff; --bg:#f5f7fb;
      --blue:#2155a3; --green:#257451; --teal:#0f766e; --amber:#b45309; --red:#b42318;
    }}
    * {{ box-sizing:border-box; }}
    html {{ scroll-padding-top:78px; }}
    body {{ margin:0; color:var(--ink); background:var(--bg); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; line-height:1.55; overflow-x:hidden; }}
    a {{ color:var(--blue); text-decoration:none; }}
    header {{ background:#fff; border-bottom:1px solid var(--line); padding:22px min(5vw,64px) 18px; }}
    .titlebar {{ display:flex; justify-content:space-between; gap:24px; align-items:flex-end; }}
    h1 {{ margin:0; font-size:clamp(28px,4vw,44px); letter-spacing:0; }}
    .subtitle {{ margin:8px 0 0; color:var(--muted); max-width:920px; }}
    .rank-chip {{ border:1px solid #b7c7de; background:#eef5ff; color:#123c73; padding:10px 14px; border-radius:8px; min-width:180px; }}
    .rank-chip strong {{ display:block; font-size:26px; }}
    nav {{ position:sticky; top:0; z-index:20; display:flex; gap:8px; align-items:center; padding:10px min(5vw,64px); background:rgba(255,255,255,.97); border-bottom:1px solid var(--line); box-shadow:0 6px 16px rgba(16,24,40,.06); overflow-x:auto; }}
    nav a {{ white-space:nowrap; padding:7px 11px; border-radius:7px; color:#263445; font-weight:700; font-size:14px; }}
    nav a:hover {{ background:#edf3ff; }}
    main {{ padding:0; }}
    section {{ padding:26px min(5vw,64px); background:#fff; border-bottom:1px solid var(--line); }}
    section:nth-of-type(even) {{ background:#f9fbff; }}
    h2 {{ margin:0 0 14px; font-size:24px; }}
    p {{ margin:8px 0; }}
    .quick {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin-top:16px; }}
    .metric {{ background:#fff; border:1px solid var(--line); border-left:5px solid var(--blue); padding:13px 14px; border-radius:8px; }}
    .metric strong {{ display:block; font-size:24px; }}
    .metric span {{ color:var(--muted); }}
    .toolbar {{ display:grid; gap:12px; margin:14px 0; padding:14px; border:1px solid var(--line); background:#fff; border-radius:8px; }}
    .filter-line {{ display:flex; flex-wrap:wrap; align-items:center; gap:8px; }}
    .filter-line b {{ min-width:72px; color:#344054; }}
    .chip {{ appearance:none; border:1px solid #b9c6d8; background:#fff; color:#123c73; padding:8px 12px; border-radius:8px; font-weight:800; cursor:pointer; }}
    .chip.active {{ background:var(--blue); color:#fff; border-color:var(--blue); }}
    .search {{ width:min(520px,100%); border:1px solid #b9c6d8; border-radius:8px; padding:10px 12px; font-size:15px; }}
    .count {{ color:var(--muted); font-weight:700; }}
    .table-wrap {{ overflow-x:auto; border:1px solid var(--line); background:#fff; border-radius:8px; }}
    table {{ width:100%; border-collapse:collapse; min-width:1160px; }}
    th,td {{ padding:10px 11px; border-bottom:1px solid var(--line); border-right:1px solid var(--line); vertical-align:top; font-size:14px; overflow-wrap:anywhere; }}
    th {{ background:#eef4ff; color:#14345f; text-align:left; }}
    td:last-child, th:last-child {{ border-right:0; }}
    tr:last-child td {{ border-bottom:0; }}
    .no {{ font-weight:900; color:#344054; }}
    .score {{ font-weight:900; color:var(--blue); font-size:20px; white-space:nowrap; min-width:42px; }}
    .mini {{ display:inline-block; color:var(--muted); font-size:12px; line-height:1.4; margin-top:3px; }}
    .badge {{ display:inline-flex; min-height:24px; align-items:center; padding:2px 8px; border-radius:999px; font-size:12px; font-weight:900; background:#edf3ff; color:#17427d; }}
    .badge.稳妥 {{ background:#eaf7ef; color:#17603e; }}
    .badge.保底 {{ background:#e7f7f5; color:#0b615a; }}
    .badge.冲刺 {{ background:#fff4df; color:#8a4b00; }}
    .card-list {{ display:none; gap:12px; }}
    .choice-card {{ border:1px solid var(--line); border-left:5px solid var(--blue); background:#fff; border-radius:8px; padding:13px; overflow-wrap:anywhere; }}
    .choice-card[data-tier="稳妥"] {{ border-left-color:var(--green); }}
    .choice-card[data-tier="保底"] {{ border-left-color:var(--teal); }}
    .card-head {{ display:flex; justify-content:space-between; align-items:center; gap:10px; }}
    .card-head strong {{ color:var(--blue); font-size:22px; }}
    .choice-card h3 {{ margin:10px 0 4px; font-size:17px; }}
    .meta {{ color:var(--muted); margin:0 0 8px; }}
    dl {{ display:grid; grid-template-columns:58px 1fr; gap:6px 10px; margin:0; }}
    dt {{ font-weight:900; color:#536173; }}
    dd {{ margin:0; min-width:0; }}
    .city-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }}
    .city-card {{ border:1px solid var(--line); background:#fff; border-radius:8px; padding:14px; }}
    .city-card strong {{ display:block; font-size:18px; }}
    .city-card span {{ color:var(--muted); }}
    .split {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }}
    .note {{ border-left:5px solid var(--amber); background:#fff8ed; padding:12px 14px; border-radius:0 8px 8px 0; }}
    .source-list {{ columns:2 320px; padding-left:18px; }}
    .is-hidden {{ display:none !important; }}
    footer {{ padding:24px min(5vw,64px); color:#667085; }}
    @media (max-width: 860px) {{
      header {{ padding:20px 16px 16px; }}
      .titlebar {{ display:block; }}
      .rank-chip {{ margin-top:14px; }}
      nav {{ padding:8px 12px; }}
      section {{ padding:22px 16px; }}
      .quick {{ grid-template-columns:1fr 1fr; }}
      .filter-line b {{ width:100%; }}
      .chip {{ flex:1 1 calc(50% - 8px); }}
      .table-wrap {{ display:none; }}
      .card-list {{ display:grid; }}
      .split {{ grid-template-columns:1fr; }}
      dl {{ grid-template-columns:1fr; gap:2px; }}
      dt {{ margin-top:8px; }}
    }}
  </style>
</head>
<body>
<header>
  <div class="titlebar">
    <div>
      <h1>重庆586分工科志愿清单</h1>
      <p class="subtitle">主逻辑：前段加少量985/211试冲，但只看工科和B及以上方向；不为校名牺牲专业。</p>
    </div>
    <div class="rank-chip"><strong>18162位</strong><span>2026重庆物理类586分</span></div>
  </div>
  <div class="quick">
    <div class="metric"><strong>{len(CHOICES)}条</strong><span>主清单，可直接排序使用</span></div>
    <div class="metric"><strong>多城</strong><span>成渝、长三角、京津、珠三角等</span></div>
    <div class="metric"><strong>B及以上</strong><span>不把C类专业放进主推</span></div>
    <div class="metric"><strong>96志愿</strong><span>专业(类)+院校，别乱填冷门</span></div>
  </div>
</header>
<nav>
  <a href="#list">完整清单</a>
  <a href="#city">城市分布</a>
  <a href="#major">专业取舍</a>
  <a href="#pending">待核/剔除</a>
  <a href="#sources">数据来源</a>
</nav>
<main>
  <section id="list">
    <h2>完整填报清单</h2>
    <p>默认顺序就是建议排序：最前面放少量985/211名校试冲，随后冲强专业，中段抓重邮/西邮/成信/中国计量等匹配项，后段用重庆理工、南京工程、南通等可接受工科保底。</p>
    <div class="toolbar">
      <div class="filter-line" data-kind="tier"><b>层级</b>{''.join(f'<button class="chip {"active" if x == "全部" else ""}" type="button" data-value="{x}">{x}</button>' for x in tier_buttons)}</div>
      <div class="filter-line" data-kind="region"><b>城市带</b>{''.join(f'<button class="chip {"active" if x == "全部" else ""}" type="button" data-value="{x}">{x}</button>' for x in region_buttons)}</div>
      <div class="filter-line" data-kind="priority"><b>专业</b>{''.join(f'<button class="chip {"active" if x == "全部" else ""}" type="button" data-value="{x}">{x}</button>' for x in priority_buttons)}<input id="search" class="search" placeholder="搜学校 / 城市 / 专业"></div>
      <div class="count" aria-live="polite">当前显示全部</div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>序</th><th>层级</th><th>学校/城市</th><th>专业</th><th>近三年位次</th><th>计划</th><th>评级依据</th><th>分</th><th>建议/风险</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <div class="card-list">{cards}</div>
  </section>
  <section id="city">
    <h2>城市分布</h2>
    <div class="city-grid">{city_cards}</div>
    <p class="note">不是大城市就自动推荐。杭州、南京、广州、北京、天津、西安进入清单，是因为专业方向和位次也能讲通；深圳、上海部分学校数据或位次不匹配，先放待核，不硬塞主表。</p>
  </section>
  <section id="major">
    <h2>专业取舍</h2>
    <div class="split">
      <div class="note"><b>优先排前：</b>通信、电子信息、软件、计算机、信息安全/网安、集成电路、自动化、电气、机器人。它们就业口径清楚，也利于考研。</div>
      <div class="note"><b>有条件放：</b>机械电子、智能制造、车辆、测控、光电、储能。只在学校有行业底盘、城市能承接、本人能接受制造业时放。</div>
    </div>
  </section>
  <section id="pending">
    <h2>待核和剔除</h2>
    <h3>待核扩展</h3>
    <div class="table-wrap"><table><thead><tr><th>学校</th><th>城市</th><th>方向</th><th>为什么要看</th><th>为什么暂不进主表</th></tr></thead><tbody>{pending_rows}</tbody></table></div>
    <h3>不建议</h3>
    <div class="table-wrap"><table><thead><tr><th>学校/类型</th><th>专业</th><th>看起来能选</th><th>不建议原因</th></tr></thead><tbody>{avoid_rows}</tbody></table></div>
  </section>
  <section id="sources">
    <h2>数据来源</h2>
    <p>位次以重庆2026一分一段为锚。学校专业录取以学校官网、官方招生系统、可溯源投档数据和专业排名交叉核验；原始候选池只作为候选池查漏，不作为页面排序依据。</p>
    <ul class="source-list">{source_items}</ul>
  </section>
</main>
<footer>最终填报前仍要用重庆志愿系统逐项核2026招生计划、校区、收费、大类分流和体检限制。</footer>
<script>
  const state = {{ tier: '全部', region: '全部', priority: '全部', q: '' }};
  const rows = [...document.querySelectorAll('.choice-row')];
  const cards = [...document.querySelectorAll('.choice-card')];
  const count = document.querySelector('.count');
  function match(el) {{
    const tierOk = state.tier === '全部' || el.dataset.tier === state.tier;
    const regionOk = state.region === '全部' || el.dataset.region === state.region;
    const priorityOk = state.priority === '全部' || el.dataset.priority === state.priority;
    const searchOk = !state.q || el.dataset.search.includes(state.q);
    return tierOk && regionOk && priorityOk && searchOk;
  }}
  function applyFilters() {{
    let visible = 0;
    rows.forEach((row) => {{
      const show = match(row);
      row.classList.toggle('is-hidden', !show);
      if (show) visible += 1;
    }});
    cards.forEach((card) => card.classList.toggle('is-hidden', !match(card)));
    count.textContent = `当前显示 ${{visible}} 条`;
  }}
  document.querySelectorAll('.filter-line').forEach((line) => {{
    line.querySelectorAll('.chip').forEach((button) => {{
      button.addEventListener('click', () => {{
        line.querySelectorAll('.chip').forEach((item) => item.classList.remove('active'));
        button.classList.add('active');
        state[line.dataset.kind] = button.dataset.value;
        applyFilters();
      }});
    }});
  }});
  document.querySelector('#search').addEventListener('input', (event) => {{
    state.q = event.target.value.trim().toLowerCase();
    applyFilters();
  }});
  applyFilters();
</script>
</body>
</html>
"""


def main() -> None:
    html = "\n".join(line.rstrip() for line in render().splitlines()) + "\n"
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
