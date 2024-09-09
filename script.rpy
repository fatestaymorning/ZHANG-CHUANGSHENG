##rain
# 定义下雨的粒子效果
#define config.rain_effect = ParticleSystem(
#    particles = "images/rain_particle.png",
#    size = 0.05,
#    speed = (50, 100),
#    gravity = (0, 50),
#    fadeout = 0.5,
#    layer = "screens",
#    xalign = 0.5,
#    yalign = 0.5,
#    xpos = 0,
#    ypos = -100,
#    area = (0, 0, renpy.config.screen_width, renpy.config.screen_height)
#)


# 定义下雨的粒子效果的类
#class ParticleSystem(object):

#    def __init__(self, particles, size, speed, gravity, fadeout, layer, xalign, yalign, xpos, ypos, area):
#        self.particles = particles
#        self.size = size
#        self.speed = speed
#        self.gravity = gravity
#        self.fadeout = fadeout
#        self.layer = layer
#        self.xalign = xalign
#        self.yalign = yalign
#        self.xpos = xpos
#        self.ypos = ypos
#        self.area = area
#        self.particle_list = []

# 开场画面


transform logscreentransition:
    yoffset 720

    on show:
        linear 1.0 yoffset 0
    on hide:
        linear 1.0 yoffset 720
label splashscreen:

    show logo at truecenter with Dissolve(2.0)
    pause 1.0
    hide logo with Dissolve(2.0)
    return
style default:
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
##角色定义部分##
define j = Character('蒋辰', what_size = 35, who_size=45, image="jiang")
default people_name = "???"
define w = Character('[people_name]', what_size = 35, who_size=45, image="wang")
##$ people_name = "王毓梦"
define z = Character('我（童年）', image="wo")
define a = Character('我', image="wo")
define ma = Character('妈', image="ma")
define ba = Character('爸')
define liulang = Character('流浪汉')
image side jiang b = "images/chara/jiang/jiang_side_01.png"
image side wang b = "images/chara/wang/wang_side_01.png"
image side ma b = "images/chara/ma/ma_side_01.png"
image side ma c = "images/chara/ma/ma_side_02.png"
image side ma d = "images/chara/ma/ma_side_03.png"
image side ma e = "images/chara/ma/ma_side_04.png"
image an = "1.png"
image side an = "1normal.png"
image home_1 = "images/background/home_r.jpg"
image home_old = "images/background/home_old.png"
image school = "images/background/bg1.png"
image park1_n = "images/background/park_night.jpg"
image park2_n = "images/background/park2_night.jpg"
image park3_n = "images/background/park3_night.png"
image str_2 = "images/background/street_2.jpg"
##黑屏文字部分
screen chapter1Screen():
    vbox:
        align (0.5, 0.5)
        text "{size=60}第一章{/size}"
        text "{size=45}恋的奇点{/size}"
screen textScreen1():
    add "images/CG/trans/trans1.png"
screen textScreen2():
    vbox:
        align (0.5, 0.5)
        text "{size=60}2009年冬{/size}"
screen textScreen3():
    add "images/CG/CG1_3.png"
screen textScreen4():
    vbox:
        align (0.5, 0.5)
        text "{size=60}2019年秋{/size}"
screen textScreen4_1():
    vbox:
        align (0.5, 0.5)
        text "{size=60}那时我不知道，与她的邂逅会带来什么{/size}"
screen textScreen4_2():
    vbox:
        align (0.5, 0.5)
        text "{size=60}呼吸随着弦音触碰着心脏{/size}"
screen textScreen4_3():
    vbox:
        align (0.5, 0.5)
        text "{size=60}虽然很不好意思承认，我想这可能就是世人所说的一见钟情{/size}"
label start:
    default nv_xing = ""
    default nv_name = ""
# The game starts here.
    show screen chapter1Screen
    with Dissolve(0.4)
    pause
    hide screen chapter1Screen
    with Dissolve(0.4)
    play music "audio/bgm/memory.mp3" fadein 3.0
    pause 3.0
    image CG1_1 = "images/CG/CG1_1.png"
    image CG1_2 = "images/CG/CG1_2.png"
    image CG2 = "images/CG/CG2.png"
    show CG1_1 with dissolve
    # 在需要显示下雨的场景中，调用下雨的粒子效果
#    scene rainy_day:
#        show bg rainy_day_bg
#        with dissolve
#        # 显示下雨的粒子效果
#        $ config.rain_effect.start()
#        # 停止下雨的粒子效果
#        $ config.rain_effect.stop()
#        # 停止播放下雨的声音
#        stop music
#        with dissolve
#    # 开始下雨的粒子效果
#    def start(self):
#        self.stop()
#        self.particle_list = []
#        renpy.scheduler.interval(self.add_particle, 0.1)
    "2019年是一个会被世界记住的年份。"
    "这并不是因为这一年发生了什么颠覆世界的大事。"
    # 添加粒子到场景中
#    def add_particle(self):
#        particle = renpy.Sprite(self.particles)
#        particle.size = (self.size, self.size)
#        particle.xpos = self.xpos
#        particle.ypos = self.ypos
#        particle.xalign = self.xalign
#        particle.yalign = self.yalign
#        particle.layer = self.layer
#        particle.velocity = (
#            random.randint(self.speed[0], self.speed[1]),
#            random.randint(self.speed[0], self.speed[1]) - self.gravity[1]
#        )
#        self.particle_list.append((particle, 1.0))
#        renpy.store.particle_list = self.particle_list
    "当然，这一年也的确有很多颇有冲击力的事情"
    # 停止下雨的粒子效果
#    def stop(self):
#        renpy.scheduler.cancel(self.add_particle)
    ##定义名字（姓
    ##python:
    ##    nv_xing = renpy.input("姓的话就随你，叫（输入后按enter键确定）", length=32)
    ##    nv_xing = nv_xing.strip()
    ##    if not nv_xing:
    ##         nv_xing = "李"
    ####定义名字（名字
    ##python:
    ##    nv_name = renpy.input("名的话就叫（输入后按enter键确定）", length=32)
    ##    nv_name = nv_name.strip()
    ##    if not nv_name:
    ##         nv_name = "狗蛋"
    ##$quan_name = nv_xing + nv_name
    ##define a = Character("[quan_name]")
    #test
    #ba "[a]，听起来可真是个好名字"
    "但无论这样大大小小的事情发生了多少，人们感受到的都是和往日无异的日常。"
    "就像平静的水面上偶尔也会被吹起大大小小的涟漪，但终究不会让船上的人感受到风浪。"
    "似乎人人都会坚信，生活就会这样波澜不惊的推进下去。"
    hide CG1_1
    show CG1_2
    "如果要在日本街上随便找几个路人采访，问他们生活中最大的烦恼是什么，想必也不过是什么事业恋爱之类的琐事吧。"
    "那年的人们应该无论如何都不会想到在未来的几年内这个世界会经历席卷全球的传染病和动摇到世界局势的战争吧。"
    "面对这样级别的大事，连摆出一副与世无争的态度说“和我无关”这种话都说不出来了。"
    "毕竟在日本生活的我可是连自肃和生活费用实打实的暴涨都经历过了。"
    "这可是连生存都受到危机了啊。"
    "这艘名为“二次元阿宅在日本留学”的船在出发还没有几海里就要侧翻了啊。"
    "总之，以这样的眼光回溯，2019年可以算是风平浪静的最后一年了。"
    "互联网上也时不时有不少怀念2019年以前的世界的言论。"
    "这些言论有多少美化的成分就不得而知了。"
    "就和文艺复兴一样，人怀念过去未必意味着往昔有多好，大多是因为现在真的很烂。"
    hide CG1_2
    "2019年也是一个会被我记住的年份。"
    "在超大都市—东京的谁也不会留意到的角落。"
    "有一个我的小小的失败的爱情故事发生了。"
    stop music
    window hide
    show screen textScreen3
    with trans_eye_open
    $ renpy.pause(2, hard=True)
    pause
    hide screen textScreen3
    with trans_eye_shut
    $ renpy.pause(2, hard=True)
    window show
    ##切换屋内场景
    show home_1
    z "…"
    z"……"
    z"…………"
    z"唉……"
    "我所等待着的，是一通来自D大的录取电话。"
    "不过，显然没有等到就是了。"
    "人类究竟会把这种等待一个明知道不会来的东西的行为称作什么呢。"
    "现在我已经没有余力思考这个问题了。"
    "我疲惫地躺倒在床上，这一无声的结果确证了我志愿校全灭的事实。"
    "即使早有预料，但巨大的挫败感还是像涨潮一样逐渐将我吞没。"
    "连手指都不想抬。"
    "我自问虽说确实无法像X水中学的学生一样压榨自己到极致、疯狂地学习，但也力所能及的做出了努力。"
    "没想到会是这样一个结果啊。"
    "……不，其实也不是没想到吧。"
    "从决定留学的那一刻，好像之后的事情都不顺利到反常啊。"
    "家庭关系破裂。"##（配个父母吵架的图）
    "老爸的生意陷入困境。"##（配个欠债或者唉声叹气之类的图）
    "现在更是志愿校全灭。"
    "真想问当初那么坚定的我，看到现在的状况还能理直气壮地喊自己要出国吗。"
    "人在做关于未来的决定时，是不是都会潜意识中以为自己会很顺利呢。"
    "这下可真是被现实毒打了啊。"
    "我就继续这么躺着看着有些泛黄的天花板，白色的灯光呛的我眼睛开始发酸。"
    "我不由得逐渐放空大脑，开始数天花板上的裂纹。"
    "其实别说，逃避现实的感觉还真不赖。"
    "……只可惜总有现实的引力拉回那些想要放空的灵魂。"
    "肚子饿了。"
    "已经十一点了。"
    "再怎么难过，也还是要吃饭的。"
    ##【开门声】
    show str_2 with Dissolve(0.4)
    "而且我也想顺便买一些含酒精的东西回来。"
    "其实我并不喜欢喝酒，但有一种这时候就是应该做这种事的感觉。"
    ##【刷啦的便利店开门的声音】
    "从便利店出来，我提着一袋冰啤酒，想要去最近的一个公园里坐着喝。"
    "三月的日本是初春，但空气中还是微微带一点凉意。"
    hide str_2 with Dissolve(0.4)
    ##【开易拉罐的声音】
    ##形容公园的句子
    "饭点过后，公园里已经几乎没什么人影了，只有零散几个人在慢跑而已"
    show park1_n with Dissolve(0.4)
    "随便找个长椅坐了下来后，我打开了啤酒罐。"
    "一口一口的喝着，规律地就像是招财猫抬手。"
    "也许在明天还是要面对现实，但今天的我只想麻痹自己。"
    ##【画几个空啤酒罐不断增多的画面】
    z "……感觉头脑开始不清醒了，回去睡觉吧。"
    ##梦醒，眼睛式转场，bgm停，风声效果音
    play music "audio/bgm/violin.mp3" fadein 3.0
    "就当我以为能借助酒精逃避这一天的现实时，一段悠扬的旋律从不远处传来。"
    z "……原来喝醉后还会出现幻听的吗。"
    "我当然很清楚，几瓶啤酒不至于让我醉到这个程度。"
    "应该是有人在那里拉小提琴吧。"
    "在微凉的夜风下，寂静的公园里回想着时而婉转时而急促的小提琴声。"
    "我并不讨厌这样的画面。"
    "即使是外行人的我，也能听出来这段琴声背后蕴含的时光。"
    "到底要跨越过多少艰难险阻，才能够拉出这样清亮深情的音色呢。"
    "不过，虽然我不懂音乐，但感觉是很寂寞的声音。"
    "这段音乐的演奏者也有什么想要诉说的东西吗。"
    "我站起身。"
    play sound "audio/SEM/革靴で歩く.mp3"
    "也许是借助酒精给的勇气，平时的我肯定不会想要凑过去看。"
    "但现在的我，突然很想看看究竟是谁。"
    "日后的我回想起来，这是最不后悔的决定。"
    hide park1_n
    show park3_n
    ##黑屏，黑字：你相信命运吗？
    "或许是出于好奇，又或者是单纯的想要去聆听"
    "不知为何，脚步不自觉的动了起来"
    "离开长椅，顺着声音的方向走去"
    "夜晚的风吹在脸上，伴着小提琴幽长而轻柔的声音，静静的吹动着发梢"
    "演奏中连绵不断的弦声中流淌的一丝丝的凄凉感"
    a "呵呵，简直是在为我现在的处境而演奏一样啊"
    "小提琴中流淌的音符，仿佛是在安慰世人哭泣的内心，静静地诉说着"
    stop sound
    hide park3_n
    ##cg2拉小提琴的少女
    window hide
    show screen textScreen4_1
    with Dissolve(0.4)
    pause
    hide screen textScreen4_1
    with Dissolve(0.4)
    window show
    image CG3 = "images/CG/CG3.png"
    show CG3 with dissolve
    "循声而去，皎洁的月光下，少女隐约可见的秀发在寒风里静静飘洒"
    "她手上的小提琴经过了岁月的洗刷"
    "虽然经过长久的练习而变得陈旧，却给人感觉仍残留着刚买时松香的气息"
    "她的双手灵活的运动着，拉伸的弦里迸发出的旋律牵动着我的情绪"
    "而她本人，彷佛一座公园里纯白色的古希腊雕像一般，庄严而又静谧"
    a "总觉着她的琴声里也蕴含着她的悲伤，究竟是怎么回事呢"
    window hide
    show screen textScreen4_2
    with Dissolve(0.4)
    pause
    hide screen textScreen4_2
    with Dissolve(0.4)
    window show
    ##我并不相信宿命论
    ##可是这一次我却真正的感受到了命运的脉搏
    ##给少女立绘加入夜晚效果shader
    image wang_b_dark = im.MatrixColor(
    "images/chara/wang/wang_b.png",
    im.matrix.tint(0.8, 0.8, 1.0)
    *im.matrix.brightness(-0.05))
    stop music fadeout 3.0
    pause 3.0
    hide CG3 with dissolve
    show park2_n
    show wang_b_dark with dissolve
    w b "！"
    "不知不觉，我已经走到了她的面前"
    stop music fadeout 3.0
    "或许是刚才沉醉于自己的演奏中，她现在才意识到我的存在"
    "少女脸上露出惊讶的表情，混杂着一丝不安和恐惧"
    a "你好，你小提琴拉的真好！（日语）"
    w b "..."
    hide wang_b_dark
    "少女扭头快步离开了"
    a "...跑掉了，是我日语发音太烂了吗"
    a "不过这么晚了，突然有人出现在身边难免会感到害怕吧"
    a "唉，不知不觉就看入迷这一点确实欠缺考虑了"
    a "希望不要因此给她留下奇怪的印象了"
    a "不过话说回来，刚刚那女孩子还真可爱啊，以后还能见得到吗"
    ##风声效果音
    a "哈啾，不行不行，我都要感冒了,回家睡觉"
    window hide
    show screen textScreen3
    with Dissolve(0.4)
    pause
    hide screen textScreen3
    with Dissolve(0.4)
    window show
    ##切场，造一个screen？作为转场
    ##CG3起床，刷牙，开学。显示制作人，音乐，背景等
##—————————————————————————第一章结束————————————————————————————————
    show jiang_b
    j b "hello"
    j b "我的名字是蒋辰"
    j b "你叫什么"
    return
