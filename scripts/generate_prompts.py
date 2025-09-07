import json
from pathlib import Path
import argparse
import random
import re

ROOT = Path(__file__).resolve().parents[1]
PROMPT_FILE = ROOT / "prompt.json"

CATEGORIES = {
    "outdoor_landscapes": [
        "alpine_lake_shore", "misty_pine_forest", "desert_dune_ridge", "lavender_field_dawn",
        "rice_terrace_overlook", "tropical_lagoon_boardwalk", "cliff_edge_ocean_spray", "mangrove_shallows",
        "snowfield_blue_hour", "countryside_orchard_blossom"
    ],
    "studio_materials": [
        "polished_concrete_pedestal", "brushed_metal_plane", "sandstone_arch_forms", "translucent_acrylic_blocks",
        "frosted_glass_wall", "satin_fabric_drape", "raw_wooden_plinth", "ceramic_tile_grid",
        "soft_felt_stage", "matte_cardstock_layers"
    ],
    "architecture_spaces": [
        "minimal_gallery_niche", "sunlit_atrium_stairs", "arcade_columns_shadow", "skylight_beam_room",
        "brutalist_corner_light", "courtyard_reflecting_pool", "modernist_balcony", "arched_window_bay",
        "terracotta_loggia", "tea_house_engawa"
    ],
    "motion_energy": [
        "silk_ribbon_swoop", "powder_burst_pastel", "water_arc_crown", "petal_swirl_vortex",
        "mist_stream_backlit", "lensflare_sweep", "sparkle_dust_trail", "bokeh_light_rain",
        "paper_confetti_float", "shadow_pan_parallax"
    ],
    "macro_textures": [
        "dew_kissed_leaf", "rose_petals_close", "citrus_peel_macro", "eucalyptus_vein_detail",
        "marble_vein_close", "soap泡_microfoam", "mica_glitter_sheen", "linen_weave_soft",
        "honeycomb_glow", "ice_crystal_lattice"
    ],
    "seasons_times": [
        "spring_blossom_breeze", "summer_noon_glare", "autumn_warm_foliage", "winter_crisp_light",
        "golden_hour_glow", "blue_hour_serenity", "overcast_softbox", "sunrise_hazy_aura",
        "twilight_ambience", "night_candlelit"
    ],
    "editorial_graphic": [
        "gridline_modern_layout", "negative_space_balanced", "color_block_triad", "diagonal_split_stage",
        "shadow_gobo_palm", "halftone_overlay_subtle", "prism_rainbow_trim", "paper_cut_collage",
        "foil_stamp_hint", "type_field_placeholder"
    ],
    "retail_display": [
        "window_boutique_glow", "endcap_symmetric", "island_table_arrangement", "lightbox_glass_reflection",
        "podium_tiered_steps", "pedestal_ring_light", "backlit_shelf_array", "rotating_turntable",
        "poster_wall_backdrop", "floor_decal_focus"
    ],
}

# Template sentence pieces for product-only prompts
INTROS = [
    "Product-only hero shot:",
    "Premium campaign visual:",
    "Flagship advertisement look:",
    "High-end cosmetic showcase:",
    "Editorial beauty hero:" ,
]

FOREGROUNDS = [
    "Place the pink skincare bottle upright with label perfectly sharp",
    "Set the pink pump bottle slightly angled, label clean and legible",
    "Center the pink bottle, pump facing forward with pristine label",
    "Position the product hero with elegant stance and crisp label",
]

LIGHTING = [
    "soft directional key and gentle fill",
    "balanced softbox lighting with subtle rim",
    "natural window-style light with refined highlights",
    "low-key cinematic contrast and controlled speculars",
    "bright airy exposure with clean shadows",
]

BACKDROPS = [
    "clean gradient backdrop",
    "soft off-white seamless",
    "muted pastel environment",
    "charcoal-to-ink vignette",
    "sunlit ambience with tasteful bokeh",
]

EXTRAS = [
    "razor detail and premium color accuracy",
    "magazine-ready composition and true-to-color finish",
    "luxury brand language with immaculate edges",
    "campaign-grade sharpness and elegant negative space",
    "refined reflections and subtle texture cues",
]


def load_prompts(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    prompts = data.get("prompts", [])
    return data, prompts


def slugify(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9_\-]", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.lower().strip("_")


def generate_one_name(cat: str, motif: str, idx: int, existing_names: set[str]) -> str:
    base = f"ultra_{cat}_{motif}_{idx:02d}"
    slug = slugify(base)
    # Ensure uniqueness
    attempt = 1
    unique = slug
    while unique in existing_names:
        attempt += 1
        unique = f"{slug}_{attempt}"
    return unique


def generate_text(cat: str, motif: str) -> str:
    intro = random.choice(INTROS)
    fg = random.choice(FOREGROUNDS)
    light = random.choice(LIGHTING)
    bg = random.choice(BACKDROPS)
    extra = random.choice(EXTRAS)
    return (
        f"{intro} {fg}. Scene theme: {cat.replace('_',' ')} — {motif.replace('_',' ')}. "
        f"Use {light}, {bg}, {extra}. Maintain a clean, modern luxury cosmetic aesthetic; the product remains the clear focal point."
    )


def main():
    parser = argparse.ArgumentParser(description="Generate additional unique prompts to reach a target total.")
    parser.add_argument("--prompt_file", type=str, default=str(PROMPT_FILE))
    parser.add_argument("--target_total", type=int, default=500, help="Desired total number of prompts after generation.")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)

    path = Path(args.prompt_file)
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")

    data, prompts = load_prompts(path)
    existing_names = {p.get("name", "") for p in prompts}

    current = len(prompts)
    to_add = max(0, args.target_total - current)
    if to_add == 0:
        print(f"Already at target ({current}). No prompts added.")
        return

    print(f"Current prompts: {current}. Adding: {to_add} to reach {args.target_total}.")

    new_entries = []
    cats = list(CATEGORIES.items())
    cat_len = sum(len(v) for v in CATEGORIES.values())

    # Round-robin through categories/motifs to build diverse set
    idx = 0
    while len(new_entries) < to_add:
        cat_name, motifs = cats[idx % len(cats)]
        motif = motifs[(idx // len(cats)) % len(motifs)]
        name = generate_one_name(cat_name, motif, idx, existing_names)
        text = generate_text(cat_name, motif)
        new_entries.append({"name": name, "text": text})
        existing_names.add(name)
        idx += 1

    prompts.extend(new_entries)
    data["prompts"] = prompts

    # Write back
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Added {len(new_entries)} prompts. New total: {len(prompts)}")


if __name__ == "__main__":
    main()
