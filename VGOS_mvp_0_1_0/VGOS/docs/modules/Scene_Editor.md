# Scene Editor

## Module Name

Scene Editor

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul Scene Editor memberikan kontrol visual kepada pengguna untuk menyusun scene menggunakan parameter terstruktur dari Knowledge Library. User tidak mengedit prompt secara langsung, melainkan mengatur Scene, Camera, Lighting, Weather, Material, Motion, Boundary, Decoration, dan Overlay.

Modul ini menjadi jembatan antara Knowledge hasil Analyze dan Compiler.

## Purpose

Menyediakan ruang editing visual yang terstruktur agar scene dapat disusun konsisten sebelum dikompilasi menjadi prompt atau payload lain.

## Responsibilities

- Menampilkan field scene terstruktur.
- Memuat active project.
- Menyimpan perubahan scene.
- Menjalankan validasi scene.
- Mengirim scene ke Compiler.

## Scope

- Editing parameter scene.
- Preview textual MVP.
- Compile prompt sederhana.
- Penyimpanan scene ke project aktif.

## Out of Scope

- Tidak melakukan freeform prompt editing sebagai workflow utama.
- Tidak menghasilkan gambar atau video.
- Tidak menjalankan AI generation.
- Tidak melakukan QC hasil video.

## Input

- Active project.
- Knowledge Result dari Analyze.
- Manual parameter scene.
- Default scene template.

## Process

```text
Load Active Project
↓
Load Scene Defaults
↓
Render Structured Fields
↓
Validate Scene
↓
Compile
↓
Save Compiled Output
```

## Output

- Structured Scene Object.
- Validation Result.
- Compiled Prompt Object.

## Dependencies

- Projects.
- Knowledge Library.
- Validator.
- Compiler.
- Storage Engine.

## Data Structure

```json
{
  "scene": "Ultra-luxury penthouse",
  "camera": "38 mm eye-level architectural perspective",
  "lighting": "Warm tungsten interior",
  "weather": "Night",
  "material": "Oak, walnut, glass",
  "motion": "Fireplace hero motion",
  "boundary": "Absolute positional stability",
  "decoration": "Tulips, wine, books",
  "overlay": "No text overlay"
}
```

## Functions

- `render()`
- `validate_scene()`
- `compile_prompt()`
- `save_project()`

## Validation Rules

- `scene`, `camera`, `lighting`, `material`, `motion`, dan `boundary` wajib diperiksa.
- Field kosong menghasilkan WARNING, bukan crash.
- Compile boleh dilakukan selama ada data minimal.

## Error Handling

- Jika active project tidak ada, gunakan default scene.
- Jika save project gagal, tampilkan error pada versi berikutnya.

## Performance Notes

- Scene Editor harus responsif.
- Jangan menjalankan proses AI berat di setiap perubahan field.

## UI Components

- Preview area.
- Inspector panel.
- Text areas per parameter.
- Compile button.
- Compiled output area.

## Configuration

- Default scene berada di `ui/scene_editor.py`.
- Validation fields berada di `engine/validator.py`.

## Test Cases

- Buka Scene Editor tanpa project.
- Compile default scene.
- Kosongkan field boundary dan cek WARNING.
- Simpan compiled prompt ke project aktif.

## Future Improvements

- Dropdown berbasis Knowledge Library.
- Parameter presets.
- Visual preview.
- Scene versioning.

## Next Module

Compiler

