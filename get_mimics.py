import xml.etree.ElementTree as ET

tree = ET.parse('/home/r/Downloads/pnd_models/adam_pro_hand/adam_pro.urdf')
root = tree.getroot()
for joint in root.findall('joint'):
    mimic = joint.find('mimic')
    if mimic is not None:
        print(f"Joint: {joint.attrib['name']} -> Mimic: {mimic.attrib['joint']}, mult: {mimic.attrib.get('multiplier', '1')}")
