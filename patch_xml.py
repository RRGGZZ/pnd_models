import re

xml_file = '/home/r/Downloads/pnd_models/adam_pro/adam_pro.xml'
with open(xml_file, 'r', encoding='utf-8') as f:
    content = f.read()

passive_joints = [
    "L_thumb_PIP_joint", "L_thumb_DIP_joint",
    "L_index_DIP_joint", "L_middle_DIP_joint",
    "L_ring_DIP_joint", "L_pinky_DIP_joint",
    "R_thumb_PIP_joint", "R_thumb_DIP_joint",
    "R_index_DIP_joint", "R_middle_DIP_joint",
    "R_ring_DIP_joint", "R_pinky_DIP_joint"
]

# 1. Remove the passive actuators
for joint in passive_joints:
    # Match something like: <motor joint="L_thumb_PIP_joint" ... />
    # handling possible spaces and newlines
    pattern = r'[ \t]*<motor[^>]*joint="' + joint + r'"[^>]*/>\n?'
    content = re.sub(pattern, '', content)

# 2. Add equality constraints before <actuator>
equality_block = """  <equality>
    <joint joint1="L_thumb_PIP_joint" joint2="L_thumb_MCP_joint2" polycoef="0 1.6 0 0 0" />
    <joint joint1="L_thumb_DIP_joint" joint2="L_thumb_MCP_joint2" polycoef="0 2.4 0 0 0" />
    <joint joint1="L_index_DIP_joint" joint2="L_index_MCP_joint" polycoef="0 1 0 0 0" />
    <joint joint1="L_middle_DIP_joint" joint2="L_middle_MCP_joint" polycoef="0 1 0 0 0" />
    <joint joint1="L_ring_DIP_joint" joint2="L_ring_MCP_joint" polycoef="0 1 0 0 0" />
    <joint joint1="L_pinky_DIP_joint" joint2="L_pinky_MCP_joint" polycoef="0 1 0 0 0" />
    <joint joint1="R_thumb_PIP_joint" joint2="R_thumb_MCP_joint2" polycoef="0 1.6 0 0 0" />
    <joint joint1="R_thumb_DIP_joint" joint2="R_thumb_MCP_joint2" polycoef="0 2.4 0 0 0" />
    <joint joint1="R_index_DIP_joint" joint2="R_index_MCP_joint" polycoef="0 1 0 0 0" />
    <joint joint1="R_middle_DIP_joint" joint2="R_middle_MCP_joint" polycoef="0 1 0 0 0" />
    <joint joint1="R_ring_DIP_joint" joint2="R_ring_MCP_joint" polycoef="0 1 0 0 0" />
    <joint joint1="R_pinky_DIP_joint" joint2="R_pinky_MCP_joint" polycoef="0 1 0 0 0" />
  </equality>
"""

if "<equality>" not in content:
    content = content.replace("<actuator>", equality_block + "  <actuator>")

with open(xml_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("done xml")
