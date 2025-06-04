import streamlit as st
from PIL import Image
st.markdown(
    """
    <style>
        img {
            border-radius: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
def home_page():
    st.markdown(
        """
        <style>
            body {
                background-color: #ddc55f;
                margin: 0;
                padding: 0;
            }
            .stApp {
                background-color: #ddc55f;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
# Lines 3-30 coded using AI
    st.markdown('<h6 style="color:#0a5247;">学习网站</h6>', unsafe_allow_html=True)
    try:
        image_path = "images/leopard.png"
        image = Image.open(image_path)
        new_width = 400
        new_height = 200
        resized_image = image.resize((new_width, new_height))
        st.image(resized_image, use_container_width=False)
    except FileNotFoundError:
        st.error("Image not found. Please check the path to the image.")
    st.markdown('<h1 style="color:#0a5247;">天天向上</h1>', unsafe_allow_html=True)
    st.markdown('<h7 style="color:#0a5247;">英语数学学习帮助</h7>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("介绍", key="introduction"):
            st.session_state.current_page = 'introduction'
    with col2:
        if st.button("学习技巧", key="tips"):
            st.session_state.current_page = 'tips'
    with col3:
        if st.button("英语", key="english"):
            st.session_state.current_page = 'english'
    with col4:
        if st.button("数学", key="math"):
            st.session_state.current_page = 'math'
def introduction_page():
    st.markdown(
        """
        <style>
            body {
                background-color: #ddc55f;
                margin: 0;
                padding: 0;
            }
            .stApp {
                background-color: #ddc55f;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("返回", key="return_intro"):
        st.session_state.current_page = 'home'
    st.markdown('<h1 style="color:#0a5247;">这个网站可以如何帮助到你?</h1>', unsafe_allow_html=True)
    st.markdown('<h6 style="color:#0a5247;">介绍</h6>', unsafe_allow_html=True)
    st.markdown(
        '<h7 style="color:#0a5347;">欢迎来到天天向上——专为你打造的英语和数学学习提升平台！ 这个网站可以为你提供帮助，让你轻松掌握，自信学习。告别压力，迎接进步——让我们一起提升你的成绩吧!</h7>',
        unsafe_allow_html=True
    )
    try:
        image_path = "images/leopard2.png"
        image = Image.open(image_path)
        new_width = 200
        new_height = 175
        resized_image = image.resize((new_width, new_height))
        st.image(resized_image, use_container_width=False)
    except FileNotFoundError:
        st.error("Image not found. Please check the path to the image.")
def tips_page():
    st.markdown(
        """
        <style>
            body {
                background-color: #ddc55f;
                margin: 0;
                padding: 0;
            }
            .stApp {
                background-color: #ddc55f;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("返回", key="return_tips"):
        st.session_state.current_page = 'home'
    tips = [
        "将学习任务分散在几天内完成，比长时间突击死记硬背更能牢固掌握知识。",
        "设定目标很重要，但务必确保它们切实可行。",
        "保持条理能节省宝贵时间，将所有学习资料集中存放在一个方便取用的地方。",
        "与其花数小时钻研单一主题，不如尝试交叉学习不同科目或话题。",
        "充足的睡眠和运动能显著提升你的学习能力和记忆效果。",
        "频繁休息。如果容易重新投入学习，可以每半小时休息5分钟。",
        "避免多任务处理。同时处理多项任务会削弱理解力、降低记忆力，并影响整体学习表现。"
    ]
# Lines 108-116 coded using AI
    st.markdown('<h1 style="color:#0a5247;">学习技巧</h1>', unsafe_allow_html=True)
    st.markdown('<h7 style="color:#0a5247;">懂得如何高效学习至关重要，以下是一些实用建议：</h7>', unsafe_allow_html=True)
    for i, tip in enumerate(tips, start=1):
        st.markdown(f'<p style="color:#0a5247; line-height: 0.5;">{i}. {tip}</p>',
                    unsafe_allow_html=True
    )
# Lines 120-122 coded using AI
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
    try:
        image_path1 = "images/leopard.png"
        image1 = Image.open(image_path1)
        new_width1 = 200
        new_height1 = 100
        resized_image1 = image1.resize((new_width1, new_height1))
        col1.image(resized_image1, use_container_width=False)
        image_path2 = "images/brain.png"
        image2 = Image.open(image_path2)
        new_width2 = 110
        new_height2 = 100
        resized_image2 = image2.resize((new_width2, new_height2))
        col5.image(resized_image2, use_container_width=False)
    except FileNotFoundError:
        st.error("One or both images not found. Please check the paths to the images.")
def english_page():
    st.markdown(
        """
        <style>
            body {
                background-color: #ddc55f;
                margin: 0;
                padding: 0;
            }
            .stApp {
                background-color: #ddc55f;
            }
            .content {
                display: inline-block;
                vertical-align: top;
                text-align: left;
            }
            .subheader {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Lines 153-159 coded using AI
    col1, col2 = st.columns(2)
    with col1:
        if st.button("返回", key="return_english"):
            st.session_state.current_page = 'home'
    with col2:
        if st.button("英语练习", key="go_to_practice_1"):
            st.session_state.current_page = 'practice_1'
    st.markdown('<h1 style="text-align: center; color:#0a5247;">英语</h1>', unsafe_allow_html=True)
    greetings = {
        "你好": "Hello",
        "嗨": "Hi",
        "你怎么样?": "How are you?",
        "再见": "Goodbye",
        "拜拜": "Bye bye",
        "早上好": "Good morning",
        "下午好": "Good afternoon",
        "晚上好": "Good evening",
        "晚安": "Goodnight",
        "待一会儿见": "See you later",
        "明天见": "See you tomorrow",
        "下周见": "See you next week"
    }
    months = {
        "一月": "January",
        "二月": "February",
        "三月": "March",
        "四月": "April",
        "五月": "May",
        "六月": "June",
        "七月": "July",
        "八月": "August",
        "九月": "September",
        "十月": "October",
        "十一月": "November",
        "十二月": "December"
    }
    food = {
        "吃": "To eat",
        "喝": "To drink",
        "水果": "Fruits",
        "蔬菜": "Vegetables",
        "肉": "Meat",
        "米饭": "Rice",
        "面条": "Noodles",
        "烧烤": "Barbecue",
        "汉堡": "Hamburgers",
        "糖果": "Sweets",
        "果汁": "Fruit juice",
        "零食": "Snacks"
    }
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">打招呼 Greetings</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/greetings.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        col1a, col1b = st.columns(2)
        for chinese, english in greetings.items():
            col1a.write(f'<span style="color:#0a5247;">{chinese}</span>', unsafe_allow_html=True)
            col1b.write(f'<span style="color:#0a5247;">{english}</span>', unsafe_allow_html=True)
# Lines 229-231 coded using AI
    with col2:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">月份 Months</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/months.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        col2a, col2b = st.columns(2)
        for chinese, english in months.items():
            col2a.write(f'<span style="color:#0a5247;">{chinese}</span>', unsafe_allow_html=True)
            col2b.write(f'<span style="color:#0a5247;">{english}</span>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">食物 Food</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/food.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        col3a, col3b = st.columns(2)
        for chinese, english in food.items():
            col3a.write(f'<span style="color:#0a5247;">{chinese}</span>', unsafe_allow_html=True)
            col3b.write(f'<span style="color:#0a5247;">{english}</span>', unsafe_allow_html=True)
    with col4:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">冠词 Articles</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/articles.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown('<h7 style="color:#0a5247;">在英语中，冠词是用来放在名词前面，表示这个名词是特定的还是不特定的。定冠词“the”用来指特定的名词，比如“the book”（那本书），在中文里我们通常会用“这个”或“那个”来表达，比如“这本书”或“那本书”。不定冠词“a”或“an”用来指不特定的名词，比如“a book”（一本书），在中文里我们通常会用“一”来表达，比如“一本书”。不过，在很多情况下，中文里可以省略这个“一”，因为上下文已经很清楚了。所以，虽然中文没有像英语那样的冠词，但我们可以根据上下文和语境来理解名词是特定的还是不特定的。</h7>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">介词 Prepositions</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/prepositions.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown('<h7 style="color:#0a5247;">英语介词是用来表示名词或代词与其他词之间关系的词。它们通常用来表示时间、地点、方向、原因、方式等概念。例如，“in”可以表示在……里面，“on”可以表示在……上面，“at”可以表示在……位置，“with”可以表示和……一起。介词后面通常跟宾语，一起构成介词短语，用来修饰句子中的名词、动词或整个句子。</h7>', unsafe_allow_html=True)
    with col6:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">时态 Tense</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/tense.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown('<h7 style="color:#0a5247;">英语的时态主要包括过去时、现在时和将来时。过去时用于描述已经发生的动作或状态，例如“I worked at a school last year”（去年我在一所学校工作）。现在时则表示当前的动作或状态，如“I work at a school”（我在一所学校工作）。而将来时用来描述尚未发生的动作或状态，比如“I will work at a school next year”（明年我将在一所学校工作）。这三种时态是英语语法的核心，帮助我们清晰地表达动作或状态发生的时间。</h7>', unsafe_allow_html=True)
def math_page():
    st.markdown(
        """
        <style>
            body {
                background-color: #ddc55f;
                margin: 0;
                padding: 0;
            }
            .stApp {
                background-color: #ddc55f;
            }
            .content {
                display: inline-block;
                vertical-align: top;
                text-align: left;
            }
            .subheader {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("返回", key="return_math"):
        st.session_state.current_page = 'home'
    st.markdown('<h1 style="text-align: center; color:#0a5247;">数学</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">毕达哥拉斯定理 (勾股定理)</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/pythagorean.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown(
            '<h7 style="color:#0a5247;">在直角三角形中，有一个非常重要的定理，即勾股定理。这个定理告诉我们，直角三角形的斜边（即直角对面的最长边）的平方等于另外两条直角边的平方和。用数学公式表示就是：c² = a² + b²，其中c代表斜边的长度，a和b分别代表两条直角边的长度。这个定理的几何意义是，如果我们以直角三角形的每条边为边长画出正方形，那么斜边上的正方形的面积正好等于两个直角边上的正方形面积之和。这个定理在数学和实际应用中都有广泛的用途，是解决直角三角形问题的关键。</h7>',
            unsafe_allow_html=True)
    with col2:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">球体体积公式</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/volume.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown(
            '<h7 style="color:#0a5247;">这个公式用于计算完美球体（比如篮球、地球、水滴）所占据的空间大小。公式可以这样表述：体积等于四分之三乘以圆周率再乘以半径的三次方。这里的“半径的三次方”指的是球体的半径自乘三次，“圆周率”是一个数学常数，大约等于3.14159，“四分之三”是一个由微积分推导出来的固定系数。这个公式在科学和工程领域都有广泛的应用。在科学中，它可以用来计算行星和原子的体积；在工程中，它可以用于设计球形水箱和轴承等。</h7>',
            unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">二次方程求根公式</h6>',
                    unsafe_allow_html=True)
        try:
            image_path = "images/quadratic.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown(
            '<h7 style="color:#0a5247;">二次方程求根公式（Quadratic Formula）用于求解形如 ax²+bx+c（其中 a≠0）的一元二次方程的实数根或复数根。该公式是解二次方程的通用方法，通过判别式快速判断根的性质，是代数和应用数学中的基础工具。</h7>',
            unsafe_allow_html=True)
    with col4:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">线性方程</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/linear.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown(
            '<h7 style="color:#0a5247;">线性方程是数学中的一种基本方程，它描述了两个变量之间的线性关系。最常见的一元线性方程形式是 y=mx+b，其中 m 是直线的斜率，表示直线的倾斜程度，b 是y轴截距，表示直线与y轴相交的点。这个方程的图形是一条直线，斜率 m 决定了直线的倾斜方向和陡峭程度，而y轴截距 b 则决定了直线在y轴上的位置。线性方程在数学、物理、经济等许多领域都有广泛的应用，它们可以用来描述和预测变量之间的关系，解决实际问题。</h7>',
            unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">SOHCAHTOA</h6>',
                    unsafe_allow_html=True)
        try:
            image_path = "images/triangle.png"
            image = Image.open(image_path)
            new_width = 300
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown(
            '<h7 style="color:#0a5247;">“SOHCAHTOA” 是一个帮助记忆直角三角形中正弦（sin）、余弦（cos）和正切（tan）函数的口诀，中文中通常被称为“正弦余弦正切口诀”。在直角三角形中，“对边”是与某个锐角相对的边，“邻边”是与该锐角相邻的直角边，“斜边”是直角三角形的最长边，与直角相对。口诀“Soh”表示正弦（sin）等于对边（opposite）除以斜边（hypotenuse）；“Cah”表示余弦（cos）等于邻边（adjacent）除以斜边（hypotenuse）；“Toa”表示正切（tan）等于对边（opposite）除以邻边（adjacent）。通过这个口诀，学生可以更轻松地记住这些三角函数的定义，从而在解决三角问题时更加高效。</h7>',
            unsafe_allow_html=True)
    with col6:
        st.markdown('<h6 class="subheader" style="color:#0a5247;">集中趋势的度量</h6>', unsafe_allow_html=True)
        try:
            image_path = "images/events.png"
            image = Image.open(image_path)
            new_width = 350
            new_height = 150
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, use_container_width=False)
        except FileNotFoundError:
            st.error("Image not found. Please check the path to the image.")
        st.markdown(
            '<h7 style="color:#0a5247;">互斥事件（Mutually Exclusive Events）是指两个事件在一次试验中不能同时发生，例如掷一枚骰子，出现1点和出现2点就是互斥事件，因为一次投掷不可能同时出现1点和2点。而相互包含事件（Mutually Inclusive Events）是指一个事件的发生必然导致另一个事件的发生，例如在一个班级中，所有男生都是学生，那么“是男生”这个事件就包含在“是学生”这个事件中。</h7>',
            unsafe_allow_html=True)
quiz_data = [
    {
        "question": "What month comes after July?",
        "options": ["May", "June", "March", "August"],
        "correct_answer": "August"
    },
    {
        "question": "What tense is the following sentence in? 'I was visiting the museum when it started to rain.'",
        "options": ["Past simple", "Past continuous", "Present perfect", "Future continuous"],
        "correct_answer": "Past continuous"
    },
    {
        "question": "You walk into class at 2:45pm. What do you say to your teacher?",
        "options": ["Good evening", "Good morning", "Good afternoon", "Goodnight"],
        "correct_answer": "Good afternoon"
    },
    {
        "question": "What is the difference between 'the' and 'a' or 'an'?",
        "options": ["'The' is a definite article used to refer to a specific noun, while 'a' and 'an' are indefinite articles, referring to a non-specific noun.", "'The' is used for plural nouns only, while 'a' and 'an' are used for singular nouns.", "The use of 'a' and 'an' indicates a precise, known object, whereas 'the' is used for more general terms.", "'The' is used for nouns that are abstract, while 'a' and 'an' apply only to concrete nouns."],
        "correct_answer": "'The' is a definite article used to refer to a specific noun, while 'a' and 'an' are indefinite articles, referring to a non-specific noun."
    },
    {
        "question": "You are ordering at a restaurant. How do you respond to the question: 'What would you like to drink?'?",
        "options": ["Snacks and sweets, please.", "I like fruit, but I don't like vegetables.", "Is there rice with meat?", "A fruit juice, please."],
        "correct_answer": "A fruit juice, please."
    },
    {
        "question": "What is the English translation of the sentence: '我的水杯在桌子上面。'?",
        "options": ["My water bottle is next to the table.", "My water bottle is under the table.", "My water bottle is on the table.", "My water bottle is in the table."],
        "correct_answer": "My water bottle is on the table."
    }
]
def practice_1_page():
    st.markdown(
        """
        <style>
            body {
                background-color: #ddc55f;
                margin: 0;
                padding: 0;
            }
            .stApp {
                background-color: #ddc55f;
            }
            .content {
                display: inline-block;
                vertical-align: top;
                text-align: left;
            }
            .subheader {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("返回", key="return_practice_1"):
        st.session_state.current_page = 'home'
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    st.markdown('<h1 style="text-align: center; color:#0a5247;">英语练习</h1>', unsafe_allow_html=True)
    question = quiz_data[st.session_state.current_question]["question"]
    options = quiz_data[st.session_state.current_question]["options"]
    correct_answer = quiz_data[st.session_state.current_question]["correct_answer"]
    st.subheader(question)
    selected_option = st.radio("选择一个答案:", options, index=None)
    if selected_option is not None:
        if st.button("提交答案"):
            if selected_option == correct_answer:
                st.success("对啦!")
            else:
                st.error(f"错误。正确答案是: {correct_answer}")
            st.session_state.current_question = (st.session_state.current_question + 1) % len(quiz_data)
# Lines 482-489 coded using AI
if st.session_state.current_page == 'home':
    home_page()
elif st.session_state.current_page == 'english':
    english_page()
elif st.session_state.current_page == 'practice_1':
    practice_1_page()
elif st.session_state.current_page == 'introduction':
    introduction_page()
elif st.session_state.current_page == 'tips':
    tips_page()
elif st.session_state.current_page == 'math':
    math_page()








