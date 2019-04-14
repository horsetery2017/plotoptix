"""
PlotOptiX predefined materials.

Copyright (C) 2019 R&D Team. All Rights Reserved.

Have a look at examples on GitHub: https://github.com/rnd-team-dev/plotoptix.
"""

import os

from plotoptix.enums import RtFormat

__pkg_dir__ = os.path.dirname(__file__)

m_flat = {
      "ClosestHitPrograms": [ "0::path_tracing_materials.ptx::flat_closest_hit" ],
      "AnyHitPrograms": [ "1::path_tracing_materials.ptx::any_hit" ]
    }
"""
Super-fast material, color is not shaded anyhow. Use color components range <0; 1>.
"""

m_eye_normal_cos = {
      "ClosestHitPrograms": [ "0::path_tracing_materials.ptx::cos_closest_hit" ],
      "AnyHitPrograms": [ "1::path_tracing_materials.ptx::any_hit" ]
    }
"""
Fast material, color is shaded by the cos(eye-hit-normal). Use color components range
<0; 1>.
"""

m_diffuse = {
      "ClosestHitPrograms": [ "0::path_tracing_materials.ptx::diffuse_closest_hit" ],
      "AnyHitPrograms": [ "1::path_tracing_materials.ptx::any_hit" ],
      "VarInt": { "material_flags": 2 }
    }
"""
Standard diffuse material. Note it is available by default under the name "diffuse".
Use color components range <0; 1>.
"""

m_mirror = {
      "ClosestHitPrograms": ["0::path_tracing_materials.ptx::reflective_closest_hit"],
      "AnyHitPrograms": ["1::path_tracing_materials.ptx::any_hit"],
      "VarInt": { "material_flags": 6 },
      "VarFloat3": {
        "surface_albedo": {
          "X": 1.0,
          "Y": 1.0,
          "Z": 1.0
        }
      }
}
"""
100% reflective mirror, quite simple to calculate and therefore a fast material. Use
surface_albedo (range <0; 1>) to colorize reflection.
"""

m_metalic = {
      "ClosestHitPrograms": ["0::path_tracing_materials.ptx::reflective_closest_hit"],
      "AnyHitPrograms": ["1::path_tracing_materials.ptx::any_hit"],
      "VarInt": { "material_flags": 6 },
      "VarFloat": {
        "reflectivity_index": 0.95,
        "reflectivity_range": 1.0,
        "refraction_index": 2.5
      },
      "VarFloat3": {
        "surface_albedo": {
          "X": 1.0,
          "Y": 1.0,
          "Z": 1.0
        }
      }
}
"""
Strongly reflective, metalic material. Use surface_albedo (range <0; 1>) to colorize
reflection. Standard color assigned to each primitive is affecting the diffuse contribution
color (range <0; 1>). Reflection to diffuse proportion is set with reflectivity_index
and reflectivity_range (both in range <0; 1>), where:
    - (1, 1) results with a mirror-like appearance
    - (0, 0) results with a diffuse-like appearance
    - intermediate values result with a plastic-like appearance and various gloss profiles. 
"""

m_plastic = {
      "ClosestHitPrograms": ["0::path_tracing_materials.ptx::reflective_closest_hit"],
      "AnyHitPrograms": ["1::path_tracing_materials.ptx::any_hit"],
      "VarInt": { "material_flags": 6 },
      "VarFloat": {
        "reflectivity_index": 0.0,
        "reflectivity_range": 0.8,
        "refraction_index": 2.0
      },
      "VarFloat3": {
        "surface_albedo": {
          "X": 1.0,
          "Y": 1.0,
          "Z": 1.0
        }
      }
}
"""
Combined reflective and diffuse surface. Reflection fraction may be boosted with reflectivity_index
set above 0 (up to 1, resulting with mirror-like appearance) or minimized with a lower than default
reflectivity_range value (down to 0). Higher refraction_index gives a more glossy look.
"""

m_clear_glass = {
      "ClosestHitPrograms": [ "0::path_tracing_materials.ptx::glass_closest_hit" ],
      "AnyHitPrograms": [ "1::path_tracing_materials.ptx::any_hit" ],
      "VarInt": { "material_flags": 12 },
      "VarFloat": {
        "refraction_index": 1.4,
        "radiation_length": 0.0,
        "vol_scattering": 1.0,
        "light_emission": 0.0
      },
      "VarFloat3": {
        "surface_albedo": {
          "X": 1.0,
          "Y": 1.0,
          "Z": 1.0
        }
      }
    }
"""
Glass, with reflection and refraction. Color components meaning is "attenuation length"
and the range is <0; inf>.
"""
