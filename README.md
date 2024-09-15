# README

## What is this repo for?

> 本仓库只是公布[GUAT](https://www.guat.edu.cn/)某个课程（仓库名写了）的习题软件答案，这些答案由本人逆向得到，不过由于获得的内容全部为特殊的资源格式，只能将其导出为图像，并通过ImageDraw方法直接绘制答案上去。

## 如何使用

> 克隆本项目或直接[下载](https://github.com/teriyakisushi/GUAT_DM_ANSWER/releases/)已经分好类的答案图像文件，按你所需要的章节查看题目图像即可，答案已经绘制在图像上。

有效利用: 可以使用OCR识别生成文本并存储起来，与本仓库的 `ans.json`联动，构建题库。


## 逆向过程

反编译其apk发现核心就只有一个flash的swf文件（🤣），再将其反编译。
用资源管理器发现题目居然都是类似图像的资源（居然多达3000个），发现其ClassSymbol 存储的 资源列表id `UI16_id` 指向了可疑的 `pid` ，通过从主文件 `MainTimeline` 中找到的有关`pid`的疑似答案（源代码是用0, 1表示的）与实际题目答案对比，确认其就是题目的id和答案！

`child_id` 与 `pid` 的关系:

```python
# e.g. child_id: 9 -> pid: 3000
def child_id_to_pid(child_id):
    a = -1 / 3
    b = 3003
    return round(a * child_id + b)
```

该软件题库总计有3000道题，实际有效题目为 998 道 (可能更少)，其余的只是打乱了选项的重复题型。

## 仓库文件说明

- `ans_imgs`: 答案图片存储的文件夹
  - 目录下已经对各章节的题目进行分类，并去除 
  - 图像命名格式为 `tid_{tid}_{episode}.png`，例如 `tid_1_A1.png`

- `ans.json` : 答案存储文件，格式为:`{"tid", "episode", "ans"}`
  - `tid`: 题目的id
  - `episode`: 题目的章节, A1-F2 
  - `ans`: 该题的答案，多选为多个字母的列表

- `src_imgs`: 从swf文件中提取的资源图像
  - 由于数量过多就不上传到仓库啦，我会很快上传到OSS并更新Link的喵

- `*.py`: - 脚本文件，供参考(通过了超级完美的Flake8检查鸭🤤！！！)
