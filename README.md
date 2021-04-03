![auto-info-collector](https://socialify.git.ci/beiyuouo/auto-info-collector/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F44976445%3Fs%3D460%26u%3D182d335f502ab38522bde613717bd77aa1f6f766%26v%3D4&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light)

# :wave: auto-info-collector

自动化打卡截图上传收集

# How to use

```sh
pip install -r requirement.txt
python main.py
```

# Changelog

<details>
    <summary>点击查看更多</summary>

## v_1.3.1_alpha
- 新增两个接口，可以查看打卡统计情况

> Usage: `query_table[?group=x]`获取table数据json形式
> Usage: `show_table[?group=x]`展示数据统计情况


## v_1.2.1_alpha
- 添加的下载文件功能，使用方法为`GET`或`POST`访问`{host}/download[?group=x]`，`[]`内为可选参数若为空，则下载全部打包文件

## v_1.1.2_alpha
- 修复了一个bug，该bug曾让日期框始终为运行日期

## v_1.1.1_alpha

- 修复了一个bug，该bug曾让非第一组成员无法正常提交

## v_1.1.0_alpha

- 读入database中名单，处理学生信息
- 提供`nama`接口供Ajax调用
- 利用Ajax和JQuery修改下拉框名单

## v_1.0.0

- 完成小组打卡收集需求


</details>

# TODO
- [x] 提供图片外网访问接口
- [x] 打包下载图片
- [ ] 前端/后端拼接图片，减少图片占用空间
- [ ] 可视化数据统计
- [ ] 网站日志分析
- [ ] 优化性能，减少重复打包、创建操作
- [ ] 界面美化
- [ ] 操作异步处理

# Welcome

Contribution is welcome!
