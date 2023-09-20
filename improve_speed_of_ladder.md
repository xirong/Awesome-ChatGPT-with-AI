
使用梯子的同学，给个建议，可以加快访问速度：

1、看对应节点的质量，理论上日本、香港的要快一些，自己可以测速试一下，延迟低的，就快；

2、梯子软件的配置，加快寻址速度，比如clash，下面有建议。

注意使用OpenAI的服务，最好别经常换IP，找个固定的节点一直用，别用香港的，日本、韩国的可以，或者直接用美国的。

我们有使用 clash [What is Clash? | Clash ](https://dreamacro.github.io/clash/) 作为梯子工具的， 这个软件本身配置的规则很多，如果选择rule模式，他自带的rule有1w多条，在1w多条里面路由也费时间，体感上总是慢。

大家可以自己创建个config，把rule下面的内容替换成自己的，比如你只用google、github、openai，别的都不需要，类似我这种，梯子路由是直连还是proxy就非常快，整体上也快多了。

如果有些网站打不开，需要访问的时候，就可以自己添加条规则就行。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/11056bef-8ca4-43da-ace0-1607a0e13dfa.png)

具体是用 domain-suffix 还是 domain-keyword ，可以参考：

修改配置参考说明文档：[https://dreamacro.github.io/clash/configuration/rules.html](https://dreamacro.github.io/clash/configuration/rules.html)

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/07181942-f32f-47b1-aa2f-24598d61417d.png)

删除这些组后，clash上那些分组的就没有了。

删除前

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/7fd736b7-afa5-4cd2-bdd3-d54e2e19479e.png)

删除后

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/7f2c79fa-2b8d-4d0a-ada6-d84d5cfb420a.png)

这样修改完后，我把浏览器用的Proxy SwitchyOmega就禁用掉了，直接都走系统代理了，浏览器、IDEA、dropbox、telegram这些需要翻的都可以，不翻的也没问题，速度快很多。

clash 代理勾选如下：

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/bf8cb1cf-3a73-43e6-b3ec-045a1c4a8f66.png)

如果不放心，可以看看 clash dashboard的日志，哪个连接最终走的是啥都有显示

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/013edf33-7009-4b9a-abe7-bff0b7bbc879.png)

------------------------------------------------------------------------------------------------

2023-09-18 更新，**clash规则实现不同的网站配置走不同的代理地址。**

例如openAI的代理走美国线路，其他的走proxy通用线路，proxy自己可以选择香港、日本等速度较快的节点，来实现不同的网站走不同的代理策略。

截图中的， 美国4-迈阿密 是我的一个代理的name，proxy就是通用的自己在clash中选择的路线。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/ed12765c-6181-4d7d-95e3-8a587aeaee8e.png)

使用效果如下，通过这个也能看到，配置的OpenAI走的是美国4的代理，google是我proxy中的香港。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonaXavdGErlXxj/img/637fa3a8-20a7-43e9-82bb-0bcc961c9b8a.png)

