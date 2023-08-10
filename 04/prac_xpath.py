from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有节点
result = html.xpath('//*')
print(result)
# 获取所有li节点
result = html.xpath('//li')
print(result)
# 获取所有li下一级的a节点
result = html.xpath('//li/a')
print(result)
# 父节点
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
# 属性匹配
result = html.xpath('//li[@class="item-0"]')
print(result)

# 提取文本 提取li自身的文本
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
# 提取文本 提取li直接子节点的文本
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# ```这里我们通过 @href 即可获取节点的 href 属性。注意，此处和属性匹配的方法不同，属性匹配是中括号加属性名和值来限定某个属性，如 [@href="link1.html"]，而此处的 @href 指的是获取节点的某个属性，二者需要做好区分。运行结果如下：```
result = html.xpath('//li/a/@href')
print(result)

# 属性多值匹配
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
