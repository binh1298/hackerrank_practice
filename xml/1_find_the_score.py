import sys
import xml.etree.ElementTree as etree


def get_attr_number(node: etree.Element):
    result = len(node.attrib)
    return result + sum([get_attr_number(child) for child in list(node)])


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
