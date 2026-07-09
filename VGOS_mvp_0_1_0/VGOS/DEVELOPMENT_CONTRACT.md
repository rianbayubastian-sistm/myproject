# VGOS Development Contract

Setiap sesi implementasi VGOS wajib memakai urutan ini:

1. ROLE
2. TASK
3. SCOPE
4. CONSTRAINTS
5. PROJECT STRUCTURE
6. FUNCTIONS
7. DEPENDENCIES
8. INPUT
9. PROCESS
10. OUTPUT
11. TEST CASE
12. VERSION
13. NEXT STEP

## Frozen Scope

VGOS v1.0 menu utama tidak berubah:

- Dashboard
- Projects
- Analyze
- Scene Editor
- Knowledge
- QC
- Production
- Research
- Reports
- Settings

## Module Documentation

Setiap modul wajib memiliki spesifikasi resmi di `docs/modules/`.

Sebelum mengubah modul, developer atau AI harus membaca:

1. `docs/MODULE_DOCUMENTATION_STANDARD.md`
2. `docs/MODULE_INDEX.md`
3. File spesifikasi modul yang akan diubah

Perubahan kode harus sesuai dengan:

- Scope
- Out of Scope
- Dependencies
- Data Structure
- Validation Rules
- Test Cases

## Milestone 1

Status: Implemented foundation.

Scope:

- Dashboard
- Projects
- Analyze image metadata and prompt text
- Scene Editor
- Simple Compiler

Constraints:

- Tidak membuat Research otomatis.
- Tidak membuat Production OS lengkap.
- Tidak membuat generator API.
- Tidak menambah menu baru.
- Knowledge memakai JSON.
- UI memakai Streamlit.

## Milestone 2

Scope planned:

- Knowledge Library CRUD lebih matang
- DNA Detection lebih kuat
- Theme Mapping lebih detail
- Validator/QC rules lebih lengkap

## Milestone 3

Scope planned:

- Production Schedule persistence
- Asset Management
- Research Center
- Auto Report
