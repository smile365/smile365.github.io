---
title: "用纯文本画流程图"
keywords: ["纯文本画流程图", "Graph-Easy教程", "ASCII字符流程图", "Graph::Easy", "graphviz", "代码注释流程图"]
tags: ["教程", "Graph-Easy", "ASCII流程图"]
description: "Graph::Easy是一款Perl语言工具，能用纯文本ASCII字符快速生成流程图和关系图，支持嵌入代码注释和Markdown文档。"
categories: ["code"]
heading: "用纯文本ASCII字符把流程图画到txt里|Graph-Easy教程"
date: "2020-08-20T06:39:14.076Z"
---
无意中在一个python库中发现如下文本信息

![ascii流程图](https://gitee.com/smile365/blogimg/raw/master/sxy91/1597890929660.png)

瞬间被惊艳到了，竟然用字符作出里一个流程图！！

究竟是什么神仙软件，能纯文本字符画流程图，我太需要这样的工具了。


有时候写代码，一般的注释只能写文字性描述信息，有了纯文本流程图，以后就能把架构设计或者其他需要流程图表示的说明写在代码注释里了。或者还能把这个粘贴到makdown的文档里或者txt文档里，简直不要太方便。

好奇是怎么生成这样的纯文本字符流程图。

通过关键词"文本流程图"、"txt流程图"，"字符流程图"等一番搜索，终于知道了这叫"ascii字符流程图"。

通过[Graph::Easy](http://bloodgate.com/perl/graph/manual/index.html)这个工具即可生成上面的流程图。`Graph::Easy`是一个perl语言实现的软件包，他的功能是"用文本画图像"。

举个栗子：

先在txt里写一段文字如下：

```
[ Bonn ] --> [ Koblenz ] --> [ Frankfurt ] --> [ Dresden ]

[ Koblenz ] --> [ Trier ] { origin: Koblenz; offset: 2, 2; }
  --> [ Frankfurt ]
```

用`Graph::Easy`可以转化成这样的文字
```
+------+     +---------+                   +-----------+     +---------+
| Bonn | --> | Koblenz | ----------------> | Frankfurt | --> | Dresden |
+------+     +---------+                   +-----------+     +---------+
               |                             ^
               |                             |
               |                             |
               |             +-------+       |
               +-----------> | Trier | ------+
                             +-------+
```


简直太方便了。


它怎么实现的呢

主要借助graphviz这个软件包，这是一个提供不同平台的二进制包，安装好以后可给其他任意语言调用，比如python、perl、c等。Graphviz是一个开源的图形可视化软件，通过DOT语言描述节点、边、属性、形状、箭头、颜色等信息，然后Graphviz即可生成图像。

灵活性非常高，[官网](https://graphviz.org/gallery/)有很多通过Graphviz生成图像的例子，简直无所不能。

![enter description here](https://gitee.com/smile365/blogimg/raw/master/sxy91/1597893101723.png)

`Graph::Easy`对`Graphviz`的DOT语言中流程图的部分进行了二次包装，提供了更简单的DSL语言，从此描述一个流程图像码文字一样简单。不用关心图像里面如何布局，箭头颜色、边从哪里画等等复杂的信息。


安装Graph::Easy的步骤如下：

- 首先需要安装 graphviz 软件包，可以在graphviz官网下载；mac用户可以 brew install graphviz；其他linux发行版参考官网。
- 安装perl；mac和linux用户可以略过；一般系统自带，没有的话和windows一起去perl官网查询如何安装; 据说windows下有傻瓜包activeperl；请自行搜索。
- 安装cpan; 这个是perl的软件包管理，类似npm, pip, apt-get; mac下直接在命令行输入 cpan 命令，一路next即可。其他系统参考cpan官网
- 安装Graph::Easy ;这一步就很容易了；在命令行输入cpan进入cpan shell；然后输入 install Graph::Easy即可。
使用

安装完检测是否安装完成
```bash
graph-easy -version
```

如果在mac系统或者linux系统安装失败
```
ERROR: Can't create '/Library/Perl/5.18/Graph'
mkdir /Library/Perl/5.18/Graph: Permission denied at /System/Library/Perl/5.18/ExtUtils/Install.pm line 469.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 at /System/Library/Perl/5.18/Module/Build/Base.pm line 3581.
  SHLOMIF/Graph-Easy-0.76.tar.gz
  ./Build install  -- NOT OK
Failed during this command:
 SHLOMIF/Graph-Easy-0.76.tar.gz               : install NO
```

一般是权限不足，先执行`sudo cpan`,然后执行`install Graph::Easy`即可

使用
```bash
graph-easy <<< '[a] -> [b]'
```

复杂的一般先写在一个txt文件里
```bash
# test.txt
[ Bonn ] --> [ Koblenz ] --> [ Frankfurt ] --> [ Dresden ]

[ Koblenz ] --> [ Trier ] { origin: Koblenz; offset: 2, 2; }
  --> [ Frankfurt ]
```

然后执行 `graph-easy test.txt`



#### Graph::Easy的dsl语法

注释
```
# 用#号注释，#号后面有空格。空格通常没有什么影响，多个空字符会合并成一个，换行的空字符会忽略
# 空格和换行通常没有什么影响，多个空字符会合并成一个，换行的空字符会忽略
```


但是发现`Graph::Easy`对中文排版不太美观，可能开发的时候没用中文做过测试，所以对中文支持的不够完美。

```bash
graph-easy <<< '[ 北京 ] - 火车 -> [ 张家口 ]'
```

输出： 

![Graph::Easy中文不对齐](https://gitee.com/smile365/blogimg/raw/master/sxy91/1597907904459.png)


可以通过如下方式修复。

```bash
# 找到Easy.pm
mdfind -name Easy.pm
# 在1572行前后
vim /Library/Perl/5.18/Graph/Easy.pm
# 修改后如下
sub as_ascii
  {
  # Convert the graph to pretty ASCII art - will return utf-8.
  my $self = shift;

  # select 'ascii' characters

  my $asc = $self->_as_ascii(@_);
  $asc =~ s/(\x{FFFF})//g;
  $asc;
  }
  
# 找到Node.pm
mdfind -name Node.pm
# 在1505行前后
vim /Library/Perl/5.18/Graph/Easy/Node.pm
# 修改后如下
  $label = $self->_un_escape($label) if !$_[0] && $label =~ /\\[EGHNT]/;
  # placeholder for han chars
  $label =~ s/([\x{4E00}-\x{9FFF}])/$1\x{FFFF}/g;

  $label;
  ```
  
修改后发现美观多了。

![Graph::Easy中文支持](https://gitee.com/smile365/blogimg/raw/master/sxy91/1597907921847.png)

`Graph::Easy`支持把文本格式的流程图直接输出为图像格式，比如png。

需要安装Graph::Easy::As_svg  
```bash
sudo cpan
install Graph::Easy::As_svg
```

使用方法
```bash
graph-easy <<< '[c]->[d]' --as_dot | dot -Tpng -o test.png
```

输出png之类的格式不支持中文，有中文会报错，但可以输出svg格式。





参考文档  
- [Graph::Easy的dsl语法](http://bloodgate.com/perl/graph/manual/syntax.html)
- [Graph::Easy文档译文](https://weishu.gitbooks.io/graph-easy-cn/content/)
- [中文支持](https://blog.codingnow.com/2016/12/ascii_graph.html)
