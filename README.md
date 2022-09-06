# MyDear
微信自推小程序爆火全网，小白版教程来喽！



一、进行微信接口配置

微信公众平台接口测试账号申请链接： 

https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login



图片



记住 “appID”  、“appsecret”（后边config需要填写）



继续下一步的搬砖操作：



用你想要接收消息的微信扫描二维码



图片



圈起来要考，当接受者微信扫描之后，这里会出现图上的列表用户数据，将微信号代码圈起来。 （config需要填写即 user ）



接下来新建模板，模板如下：

{{date.DATA}} 

地区：{{region.DATA}} 

天气：{{weather.DATA}} 

气温：{{temp.DATA}} 

风向：{{wind_dir.DATA}} 

今天是我们恋爱的第{{love_day.DATA}}天 

{{birthday1.DATA}} 

{{birthday2.DATA}}





{{note_en.DATA}} 

{{note_ch.DATA}}



咳咳，同样需要记住模板id  。



二、配置config文件



配置文件我放在了GitHub上，链接如下：

https://hub.fastgit.xyz/underwork921/Wx-daily-push-.git



三、获取天气



https://id.qweather.com

进入应用管理，根据自己的需求创建文件之后，切记选择 Web API

图片

获取KEY（weather_key）

这样我们的config所需要的内容就齐活了！

你只需要将每一步圈起来的内容填写到config文件中保存即可。



四、Python文件执行



在以上的github链接里，我们下载main文件，进行文件执行操作。

图片



效果图如下：

图片

