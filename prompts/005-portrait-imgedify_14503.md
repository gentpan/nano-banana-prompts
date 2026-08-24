---
id: imgedify_14503
category: portrait
style: realistic
tags: ["blonde woman", "outdoor cafe", "striped sweater", "cinematic lighting", "photorealistic"]
source: ImgEdify/awesome-nano-banana-pro-prompts
license: MIT
---

# GPT Image 2 (left) vs Nano Banana 2 (right)  Prompt: {   "meta": {     "image_quality": "Very High",

## 中文

**人像摄影 - 详细型提示词**

这是一个关于 灯光 的 Gemini 图像生成提示词。

**关键特征：**
- 提示词长度：约 10026 字符
- 风格分类：人像摄影
- 标签：blonde woman, outdoor cafe, striped sweater, cinematic lighting, photorealistic

**使用说明：**
这个提示词设计用于 Google Gemini 的图像生成功能（Nano Banana），可以直接复制使用或根据需求调整参数。

---

*完整英文提示词见下方。*

## English

{
  "meta": {
    "image_quality": "Very High",
    "image_type": "Photo",
    "file_characteristics": {
      "compression_artifacts": "Low",
      "noise_level": "None",
      "lens_type_estimation": "Standard prime, approximately 35mm-50mm equivalent"
    }
  },
  "global_context": {
    "scene_description": "A medium shot of a young woman with blonde hair sitting at an outdoor cafe table. She is resting her chin on her right hand, wearing dark oversized sunglasses and a black-and-white horizontally striped knit sweater over a white collared shirt. On the wooden table in front of her sits a black ceramic cup of coffee with latte art. Behind her is a dark-framed glass storefront reflecting the street and interior cafe lights. The atmosphere is urban, chic, and serene.",
    "environment_type": "Outdoor",
    "time_of_day": "Day",
    "weather_atmosphere": "Serene",
    "lighting": {
      "source": "Natural daylight with ambient interior reflections",
      "direction": "Front-left",
      "quality": "Soft/Diffused",
      "color_temperature": "Neutral (approx. 5500K)"
    },
    "color_palette": {
      "dominant_hex_estimates": [
        "#000000",
        "#FFFFFF",
        "#D2B48C",
        "#2B2B2B"
      ],
      "accent_colors": [
        "#C19A6B",
        "#8B4513"
      ],
      "contrast_level": "High"
    }
  },
  "composition": {
    "camera_angle": "Eye-level",
    "framing": "Medium shot",
    "depth_of_field": "Shallow",
    "focal_point": "The woman's face and sunglasses",
    "symmetry_type": "None",
    "rule_of_thirds_alignment": "Subject is centered; coffee cup aligns with the bottom horizontal third"
  },
  "objects": [
    {
      "id": "obj_001",
      "label": "Young Woman",
      "category": "Person",
      "location": {
        "relative_position": "Center",
        "bounding_box_percentage": {
          "x": 10.0,
          "y": 20.0,
          "width": 80.0,
          "height": 80.0
        }
      },
      "dimensions_relative": "Large",
      "distance_from_camera": "Near",
      "pose_orientation": "Facing forward, slight head tilt to her left, right hand under chin, left hand near coffee cup",
      "material": "Skin/Hair",
      "surface_properties": {
        "texture": "Smooth skin, wavy hair",
        "reflectivity": "Low",
        "micro_details": "Subtle makeup, peach-toned lipstick, manicured nails",
        "wear_state": "Pristine"
      },
      "color_details": {
        "base_color_hex": "#F5D0C1",
        "secondary_colors": [
          "#E5BE9E"
        ],
        "gradient_or_pattern": "Natural skin tones"
      },
      "interaction_with_light": {
        "shadow_casting": "Soft shadow under chin and nose",
        "highlight_zones": "Forehead, bridge of nose, cheekbones",
        "translucency": "Low"
      },
      "text_content": null,
      "relationships": [
        {
          "type": "sitting_at",
          "target_object_id": "obj_005"
        },
        {
          "type": "wearing",
          "target_object_id": "obj_002"
        },
        {
          "type": "wearing",
          "target_object_id": "obj_003"
        }
      ]
    },
    {
      "id": "obj_002",
      "label": "Striped Sweater",
      "category": "Clothing",
      "location": {
        "relative_position": "Center-bottom",
        "bounding_box_percentage": {
          "x": 8.0,
          "y": 45.0,
          "width": 75.0,
          "height": 45.0
        }
      },
      "dimensions_relative": "Large",
      "distance_from_camera": "Near",
      "pose_orientation": "Fitted to torso",
      "material": "Fabric/Knit",
      "surface_properties": {
        "texture": "Ribbed knit",
        "reflectivity": "None",
        "micro_details": "Horizontal black and white stripes, thick knit texture",
        "wear_state": "New"
      },
      "color_details": {
        "base_color_hex": "#000000",
        "secondary_colors": [
          "#FFFFFF"
        ],
        "gradient_or_pattern": "Even horizontal stripes"
      },
      "interaction_with_light": {
        "shadow_casting": "Soft shadows in the knit grooves",
        "highlight_zones": "Shoulders",
        "translucency": "None"
      },
      "relationships": [
        {
          "type": "layered_over",
          "target_object_id": "obj_004"
        }
      ]
    },
    {
      "id": "obj_003",
      "label": "Sunglasses",
      "category": "Accessory",
      "location": {
        "relative_position": "Center-top",
        "bounding_box_percentage": {
          "x": 37.0,
          "y": 30.0,
          "width": 25.0,
          "height": 10.0
        }
      },
      "dimensions_relative": "Small",
      "distance_from_camera": "Near",
      "pose_orientation": "Worn on face",
      "material": "Plastic/Acetate",
      "surface_properties": {
        "texture": "Smooth/Glossy",
        "reflectivity": "High",
        "micro_details": "Slight gold or silver hinge detail",
        "wear_state": "New"
      },
      "color_details": {
        "base_color_hex": "#1A1A1A",
        "secondary_colors": [],
        "gradient_or_pattern": "Solid"
      },
      "interaction_with_light": {
        "shadow_casting": "Small shadow on bridge of nose",
        "highlight_zones": "Upper edges of frames",
        "translucency": "None"
      }
    },
    {
      "id": "obj_004",
      "label": "White Collared Shirt",
      "category": "Clothing",
      "location": {
        "relative_position": "Center-neckline",
        "bounding_box_percentage": {
          "x": 48.0,
          "y": 50.0,
          "width": 10.0,
          "height": 5.0
        }
      },
      "dimensions_relative": "Small",
      "distance_from_camera": "Near",
      "pose_orientation": "Under sweater",
      "material": "Cotton/Fabric",
      "surface_properties": {
        "texture": "Smooth",
        "reflectivity": "None",
        "micro_details": "Sharp pointed collar",
        "wear_state": "Pristine"
      },
      "color_details": {
        "base_color_hex": "#FFFFFF",
        "secondary_colors": [],
        "gradient_or_pattern": "Solid"
      }
    },
    {
      "id": "obj_005",
      "label": "Wooden Table",
      "category": "Furniture",
      "location": {
        "relative_position": "Bottom-center",
        "bounding_box_percentage": {
          "x": 30.0,
          "y": 85.0,
          "width": 50.0,
          "height": 15.0
        }
      },
      "dimensions_relative": "Medium",
      "distance_from_camera": "Near",
      "pose_orientation": "Horizontal plane",
      "material": "Wood",
      "surface_properties": {
        "texture": "Grainy",
        "reflectivity": "Low",
        "micro_details": "Natural wood grain lines",
        "wear_state": "Used"
      },
      "color_details": {
        "base_color_hex": "#D2B48C",
        "secondary_colors": [
          "#8B4513"
        ],
        "gradient_or_pattern": "Wood grain"
      }
    },
    {
      "id": "obj_006",
      "label": "Coffee Cup",
      "category": "Kitchenware",
      "location": {
        "relative_position": "Bottom-center",
        "bounding_box_percentage": {
          "x": 31.0,
          "y": 85.0,
          "width": 18.0,
          "height": 15.0
        }
      },
      "dimensions_relative": "Small",
      "distance_from_camera": "Near",
      "pose_orientation": "Upright",
      "material": "Ceramic",
      "surface_properties": {
        "texture": "Matte/Smooth",
        "reflectivity": "Low",
        "micro_details": "White foam art on top of liquid",
        "wear_state": "Clean"
      },
      "color_details": {
        "base_color_hex": "#000000",
        "secondary_colors": [
          "#C19A6B",
          "#FFFFFF"
        ],
        "gradient_or_pattern": "Solid exterior with foam pattern inside"
      },
      "text_content": {
        "raw_text": "kern.",
        "font_style": "Cursive/Handwritten",
        "font_weight": "Regular",
        "text_case": "Lowercase",
        "alignment": "Center",
        "color_hex": "#FFFFFF"
      },
      "relationships": [
        {
          "type": "resting_on",
          "target_object_id": "obj_005"
        }
      ]
    },
    {
      "id": "obj_007",
      "label": "Cafe Window",
      "category": "Structure",
      "location": {
        "relative_position": "Background",
        "bounding_box_percentage": {
          "x": 0.0,
          "y": 0.0,
          "width": 100.0,
          "height": 80.0
        }
      },
      "dimensions_relative": "Large",
      "distance_from_camera": "Mid",
      "pose_orientation": "Vertical",
      "material": "Glass/Metal",
      "surface_properties": {
        "texture": "Smooth/Reflective",
        "reflectivity": "High",
        "micro_details": "Black metal frames, star-shaped light decoration in top right, reflected street lights",
        "wear_state": "Clean"
      },
      "color_details": {
        "base_color_hex": "#000000",
        "secondary_colors": [
          "#2F2F2F"
        ],
        "gradient_or_pattern": "Complex reflections"
      }
    }
  ],
  "background_details": {
    "texture": "Reflective glass and dark metal frame",
    "patterns": "Reflected bokeh lights and architectural lines",
    "lighting_behavior": "Specular highlights from interior lights and sky",
    "additional_elements": [
      "Star-shaped decorative light",
      "Reflected human figures",
      "Warm interior glow"
    ]
  },
  "foreground_elements": {
    "particles": "None",
    "artifacts": "Slight bokeh in the background reflections"
  },
  "reconstruction_notes": {
    "mandatory_elements_for_recreation": "Black and white horizontal striped sweater, oversized black sunglasses, blonde wavy hair, coffee cup with 'kern.' logo, outdoor cafe setting",
    "sensitivity_factors": "The contrast between the black and white stripes and the warm wood of the table; the specific cursive typography on the cup",
    "ambiguities": "The exact contents of the reflection in the window; the specific brand of the sunglasses"
  }
}

---

**整理：** Yep（[gentpan](https://github.com/gentpan)）  
**来源：** [ImgEdify/awesome-nano-banana-pro-prompts](https://x.com/rovvmut_/status/2046618453562609975)  
**许可：** MIT
