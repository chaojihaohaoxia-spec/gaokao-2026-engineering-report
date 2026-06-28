from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "index.html"


SOURCES = {
    "重庆2026一分一段": "https://www.dxsbb.com/news/100977.html",
    "重庆2026志愿规则": "https://www.cq.gov.cn/zwgk/zfxxgkml/zcwd/cqs2026nptgdxxzsgzssbf/202606/t20260601_15716828.html",
    "重庆邮电历年录取": "https://www.dxsbb.com/news/33445.html",
    "重庆邮电软科": "https://www.shanghairanking.cn/institution/chongqing-university-of-posts-and-telecommunications",
    "重庆邮电学科评估": "https://www.dxsbb.com/news/73477.html",
    "成都信息工程2026计划": "https://zs.cuit.edu.cn/info/1096/1688.htm",
    "成都信息工程历年录取": "https://zssj.cuit.edu.cn/sjTj.asp?sf=%D6%D8%C7%EC&kl=%CE%EF%C0%ED%2B%BB%AF%D1%A7",
    "成都信息工程软科": "https://www.shanghairanking.cn/institution/chengdu-university-of-information-technology",
    "浙江工业历年录取系统": "https://zs.zjut.edu.cn/jsp/lnzssearch.jsp",
    "江苏大学2025录取": "https://zb.ujs.edu.cn/info/1138/15458.htm",
    "江苏大学2024录取": "https://zb.ujs.edu.cn/info/1138/13668.htm",
    "江苏大学2023录取": "https://zb.ujs.edu.cn/info/1138/11738.htm",
    "西南石油重庆录取": "https://www.dakao100.com/article_94823909058.html",
    "西南石油专业排名": "https://www.dakao100.com/article_60620.html",
    "重庆理工历年录取": "https://www.dxsbb.com/news/33519.html",
    "重庆理工专业排名": "https://www.sohu.com/a/887883078_356902",
    "浙江理工录取入口": "https://zs.zstu.edu.cn/info/1038/3883.htm",
    "CNUR机械电子工程": "https://www.cnur.com/major/2740.html",
    "CNUR机器人工程": "https://www.cnur.com/major/3086.html",
    "CNUR网络工程": "https://www.cnur.com/major/3148.html",
    "CNUR物联网工程": "https://www.cnur.com/major/3130.html",
    "CNUR电气工程": "https://www.cnur.com/major/2543.html",
    "CNUR网络空间安全": "https://www.cnur.com/major/3129.html",
    "CNUR智能车辆工程": "https://www.cnur.com/major/2733.html",
    "CNUR车辆工程": "https://www.cnur.com/major/2734.html",
}


@dataclass(frozen=True)
class Candidate:
    tier: str
    order: int
    school: str
    city_campus: str
    major: str
    ranks: str
    plan_2026: str
    strength: str
    city_logic: str
    reason: str
    risk: str
    score: int
    level: str
    final: str
    source_keys: tuple[str, ...]


reach = [
    Candidate(
        "冲刺",
        1,
        "重庆邮电大学",
        "重庆南岸/校本部",
        "计算机科学与技术",
        "2025:13287；2024:同类14392；2023:同类14664",
        "暂未查到可靠公开2026分专业计划；2025普通类117人",
        "信息与通信、计算机是学校核心板块；学科评估中计算机科学与技术为B+，软科计算机相关学科前12%。",
        "重庆本地数字产业、通信运营商、软件企业和成渝就业半径都匹配。",
        "专业质量强，方向最贴合第一优先级；586/18162比近三年最低位次低约3500-5000位，只能少量冲。",
        "热门专业位次上行概率大；2024/2023为专业类口径，不能机械等同；失败风险高。",
        86,
        "高风险冲刺",
        "建议放入前段少量冲刺",
        ("重庆邮电历年录取", "重庆邮电软科", "重庆邮电学科评估"),
    ),
    Candidate(
        "冲刺",
        2,
        "重庆邮电大学",
        "重庆南岸/校本部",
        "通信与信息类",
        "2025:13949；2024:15413；2023:15839",
        "暂未查到可靠公开2026计划；2025普通类266人",
        "软科显示通信工程A第12、电子信息工程A第31；学校信息通信工程底盘强，是重邮最有标识度的方向。",
        "通信、设备、运营商、ICT集成、车联网和成渝电子信息产业都能承接。",
        "比单纯冲985/211冷门专业更有逻辑，专业和学校强项高度一致。",
        "仍高于考生位次约2300-4200位；大类内分流要核具体包含专业。",
        90,
        "值得冲",
        "建议放入前段冲刺",
        ("重庆邮电历年录取", "重庆邮电软科"),
    ),
    Candidate(
        "冲刺",
        3,
        "重庆邮电大学",
        "重庆南岸/校本部",
        "智能技术类",
        "2025:14652；2024:同类14392/16864；2023:同类14664/17392",
        "暂未查到可靠公开2026计划；2025普通类166人",
        "软科可核智能科学与技术A第13、数据科学与大数据技术A第35；学校计算机/通信平台能支撑AI方向。",
        "重庆和成都都有智能网联、工业软件、AI应用岗位，但本科就业仍需项目和算法/开发能力。",
        "属于可以冲的热门工科大类，比经管包装的数据类更接近真实工程。",
        "专业类口径变化大；若类内含不想读方向，排序应低于通信/计算机。",
        86,
        "冲刺",
        "建议放入冲刺",
        ("重庆邮电历年录取", "重庆邮电软科"),
    ),
    Candidate(
        "冲刺",
        4,
        "西南石油大学",
        "成都/成都校区",
        "电气工程及其自动化",
        "2025:14652；2024:16151；2023:17392",
        "暂未查到可靠公开2026计划；机构表列2026计划14人，需以重庆系统核",
        "CNUR电气工程及其自动化B+第121；学校虽有石油行业底色，但电气方向通用就业面更宽。",
        "成都电子信息、能源装备、电力设备、制造业岗位都可承接，城市资源明显加分。",
        "电气属于第一优先级，三年位次从17392抬到14652，说明热度上行但仍不是完全没机会。",
        "2025位次高于考生约3500位，属于冲刺；学校行业标签偏能源，不能把它当纯电力强校。",
        84,
        "冲刺",
        "建议少量放入冲刺",
        ("西南石油重庆录取", "CNUR电气工程", "西南石油专业排名"),
    ),
    Candidate(
        "冲刺",
        5,
        "浙江工业大学",
        "杭州/朝晖校区",
        "机器人工程",
        "2025:594分约13602；2024:589分约16864；2023:551分约19711",
        "暂未查到可靠公开2026计划；2025官方录取5人",
        "CNUR机器人工程A第32；学校工科底盘较强，杭州制造业数字化和机器人生态较好。",
        "杭州的软件、智能制造、自动化、机器人产业资源明显加分。",
        "城市、专业、学校工科氛围都好，值得作为高质量冲刺。",
        "2025突然抬到约13602位，且招生少，波动风险很高；不能把2023低位当常态。",
        84,
        "高波动冲刺",
        "建议少量冲",
        ("浙江工业历年录取系统", "CNUR机器人工程"),
    ),
    Candidate(
        "冲刺",
        6,
        "江苏大学",
        "江苏镇江/校本部",
        "机械电子工程",
        "2025:589分约15346；2024:585分约18320；2023:未查到同名可比数据",
        "暂未查到可靠公开2026计划；2025官方录取3人",
        "机械工程学科评估B+；CNUR机械电子工程A、前10%，约第9。",
        "镇江城市弱于南京/苏州，但长三角制造业半径较好，机械电子就业链清晰。",
        "适合能接受机械电子、愿意做智能制造/机电控制的学生。",
        "招生3人，大小年风险极高；如果只想电子信息/计算机，应放在重邮之后。",
        82,
        "冲稳边界",
        "可放入冲刺末段或稳妥前段",
        ("江苏大学2025录取", "江苏大学2024录取", "江苏大学2023录取", "CNUR机械电子工程"),
    ),
    Candidate(
        "冲刺",
        7,
        "江苏大学",
        "江苏镇江/校本部",
        "机械设计制造及其自动化",
        "2025:590分约14988；2024:590分约16513；2023:556分约18037",
        "暂未查到可靠公开2026计划；2025官方录取5人",
        "机械工程学科评估B+，传统机械强校；机械类专业在第三方/软科口径中处于A类区间。",
        "长三角制造业、汽车零部件、装备制造资源优于普通地级市。",
        "若能接受第二优先级机械方向，这是比“冷门211工科”更实在的冲刺。",
        "不是第一优先级；招生数小；本科就业质量更依赖个人实践和考研。",
        80,
        "冲刺",
        "可少量放入",
        ("江苏大学2025录取", "江苏大学2024录取", "江苏大学2023录取"),
    ),
]

stable = [
    Candidate(
        "稳妥",
        1,
        "重庆邮电大学",
        "重庆南岸/校本部",
        "电子工程类",
        "2025:18260；2024:18694；2023:集成电路与电子工程类20706",
        "暂未查到可靠公开2026计划；2025普通类252人",
        "重邮电子信息工程软科A第31，信息通信和电子信息是学校核心工科平台。",
        "重庆电子信息、汽车电子、通信设备和成渝产业带匹配。",
        "位次几乎贴合586/18162，是最核心的稳妥选择之一。",
        "必须核大类具体专业和分流规则；若不含目标电子信息方向，排序下调。",
        88,
        "核心稳妥",
        "强烈建议放入",
        ("重庆邮电历年录取", "重庆邮电软科"),
    ),
    Candidate(
        "稳妥",
        2,
        "重庆邮电大学",
        "重庆南岸/校本部",
        "软件工程",
        "2025:19815；2024:20262；2023:20706",
        "暂未查到可靠公开2026计划；2025普通类193人",
        "软科软件工程A第42；重邮软件、计算机和通信平台叠加，就业方向清楚。",
        "重庆本地软件园、成都互联网/软件岗位均可辐射。",
        "考生位次优于近三年最低位次，专业热度高但录取匹配好。",
        "学费和培养模式需核；软件工程学习强度高，不能只看专业名。",
        89,
        "核心稳妥",
        "强烈建议放入",
        ("重庆邮电历年录取", "重庆邮电软科"),
    ),
    Candidate(
        "稳妥",
        3,
        "重庆邮电大学",
        "重庆南岸/校本部",
        "机器人工程",
        "2025:19441；2024:19519；2023:智能制造与机器人类23650/相关20043",
        "暂未查到可靠公开2026计划；2025普通类72人",
        "CNUR机器人工程B+第54；控制/智能相关学科有支撑。",
        "重庆汽车、智能制造、工业自动化场景丰富；就业可走自动化、嵌入式、机器人应用。",
        "位次匹配，专业方向符合第一优先级后段。",
        "机器人本科口径偏宽，若课程偏机械/控制，未来最好通过项目或考研增强竞争力。",
        83,
        "稳妥",
        "建议放入",
        ("重庆邮电历年录取", "CNUR机器人工程", "重庆邮电软科"),
    ),
    Candidate(
        "稳妥",
        4,
        "西南石油大学",
        "成都/成都校区",
        "机器人工程",
        "2025:17490；2024:19109；2023:19711",
        "暂未查到可靠公开2026计划；机构表列2026计划4人，需以重庆系统核",
        "CNUR机器人工程B+，学校机械/能源装备背景可支撑机器人应用方向。",
        "成都智能制造、自动化、机器人应用和软件岗位资源较好。",
        "位次贴近且略优于18162，专业方向符合第一优先级后段，比冷门石油/地质方向更适合。",
        "2026计划可能只有4人，小计划波动很大；机器人方向本科就业需要项目能力支撑。",
        82,
        "稳妥后段",
        "可放入稳妥后段",
        ("西南石油重庆录取", "CNUR机器人工程", "西南石油专业排名"),
    ),
    Candidate(
        "稳妥",
        5,
        "成都信息工程大学",
        "成都/航空港校区",
        "电子信息工程",
        "2025:公开聚合约19441，待官方更新；2024:582分约19519；2023:550分约20043",
        "2026重庆计划7人，航空港校区",
        "软科显示电子信息工程A第51；学校信息类和电子工程学院专业口径清楚。",
        "成都电子信息、软件、通信和半导体岗位多，航空港校区区位较好。",
        "城市和专业都匹配，录取位次略低于考生位次，是稳妥核心备选。",
        "2026计划只有7人，小样本会放大波动；2025明细需等学校历史库更新核验。",
        84,
        "稳妥",
        "建议放入",
        ("成都信息工程2026计划", "成都信息工程历年录取", "成都信息工程软科"),
    ),
    Candidate(
        "稳妥",
        6,
        "成都信息工程大学",
        "成都/航空港校区",
        "电子信息科学与技术",
        "2025:公开聚合约19441，待官方更新；2024:583分约19109；2023:551分约19711",
        "2026重庆计划6人，航空港校区",
        "软科显示电子信息科学与技术B+第34；电子工程学院办学，方向偏电子信息和光电/信号。",
        "成都产业资源明显优于一般省会，适合电子信息就业与考研。",
        "专业实力、城市和录取匹配度均衡。",
        "招生6人，波动风险高；与电子信息工程相比，岗位识别度略弱。",
        82,
        "稳妥",
        "建议放入",
        ("成都信息工程2026计划", "成都信息工程历年录取", "成都信息工程软科"),
    ),
    Candidate(
        "稳妥",
        7,
        "成都信息工程大学",
        "成都/航空港校区",
        "网络工程",
        "2025:公开聚合约21426，待官方更新；2024:578分约21039；2023:547分约21046",
        "2026重庆计划4人，航空港校区",
        "软科显示网络工程A第22，CNUR显示B+第62；网络空间安全学院办学，就业方向清楚。",
        "成都网络安全、软件开发、云计算和运维岗位资源较好。",
        "考生位次明显优于近两年最低位次，是较好的稳妥偏安全项。",
        "计划仅4人，必须防波动；网络工程不同于网络空间安全，课程偏网络系统和工程实现。",
        82,
        "稳妥偏安全",
        "建议放入",
        ("成都信息工程2026计划", "成都信息工程历年录取", "CNUR网络工程"),
    ),
    Candidate(
        "稳妥",
        8,
        "浙江理工大学",
        "杭州/下沙校区",
        "机械电子工程",
        "2025:公开聚合约18260；2024:约19881；2023:约20043，需在官方查询系统复核",
        "暂未查到可靠公开2026计划",
        "机械电子工程A类、第三方榜单前10%；杭州城市产业强，机电、自动化和智能制造场景丰富。",
        "杭州的制造业数字化、机器人和自动化公司较多，城市加分明显。",
        "如果接受第二优先级机械电子，这是城市和专业都较均衡的稳妥项。",
        "录取数据需在浙江理工官方查询系统逐项核；专业不是计算机/通信主线。",
        80,
        "稳妥待核",
        "可放入，但需最终核官方数据",
        ("浙江理工录取入口", "CNUR机械电子工程"),
    ),
]

safety = [
    Candidate(
        "保底",
        1,
        "重庆理工大学",
        "重庆/两江校区",
        "机械电子工程",
        "2025:32804；2024:37057；2023:39688",
        "暂未查到可靠公开2026计划；2025普通类133人",
        "软科口径机械电子工程A第31，CNUR口径B+第46；学校机械与车辆方向有基础。",
        "重庆汽车、装备制造、电子制造资源能承接机电控制方向。",
        "考生位次明显优于近三年最低位次，安全性高且专业不差。",
        "不是第一优先级；两江校区与花溪校区资源差异需核；本科就业要靠项目经验。",
        86,
        "高质量保底",
        "强烈建议作为保底",
        ("重庆理工历年录取", "CNUR机械电子工程"),
    ),
    Candidate(
        "保底",
        2,
        "重庆理工大学",
        "重庆/两江校区",
        "智能车辆工程",
        "2025:31746；2024:35590；2023:37366",
        "暂未查到可靠公开2026计划；2025普通类98人",
        "智能车辆工程B+第11；学校车辆行业背景清楚。",
        "重庆智能网联新能源汽车产业链强，长安、赛力斯及配套企业形成就业半径。",
        "安全边际大，方向比传统车辆更贴近电控、智能化。",
        "车辆方向有周期性；如果学生排斥汽车行业，则不应作为核心保底。",
        84,
        "高质量保底",
        "建议放入",
        ("重庆理工历年录取", "CNUR智能车辆工程", "重庆理工专业排名"),
    ),
    Candidate(
        "保底",
        3,
        "重庆理工大学",
        "重庆/花溪校区",
        "电气工程及其自动化",
        "2025:24396；2024:26509；2023:28698",
        "暂未查到可靠公开2026计划；2025普通类100人",
        "CNUR电气工程及其自动化B第228；工科就业方向清晰，适合电气、电控、制造业自动化。",
        "重庆制造、电力设备、汽车电子和国企岗位均有承接。",
        "位次安全，专业接受度高，是保底里更适合家长理解的一项。",
        "若目标是国家电网核心岗位，本科院校层级不算强；需要考研或提高证书/实践竞争力。",
        83,
        "稳保结合",
        "建议放入保底前段",
        ("重庆理工历年录取", "CNUR电气工程", "重庆理工专业排名"),
    ),
    Candidate(
        "保底",
        4,
        "重庆理工大学",
        "重庆/两江校区",
        "车辆工程",
        "2025:28271；2024:30664；2023:31976",
        "暂未查到可靠公开2026计划；2025普通类118人",
        "车辆工程为学校传统优势方向；第三方评级可核为B及以上区间。",
        "重庆汽车产业资源全国突出，行业对口性强。",
        "作为保底比材料、化工、土木等方向更可控。",
        "传统车辆不等于自动驾驶；若只想计算机/电子，应放在电气和机械电子之后。",
        81,
        "保底",
        "建议放入",
        ("重庆理工历年录取", "CNUR车辆工程", "重庆理工专业排名"),
    ),
    Candidate(
        "保底",
        5,
        "重庆理工大学",
        "重庆/两江校区",
        "物联网工程",
        "2025:28751；2024:29235；2023:30304",
        "暂未查到可靠公开2026计划；2025普通类32人",
        "CNUR物联网工程B第126；方向贴近嵌入式、网络、传感和应用开发。",
        "重庆电子信息、智能制造和车联网场景能提供实习与就业机会。",
        "分数安全，专业方向比纯管理类数据专业更贴近工科。",
        "招生32人不算大；学校计算机平台不如重邮，不能把它当强计算机替代。",
        79,
        "保底",
        "可放入保底",
        ("重庆理工历年录取", "CNUR物联网工程"),
    ),
]


review_rows = [
    ("位次核验", "机构表写586分=18162位", "该项与公开一分一段一致。", "不影响，保留", "以2026重庆物理类一分一段为锚点。"),
    ("Excel导向过强", "把很多B+、A专业机械排进去", "评级写在表里不等于适合；还要看专业方向、城市、校区、招生人数。", "影响很大", "改为先从公开专业实力和就业逻辑筛选，再回看位次。"),
    ("学校强弱错配", "河海交通工程、中国石油过程装备等看着学校好", "专业不是学生第一优先级，且有冷门或行业窄风险。", "影响很大", "不因校名冲交通、过程装备、材料、化工。"),
    ("校区风险", "浙江工业朝晖、成信航空港、重理两江/花溪等未充分说明", "同一学校不同校区的实习、交通、资源差异会影响体验。", "影响中等", "每个推荐都标城市/校区；校区未核清不排前。"),
    ("计划太少", "北方工业电气1人、成信网络4人、江苏大学机械电子3人", "小计划专业位次波动会很大，不能按一年最低位次下结论。", "影响很大", "小计划只少量冲或放稳妥后段。"),
    ("冷门工科未充分提示", "材料、化工、过程装备、交通、医学信息工程、数字媒体等混入", "这些专业就业逻辑和学生偏好不完全匹配。", "影响很大", "单独列入谨慎/不建议，不进主推荐。"),
    ("经管包装数据类", "重邮大数据+经济联合、财经类数据科学看似热门", "平台偏经管或联合学位，容易偏离工科主线。", "影响中等", "除非学校工科平台强且课程工程化，否则不优先。"),
]

excel_stats = [
    ("机构表总条目", "96条", "覆盖38所学校，本质是候选池，不是最终推荐表。"),
    ("表内B及以上", "65条", "看似很多，但不能直接照搬，因为里面混有冷门工科、经管包装和小计划。"),
    ("符合目标工科且B及以上", "45条", "这是可继续研究的上限，不等于都适合放主表。"),
    ("谨慎专业条目", "15条", "含材料、化工、交通、过程装备、医学信息工程、数字媒体等。"),
    ("谨慎专业且B及以上", "10条", "说明“评级高”也可能不适合本考生目标。"),
    ("计划数≤2", "36条", "小计划极易大小年，不能按一年最低位次机械判断。"),
    ("B及以上且计划数≤5", "49条", "机构表大量推荐存在招生人数波动风险。"),
]

excel_risky_examples = [
    ("河海大学", "交通工程", "A", "计划2人", "学校名气好，但交通工程不是目标优先级，且校区流转/小计划风险大。"),
    ("中国石油大学(北京)", "过程装备与控制工程", "B+", "计划4人", "行业偏石化装备，不适合电子信息/计算机/智能制造主线。"),
    ("成都理工大学", "数字媒体技术", "B", "计划2人，宜宾校区", "名字热门但不是核心工科方向，且校区不是成都主城。"),
    ("广州中医药大学", "医学信息工程", "B", "计划1人", "学校平台偏医学，中医药院校的信息工程不应优先。"),
    ("南京工业大学", "材料科学与工程/无机非金属材料", "B+", "计划2-4人", "材料方向与家庭偏好不匹配，不能为了学校层级牺牲专业。"),
]

priority_rows = [
    ("第一优先级", "通信、电子信息、计算机、软件、AI、网安、自动化、电气、集成电路、机器人", "推荐", "就业口径清楚，升学方向明确，和成渝/长三角产业匹配。", "热门专业位次上涨；课程难度高；大类分流要核。", "数学、编程、物理基础不差，愿意做项目的学生。"),
    ("第二优先级", "机械电子、智能制造、车辆、测控、光电、能源动力、储能", "有条件推荐", "在强校、强城市、强行业背景下可选，尤其机电控制和智能制造。", "本科就业质量差异大，部分方向更依赖考研。", "接受制造业、设备、汽车、电控方向的学生。"),
    ("谨慎考虑", "材料、化工、土木、环境、生物工程、交通、过程装备", "谨慎", "只有学校该学科很强且本人接受行业路径时才考虑。", "岗位环境、行业周期、转行成本、考研依赖都要说清。", "愿意深造或明确喜欢对应行业的学生。"),
    ("不建议优先", "财经/管理包装的数据类、医学信息工程、数字媒体技术、外语/法学/经管", "不推荐", "不符合本次工科强专业优先逻辑。", "看似热门但工程训练弱或平台错位。", "本次考生不适合优先选择。"),
]

not_recommended = [
    ("河海大学", "交通工程", "211、学校名气好，专业评级A", "不是目标优先级；交通工程就业/深造路径窄，且有校区流转和计划2人风险。", "不彻底排除，但不建议冲"),
    ("中国石油大学(北京)", "过程装备与控制工程", "211、评级B+", "过程装备偏石化装备，行业窄，不适合只想电子信息/计算机/智能制造的目标。", "建议排除"),
    ("重庆邮电大学", "医学信息工程", "重邮平台好，评级高", "医学信息工程就业口径不如计算机/软件/电子明确，用户已列入谨慎专业。", "建议排除"),
    ("重庆邮电大学", "数据科学与大数据技术+经济学联合", "分数和评级好看", "联合经济学，容易偏离纯工科；不是不能读，但不应压过软件/电子/通信。", "不优先"),
    ("成都理工大学", "数字媒体技术", "名字热门、城市成都", "数字媒体偏交互/内容技术，不是本次核心工科方向，且需看具体校区。", "不优先"),
    ("西南大学/南京工业/江苏大学等", "材料、化工、无机非金属", "学校层级或学科看起来不错", "与家庭明确偏好不匹配，就业和转方向成本较高。", "建议排除"),
    ("财经/经贸类院校", "数据科学与大数据技术", "专业名含数据", "学校平台偏财经，经管包装风险高，不符合工科强专业逻辑。", "建议排除"),
    ("北方工业大学", "电气工程及其自动化", "北京城市+评级B+", "2026机构表计划仅1人，近年位次远高于18162，性价比不高。", "只可极少量冲，不建议主冲"),
]

pending = [
    ("重庆邮电大学", "集成电路类", "2025位次17490、城市和电子信息平台都好，方向符合第一优先级", "独立专业评级暂未稳定核到B及以上；需核2026大类包含专业和分流规则", "只要核到B以上，可插入稳妥前段；未核前不进主表"),
    ("中国计量大学", "测控技术与仪器/智能感知工程", "杭州；仪器方向强，测控A、智能感知B+可核", "重庆2026专业计划和近三年专业位次仍需在官方系统补齐", "若计划稳定，可作为稳妥后段"),
    ("湖北工业大学", "电气工程及其自动化", "武汉；机构表位次约19815/21039/22909，第三方评级B+", "软科或学校官方专业评级需复核，不能只靠机构表", "待核后可进稳妥"),
    ("上海海事大学", "机械电子工程", "上海临港，机电方向B+，城市资源好", "招生少，专业和学校行业偏航运，需要确认是否接受", "待核后可少量放稳妥"),
    ("南通大学", "物联网工程/通信工程", "长三角；部分专业B/B+", "校区启东/啬园切换，城市和学校工科平台不如重邮/成信", "可作保底扩展"),
    ("北京联合大学", "计算机科学与技术", "北京城市，位次安全性较高", "学校层级和专业平台一般，评级来源需复核", "只作保底扩展"),
    ("重庆交通大学", "机械设计制造及其自动化", "重庆本地，位次安全", "学校强项偏交通土木，非电子信息主线", "只在保底不足时考虑"),
]


def link(key: str) -> str:
    url = SOURCES[key]
    return f'<a href="{escape(url)}" target="_blank" rel="noopener">{escape(key)}</a>'


def links(keys: tuple[str, ...]) -> str:
    return "、".join(link(k) for k in keys)


def table(headers: list[str], rows: list[list[str]], cls: str = "") -> str:
    thead = "".join(f"<th>{escape(h)}</th>" for h in headers)
    body = []
    for row in rows:
        cells = "".join(f"<td>{c}</td>" for c in row)
        body.append(f"<tr>{cells}</tr>")
    return f'<div class="table-wrap {cls}"><table><thead><tr>{thead}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def candidate_table(items: list[Candidate]) -> str:
    rows = []
    for item in items:
        rows.append(
            [
                str(item.order),
                escape(item.school),
                escape(item.city_campus),
                escape(item.major),
                escape(item.ranks),
                escape(item.plan_2026),
                escape(item.strength) + "<br>" + links(item.source_keys),
                escape(item.city_logic),
                escape(item.reason),
                escape(item.risk),
                f'<span class="score">{item.score}</span><br><span class="tag">{escape(item.level)}</span>',
            ]
        )
    return table(
        ["排序", "学校", "城市/校区", "专业/专业类", "2023-2025重庆物理类录取位次", "2026招生计划", "专业实力依据", "城市就业逻辑", "推荐理由", "风险提示", "综合评分"],
        rows,
        "wide",
    )


def candidate_cards(items: list[Candidate], data_tier: str | None = None) -> str:
    blocks = []
    for item in items:
        tier = data_tier or item.tier
        blocks.append(
            f"""
            <article class="choice-card" data-tier="{escape(tier)}">
              <div class="card-top">
                <span class="pill">{escape(item.tier)} {item.order}</span>
                <span class="score">{item.score}</span>
              </div>
              <h4>{escape(item.school)}｜{escape(item.major)}</h4>
              <p class="campus">{escape(item.city_campus)}</p>
              <dl>
                <dt>位次</dt><dd>{escape(item.ranks)}</dd>
                <dt>评级/排名</dt><dd>{escape(item.strength)}<br>{links(item.source_keys)}</dd>
                <dt>推荐逻辑</dt><dd>{escape(item.reason)}</dd>
                <dt>风险</dt><dd>{escape(item.risk)}</dd>
              </dl>
            </article>
            """
        )
    return '<div class="card-grid">' + "".join(blocks) + "</div>"


def pending_cards() -> str:
    blocks = []
    for school, major, value, missing, advice in pending:
        blocks.append(
            f"""
            <article class="choice-card" data-tier="待核">
              <div class="card-top"><span class="pill pending">待核</span></div>
              <h4>{escape(school)}｜{escape(major)}</h4>
              <dl>
                <dt>保留价值</dt><dd>{escape(value)}</dd>
                <dt>缺什么</dt><dd>{escape(missing)}</dd>
                <dt>处理</dt><dd>{escape(advice)}</dd>
              </dl>
            </article>
            """
        )
    return "".join(blocks)


def avoid_cards() -> str:
    blocks = []
    for school, major, looks_good, problem, exclude in not_recommended:
        blocks.append(
            f"""
            <article class="choice-card" data-tier="谨慎">
              <div class="card-top"><span class="pill avoid">谨慎/不建议</span></div>
              <h4>{escape(school)}｜{escape(major)}</h4>
              <dl>
                <dt>看起来能选</dt><dd>{escape(looks_good)}</dd>
                <dt>问题</dt><dd>{escape(problem)}</dd>
                <dt>结论</dt><dd>{escape(exclude)}</dd>
              </dl>
            </article>
            """
        )
    return "".join(blocks)


def tier_browser() -> str:
    cards = candidate_cards(reach) + candidate_cards(stable) + candidate_cards(safety) + f'<div class="card-grid">{pending_cards()}{avoid_cards()}</div>'
    return f"""
    <section id="tier-browser" class="tier-browser">
      <h2>快速分级浏览</h2>
      <p>先用按钮看分层，再决定是否展开后面的详细表格。默认显示全部推荐，点“冲刺/稳妥/保底/待核/谨慎”可以只看对应类别。</p>
      <div class="filter-bar" role="group" aria-label="志愿分级筛选">
        <button type="button" class="filter-btn active" data-filter="全部">全部</button>
        <button type="button" class="filter-btn" data-filter="冲刺">冲刺</button>
        <button type="button" class="filter-btn" data-filter="稳妥">稳妥</button>
        <button type="button" class="filter-btn" data-filter="保底">保底</button>
        <button type="button" class="filter-btn" data-filter="待核">待核</button>
        <button type="button" class="filter-btn" data-filter="谨慎">谨慎/不建议</button>
      </div>
      <div class="card-count" aria-live="polite">当前显示全部条目</div>
      <div id="tier-cards" class="tier-cards">{cards}</div>
    </section>
    """


def render() -> str:
    review = table(
        ["问题类型", "具体表现", "为什么是问题", "是否影响最终填报", "如何修正"],
        [[escape(c) for c in row] for row in review_rows],
    )
    excel_stat_table = table(
        ["审查项", "统计结果", "怎么解读"],
        [[escape(c) for c in row] for row in excel_stats],
    )
    excel_risky_table = table(
        ["学校", "专业", "表内评级", "招生计划", "处理判断"],
        [[escape(c) for c in row] for row in excel_risky_examples],
    )
    priorities = table(
        ["优先级", "专业方向", "是否推荐", "推荐原因", "风险", "适合什么类型学生"],
        [[escape(c) for c in row] for row in priority_rows],
    )
    no_table = table(
        ["学校", "专业", "为什么看起来能选", "为什么不建议或需谨慎", "是否彻底排除"],
        [[escape(c) for c in row] for row in not_recommended],
    )
    pending_table = table(
        ["学校", "专业", "保留价值", "缺什么数据", "处理建议"],
        [[escape(c) for c in row] for row in pending],
    )

    source_list = "".join(f"<li>{link(k)}</li>" for k in SOURCES)

    final_order = [
        "前7个：重邮计算机、重邮通信、重邮智能技术、西南石油电气、浙工大机器人、江苏大学机械电子、江苏大学机械设计。",
        "第8-16个：重邮电子工程、重邮软件、重邮机器人、西南石油机器人、成信电子信息工程、成信电子信息科学与技术、成信网络工程、浙江理工机械电子。",
        "第17-21个：重庆理工机械电子、智能车辆、电气、车辆、物联网。",
        "待核扩展池：重邮集成电路、中国计量测控/智能感知、湖北工业电气、上海海事机械电子、南通物联网/通信、北京联合计算机等，只有核到2026计划和B以上评级后再插入。",
    ]

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,">
  <title>重庆2026物理类586分工科志愿复核报告</title>
  <style>
    :root {{
      --ink: #17202a;
      --muted: #5e6a78;
      --line: #d8dee8;
      --bg: #f6f8fb;
      --paper: #ffffff;
      --blue: #2155a3;
      --teal: #0f766e;
      --red: #b42318;
      --amber: #b45309;
      --green: #26734d;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-padding-top: 72px; }}
    body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; color: var(--ink); background: var(--bg); line-height: 1.65; overflow-x: hidden; }}
    a {{ color: var(--blue); text-decoration: none; }}
    header {{ background: #0f172a; color: #fff; padding: 44px min(6vw, 72px) 32px; }}
    header h1 {{ margin: 0 0 12px; font-size: clamp(28px, 4vw, 48px); letter-spacing: 0; }}
    header p {{ margin: 6px 0; color: #dbe7ff; max-width: 1040px; }}
    nav {{ position: sticky; top: 0; z-index: 10; background: rgba(255,255,255,.96); border-bottom: 1px solid var(--line); padding: 10px min(6vw, 72px); display: flex; gap: 10px; overflow-x: auto; box-shadow: 0 8px 18px rgba(15,23,42,.06); }}
    nav a {{ white-space: nowrap; font-size: 14px; color: #1f2937; padding: 4px 8px; }}
    main {{ padding: 0; }}
    section {{ padding: 34px min(6vw, 72px); border-bottom: 1px solid var(--line); background: var(--paper); }}
    section:nth-of-type(even) {{ background: #f9fbff; }}
    h2 {{ margin: 0 0 18px; font-size: 26px; }}
    h3 {{ margin: 24px 0 10px; font-size: 20px; }}
    h4 {{ margin: 0 0 8px; font-size: 17px; }}
    p {{ margin: 8px 0; }}
    .lead {{ font-size: 18px; max-width: 1100px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; margin: 18px 0; }}
    .metric {{ background: #fff; border: 1px solid var(--line); border-left: 5px solid var(--blue); padding: 16px; }}
    .metric strong {{ display: block; font-size: 28px; }}
    .metric span {{ color: var(--muted); }}
    .callout {{ border-left: 5px solid var(--red); background: #fff7f6; padding: 14px 16px; margin: 16px 0; }}
    .ok {{ border-left-color: var(--green); background: #f2fbf6; }}
    .warn {{ border-left-color: var(--amber); background: #fff8ed; }}
    .tier-browser {{ background: #f5f8fd; }}
    .filter-bar {{ display: flex; gap: 10px; flex-wrap: wrap; margin: 16px 0 10px; max-width: 100%; }}
    .filter-btn {{ appearance: none; border: 1px solid #b9c6d8; background: #fff; color: #102a56; padding: 9px 14px; border-radius: 8px; font-weight: 700; cursor: pointer; white-space: nowrap; }}
    .filter-btn:hover {{ border-color: var(--blue); }}
    .filter-btn.active {{ background: var(--blue); border-color: var(--blue); color: #fff; }}
    .card-count {{ color: var(--muted); font-size: 14px; margin-bottom: 12px; }}
    .tier-cards {{ display: grid; gap: 16px; }}
    .card-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; }}
    .choice-card {{ border: 1px solid var(--line); border-left: 5px solid var(--blue); background: #fff; padding: 14px; border-radius: 8px; min-width: 0; overflow-wrap: anywhere; }}
    .choice-card[data-tier="稳妥"] {{ border-left-color: var(--green); }}
    .choice-card[data-tier="保底"] {{ border-left-color: var(--teal); }}
    .choice-card[data-tier="待核"] {{ border-left-color: var(--amber); }}
    .choice-card[data-tier="谨慎"] {{ border-left-color: var(--red); }}
    .choice-card.is-hidden {{ display: none; }}
    .card-top {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-bottom: 8px; }}
    .pill {{ display: inline-flex; align-items: center; min-height: 26px; padding: 2px 9px; border-radius: 999px; background: #e8f0ff; color: #17427d; font-size: 13px; font-weight: 800; }}
    .pill.pending {{ background: #fff4d6; color: #8a4b00; }}
    .pill.avoid {{ background: #ffe8e4; color: #9b1c13; }}
    .campus {{ color: var(--muted); margin-top: -4px; }}
    dl {{ display: grid; grid-template-columns: 76px 1fr; gap: 6px 10px; margin: 10px 0 0; }}
    dt {{ color: var(--muted); font-weight: 800; }}
    dd {{ margin: 0; min-width: 0; overflow-wrap: anywhere; }}
    .detail-table {{ margin-top: 14px; }}
    .detail-table summary {{ cursor: pointer; font-weight: 800; color: #123c73; padding: 10px 0; }}
    .table-wrap {{ overflow-x: auto; margin: 12px 0 16px; border: 1px solid var(--line); background: #fff; max-width: 100%; width: 100%; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 900px; }}
    .wide table {{ min-width: 1280px; }}
    th, td {{ border-bottom: 1px solid var(--line); border-right: 1px solid var(--line); padding: 10px 11px; vertical-align: top; font-size: 14px; overflow-wrap: anywhere; }}
    th {{ background: #edf3ff; text-align: left; color: #102a56; }}
    tr:last-child td {{ border-bottom: 0; }}
    td:last-child, th:last-child {{ border-right: 0; }}
    .score {{ font-size: 22px; font-weight: 800; color: var(--blue); }}
    .tag {{ display: inline-block; margin-top: 4px; padding: 2px 8px; background: #e8f0ff; color: #1d4f91; border-radius: 999px; font-size: 12px; }}
    .ranking {{ display: grid; grid-template-columns: 1fr; gap: 8px; margin: 16px 0; max-width: 950px; }}
    .bar {{ display: grid; grid-template-columns: 160px 1fr 82px; align-items: center; gap: 10px; font-size: 14px; }}
    .bar div:nth-child(2) {{ height: 14px; background: #e5e7eb; position: relative; overflow: hidden; }}
    .bar i {{ display: block; height: 14px; background: var(--teal); max-width: 100%; }}
    .small {{ color: var(--muted); font-size: 13px; }}
    .cols {{ columns: 2 360px; column-gap: 28px; }}
    footer {{ padding: 28px min(6vw, 72px); background: #0f172a; color: #dbe7ff; }}
    @media (max-width: 720px) {{
      header {{ padding: 28px 18px 22px; }}
      section {{ padding: 26px 16px; }}
      nav {{ padding: 8px 12px; }}
      h2 {{ font-size: 23px; }}
      .card-grid {{ grid-template-columns: 1fr; }}
      .choice-card {{ padding: 13px; }}
      .filter-bar {{ gap: 8px; }}
      .filter-btn {{ flex: 1 1 calc(50% - 8px); padding: 9px 10px; }}
      dl {{ grid-template-columns: 1fr; gap: 2px; }}
      dt {{ margin-top: 8px; }}
      .bar {{ grid-template-columns: 110px 1fr 62px; }}
      table {{ min-width: 680px; }}
      .wide table {{ min-width: 960px; }}
    }}
  </style>
</head>
<body>
<header>
  <h1>重庆2026物理类586分工科志愿复核报告</h1>
  <p>本版执行新规则：机构Excel只作审查材料；主表优先采用公开招生数据、学校官方数据、软科/学科评估/第三方专业评级，且只讨论B及以上评级或需核B以上的工科方向。</p>
  <p>考生：重庆物理类，586分，物理/化学/生物，男生，只考虑工科，不考虑中外合作、文社经管法外语教育艺术等方向。</p>
</header>
<nav>
  <a href="#conclusion">结论</a><a href="#tier-browser">分级按钮</a><a href="#data">数据核验</a><a href="#excel">Excel审查</a><a href="#priority">专业优先级</a>
  <a href="#reach">冲刺</a><a href="#stable">稳妥</a><a href="#safety">保底</a><a href="#avoid">谨慎</a><a href="#order">排序</a><a href="#summary">简单版</a>
</nav>
<main>
  <section id="conclusion">
    <h2>1. 先给家长能看懂的结论</h2>
    <p class="lead">586分在2026重庆物理类对应约18162位，属于“能摸到强双非热门工科、少量冲中上211边缘/强工科专业，但不适合为了校名去读冷门工科”的层级。</p>
    <div class="grid">
      <div class="metric"><strong>18162位</strong><span>2026重庆物理类586分累计位次</span></div>
      <div class="metric"><strong>专业优先</strong><span>本分段不建议牺牲专业去冲校名</span></div>
      <div class="metric"><strong>B以上</strong><span>主表仅保留B/B+/A/A+或强学科支撑方向</span></div>
      <div class="metric"><strong>96个</strong><span>重庆普通本科批专业平行志愿逻辑</span></div>
    </div>
    <div class="callout ok"><b>最稳妥的方向：</b>重庆邮电大学电子工程/软件/机器人，成都信息工程大学电子信息/网络工程，西南石油大学机器人，重庆理工大学机械电子/智能车辆/电气等。</div>
    <div class="callout warn"><b>最大风险：</b>热门信息类专业继续上涨，小计划专业波动大；机构表里不少“学校好但专业不适合”的选项要剔除。</div>
    <p>策略上，前段少量冲真正值得的强工科，中段集中放专业和城市都匹配的重邮/成信/浙江理工，后段用重庆理工的强应用工科做保底。不要拿材料、化工、过程装备、交通、医学信息工程、财经类数据科学去换一个看起来更响的学校名字。</p>
  </section>

  {tier_browser()}

  <section id="data">
    <h2>2. 数据核验结果</h2>
    <p><b>位次：</b>2026年重庆物理类586分，一分一段表显示本分数段404人，累计18162人；机构Excel写的18162位与此一致。来源：{link("重庆2026一分一段")}。</p>
    <p><b>志愿模式：</b>重庆普通本科批采用专业平行志愿，一般按“专业(类)+院校”为一个志愿单位，普通本科批可填96个志愿。来源：{link("重庆2026志愿规则")}。</p>
    <p><b>填报影响：</b>这种模式下没有传统“冲学校后服从调剂”的空间，每一个专业(类)+院校都必须能接受；不喜欢的专业即使学校好，也不要放前面。</p>
    <p><b>相近位次层级：</b>近三年18162位附近，重邮电子工程/软件/机器人、成信电子信息与网络方向、西南石油机器人、浙江理工机械电子、重庆理工强保底专业较常见；重邮计算机/通信、西南石油电气、浙工大机器人、江苏大学强机械多为冲刺。</p>
    <div class="ranking">
      <div class="bar"><span>重邮计算机2025</span><div><i style="width:73%"></i></div><span>13287</span></div>
      <div class="bar"><span>重邮通信2025</span><div><i style="width:77%"></i></div><span>13949</span></div>
      <div class="bar"><span>考生位次</span><div><i style="width:100%; background:#b42318"></i></div><span>18162</span></div>
      <div class="bar"><span>重邮电子工程2025</span><div><i style="width:101%"></i></div><span>18260</span></div>
      <div class="bar"><span>重邮软件2025</span><div><i style="width:109%"></i></div><span>19815</span></div>
      <div class="bar"><span>重理机械电子2025</span><div><i style="width:181%"></i></div><span>32804</span></div>
    </div>
    <p class="small">图中条越短代表往年录取位次越靠前、录取难度越高；超过考生位次越多，安全边际越大。</p>
    <div class="callout warn"><b>2026招生计划风险：</b>多数学校的2026重庆分专业计划仍需要以重庆志愿填报系统最终数据为准。本报告能核到成信2026分省计划，其他学校若未公开稳定分专业计划，均写“暂未查到可靠公开数据”。</div>
  </section>

  <section id="excel">
    <h2>3. 对机构Excel的批判性评价</h2>
    <p>Excel的价值是提供了候选池和初步位次，但不能作为最终导向。它最大的问题是把“往年最低位次+表内评级”混成推荐，缺少专业真实强弱、城市产业、校区、招生人数和专业风险的解释。</p>
    {review}
    <h3>Excel审查统计</h3>
    <p>我没有按Excel排序重做志愿，而是把它拆成可审查数据：看它有多少条、多少B及以上、多少小计划、多少看似评级高但专业方向不匹配。</p>
    {excel_stat_table}
    <h3>表内明显需要重审的例子</h3>
    {excel_risky_table}
  </section>

  <section id="priority">
    <h2>4. 专业方向优先级</h2>
    {priorities}
  </section>

  <section id="reach">
    <h2>5. 冲刺志愿清单</h2>
    <p>冲刺只放“冲上了值得读”的专业，不用冷门工科冲学校名气。</p>
    <details class="detail-table"><summary>展开冲刺详细表格</summary>{candidate_table(reach)}</details>
  </section>

  <section id="stable">
    <h2>6. 稳妥志愿清单</h2>
    <p>稳妥部分是本方案核心：录取位次贴近18162，且专业、城市、就业逻辑较均衡。</p>
    <details class="detail-table"><summary>展开稳妥详细表格</summary>{candidate_table(stable)}</details>
  </section>

  <section id="safety">
    <h2>7. 保底志愿清单</h2>
    <p>保底不是乱保；这里仍然只放能接受、就业逻辑清楚、评级达到B以上或有强应用背景的工科方向。</p>
    <details class="detail-table"><summary>展开保底详细表格</summary>{candidate_table(safety)}</details>
  </section>

  <section id="avoid">
    <h2>8. 不建议选择 / 需要谨慎的学校专业</h2>
    <details class="detail-table"><summary>展开谨慎/不建议表格</summary>{no_table}</details>
    <h3>待核扩展池</h3>
    <p>这些不是否定，而是当前公开数据还不足以直接放进最终主表。等重庆志愿系统开放后，应逐项核2026计划、校区、专业评级和近三年位次。</p>
    <details class="detail-table"><summary>展开待核扩展池表格</summary>{pending_table}</details>
  </section>

  <section id="order">
    <h2>9. 最终志愿排序建议</h2>
    <p>如果重庆2026仍按“专业(类)+院校”专业平行志愿执行，排序应理解为“我更想读哪个具体组合”，不是传统院校顺序。</p>
    <ol>{"".join(f"<li>{escape(x)}</li>" for x in final_order)}</ol>
    <div class="callout"><b>不要排太前：</b>材料、化工、过程装备、交通、土木、环境、生物工程、医学信息工程、数字媒体技术、财经/经管包装的数据科学。即使学校名字好听，也不符合本次目标。</div>
    <p><b>关于服从调剂：</b>专业平行志愿下通常按具体专业(类)+院校投档，调剂风险弱于专业组模式；但若遇到专业组/院校专业组规则，必须只填“组内所有专业都能接受”的组，否则不要填。最终以重庆考试院志愿系统当年提示为准。</p>
  </section>

  <section id="summary">
    <h2>10. 最后给一个简单版总结</h2>
    <div class="cols">
      <p><b>最值得冲：</b>重邮通信与信息类、重邮计算机、重邮智能技术类、西南石油电气、浙江工业机器人工程、江苏大学机械电子、江苏大学机械设计。</p>
      <p><b>最稳：</b>重邮电子工程、重邮软件、重邮机器人工程、西南石油机器人工程、成信电子信息工程、成信电子信息科学与技术、成信网络工程、浙江理工机械电子。</p>
      <p><b>最适合保底：</b>重庆理工机械电子、智能车辆、电气、车辆、物联网。</p>
      <p><b>不要因校名好听就选：</b>材料、化工、过程装备、交通、土木、环境、生物工程、医学信息工程、数字媒体技术、财经类数据科学。</p>
      <p><b>一句话：</b>586/18162这个分数段，最该做的是“守住强工科专业”，用重邮、成信和少量成都/长三角强工科做主轴，用重庆理工强应用工科保底，不要用冷门专业换校名。</p>
    </div>
  </section>

  <section id="sources">
    <h2>主要来源</h2>
    <p>本报告已尽量区分官方、学校官网、软科/第三方评级和机构表。若2026招生计划或学校官方录取库尚未公开，则明确标注“暂未查到可靠公开数据”或“待核”。</p>
    <ul>{source_list}</ul>
  </section>
</main>
<footer>
  <p>生成日期：2026-06-28。用途：家庭志愿讨论与正式填报前复核，不替代重庆志愿填报系统最终专业计划和投档规则。</p>
</footer>
<script>
  const filterButtons = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('#tier-cards .choice-card');
  const cardCount = document.querySelector('.card-count');
  function applyFilter(filter) {{
    let visible = 0;
    cards.forEach((card) => {{
      const show = filter === '全部' || card.dataset.tier === filter;
      card.classList.toggle('is-hidden', !show);
      if (show) visible += 1;
    }});
    cardCount.textContent = filter === '全部' ? `当前显示全部 ${{visible}} 条` : `当前显示「${{filter}}」${{visible}} 条`;
  }}
  filterButtons.forEach((button) => {{
    button.addEventListener('click', () => {{
      filterButtons.forEach((item) => item.classList.remove('active'));
      button.classList.add('active');
      applyFilter(button.dataset.filter);
    }});
  }});
  applyFilter('全部');
</script>
</body>
</html>"""


def main() -> None:
    html = "\n".join(line.rstrip() for line in render().splitlines()) + "\n"
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
