# Projects

## Module Name

Projects

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul Projects mengelola daftar project visual dalam VGOS. Modul ini memungkinkan user membuat project baru, melihat daftar project, membuka project ke Scene Editor, dan membuat clone project sebagai basis variasi.

Projects menjadi titik awal workflow produksi karena setiap Analyze, Scene Editor, Compile, QC, dan Report idealnya terhubung ke project aktif.

## Purpose

Mengorganisir pekerjaan visual agar semua input, knowledge, scene, prompt, QC, dan report tersimpan dalam unit project yang jelas.

## Responsibilities

- Membuat project baru.
- Menampilkan project list.
- Membuka project aktif.
- Clone project.
- Menyiapkan struktur data project.

## Scope

- Project lokal berbasis JSON.
- Status project dasar.
- Integrasi awal dengan Scene Editor.

## Out of Scope

- Tidak membuat asset management penuh.
- Tidak melakukan archive permanen pada MVP.
- Tidak melakukan sinkronisasi cloud.
- Tidak membuat permission system.

## Input

- Project name.
- Project description.
- Existing project file.

## Process

```text
Receive Project Metadata
↓
Generate Project ID
↓
Create Project Object
↓
Save JSON
↓
Set Active Project
↓
Open Scene Editor
```

## Output

- Project JSON.
- Active project state.
- Project list UI.

## Dependencies

- Storage Engine.
- Scene Editor.
- Project folder.

## Data Structure

```json
{
  "id": "beach_cafe_rain",
  "name": "Beach Cafe Rain",
  "description": "Luxury rainy beach cafe cinemagraph.",
  "status": "Draft",
  "scene": {},
  "analysis": {},
  "compiled": {}
}
```

## Functions

- `render()`
- `save_project()`
- `list_projects()`
- `project_path()`

## Validation Rules

- Project name tidak boleh kosong secara logis.
- Project ID harus aman untuk nama file.
- Project harus memiliki field `scene`, `analysis`, dan `compiled`.

## Error Handling

- Jika project file rusak, tampilkan error dan jangan overwrite otomatis.
- Jika nama project duplikat, clone atau overwrite harus dilakukan eksplisit pada versi berikutnya.

## Performance Notes

- Project list dibaca dari file JSON lokal.
- Untuk ratusan project, perlu pagination pada milestone berikutnya.

## UI Components

- New Project form.
- Project List.
- Open button.
- Clone button.
- Archive placeholder.

## Configuration

- Project folder: `projects/`.
- Default status: `Draft`.

## Test Cases

- Buat project baru.
- Project muncul di list.
- Klik Open masuk Scene Editor.
- Clone membuat file project baru.

## Future Improvements

- Archive project.
- Search dan filter.
- Project tags.
- Project status workflow.

## Next Module

Analyze

