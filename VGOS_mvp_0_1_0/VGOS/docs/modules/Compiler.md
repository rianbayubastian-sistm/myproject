# Compiler

## Module Name

Compiler

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul Compiler mengubah Knowledge dan scene yang telah divalidasi menjadi output sesuai target AI, seperti prompt, negative prompt, JSON, Python, atau payload API. Pada MVP 0.1.0, Compiler menghasilkan prompt teks dan negative prompt dasar.

Compiler tidak mengubah makna visual yang telah ditetapkan pada tahap Analyze dan Scene Editor.

## Purpose

Menghasilkan output siap pakai dari struktur scene tanpa kehilangan intent visual.

## Responsibilities

- Membaca structured scene.
- Menormalisasi field scene.
- Mengurutkan section prompt.
- Membuat prompt final.
- Membuat negative prompt default.
- Menyertakan metadata output.

## Scope

- Prompt text compiler.
- Negative prompt default.
- MP4/GIF metadata dasar.
- Versioned output.

## Out of Scope

- Tidak memanggil API generator.
- Tidak membuat video.
- Tidak melakukan QC hasil visual.
- Tidak mengubah Knowledge Library.

## Input

- Scene Object.
- Negative prompt optional.
- Format output optional.
- Duration optional.

## Process

```text
Receive Scene Object
↓
Normalize Scene Fields
↓
Order Prompt Sections
↓
Build Prompt Text
↓
Attach Negative Prompt
↓
Return Compiled Object
```

## Output

- Prompt.
- Negative Prompt.
- Format.
- Duration.
- Version.

## Dependencies

- Normalizer.
- Scene Editor.
- Knowledge Library.

## Data Structure

```json
{
  "prompt": "Scene: ... Camera: ...",
  "negative_prompt": "no camera movement, no morphing",
  "format": "MP4",
  "duration_seconds": 5,
  "version": "0.1.0"
}
```

## Functions

- `compile_prompt()`
- `normalize_scene()`
- `normalize_prompt_text()`

## Validation Rules

- Prompt boleh kosong hanya jika scene kosong.
- Negative prompt harus selalu tersedia.
- Version harus disertakan.

## Error Handling

- Missing optional field dilewati.
- Non-string field dinormalisasi secara aman.

## Performance Notes

- Compiler harus deterministic.
- Input yang sama harus menghasilkan output yang sama.

## UI Components

- Compile button di Scene Editor.
- Prompt output text area.
- Negative prompt output text area.

## Configuration

- Section order berada di `engine/compiler.py`.
- Default negative prompt berada di `engine/compiler.py`.

## Test Cases

- Compile scene lengkap.
- Compile scene sebagian.
- Compile dengan negative prompt custom.

## Future Improvements

- Multi-target compiler.
- API payload compiler.
- JSON schema compiler.
- Platform-specific prompt profiles.

## Next Module

QC

