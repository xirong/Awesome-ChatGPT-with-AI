
# GPT 应用开发和思考

2023年7月31日 · 9015 字 · 18 分钟

在过去几个月的时间中，我们似乎正处于人工智能的革命中。除了大多数人了解的 OpenAI ChatGPT 之外，许多非常新颖、有趣、实用的 AI 应用也是层出不穷，并且在使用这些应用时时，笔者也确确实实的感受到了生产力的提高。

但是关于 GPT 应用的开发知识和路线，目前似乎还没有太多的资料，所以笔者决定将自己的一些经验和思考整理成一个系列，希望能够帮助到大家。

本篇文章主要介绍的是 GPT 相关应用的开发思考，在今年 4 月份的时候，笔者因为开发 [ChatFiles](https://github.com/guangzhengli/ChatFiles) 这个开源项目，从而学习了 GPT 相关的技术知识，但是由于笔者的时间精力有限，所以一直没有机会将这些知识整理成一篇文章，直到最近笔者又因为有了新的想法，开源了 [VectorHub](https://github.com/guangzhengli/vectorhub) 这个同样基于 GPT Prompt 和 Embeddings 技术的项目，进而对 GPT 和 Embeddings 等技术知识有了更深入的了解，所以就有了这一篇分享。

## 从 Prompt 开始

AI 应用开发在过去一段时间内吸引了众多开发者入场，除了大家所熟知的 ChatGPT 之外，还涌现了大量有实际价值的 AI 应用，例如基于 AI 的翻译类的应用如 [openai-translator](https://github.com/openai-translator/openai-translator)、[immersivetranslate](https://immersivetranslate.com/)，写作类的应用如 [Notion AI](https://www.notion.so/product/ai)，编程辅助类的应用如 [GitHub Copilot](https://github.com/features/copilot) 和 [GitHub Copilot Chat](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat?tool=vscode)。

这些应用有些是优化了原有的体验，如基于 GPT 的翻译的 [openai-translator](https://github.com/openai-translator/openai-translator)，翻译质量和阅读体验远胜于之前的机器翻译，还有些则是提供了之前无法实现的功能，如 [GitHub Copilot](https://github.com/features/copilot) 的代码补全和生成，还有像 [GitHub Copilot Chat](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat?tool=vscode) 提供回答编码相关问题、解释代码、生成单元测试、给错误代码提出修复意见等等功能，这些功能的实现难度在以前是完全无法想象的。

这些应用在功能上虽然没有相似之处，但是在实现原理中，它们都是主要基于 GPT 的 Prompt(提示)实现。Prompt 指的是提供给模型的文本或指令，可以用来引导模型生成自然语言输出(Completion)。它可以给模型提供上下文信息，对模型的输出结果至关重要。

我们知道 GPT（Generative Pre-trained Transformer）是一个推理模型，它主要基于预训练和微调两个阶段。

在预训练阶段会使用一个大规模的语料库进行基础训练，例如使用维基百科、新闻文章、小说等来进行训练。当训练完成后，输入一句话给它，它会基于这句话给出一个概率上的预测，预测后续应该拼接上什么单词，这个拼接的单词是基于它在预训练阶段学习到的知识来进行概率选定的，通过一次次循环的单词预测，最终可以拼接出一段话来。这也是它被称为生成式 AI 的原因。

这一句话就是我们所说的 Prompt，也是生成式 AI 概率生成的基础。这能解释为什么我们每次输入相同的 Prompt，但是每次得到的结果都会有所不同，因为每次的结果都是基于概率生成的。

所以我们也就能理解为什么 Prompt 对于 GPT 应用开发的重要性，因为它是除了微调以外，我们能与 GPT 模型唯一的交互方式（当然除此之外还可以通过调整模型的 temperature 和 top_p 两个配置来控制 GPT 更多样化或更具创造性的输出，不过对于输出质量和对下游任务的处理能力并无明显影响）。所以 Prompt 是 GPT 应用开发最核心的部分，也是最需要开发者去思考和优化的部分。

在预训练完成后，在微调阶段会将 GPT 模型加载到特定的任务上，并使用该任务的数据集对模型进行训练。这样，模型就可以根据任务的要求进行微调，以便更好地理解 Prompt 并生成与任务相关的文本。通过微调，GPT 可以适应不同的任务，如文本分类、情感分析、问答系统等。不过目前微调因为成本昂贵和最终效果并不稳定，对于广大 GPT 开发者来讲，并不是非常好的选择，所以目前大部分的 GPT 应用开发者都是基于 Prompt 来开发应用。

## Prompt 学习路线

关于 Prompt 的基础知识，可以先去看看吴恩达老师的 [ChatGPT Prompt 工程](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)。可以通过两个小时不到的视频可以快速的了解 Prompt 的使用方式和它的魅力所在。

在有了一个初步的了解之后，笔者推荐 [Prompt Engineering Guide](https://www.promptingguide.ai/) 这份文档，该文档包含了大量的 Prompt 基础知识和未来的发展方向，对于 GPT 应用开发者来说，除了学习 Prompt 的基础知识之外，还可以从中获取到一些工程界和学术界对于 Prompt 的发展方向的思考，对于开发 AI 应用来说，这些思考弥足珍贵。

最后，非常推荐大家去看看 OpenAI 官方的 [GPT 最佳实践](https://platform.openai.com/docs/guides/gpt-best-practices) 这份文档，它是由 OpenAI 官方提供的 GPT 最佳实践指南，里面包含了大量的 Prompt 示例和使用技巧，对于 GPT 应用开发者来说，是一份非常有价值的文档。因为它是 OpenAI 官方通过合作伙伴或者 Hackathon 等不同的方式，在不同的业务领域 GPT 应用开发中总结出来的最佳实践，对于开发者来讲非常有启发价值！下面是对这一份文档的摘录：

## Prompt 最佳实践

关于 Prompt 编写的最佳实践，最为推荐的当然是 OpenAI 官方出品的 [GPT 最佳实践](https://platform.openai.com/docs/guides/gpt-best-practices) 这份文档，但对于开发 GPT 应用来讲，笔者还是想结合这份最佳实践和一些自己的经验，给大家分享一些 GPT 开发的实践。

### 清晰和详细

现实中大部分开发者在平常使用 GPT 的时候，都是以解决编程问题或者询问问题为主，所以容易带入以往使用 Google 等搜索引擎的经验来使用和开发 GPT。

例如当你想知道如何用 Python 编写斐波那契数列的时候，如果在以前使用 Google 搜索引擎，你可能会输入 `python fibonacci`。因为这样就足够了，Google 是基于倒排索引和 PageRank 算法的，只需要输入关键字，就能得到高质量的网页答案。

所以只需要这种输入两个字的输入方式是最简单和最高效的，毕竟就算多输入几个字 `how to write python fibonacci` ，对于 Google 搜索引擎来讲，输出质量是相差不大的。

而如果你使用的是 GPT，像 `python fibonacci` 这样的输入对于 GPT 来说是非常不友好的，因为它无法清晰的理解你的意图，所以它可能会给出一些不相关的结果（根据不同模型的质量会略有差异）。

但如果你输入的是 `编写一个用 python 函数来高效地计算 fibonacci 数列。评论每一行代码以解释每一部分的作用以及为什么这样写`。这样的输入对于 GPT 来说就非常清晰和详细，它能够清晰的理解你的意图，所以它给出的结果也会更加准确，**在保证输出质量下限的同时，还可以提高输出质量的上限！**

这和开发者以往使用 Google 等搜索引擎的经验是完全不同的，也是 GPT 开发者和使用者最容易忽视的地方。笔者在今年很早的时候开发 [ChatFiles](https://github.com/guangzhengli/ChatFiles) 项目时，曾匿名收集过使用者的 Prompt，发现 95% 以上的使用者使用的都是非常简单的 Prompt，简单的甚至看起来有一种一字千金的感觉。

所以当开发者开发 GPT 应用时，一定要注意 Prompt 的清晰和详细，多试几次，选择一个输出质量稳定和格式相同的 Prompt，这是保证 GPT 应用质量的关键。

### 如何处理更加复杂的任务

相信所有开发者面对简单的场景任务，多花费一些时间来调整 Prompt，都能设计好程序的 Prompt 并得到不错的输出质量。但是面对复杂任务时，想要提高 GPT 的输出质量还需要两个非常重要的技巧：**让 GPT 推理而不是回答，和拆分任务进行引导**。

#### 推理而不是回答

推理而不是回答是指在 Prompt 中，要求 GPT 模型不要立即判断正确与否或者立刻给出答案，而是引导模型进行深入思考。可以要求其先列出对问题的各种看法，对任务进行拆分，说明每一步的推理依据，然后再得出最终结论。在 Prompt 中添加逐步推理的要求，能让语言模型投入更多时间逻辑思维，输出结果也将更可靠准确。

举一个[OpenAI 官方的例子](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-instruct-the-model-to-work-out-its-own-solution-before-rushing-to-a-conclusion)，如果你需要 GPT 回答某一个学生的答案是否正确，Prompt 是 `判断学生的解决方案是否正确`的话，面对复杂的计算问题和答案，GPT 有很大的概率会给出错误的答案，因为 GPT 并不会像人一样先进行推理答案再进行回答，而是会立即给出判断。在短暂的判断中，就无法给出正确的答案（就好比人类无法在短时间计算复杂数学一样）。

所以如果我们的 Prompt 是 `首先自己解决问题，然后再将自己的解决方案与学生的解决方案进行比较，并评估学生的解决方案是否正确。在自己完成问题之前，不要确定学生的解决方案是否正确`。在 Prompt 中给出明确的引导和条件，就能够让 GPT 模型花费更多的时间推导答案，从而得到更加准确的结果。

#### 拆分任务

拆分任务进行引导是指将一个复杂的任务拆分成多个子任务，然后分别引导 GPT 模型进行推理，最后将多个子任务的结果进行整合，得到最终的结果。这样做的好处是可以让 GPT 模型更加专注于一个子任务，从而提高输出质量。

举一个不太恰当的例子，当你需要对一本书籍进行摘要的时候，GPT 直接进行总体的摘要的效果并不好，我们可以使用一系列子任务来摘要每个部分。最后再汇总产生的摘要。

当然拆分任务也会带来一些新的问题，即当单个任务输出质量有问题时，整体的输出质量也会受其影响。加上目前的 token 费用不菲，拆分任务进行引导也会带来额外的成本。但是无论如何，目前关于如何设计和拆分复杂任务是所有 GPT 应用最需要思考，和维护自身 AI 应用护城河的核心问题，也是目前大模型 AI 框架像 LangChain 等项目的核心设计点，有空可以单独写一篇文章来讨论。

### 使用技巧

除了上述的一些比较重要的实践之外，还有一些小技巧对于开发应用也是非常有帮助，下面是笔者总结的一些使用技巧：

- 提供少量示例(Few-Shot Prompting): 给模型一两个期望的输入输出样例，让模型了解我们的要求和期望的输出样式。
- Prompt 中要求结构化输出：以 Json 的方式输出，这样可以方便后续代码程序处理。
- 分隔符：使用分隔符像 `"""` 将不同的指令、上下文之间进行隔离，防止系统的 Prompt 和用户输入的 Prompt 混淆冲突。

## GPT Embedding 应用开发

在上面我们主要介绍了基于 Prompt 如何开发 AI 应用，但是有时候我们还会遇到新的问题。例如大模型的训练数据往往是基于几个月前、甚至是几年前的，当我们有一些需求场景是需要 GPT 应用提供最新的数据，例如基于最近的新闻来回答问题，或者根据私有文档来回答问题，这时候大模型本身就没有基于这些材料进行过训练，也就无法解决该类问题。

这个时候我们可以通过让模型使用参考文本来回答问题，例如我们的 prompt 可以写成:

```erlang
你将会得到一个由三个引号分隔的文档和一个问题。

你的任务是使用提供的文档回答问题，并引用用于回答问题的文本段落。

如果文档中没有包含回答该问题所需的信息，则简单地写下：“信息不足”。

如果提供问题的答案，必须附带引用注释。
使用以下格式引用相关段落（{"citation": …}）。
```

这种使用方式可以让 GPT 针对于我们给予它的参考文本进行回答，例如我们想问最新的世界杯冠军是谁，就可以附上最新的世界杯新闻的参考文本，这样 GPT 会先理解整篇新闻，再来问答问题。通过这种方式，就可以解决大模型针对于时效性和特定的下游任务的问题。

但是这种解决方案会带来另外一个问题，即参考文本长度限制的问题。GPT Prompt 是有大小限制的，像 gpt-3.5-turbo 模型它的限制是 4K tokens(～3000字)，这意味着使用者最多只能输入 3000 字给 GPT 来理解和推理答案。

那么一旦需要的参考文本大于 3000 字，就无法一次性通过 GPT 得到答案，需要开发者想办法将参考文本拆分成多个部分，然后分别进行 GPT Embeddings 转化为向量存储到向量数据库中。关于向量数据库的更多信息，可以参考我另外一篇博客 [向量数据库](https://guangzhengli.com/blog/zh/vector-database/)，当需要针对于参考文本进行提问时，需要先将问题转化为向量，然后通过向量数据库进行检索，最后再将检索到的向量转化为文本输出。这样就能得到符合 GPT tokens 限制的参考文本，并且这段参考文本是和问题具有关联的。

我们拿到问题本身和这段具有关联的参考文本，同时提交给 GPT，就能得到我们想要的答案。这个过程就是 GPT Embeddings 应用开发核心，它的核心思想是通过向量检索的方式检索与问题最相关的文本段，从而绕过 GPT tokens 的限制。

![Embedding](https://storage.guangzhengli.com/images/Embedding.png)

整体的开发流程如上图所示：

1. 加载文档，获取目标文本信息。例如 LLM 主流框架 LangChain 中 File Loader 和 Web Loader 的两种文本获取方式。
    1. 基于文件系统的 File Loader，如加载 PDF 文件、Word 文件等。
    2. 基于网络的 Web Loader，如某个网页，AWS S3 等。
2. 将目标文本拆分为多个段落，拆分方式主要基于两种。
    1. 一种是基于文字数量的拆分法，例如 1000 字为一段，这种方式的优点是简单，缺点是可能会将一个段落拆分成多个段落，导致段落的连贯性变差，从而导致最终回答结果可能缺少上下文而降低回答质量。
    2. 另一种是基于标点符号的拆分法，例如以换行为分隔符，这种方式的优点是段落的连贯性好，缺点是每个段落大小不一，可能会导致触发 GPT tokens 的限制。
    3. 最后一种是基于 GPT tokens 限制的拆分法，例如以 2000 tokens 为一组，最终查询时搜索出最相关的两个段落，这样加到一起也才 4000 tokens,就不会触发到 4096 tokens 的限制。
3. 将拆分的文本块统一存入 [向量数据库](https://guangzhengli.com/blog/zh/vector-database/) 中。
4. 将用户问题转化为向量，然后通过向量数据库进行检索，得到最相关的文本段落。（需要注意的是，这里的检索并不是传统数据库的模糊匹配或者倒排索引，而是基于语义化的搜索能力，所以检索出的文本才能回答用户问题，详细请看另外一篇博客 [向量数据库](https://guangzhengli.com/blog/zh/vector-database/）
5. 将检索出来的相关文本信息，用户问题和系统的 prompt 三个组合成一个针对于 Embeddings 场景的 Prompt，例如 Prompt 中明确写到使用参考文本回答问题，而不是 GPT 自己回答。
6. GPT 回答最终得到的 Prompt，得到最终的答案。

如果你对具体的实现代码感兴趣，可以去看看 LangChain 中关于 [Retrieval 的章节](https://js.langchain.com/docs/modules/data_connection/)。

GPT embeddings 应用能解决某些场景下 GPT 无法回答的问题，这是他最大的优点。无需训练，无需微调，只需要将文本转化为向量再通过检索就能实现，以低成本的方式就能让某些业务场景变成可能。

但这个方案同样会带来一些新的问题，例如 embeddings 文本拆分和检索的质量将在很大的程度上影响最终的结果，还有查询范围、质量和查询时间该如何均衡，检索出的参考文本无法回答用户问题时该如何处理？这都是开发者在面对业务需求和场景时需要仔细思考的问题。

如果思考更远一点，在人类过去的时间中，所有的文档都是面向人来编写，对于向量检索来说并不是最佳组织模式，以后是否会存在专门面向 AI 和检索编写的文本？让 AI 更好理解和更好符合数据库检索？不过这些问题需要长期的思考和论证，这里不再扩展。

## GPT Agents 应用开发

除了上述的 prompt 和 embeddings 两种方案能解决的业务需求外，GPT 应用开发还有一个非常常见的需求，即如何集成现有系统，或者说是如何集成现有 API。

因为软件行业已经发展了很多年，很多公司都有自己的系统和 API，这些 API 能够极大的提高 GPT 应用的能力边界。如果 GPT 应用想要在实际生活场景中落地，是不可避免的需要和现有系统进行集成。

就像如果你想要询问 GPT 一个非常简单的问题，今天北京的天气是什么？看完上面的章节，我们知道 GPT 自己是无法回答这类问题的，如果 GPT 能够自行调用某个天气 API，那么开发起来将非常的方便。

想要实现 GPT 调用查询天气这个 API 的需求，我们会面临两个问题，一个是让 GPT 应用理解某个 API 的功能，并在它觉得合适的时候调用；另一个是输入输出必须结构化，从而保证系统的稳定性。

### 理解和调用现有的 API

想让 GPT 理解某个 API 的功能，最佳的方式当然是开发者手动给 API 添加名字和具体的描述信息，包括输入和输出值的结构，和每个字段代表着什么意思，这能很大程度上影响 GPT 的判断，最后决定是否调用该 API。

如 OpenAI 官网中 [function calling 例子](https://openai.com/blog/function-calling-and-other-api-updates)中，关于调用天气 API 的描述如下所示。

```ini
function_descriptions = [
            {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {
                            "type": "string",
                            "description": "The temperature unit to use. Infer this from the users location.",
                            "enum": ["celsius", "fahrenheit"]
                        },
                    },
                    "required": ["location"],
                },
            }
        ]
```

上面的方法详细描述了如果需要调用该函数，至少需要提供当前所在的位置信息，并且可以选择性的提供温度单位。GPT 会根据问题是否和该函数的描述相关联，来决定是否调用该函数。具体的代码细节以后有几乎再写一篇，暂时不展开。

我们可以通过提供大量的 APIs 的说明文档，让 LLMs 理解并学会这些 APIs 的功能、使用方式、组合方式。最终达到根据提出的总体要求，将总体要求拆分为多个子任务，具体子任务再与某个 API 进行交互，最终达到自动化以及 AI 的目标。

我们这里描述的现有 APIs 并不仅仅是基于 HTTP 的请求，可以包括转化为 SQL 查询数据库，调用 SDK 实现复杂功能，甚至在未来，可以扩展为调用物理世界里面的开关、机械臂等。个人认为，基于目前已有的 GPT 能力和发展趋势，人机交互的方式将产生巨大的变化。

### 结构化输出

除了让 GPT 理解和调用现有的 API 之外，还需要让 GPT 输出的结果能够被现有系统所理解，这就需要 GPT 输出的结果是结构化的，例如 JSON 格式的数据。

那么你可能马上想到，我们通过 prompt 不就可以实现这种功能吗？在大部分情况下确实可以，但是有些少量的情况，prompt 并不如 function calling 的方式稳定，而我们传统的系统，对于稳定性的要求是非常高的，举个例子。

```ini
student_description=小王是北京大学计算机科学专业的二年级学生，绩点为 3.8 GPA。他的编程很厉害，是该大学机器人俱乐部的活跃成员。他希望在毕业后追求人工智能方面的工作。
```

这段话中，我们可以通过 prompt 来要求输出的结构为 json 格式，例如 prompt 为

```applescript
Please extract the following information from the given text and return it as a JSON object:

name
major
school
grades
club

This is the body of text to extract the information from:
{student_1_description}
```

但是比较难处理的是，我们没有办法能够确定 GPT 最终会输出的 grades 是 `3.8` 还是 `3.8 GPA`，这两种输出结果对于人类来讲没有如何区别，但是对于计算机来讲，这两种输出结果是完全不同的，前者是一个浮点数，后者是一个字符串。对于某些语言来讲转换就会直接出错。

我们当然可以通过增加 prompt 的描述来减少这类问题，但是现实情况是比较复杂的，我们很难通过自然语言完全描述清楚需求，很难保证 GPT 的回答会每次都保持相同的输出。所以针对于这类问题，通过 OpenAI 提供的 function calling 的方式，能够在一定程度上解决自然语言与机器语言交互的问题。

就像上述的问题可以描述为一个函数，我们将 grades 这个字段描述为 integer 来避免这类问题。这种结构化的能力对于开发一个稳定的系统是至关重要的。

```ini
student_custom_functions = [
    {
        'name': 'extract_student_info',
        'description': 'Get the student information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person'
                },
                'major': {
                    'type': 'string',
                    'description': 'Major subject.'
                },
                'school': {
                    'type': 'string',
                    'description': 'The university name.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                },
                'club': {
                    'type': 'string',
                    'description': 'School club for extracurricular activities. '
                }
                
            }
        }
    }
]
```

完整的调试过程可以去看看这个[OpenAI function calling 的例子](https://www.datacamp.com/tutorial/open-ai-function-calling-tutorial)。

## GPT 应用需求分析

上面主要是关于如何开发 GPT 应用的一些技巧，但是如果想要创造产品，我们还是需要从业务需求出发，去思考我们能够创造出什么样的业务价值，从而满足当前潜在用户的需求。

> 2023/09/06 更新：LangChain 官方文档更新，将文档分为 RAG(RetrievalAugmentedGeneration) 和 Agents 两部分。这说明从 GPT 爆发几个月以来，工业界目前也觉得 RAG 和 Agents 是业务需求落地的两个方向。其中 RAG 就是我们上面主要讲的 GPT Embeddings 部分，后续我们会也从这两个方向举例说明。我觉得锚定像 langchain 这样的头部框架对于开发者来讲是非常有价值的，因为它们会在业务落地的过程中，总结出一些最佳实践和经验，这些经验对于开发者理解业务需求有很帮助。

### 内容生成

内容生成是目前最主流的需求，也是当前 AI 应用中流量统计最高的一个方向。除了 ChatGPT 这样大家所知的产品外，还有像 [Character AI](https://beta.character.ai/) 这样主要基于 Prompt 开发的人工智能伴侣（角色扮演类）应用流量也是非常的高。

在更广泛的内容生成类中，图像生成领域如 [Midjourney](https://www.midjourney.com/)，语音生成领域如 [ElevenLabs](https://elevenlabs.io/)。文字创意类领域如 [copy ai](https://www.copy.ai/)，还包括一些细分领域的文字内容生成，如小说生成辅助 [AI-Novel](https://ai-novel.com/) 等等。

内容生成是当前互联网流量最高的 AI 需求领域，也是最容易落地的领域，因为它的应用场景非常广泛，内容生成辅助往往能够直接提高生产力，所以付费意愿往往不低，对于这个领域的争夺，往往也是最激烈的。

### GPT Embeddings 需求

GPT Embeddings 是我觉得是非常有潜在价值的方向，其中 [ChatFiles](https://github.com/guangzhengli/ChatFiles) 刚开源不久的时候，我就收到了一些的咨询，问能否在客服、销售、操作手册、知识库等场景下优化现有场景和业务，我个人的回答是 GPT Embeddings 在这些场景下是非常有前景的。

这个领域目前能看到的创业企业像 [mendable ai](https://www.mendable.ai/) 就已经占据了一定的市场份额，支持了像 [LangChain](https://js.langchain.com/) 等头部 GPT 框架的文档问答功能。并且还在积极扩展销售、客户等业务场景。

除此之外，这个领域目前流量最高的当属于 [ChatPDF](https://www.chatpdf.com/) 这个网站，可以上传 PDF 文件，然后基于 PDF 提出问题和需求如总结等。这个方向也衍生出各个细分领域的需求，如辅助论文阅读和协作的像 [Jenni AI](https://jenni.ai/) 等。

### GPT Agents 需求

GPT Agents 的需求五花八门的，因为它是基于现有系统的集成，所以我们可以通过分析现有系统的 API 来确定我们能够创造出什么样的业务价值。例如很多 GPT 提供的联网功能就是通过集成 SerpAPI 来实现的，这是一个集成了各大搜索引擎的聚合查询网站，这样就能够让 ChatGPT 能够回答一些基于搜索的问题，如当前天气、股市、新闻等等。

其中比较出名的自然是 [Auto GPT](https://github.com/Significant-Gravitas/Auto-GPT) 和 [AgentGPT](https://github.com/reworkd/AgentGPT) 这两个项目，如果对 GPT Agents 应用感兴趣，不妨看看这两个项目。除此之外，也许像 [cal.com](https://github.com/calcom/cal.com/tree/main/apps/ai) 这样的公司集成 AI agents 来使用自然语言增强预定会议这样的功能，也许能够给你一些不一样的启发。

### 非结构化输入和结构化输出

还有就是我觉得被很多人忽视的一点是 GPT/LLM 处理非结构化数据的能力。在过去，我们想要处理一些简单的文本都是需要耗费大量开发时间的，例如从短信中提取出一些关键信息，例如姓名、电话号码、地址等等，由于不同的短信模版不同，所以这些信息都是非结构化。

我们无法通过一个简单方法，就能够将这些内容转成 Json 等格式的结构化输出，所以我们往往需要通过一套复杂的正则表达式，或者 NLP 技术来将这些信息提取出来。但是正则表达式开发复杂，对于不同的短信模版，再加上模版会随着时间不短的改变，我们需要不断的调整正则表达式，这个过程是非常消耗开发时间和工程师精力的。

NLP 技术又只能针对于某一些特定的场景，例如提取电话号码，提取地址等等，对于不同的场景，我们需要不同的 NLP 技术，所以一旦业务需求发生了变化，例如识别车牌，我们还需要重新开发和调整。

但是有了 OpenAI GPT 这样统一的一个 API，我们只需要给服务提供不同的 Prompt，就可以通过 Prompt 来引导 GPT 进行推理，从而得到我们想要的结果。这样就能够大大的简化我们的开发流程，缩短开发时间，从而快速的响应市场的变化。

并且由于 GPT 的强大的泛化能力，我们只需要针对于不同的场景，思考好如何处理非结构化数据即可。这种处理非结构化数据的能力，在未来软件开发中会改变很多以往业务的开发流程和方式，对于软件的生命周期将产生深远的影响。

### 自然语言交互

最后我想说的是，GPT 能够处理自然语言的能力将深度改变人类与机器的交互方式。在过去，从命令行到图形界面，再到触摸屏，这些都是人机交互的变革史。大多数人和机器的交互方式其实是需要程序员这个载体的，人们有各种需求，业务分析师和开发人员将需求挖掘出来，由程序员通过代码的方式产生图形页面，人们再和图形页面产生交互，从而达到人机交互的能力。

这个过程是信息传递损失的，并且产生了大量的限制和成本。如果机器能够理解自然语言，我们能够直接和机器进行交互，那么软件、机器、智能这几个我们熟悉的概念将会发生巨大的变化，人机交互也将发生翻天覆地的变化。

如果你很难理解这种不确定的、没有任何参考的变化，可以去感受一下 [open interpreter](https://github.com/KillianLucas/open-interpreter) 这个项目，它是基于自然语言产生代码，并在电脑上直接执行的项目，虽然非常的原始和不稳定，但从中可以看到未来人机交互的变革。

## References

- [https://github.com/guangzhengli/ChatFiles](https://github.com/guangzhengli/ChatFiles)
- [https://github.com/guangzhengli/vectorhub](https://github.com/guangzhengli/vectorhub)
- [https://js.langchain.com/docs/modules/data_connection](https://js.langchain.com/docs/modules/data_connection)
- [https://www.datacamp.com/tutorial/open-ai-function-calling-tutorial](https://www.datacamp.com/tutorial/open-ai-function-calling-tutorial)
- [https://openai.com/blog/function-calling-and-other-api-updates](https://openai.com/blog/function-calling-and-other-api-updates)
- [https://openai.com/blog/chatgpt-plugins#code-interpreter](https://openai.com/blog/chatgpt-plugins#code-interpreter)
- [https://github.com/KillianLucas/open-interpreter](https://github.com/KillianLucas/open-interpreter)
- [https://www.chatpdf.com](https://www.chatpdf.com/)
- [https://jenni.ai](https://jenni.ai/)
- [https://github.com/reworkd/AgentGPT](https://github.com/reworkd/AgentGPT)
- [https://a16z.com/how-are-consumers-using-generative-ai](https://a16z.com/how-are-consumers-using-generative-ai)

[向量数据库](https://guangzhengli.com/blog/zh/vector-database/)

### 相关系列文章推荐

- [向量数据库](https://guangzhengli.com/blog/zh/vector-database/)

© 2023 [GuangzhengLi](https://guangzhengli.com/) Powered by [Hugo️️](https://gohugo.io/) [Ladder](https://github.com/guangzhengli/hugo-theme-ladder) ️