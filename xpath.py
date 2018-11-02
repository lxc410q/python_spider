from lxml import  etree
text= '''
<div>
    <ul>
        <li class="red"><h1>red flowers</h1></li>
        <li class="yellow"><h2>yellow flowers</h2></li>
        <li class="blue"><h3>blue flowers</h3></li>
        <li class="block"><h4>block flowers</h4></li>
        <li class="pick"><h5>pick flowers</h5>
    </ul>
</div>
'''
html=etree.HTML(text)
result=etree.tostring(html)
print(result)