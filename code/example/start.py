import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

def printSeparator():
    print("...")
    print("...")
    print("...")
    print("...")

# 一个封装 OpenAI 接口的函数，参数为 Prompt，返回对应结果
def get_completion(prompt, model="gpt-3.5-turbo"):
    '''
    prompt: 对应的提示词
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # 模型输出的温度系数，控制输出的随机程度
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message["content"]
##############################################################################################################
##############################################################################################################



def main():
    printSeparator()
##### 2.1.1 提供清晰的指示（清晰提示词，Clear prompting）
    text =f"""
    您应该提供尽可能清晰、具体的指示，以表达您希望模型执行的任务。\
    这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。\
    不要将写清晰的提示词与写简短的提示词混淆。\
    在许多情况下，更长的提示词可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。
    """

    prompt =f"""
    把下面用三个反引号括起来的文本总结成一句话：
    ```{text}```
    """
##### 2.1.2 寻求结构化的输出（结构化提示词，Structured prompting）
    prompt2 =f"""
        请生成包括书名、作者和类别的三本虚构书籍清单，\
并以 JSON 格式提供，其中包含以下键:ID、title、author、genre，键值的内容为中文。
"""
##### 2.1.3 要求模型检查是否满足条件（检查提示词，Checklist prompting）
    text2 =f"""
    泡一杯茶很容易。首先，需要把水烧开。\
在等待期间，拿一个杯子并把茶包放进去。\
一旦水足够热，就把它倒在茶包上。\
等待一会儿，让茶叶浸泡。几分钟后，取出茶包。\
如果您愿意，可以加一些糖或牛奶调味。\
就这样，您可以享受一杯美味的茶了。
    """
    text3 =f"""
    今天阳光明媚，鸟儿在歌唱。\
这是一个去公园散步的美好日子。\
鲜花盛开，树枝在微风中轻轻摇曳。\
人们外出享受着这美好的天气，有些人在野餐，有些人在玩游戏或者在草地上放松。\
这是一个完美的日子，可以在户外度过并欣赏大自然的美景。
    """
    prompt3 =f"""
    下面将输入用三个反引号括起来的文本，
    如果它包含一系列步骤，请按照以下格式重新编写这些指令：

    第一步- ....
    第二步- ....
    第三部- ....
    ...
    第n步- ....

    如果文本中不包含一系列的步骤，请直接写“未提供步骤”

    ```{text2}```
"""

##### 2.1.4 提供少量示例（少样本提示词，Few-shot prompting）

    prompt4 =f"""
    现在你的任务是以一直的风格回答问题

    孩子：爷爷，什么是耐心？
    爷爷：孩子啊，开凿出最深峡谷的河流源于一处不起眼的泉眼；最宏伟的交响乐从单一的音符开始；最复杂的挂毯以一根孤独的线开始编织。
    孩子：爷爷，那什么又是韧性呢？
"""


##### 2.2 给模型时间去思考
##### 2.2.1 指定完成任务所需的步骤（指定步骤，Specify steps）
    text5  =f"""
        In a charming village, siblings Jack and Jill set out on \ 
a quest to fetch water from a hilltop \ 
well. As they climbed, singing joyfully, misfortune \ 
struck—Jack tripped on a stone and tumbled \ 
down the hill, with Jill following suit. \ 
Though slightly battered, the pair returned home to \ 
comforting embraces. Despite the mishap, \ 
their adventurous spirits remained undimmed, and they \ 
continued exploring with delight.
"""
    prompt5 =f"""
    Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into Chinese.
3 - List each name in the chinese summary.
4 - Output a json object that contains the following \
keys: chinese_summary, num_names.

Separate your answers with line breaks.

Text:
```{text5}```
"""

    prompt5_1 =f"""
    Your task is to perform the following actions: 
1 - Summarize the following text delimited by <> with 1 sentence.
2 - Translate the summary into Chinese.
3 - List each name in the Chinese summary.
4 - Output a json object that contains the 
following keys: Chinese_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in Chinese summary>
Output JSON: <json with summary and num_names>

Text: <{text5}>
    """
###### 2.2.2 指导模型在下结论之前找出一个自己的解法
# 中间的计算问题有个小错误，chatGPT没能找出来，那么怎么样才能让他判断正确呢？

    text6 =f"""
    """
    prompt6 =f"""
请判断学生针对问题的解决方案是否正确。

问题:
我正在建造一个太阳能发电站，需要帮助计算财务。
    土地费用为 100美元/平方英尺
    我可以以 250美元/平方英尺的价格购买太阳能电池板
    我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付10美元/平方英尺
    作为平方英尺数的函数，首年运营的总费用是多少。

学生的解决方案：
设x为发电站的大小，单位为平方英尺。

费用：
    土地费用：100x
    太阳能电池板费用：250x
    维护费用：100,000美元+100x
    总费用：100x+250x+100,000美元+100x=450x+100,000美元
    """

    prompt7 =f"""
    请判断学生的针对问题的解决方案是否正确，请通过如下步骤解决这个问题：

步骤：

    首先，自己解决问题。
    然后将您的解决方案与学生的解决方案进行比较，并评估学生的解决方案是否正确。
    在自己完成问题之前，请勿决定学生的解决方案是否正确。

使用以下格式：

    问题：问题文本
    学生的解决方案：学生的解决方案文本
    实际解决方案和步骤：实际解决方案和步骤文本
    学生的解决方案和实际解决方案是否相同：是或否
    学生的成绩：正确或不正确

问题：
    我正在建造一个太阳能发电站，需要帮助计算财务。 
    - 土地费用为每平方英尺100美元
    - 我可以以每平方英尺250美元的价格购买太阳能电池板
    - 我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付每平方英尺10美元
    作为平方英尺数的函数，首年运营的总费用是多少。

学生的解决方案：

    设x为发电站的大小，单位为平方英尺。
    费用：
    1. 土地费用：100x
    2. 太阳能电池板费用：250x
    3. 维护费用：100,000+100x
    总费用：100x+250x+100,000+100x=450x+100,000

实际解决方案和步骤：
"""
    #用英文试试看，能问能正确判断，学生的答案不正确，中文怎么不行呢。
    prompt7_1 =f"""
        Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem. 
- Then compare your solution to the student's solution \ 
and evaluate if the student's solution is correct or not. 
Don't decide if the student's solution is correct until 
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```

Question:
```
I'm building a solar power installation and I need help \
working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
``` 
Student's solution:
```
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
Actual solution:

"""

    prod_review_zh=f"""
这个熊猫公仔是我给女儿的生日礼物，她很喜欢，去哪都带着。
公仔很软，超级可爱，面部表情也很和善。但是相比于价钱来说，
它有点小，我感觉在别的地方用同样的价钱能买到更大的。
快递比预期提前了一天到货，所以在送给女儿之前，我自己玩了会。
"""

    prompt8 = f"""
您的任务是从电子商务网站上生成一个产品评论的简短摘要。
请对三个反引号之间的评论文本进行概括，最多30个词汇，并且聚焦在产品价格和质量上。
评论内容: ```{prod_review_zh}```
"""


    prompt9 =f"""
    ```
    "La performance du système est plus lente que d'habitude.", 
    "Mi monitor tiene píxeles que no se iluminan.",            
    "Il mio mouse non funziona",                               
    "Mój klawisz Ctrl jest zepsuty",                          
    "我的屏幕在闪烁"                           
```

上面三个反引号的内容：
1. 这是什么语种？
2. 将消息分别翻译成英语和中文。

格式如下：

原文（xx语种）：原文内容
英文翻译：xxxx
中文翻译：xxxx

    """
    print(get_completion(prompt6))
    printSeparator()

# 检查脚本是否直接执行
if __name__ == "__main__":
    main()
