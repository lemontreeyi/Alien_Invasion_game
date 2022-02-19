# Alien_Invasion_game
A basic project training
---
## Brief Introduction
    本项目以面向对象为主体，将游戏中的ship，aliens，bullet三个主要游戏要素封装到三个文件中，同时创建Settings类方便后期修改游戏的设置选项，有利于迭代。游戏本体也是封装在一个类中，并且在编写期间通过多次重构，让代码结构更加简单易懂
    主要利用了python提供的pygame模块，以及其中的Sprite类，通过继承Sprite类，让游戏对象之间的大部分操作都可以通过库函数实现
    
## 图像处理
主要利用opencv的resize函数压缩分辨率，导致图像有些模糊

## 运行
```bash
cd Alien_Invasion_game
python alien_invasion.py
```
