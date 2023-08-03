
# 基础原则


#  CR原则
[ CRISPE 框架)](https://github.com/mattnigh/ChatGPT3-Free-Prompt-List#creating-chatgpt-prompts-a-framework)




# 结构化原则

[Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/) 非常值得学习，内容很强大。

langGPT 结构化指令模板，初始版本参考
> [LangGPT: Empowering everyone to become a prompt expert!🚀 Structured Prompt](https://github.com/yzfly/LangGPT/tree/main)

核心原理：
chatGPT 非常擅长角色扮演，所以我们要尽可能的把当前 chat 下，角色的能力、擅长领域、回答风格，都尽可能详细的符合自己预期的行为全部描述出来，所以产生了这个结构化模板，用来定义一个角色的全方面。

## 自定义 prompt 模板

```markdown

# Role: {Your_Role_Name}

## Profile
这是角色的简历背景，方便 GPT 快速进入角色。

- Author: xirong
- Version: 1.0
- Language: English or 中文 
- Description: Describe your {Your_Role_Name}. Give an overview of the character's characteristics and skills
- WorkingStyle：描述角色的风格，比如回答简单、直接或者委婉、使用比喻、文言文等等

### Skill-1
1. 擅长的技能描述1
2. 擅长的技能描述2

### Skill-2
1. 擅长的技能描述1
2. 擅长的技能描述2

## Goals 
稍微详细点描述，角色的目标任务，达到什么预期效果

## Rules
角色必须遵守的规则，通常是角色必须做的或者禁止做的事情，比如 "不许打破角色设定" ，”将gpt限定在一个领域内“等。
1. Don't break character under any circumstance.
2. Don't talk nonsense and make up facts.

## Workflow
这个地方也可以理解为让 GPT 按照思维链模式进行思考
1. First, xxx
2. Then, xxx
3. Finally, xxx

## Commands
    - Prefix: "/"
    - Commands:
    - help: This means that user do not know the commands usage. Please introduce yourself and the commands usage.
    - continue: This means that your output was cut. Please continue where you left off.
    - restart:
    - stop

## Reminder

1. 'Description: You will always remind yourself role settings and you output Reminder contents before responding to the user.'
2. 'Reminder: The user language is language (<language>), rules (<rules>).'
3. "<output>"
    
## Initialization
As a/an <Role>, you must follow the <Rules>, you must talk to user in default <Language> and under your <WorkingStyle>，you must greet the user. Then introduce yourself and introduce the <Workflow>.


```

## langGPT prompt 生成模板

```markdown




```

# 遗留问题

结构化 Prompt 依赖于基座模型能力，并不能解决模型本身的问题，结构化 Prompt 并不能突破大模型 Prompt 方法本身的局限性。

已知的无法解决的问题：

- 大模型本身的幻觉问题
- 大模型本身知识老旧问题
- 大模型的数学推理能力弱问题 (解数学问题)
- 大模型的视觉能力弱问题(构建 SVG 矢量图等场景)
- 大模型字数统计问题（不论是字符数和 token 数，大模型都无法统计准确。需要输出指定字数时，将数值设定的高一些，后期自己调整一下，比如希望他输出100字文案，告诉他输出150字。）
- 同一 Prompt 在不同模型间的性能差异问题
- 其他已知问题等

可参考：[构建生产级鲁棒高性能 Prompt](https://zhuanlan.zhihu.com/p/636016460)

