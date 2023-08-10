from pyquery import PyQuery as pq
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# doc = pq(html)
# print(doc('li'))

# doc = pq(url='http://cuiqingcai.com')
# print(doc('title'))

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
# lis = items.children()
# print(type(lis))
# print(lis)
# container = items.parent()
# print(type(container))
# print(container)
# parents = items.parents()
# print(type(parents))
# print(parents)

# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())

# doc = pq(html)
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li, type(li))

# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))
# print(a.text())

# li = doc('.item-0.active')
# print(li)
# print(li.text())
# print(li.html())

# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)

# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)

doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)
# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())