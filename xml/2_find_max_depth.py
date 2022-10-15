import xml.etree.ElementTree as etree


maxdepth = 0


def depth(elem: etree.Element, level: int):
    global maxdepth
    currentDepth = level + 1
    maxdepth = max(maxdepth, currentDepth)
    for child in elem:
        depth(child, currentDepth)


standard_input = """6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>"""

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
