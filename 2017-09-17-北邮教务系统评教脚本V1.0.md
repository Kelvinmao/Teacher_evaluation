---
layout: post
title: 北邮教务系统评教脚本
description: ""
modified: 2018-01-09T15:27:45-04:00
tags: [Tools]
image:
  feature: abstract-10.jpg
  credit: dargadgetz
  creditlink: http://www.dargadgetz.com/ios-7-abstract-wallpaper-pack-for-iphone-5-and-ipod-touch-retina/
---

# 为什么会有这样一个工具？

    <p>
        之前是有一位学长写了JS版和Python版的评教脚本，不过自从教务系统加了验证码后就废弃无人维护了。
        
        众所周知，北邮的教学评估总是安排在期中期末复习周，然而，凡是使用过教学评估界面的同学都能理解在评教界面上找到选项并点击有多困难。
        
        <br>更可怕的是,每个老师通常都会有7~8个选项，一个一个点下来眼睛都要瞎了。<br>
        鉴于此，为了解决这个问题，我写了这样一个“糙猛快”的脚本，来帮助大家一键评教。
    </p>

# 我该如何使用它？

<p>
    仓库地址：
    
    环境配置：
    
        Python 3.6
    
    依赖模块：
    
        Beautifulsoup
        Request
        urllib
        lxml
        
    上述模块通过pip安装即可（pip install + 模块名）
    
    安装完毕，确认自己处于校园网环境下并能正常打开教务系统后，更改param中的参数<strong>“zjh”</strong>和<strong>"mm"</strong>为自己的教务系统登录账号和密码即可。
    
    运行之后，会提示输入验证码，验证码默认保存在D盘，需要改的请自己更改<code>"dest_url"</code>参数至别的路径。
    
    验证码输入后，如果未抛出任何异常，应该可以在console中看到一闪而过的课程列表以及最希望看到的评估成功。
    
    至此，评教就已经顺利完成了。
</p>

# 写在最后

1.因为是突发奇想写的，所以可能会存在一些问题，使用时遇到问题记得先问问谷歌

2.还是由于突发奇想写的，界面十分简陋，其实验证码可以通过OCR解决的，不过懒得折腾，有想法的同学自己折腾一下吧。最好能部署成云服务的形式，使用更方便，用户也就不用配置各种依赖了。

