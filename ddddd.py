word="本单元的内容是介绍称为Scrum的敏捷开发过程以及介绍称为Python的编程语言。
请先观看视频并幻灯片。请在正式上课之前安装Python运行时。
Scrum简介
Scrum是一个敏捷的开发过程，逐步在最短的短期交付业务价值。它被广泛使用，并且经常与其他敏捷开发过程混合在一起。
视频1：Scrum简介
https://www.acfun.cn/v/ac13145403
视频2：Scrum中的冲刺
https://www.acfun.cn/v/ac13145466
视频3：Scrum中的角色，会议和文档
https://www.acfun.cn/v/ac13145616
幻灯片：English-Redistributable-Intro-Scrum.pdf
Python简介
使用miniconda安装Python
https://docs.conda.io/en/latest/miniconda.html
视频1：变量
https://www.acfun.cn/v/ac13164403_1
视频2：控制流，分支
https://www.acfun.cn/v/ac13164403_2
视频3：列表，元组和字典
https://www.acfun.cn/v/ac13164403_3
视频4：控制，循环
https://www.acfun.cn/v/ac13164403_4
视频5：功能和模块
https://www.acfun.cn/v/ac13164403_5
发挥
编写Python代码以计算本自述文件中的单词数。
使用Git将代码提交到unit2目录中，并推送到您的存储库。还可以通过代码链接评论该问题。
参考
肯尼斯·鲁宾（Kenneth S. Rubin），《基本Scrum：最流行的敏捷过程实用指南》，2012年
Eric Matthes，Python速成班，第二版：动手实践，基于项目的编程简介（第二版），2019年
Mark Pilgrim，《深度Python 3》，2009年
笔记
也可以在bilibili.com上找到相同的视频集。
建议没有计算机的学生阅读直到“ Dive Into Python 3”的第7章，该章可从https://diveintopython3.problemsolving.io或以下地址的第1、2、3、4、5、9节在线获取官方Python教程https://docs.python.org/3/tutorial/。
这个单元不需要学生组队。"     #输入文本
word=word.replace(',','').replace('.','')
word=word.split()
print(word)
x=0
setword=set(word)
for i in setword:
    count=word.count(i)
    x=count+x
print("单词数为：")
print(x)

