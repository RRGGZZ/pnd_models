import xml.etree.ElementTree as ET

urdf_file = '/home/r/Downloads/pnd_models/adam_pro/adam_pro.urdf'
tree = ET.parse(urdf_file)
root = tree.getroot()

mimics = {
    "L_thumb_PIP_joint": {"joint": "L_thumb_MCP_joint2", "multiplier": "1.6", "offset": "0"},
    "L_thumb_DIP_joint": {"joint": "L_thumb_MCP_joint2", "multiplier": "2.4", "offset": "0"},
    "L_index_DIP_joint": {"joint": "L_index_MCP_joint", "multiplier": "1", "offset": "0"},
    "L_middle_DIP_joint": {"joint": "L_middle_MCP_joint", "multiplier": "1", "offset": "0"},
    "L_ring_DIP_joint": {"joint": "L_ring_MCP_joint", "multiplier": "1", "offset": "0"},
    "L_pinky_DIP_joint": {"joint": "L_pinky_MCP_joint", "multiplier": "1", "offset": "0"},
    "R_thumb_PIP_joint": {"joint": "R_thumb_MCP_joint2", "multiplier": "1.6", "offset": "0"},
    "R_thumb_DIP_joint": {"joint": "R_thumb_MCP_joint2", "multiplier": "2.4", "offset": "0"},
    "R_index_DIP_joint": {"joint": "R_index_MCP_joint", "multiplier": "1", "offset": "0"},
    "R_middle_DIP_joint": {"joint": "R_middle_MCP_joint", "multiplier": "1", "offset": "0"},
    "R_ring_DIP_joint": {"joint": "R_ring_MCP_joint", "multiplier": "1", "offset": "0"},
    "R_pinky_DIP_joint": {"joint": "R_pinky_MCP_joint", "multiplier": "1", "offset": "0"},
}

for joint in root.findall('joint'):
    name = joint.attrib.get('name')
    if name in mimics:
        # Check if already has mimic
        if joint.find('mimic') is None:
            mimic_element = ET.Element('mimic', mimics[name])
            
            # format properly (rough appending at end, but better to indent)
            mimic_element.tail = '\n  '
            joint.append(mimic_element)

# ET.write strips some formatting but we can use minidom or just write back
tree.write(urdf_file, encoding='utf-8', xml_declaration=True)
print("done urdf")
