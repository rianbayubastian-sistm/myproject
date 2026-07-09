# Knowledge

## Module Name

Knowledge

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul Knowledge menjadi pusat penyimpanan seluruh pengetahuan sistem. Modul ini mengelola World, Camera, Lighting, Material, Weather, Boundary, Motion, Grammar, Vocabulary, Architecture, dan Decoration agar seluruh modul menggunakan sumber data yang konsisten.

Pada MVP, Knowledge disimpan sebagai file JSON dan dapat diedit melalui UI sederhana.

## Purpose

Menjadi source of truth untuk semua istilah, rule, kategori, dan prompt terms yang dipakai VGOS.

## Responsibilities

- Menampilkan library knowledge.
- Menambah item knowledge dasar.
- Mengedit JSON knowledge.
- Menghapus item terakhir pada MVP.
- Menjaga struktur knowledge tetap terbaca engine.

## Scope

- JSON Knowledge Library.
- CRUD dasar.
- Manual editing.
- Source of truth lokal.

## Out of Scope

- Tidak melakukan approval workflow penuh.
- Tidak otomatis menerima hasil Research.
- Tidak membuat version control lengkap pada MVP.
- Tidak melakukan embedding/vector search.

## Input

- JSON knowledge.
- Manual edit user.
- Item baru.

## Process

```text
Select Library
↓
Load JSON
↓
Render Editable Data
↓
Validate JSON Syntax
↓
Save Knowledge
```

## Output

- Updated JSON file.
- Knowledge item list.
- Save status.

## Dependencies

- Storage Engine.
- Analyze.
- Scene Editor.
- Compiler.

## Data Structure

```json
{
  "id": "warm_tungsten",
  "label": "Warm Tungsten",
  "keywords": ["warm", "lamp", "tungsten"],
  "prompt_terms": ["warm interior tungsten illumination"]
}
```

## Functions

- `render()`
- `load_knowledge()`
- `write_json()`

## Validation Rules

- JSON harus valid sebelum disimpan.
- Knowledge module harus berupa list atau struktur yang disetujui.
- Item idealnya memiliki `id`, `label`, `keywords`, dan `prompt_terms`.

## Error Handling

- JSON invalid tidak disimpan.
- Missing file menghasilkan list kosong.

## Performance Notes

- JSON cukup untuk MVP.
- Jika library besar, perlu indexing pada milestone berikutnya.

## UI Components

- Library selector.
- JSON editor.
- Tambah button.
- Edit / Save button.
- Delete Last button.
- Version placeholder.

## Configuration

- Knowledge folder: `knowledge/`.
- Module list berada di `ui/knowledge.py`.

## Test Cases

- Buka setiap library.
- Tambah item.
- Simpan JSON valid.
- Coba simpan JSON invalid dan pastikan error muncul.

## Future Improvements

- Item-level editor.
- Version history.
- Approval flow dari Research.
- Knowledge import/export.

## Next Module

Scene Editor

