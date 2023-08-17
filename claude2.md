Claude2 网站：[https://claude.ai/](https://claude.ai/chats)

>Introducing Claude 2! Our latest model has improved performance in coding, math and reasoning. It can produce longer responses, and is available in a new public-facing beta website at [http://claude.ai](https://t.co/uLbS2JNczH) in the US and UK.

>Claude 2 has improved from our previous models on evaluations including Codex HumanEval, GSM8K, and MMLU. You can see the full suite of evaluations in our model card: [https://www-files.anthropic.com/production/images/Model-Card-Claude-2.pdf](https://www-files.anthropic.com/production/images/Model-Card-Claude-2.pdf)

>Thousands of businesses are working with Claude, and we are pleased to offer them access to Claude 2 via API at the same price as Claude 1.3!

关于Claude2，也可以看看福布斯这篇英文报道：[https://www.forbes.com/sites/alexkonrad/2023/07/11/anthropic-ai-claude-2-release/](https://www.forbes.com/sites/alexkonrad/2023/07/11/anthropic-ai-claude-2-release/)

也可以看看 [重磅！Claude vs GPT-4：14.5亿美元投资背后的AI大战，个人免费，数据已到2023年！ (qq.com)](https://mp.weixin.qq.com/s/DSVEXAJ_K9z6fwQpcGLsjg) 这个里面包含官方的介绍视频和解读。

### Claude是前OpenAI的两个大佬创办的，其中一个是GPT3的架构设计者，这两天 claude2 刚刚发布，效果看起来不错，关键免费，创建账号贼简单，一个邮箱+有个美国/英国区的梯子就行了，可以上传文件，分析文件内容，chatGPT 定于plus后，GPT4有插件才可以干这事，注册也不用花钱，ChatGPT注册还需要个国外手机号呢

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/95a1c3f2-f798-40c3-932a-6529fa43d8a1.png)

两位创始人的背景：

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/8ef82a48-7207-4cfe-9c64-1e20bcc228e2.png)   ![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/a33d0132-af68-435e-a07e-74599151460f.png)

## 以前那个案例

彩蛋：

gpt3.5  vs gpt4.0 ，体感上，同一个问题，GPT4 像是一个有经验的专家工程师给的答案， GPT3.5 像是一个刚刚工作没几年，会基础但不能完全解决问题的初级工程师。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyaY9WjJPnLbj/img/14748633-1016-493b-b447-1323d5e35565.png)

看看Claude2的答复，看起来也像个专家，比chatGPT要好一些。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/1722e9c4-9a67-4616-b413-09b95aea7634.png)

分析PDF内容，以这个流程为例：[双周迭代流程]()

黑色背景的是 GPT4withplugin ， 偏黄色背景的是 Claude2 ，Claude2的效果也不错。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/cdb6a832-52df-4317-b0b3-23f3c63b8581.png)

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/a0e24e92-8c62-4f3a-a224-1b972a677ce2.png)

### 再来个准确点的数学题案例，结果好坏是 gpt4>claude2>chatGPT。

请看具体咨询三个的内容，这个内容里面的维护费用：正确答案10w+10x ，学生是10w+100x

`请判断学生针对问题的解决方案是否正确。  问题: 我正在建造一个太阳能发电站，需要帮助计算财务。     土地费用为 100美元/平方英尺     我可以以 250美元/平方英尺的价格购买太阳能电池板     我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付10美元/平方英尺     作为平方英尺数的函数，首年运营的总费用是多少。  学生的解决方案： 设x为发电站的大小，单位为平方英尺。  费用：     土地费用：100x     太阳能电池板费用：250x     维护费用：100,000美元+100x     总费用：100x+250x+100,000美元+100x=450x+100,000美元`

GP4回答非常漂亮，给出了正确答案，看图：

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/9b7c77b1-ec06-4285-a51e-a134a7928e81.png)

Claude2一开始给出了整个计算过程，有一点小失误，回答失败。经过我提示后，回答对了。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/d84f6d9c-ba76-4e51-8179-0e8cad2af99d.png)

chatGPT计算错误，我提示后，依然是计算错误。 但是当我换个提示词后，就能计算对了，这也说明了我们用ChatGPT时，prompt非常关键，prompt可以称得上是一门语言了，需要大家认真学习才行。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/4b70f1fd-1d83-40b7-96af-18f4459cdcce.png)

换个提示词，提示词核心要引导ChatGPT一步步的来自己计算，把自己计算的结果和学生的比对，来判断是否正确。

`请判断学生的针对问题的解决方案是否正确，请通过如下步骤解决这个问题：  步骤：      首先，自己解决问题。     然后将您的解决方案与学生的解决方案进行比较，并评估学生的解决方案是否正确。     在自己完成问题之前，请勿决定学生的解决方案是否正确。  使用以下格式：      问题：问题文本     学生的解决方案：学生的解决方案文本     实际解决方案和步骤：实际解决方案和步骤文本     学生的解决方案和实际解决方案是否相同：是或否     学生的成绩：正确或不正确  问题：     我正在建造一个太阳能发电站，需要帮助计算财务。      - 土地费用为每平方英尺100美元     - 我可以以每平方英尺250美元的价格购买太阳能电池板     - 我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付每平方英尺10美元     作为平方英尺数的函数，首年运营的总费用是多少。  学生的解决方案：      设x为发电站的大小，单位为平方英尺。     费用：     1. 土地费用：100x     2. 太阳能电池板费用：250x     3. 维护费用：100,000+100x     总费用：100x+250x+100,000+100x=450x+100,000  实际解决方案和步骤：`

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/dbf63728-5e31-4efe-abac-7af016bec8d8.png)

看看英文版本，直接能正确。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/0da3348f-7f43-4144-9470-76877ec7f9b1.png)

彩蛋：google bard 的能力测试下来，现在还差的远，你看看这个答案，离谱的很。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/vBPlNkAapaz4ndG8/img/3df14483-9b80-42a3-91cb-2282287bfeaa.png)