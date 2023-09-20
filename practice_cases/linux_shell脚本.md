场景分享：ChatGPT 写 Linux shell 命令，辅助排查日志问题

今天券包售卖项目上线，上了灰度环境，从监控角度看avg，p95都挺快，但最大值有几个177ms的，想找到这个条具体日志，比如这一条：

```  
{"date":"2023-09-19T20:46:23.314","level":"INFO","traceId":"xxx","thread":"DubboServerHandler","logger":"rpc-params","class":"com.xxx.xxx.service.thrid.rpc.MallServiceRpc","method":"getRecommendCouponGoods","success":"T","rt1":177,"uid":"xx","cid":"xxx","appName":"marketing-service","message":"mt=177,args={`requestDto`:{`cityId`:xx,`distance`:xx,`distanceFee`:xx,`orderChannel`:3,`orderNumber`:`xxx`,`orderServeType`:`xxx`,`qualityDelivery`:2,`useDate`:xxx,`userId`:xxx,`userMobile`:`xxx`}},result="}  
```

方法1，就是上机器上，Shell脚本 awk 处理文本，找到method=getRecommendCouponGoods 并且 rt1>100 毫秒的请求。

这个不熟悉 awk 命令的，估计一时半时写不出来，让ChatGPT写，效率很快。

这个只有 rt1>100 毫秒

![](../attachment/Pasted%20image%2020230920162040.png)

这个是method=getRecommendCouponGoods 并且 rt1>100 毫秒的请求。

![](../attachment/Pasted%20image%2020230920162048.png)

我们要做的就是 点击 这个 markdown代码框里面的命令， copy code ，黏贴到 iterm2终端中，就出来结果了。