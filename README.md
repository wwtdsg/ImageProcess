ImageProcess
============

ImageProcessHomework  
2014/12/23:  
      今天做完了均值平滑和K个邻点平均法的作业，这是图像增强中常用到的平滑技术，可以消除噪声，但是对细节有损害。在用Python写程序的过程中，遇到了如下问题：  
      1.矩阵的创建。一开始以为是二维数组，但后来发现数组其实是一种列表，但矩阵不是。Python内建函数没有可以直接生成矩阵的，不过幸好有numpy这个模块可以帮助我们生成矩阵  
      2.空列表的创建。这是一个愚蠢的错误。我创建空列表后竟然尝试直接对列表元素赋值，显示，失败了，因为在空列表中元素个数为零，想要往空列表中添加元素应该使用append方法。我最初的目的是想要建立一个元素值为None的列表，那么就应该用[]*n来创建一个具有n个元素的列表。  
      3.数据类型错误。因为以前没有用过numpy模块，所以不知道numpy创建的实例和Python标准模块中的实例有所不同，numpy里面数据类型需要指定，否则会出现溢出。解决这个问题花了我很多时间，一开始我以为是abs函数出了错，于是修改了代码重写了一个实现绝对值的函数，可问题依然存在，原来是数据类型未定义，导致数据溢出。这里我也犯了一个愚蠢的错误，没有认真查看报错情况，对异常的处理不够细致，忽略了warning，导致排错花了很长时间。 
