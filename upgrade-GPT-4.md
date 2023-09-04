目前业内尝试成功的方案有几类，做个汇总，大家可以参考，随着时间的推移，这些方法不确保能正常。

# 实体卡

最靠谱、正规、无风险的方案，就是你真的有一张美国银行实体卡，但是这个对大多数人来说比较困难，稍微简单点的就是【华美银行】，美国本土的银行，资质不错，近年来做中国业务，开卡、转账非常简单、小白，下载手机 app 或者微信公众号里面即可开卡。但是开发费貌似是 50 刀，每月账户管理费 25 刀，转账手续费都有。（美国银行卡要转账，走国际汇款，需要手续费，这是通例）

# 虚拟卡

针对大多数人，尤其是仅仅只是订阅个 OpenAI ChatGPT Plus 会员的，美国银行虚拟卡是最具有性价比的方案。做这个业务的有很多企业，网上搜索到的资料大部分也都是，比如 depay虚拟信用卡 ，注册成功后，需要先开卡，卡的种类如下图，分别对应的开发费、转账手续费、转账金额等。这个需要将我们法币（人民币）转换成 USTD（玩币的应该知道），一步步操作就行，网上也有一大堆教程。

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/9bb01d3a-366d-4ef1-9807-868092cd3faf.png)

类似流程的还有 onekey ，这两家都是比较大的，从业务流程上讲都比较正规些，其他的就别看了。这类卡有个风险，就是大量 web3、币圈的黑产/灰产进行套利经常使用他们的虚拟卡，导致开通的卡用着用着就有被封的可能性，也就是无法续费了。

详细可以看看这个：

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/1f45452a-8378-49b0-88f2-f25fb3dc7c93.png)

志达是前老虎证券的高管，有美国银行资源，在风控方面做了很多动作，现在 AI 方向创业，第一个做的产品就是虚拟银行卡业务，[WildCard (bewildcard.com)](https://bewildcard.com/card) ，风险和内容都如上图说了。

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/ec6e627e-e186-4ce0-aa01-e59f4978bec7.png)   ![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/ac921378-5a75-4e42-aaa6-7cbd84271f38.png)

这个的好处就是整个操作体验非常流畅，开卡需要实名认证，防止卡被乱用，后面被风控，实名用支付宝扫人脸即可。

充值直接支付宝充值，也可以采用scripe 绑定微信支付充值，直接付款人民币。开卡费最近涨了，15,9$ ，防止黑灰产借用，造成后面卡段被封无法使用。

付费 OpenAI时，对网络要求非常严格，他们提供了美国家庭网络远程桌面，在他们的桌面里面操作成功率基本上 95%以上。

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/6911f3f2-5f33-43e1-ae64-aa92223eb17d.png)

开卡可以直接官网注册账号、实名认证、开卡就行，[https://bewildcard.com/](https://bewildcard.com/) 。

我个人是 6 月底那会他们这个产品还在内测的时候用的，开卡费和充值手续费都有一些优惠，通过我的邀请链接注册开卡，可以享受 88 折，开发费由 15.9 变成 14 刀，给我这边返 2 美元，需要这个折扣的同学，可以通过 [https://bewildcard.com/i/XIRONG](https://bewildcard.com/i/XIRONG) 这个链接注册、实名认证、开卡。

他们也有个电报群，里面有很多信息可以看，也能了解最新资讯。

# chatGPT IOS app 充值

美区 appstore 礼品卡充值，在手机 app 上 chatGPT IOS app 中进行充值升级。

整个过程也比较费劲，感兴趣的可以去网上搜一搜，中间科学上网的环境非常重要。也有风险，有好多白花钱买礼品了，但是没法充值

# Microsoft Azure cloud OpenAI API（新用户免费用30天）

这个不是通过网页版 chat.openai.com 访问 GPT4 的（需要订阅 ChatGPT Plus 会员，一月 20 刀，官网订阅），这个方法是让你可以通过 API 的形式，使用 gpt-4 模型，申请后，可以使用 IDEa 的一些插件，配置地址填写 Azure 的就能用。

Azure 最大的好处就是网络快，无需翻墙，不用科学上网，对没有梯子的同学比较友好。

首先注册 Microsoft Azure 账号，[https://portal.azure.com/](https://portal.azure.com/)  ，一般新人都有 30 天免费 200 刀的订阅，这个可以用来付费使用 OpenAI 的 API 接口。

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/a4c01b5b-e2e9-41fd-bc4a-9e8cf57df864.png)

Azure账号申请完后，默认是不支持 OpenAI 服务的，需要申请接口权限，申请地址：[https://aka.ms/oai/access](https://aka.ms/oai/access)

如下图，申请后等待审核通过。新用户是可以免费试用 1 年的，也就是说，你可以免费使用 ChatGPT（GPT3.5 ）的 API，对无法科学上网的同学非常合适。

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/1cad7a28-007f-4000-abda-342eb47e0284.png)

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/803a12f7-e111-4b83-973e-a4f93ca718a3.png)

等一等，大概 1 天左右，收到了试用邮件。

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/a5abd49f-890d-4221-8891-a82045de20fd.png)

收到邮件后，就可以在后台创建 OpenAI 的服务了，[https://portal.azure.com/](https://portal.azure.com/)

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/8498d752-bf6e-43c8-a917-eeaf70fc8f02.png)

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/052d65c0-f20d-442f-bb8f-1505f734f0be.png)

下一步，转到资源，去部署模型版本：

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/e2342fc1-c616-454e-9a79-3dcb7cedb291.png)

关于微软 Azure 云提供的模型版本说明：[Azure OpenAI 服务模型 - Azure OpenAI | Microsoft Learn](https://learn.microsoft.com/zh-cn/azure/ai-services/openai/concepts/models)，一开始注册的默认都没有 GPT-4 的，需要在这里面申请 GPT-4.0 的使用权限，申请连接：[https://aka.ms/oai/get-gpt4](https://aka.ms/oai/get-gpt4)

打开后，填写资料就行

![|500](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/55228b7c-e6ee-4ec6-a483-2ca7f45eb23a.png)

申请完了会有邮件通知，等待加入：

![|500](attachment/Pasted%20image%2020230817213159.png)

剩下的就是等待期，可能几天，也可能很快。

尤其是现在，openAI 全面开放了 gpt-4 的付费申请，尤其是现在，openAI 全面开放了 gpt-4 的付费申请，申请后被接受的速度快多了。

微软云同样，价钱一样，不用翻墙，国内卡付费就行了。自己折算下，大概 1 元人民币 2000 个汉字左右，包括输入和输出的 token，这个明显要比 chatgpt 3.5 贵多了，gpt-3.5 的版本 1 元人民币大概能 3.5w 个汉字。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/ed6845b1-9f75-448f-b77f-d7e7f9510a3d.png)

回到控制台，看到有了 gpt-4 的模型：

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/f5330103-7b14-4f67-9a27-2529bdb1ca63.png)

下一步，去创建部署，如下图，点击左侧部署-弹出的页面中，新建部署，选择参数。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/07a2f48c-e32f-4b05-9690-aa311bc0a3b7.png)

等一会，就显示创建成功了。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/edc33323-d434-40ba-88c0-1aabe5ee40ff.png)

之后转到  在操场中打开，就能在 Playgroud 聊天了

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/4eeb7154-844e-495f-9b48-d434b856991c.png)

好了，我们平日工作中使用，毕竟不在这里面，下面看怎么结合 IDEA 编辑器来使用 Azure 的 gpt4 模型。

先下载这个 ChatGPT 插件，这个是支持 Azure 的地址的，其他的我没有找到合适支持 Azure 的。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/b4f6a326-d4d0-4eee-849d-436310722c86.png)

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/c368bebb-f65e-4303-8191-7b59d82e642b.png)

配置好后，就可以用了，这个是 3.5 效果。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/82b4345f-6983-4d14-a745-b6292f1bc51c.png)

同样一段代码，这个是 gpt4 的效果

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGepEGavOBQN/img/4bb52873-ae18-48b7-b1f1-1ea4fe14aaba.png)

好了，到此为止，就可以在 IEDA 开发环境下，利用 微软 Azure ChatGPT（3.5）和 gpt-4.0 来进行辅助开发工作了 。

微软Azure云提供的 OpenAI 服务相对于 OpenAI 官网api 调用来说：

优点：速度快，无需翻墙，大陆手机号直接注册，新注册的用户可以免费使用 1 个月（或者 使用费用200 刀），GPT-4 也可以免费。后续需要付费的时候，直接使用国内银联卡即可，无需美国卡。

缺点：版本更新不及时，不如 OpenAI 官网的版本新。 目前 9.4 号可以用的 3.5 和 4.0 都是2023-07-01-preview的版本。另外，OpenAI 每个月都有 5 刀的免费额度，也就是每个月你的用量费用超不过 5 刀时，都是免费的白嫖的。