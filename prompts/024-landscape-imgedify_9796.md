---
id: imgedify_9796
category: landscape
style: 3d
tags: ["steampunk", "diorama", "miniature", "procedural generation", "isometric"]
source: ImgEdify/awesome-nano-banana-pro-prompts
license: MIT
---

# A whimsical diorama of a steampunk scene generated using Nano banana 2 with t...

## 中文

**专业图像生成提示词（详细型）**

这是用于 Google Gemini 图像生成的提示词，长度约 9646 字符。

*完整英文提示词见下方。*

## English

VARIABLE GUIDE
GLOBAL_COMPLEXITY = Possible values: 'low','medium','high','ultra'. Controls density of buildings, props, characters, and environmental detail. If blank choose randomly between 'medium' and 'high'.
PUNK_STYLE = 
If PUNK_STYLE is empty, then one style is randomly selected from LIST_OF_PUNK_STYLES, otherwise what is in the PUNK_STYLE variable is chosen
LIST_OF_PUNK_STYLES = Steampunk, Dieselpunk, Atompunk, Cyberpunk, Biopunk, Nanopunk, Solarpunk, Decopunk, Clockpunk, Coalpunk, Raypunk, Stonepunk, Sailpunk, Cassettepunk, Teslapunk, Mythpunk, Sandalpunk, Oceanpunk, Frostpunk, Junglepunk, Desertpunk, Gothicpunk, Ironpunk, Crystalpunk, Rustpunk, Vaporwavepunk, Neonpunk, Skypunk, Aquapunk, Arborpunk, Astropunk, QuantumPunk, Mechanopunk, Technopunk, Retrocomputingpunk, Cattlepunk, Hopepunk
SUBSTYLE = If specified use exactly. If set to none disable. If blank infer logically from PUNK_STYLE.
TECHNOLOGY_LEVEL = If specified use exactly. If set to none disable. If blank infer from PUNK_STYLE.
ENVIRONMENT = If specified use exactly. If set to none disable. If blank infer logically from active layers.
CULTURE = If specified use exactly. If set to none disable. If blank infer culturally appropriate framework.
PROCEDURAL_SCENE_GENERATOR = 'on'
PROCEDURAL_PROP_GENERATOR = 'on'
PROCEDURAL_ARCHITECTURE_GENERATOR = 'on'
PROCEDURAL_LIGHTING_ATMOSPHERE_GENERATOR = 'on'
PROCEDURAL_CHARACTER_POPULATION_GENERATOR = 'on'
PROCEDURAL_DIORAMA_BASE_GENERATOR = 'on'
FOCAL_INTEREST_LAYER = off
MATERIAL_COHESION_LAYER = 'on'
VISUAL_CLARITY_OPTIMIZER = 'on'
MICRO_LIFE_LAYER = 'on'
COMPOSITION_ENGINE = 'on'
EDGE_DEFINITION_LAYER = 'on'
COLOR_HARMONY_LAYER = 'on'
DIORAMA_CRAFTSMANSHIP_LAYER = 'on'

PSG LAYER
Implement only if PROCEDURAL_SCENE_GENERATOR='on'. Generate core scene structure using:
LANDSCAPE_STRUCTURE (floating island, cliff terraces, canyon basin, harbor cove, forest clearing, mountain ridge, giant tree canopy, desert oasis, ice shelf, volcanic ridge)
SETTLEMENT_TYPE (village, harbor town, trading port, monastery complex, research outpost, fortress town, sky dock, industrial district, hidden enclave)
INFRASTRUCTURE_ELEMENTS (bridges, windmills, rail lines, cable lifts, aqueducts, airship docks, solar arrays, reactor towers, waterwheels)
CIVILIAN_ACTIVITY (market trading, fishing, cargo loading, harvesting, machine repair, patrol movement, festival gathering, workshop crafting)
MICRO_NARRATIVE (delivery arrival, festival beginning, storm approaching, caravan arrival, wildlife encounter, machine malfunction, lantern celebration)

PPG LAYER
Implement only if PROCEDURAL_PROP_GENERATOR='on'. Populate the diorama with contextual props derived from world logic and PSG output including:
TOOLS (mechanical tools, farming implements, repair kits, navigation instruments)
MARKET_OBJECTS (crates, cargo barrels, trade goods, produce baskets, supply chests)
WORKSHOP_ITEMS (workbenches, machine parts, gears, coils, circuitry boards, alchemical vessels)
INFRASTRUCTURE_PROPS (pipes, cables, valves, ducts, lanterns, signage, signal lights)
VEHICLES_AND_TRANSPORT (carts, air skiffs, steam wagons, hover sleds, cargo drones, sailing boats depending on PUNK_STYLE)
DECORATIVE_ELEMENTS (banners, flags, statues, murals, street lamps, garden plots, shrine objects)
STREET_DETAIL (stairs, ladders, railings, benches, fences, tool racks, storage piles)

PAG LAYER
Implement only if PROCEDURAL_ARCHITECTURE_GENERATOR='on'. Generate architecture appropriate to the world logic:
BUILDING_TYPES (workshops, homes, warehouses, guild halls, taverns, temples, watchtowers, research labs, market halls)
ROOF_STYLES (domed roofs, tiled roofs, copper plates, glass domes, canvas canopies, wooden shingles, mechanical housings)
STRUCTURAL_FORMS (stacked terraces, narrow towers, courtyard clusters, cliffside supports, elevated platforms, ring structures)
MATERIAL_SYSTEMS (stone blocks, brass panels, iron beams, wood frames, crystal structures, reinforced concrete, bio-organic growth)
ARCHITECTURAL_DETAILS (balconies, gears, antennae, chimneys, pipes, cables, banners, mechanical vents)

PLAG LAYER
Implement only if PROCEDURAL_LIGHTING_ATMOSPHERE_GENERATOR='on'. Generate cinematic lighting and atmospheric conditions:
TIME_OF_DAY (sunrise glow, golden hour, bright midday, sunset haze, blue hour twilight, night illumination)
LIGHT_SOURCE_STYLE (sunlight beams, lantern glow, neon signage, reactor light, forge fire, bioluminescent flora, electrical arcs)
WEATHER_STATE (clear skies, drifting mist, light rain, snowfall, desert dust, ocean spray, storm clouds)
ATMOSPHERIC_EFFECTS (volumetric light rays, fog layers, glowing particles, drifting leaves, steam vents, sparks, embers)
MOOD_TONE (peaceful village life, bustling trade activity, mysterious fog settlement, festival celebration, incoming storm tension)

PCPG LAYER
Implement only if PROCEDURAL_CHARACTER_POPULATION_GENERATOR='on'. Generate population behavior and character diversity:
POPULATION_DENSITY (sparse settlement, small community, busy town center, festival crowd)
OCCUPATION_TYPES (merchants, engineers, mechanics, farmers, sailors, scholars, monks, guards, traders)
CHARACTER_ACTIVITIES (bartering goods, repairing machines, loading cargo, tending gardens, fishing docks, teaching apprentices, celebrating festivals)
CLOTHING_STYLES (punk-style attire reflecting PUNK_STYLE, SUBSTYLE, CULTURE, and TECHNOLOGY_LEVEL)
SOCIAL_INTERACTIONS (conversations, cooperative work, bargaining, storytelling, celebrations, training apprentices)
CREATURE_VARIANTS (pets, livestock, mechanical companions, flying drones, wildlife depending on ENVIRONMENT)

PDBG LAYER
Implement only if PROCEDURAL_DIORAMA_BASE_GENERATOR='on'. Generate the miniature base structure:
BASE_SHAPE (oval island base, circular pedestal base, irregular floating rock, layered terrain slab, ring island, stepped plateau)
CUTAWAY_TERRAIN (visible soil layers, rock strata, root systems, crystal veins, mechanical foundations)
EDGE_STYLE (clean display cut, fractured rock edge, carved museum pedestal, floating stone fragments)
WATER_CROSS_SECTIONS (waterfalls spilling from edges, exposed river channels, subterranean water layers)
GEOLOGICAL_DETAIL (sediment layers, mineral veins, fossil fragments, crystal growth)
FLOATING_ELEMENTS (detached rocks, hovering debris, mechanical levitation supports, root tendrils)

SCENE
Describe a visually rich whimsical environment blending civilization and nature. The environment must clearly read as a handcrafted miniature world containing terrain, architecture, and tiny characters interacting with the environment. Build the scene around LANDSCAPE_STRUCTURE, SETTLEMENT_TYPE, INFRASTRUCTURE_ELEMENTS, CIVILIAN_ACTIVITY, and MICRO_NARRATIVE. Ensure buildings follow generated architectural systems. Populate the settlement with logical props, environmental storytelling details, and tiny inhabitants performing occupations, social interactions, and daily activities. Ensure the terrain base reflects the generated miniature base structure and geological cross-sections.

STYLE
Create a premium whimsical miniature diorama where terrain and structures form a continuous sculpted base. The entire diorama floats freely in mid-air inside a blank single-color background chosen for strong contrast. Adjust density according to GLOBAL_COMPLEXITY. Apply the selected PUNK_STYLE consistently across architecture, clothing, tools, props, vehicles, infrastructure, and materials. SUBSTYLE, TECHNOLOGY_LEVEL, ENVIRONMENT, and CULTURE influence design language and storytelling. Allow natural irregularity in terrain shapes and settlement layout. Maintain clean collectible presentation and lock render to 4:3 aspect ratio.

FOCAL INTEREST LAYER
Implement only if FOCAL_INTEREST_LAYER='on'. Introduce a dominant landmark such as a tower, giant tree, temple complex, reactor core, monumental machine, lighthouse, windmill cluster, or sky dock.

MATERIAL COHESION LAYER
Implement only if MATERIAL_COHESION_LAYER='on'. Ensure terrain and architecture resemble handcrafted miniature materials such as painted resin terrain, sculpted foam rock, textured bases, miniature foliage, and model architecture.

VISUAL CLARITY OPTIMIZER
Implement only if VISUAL_CLARITY_OPTIMIZER='on'. Maintain clear spatial readability between paths, elevation levels, structures, and props.

MICRO LIFE LAYER
Implement only if MICRO_LIFE_LAYER='on'. Add animals, birds, fish, insects, drones, or small mechanical creatures interacting with the environment.

COMPOSITION ENGINE
Implement only if COMPOSITION_ENGINE='on'. Organize settlements using strong spatial patterns such as radial towns, terraced villages, harbor crescents, cliffside tiers, spiral hill settlements, or ring towns.

EDGE DEFINITION LAYER
Implement only if EDGE_DEFINITION_LAYER='on'. Ensure the terrain silhouette reads clearly like a collectible display model.

COLOR HARMONY LAYER
Implement only if COLOR_HARMONY_LAYER='on'. Maintain a cohesive palette appropriate to the world.

DIORAMA CRAFTSMANSHIP LAYER
Implement only if DIORAMA_CRAFTSMANSHIP_LAYER='on'. Emphasize miniature craftsmanship with detailed paint textures and believable materials.

LIGHTING
Follow the generated lighting and atmosphere conditions from the PLAG layer.

CAMERA
Use an isometric camera capturing the entire floating miniature diorama clearly from top to bottom and side to side.

DESCRIPTION PLAQUE
Place an ornate plaque at the top right corner designed in materials matching the world aesthetic.
Heading — scene name in larger lettering.
Description — short world-appropriate description, must include a mention of the punk style.

---

**整理：** Yep（[gentpan](https://github.com/gentpan)）  
**来源：** [ImgEdify/awesome-nano-banana-pro-prompts](https://x.com/artingent/status/2032813176702775604)
