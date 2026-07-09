# QC

## Module Name

Quality Control

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul QC memvalidasi hasil produksi berdasarkan standar kualitas VGOS. Modul ini mendeteksi potensi artefak, ketidakkonsistenan visual, pelanggaran identitas channel, masalah loop, refleksi, geometri, resolusi, overlay, dan channel identity.

Pada MVP, QC menjalankan rule check terhadap compiled prompt. QC visual penuh dilakukan pada milestone berikutnya.

## Purpose

Memastikan output yang akan diproduksi memenuhi standar dasar sebelum masuk pipeline Production dan Report.

## Responsibilities

- Prompt Detection.
- Artifact check.
- Loop check.
- Reflection check.
- Geometry check.
- Identity check.
- Resolution check.
- Overlay check.
- Channel Identity check.

## Scope

- Rule-based prompt QC.
- Status PASS/WARNING/FAIL.
- QC report sederhana.

## Out of Scope

- Tidak menganalisis video aktual pada MVP.
- Tidak melakukan computer vision QC.
- Tidak melakukan render ulang.
- Tidak mengubah prompt otomatis tanpa persetujuan.

## Input

- Compiled prompt.
- Negative prompt.
- Scene metadata.

## Process

```text
Receive Compiled Prompt
↓
Run Rule Checks
↓
Classify PASS/WARNING/FAIL
↓
Show QC Result
```

## Output

- QC item list.
- PASS/WARNING/FAIL status.
- Notes per issue.

## Dependencies

- Compiler.
- Scene Editor.
- Production.
- Report.

## Data Structure

```json
{
  "item": "Artifact",
  "status": "WARNING",
  "note": "Negative prompt belum menjaga morphing."
}
```

## Functions

- `run_prompt_qc()`
- `render()`

## Validation Rules

- QC harus memiliki status jelas.
- Compiled prompt kosong menghasilkan warning.
- Negative prompt harus dicek untuk artifact guard.

## Error Handling

- Jika belum ada compiled prompt, tampilkan instruksi ke Scene Editor.
- Missing negative prompt harus menjadi WARNING.

## Performance Notes

- Rule check harus cepat.
- Video QC berat tidak boleh masuk MVP foundation.

## UI Components

- QC status list.
- PASS/WARNING/FAIL message.

## Configuration

- QC item list berada di `engine/qc.py`.

## Test Cases

- Buka QC sebelum compile.
- Compile prompt lalu buka QC.
- Hapus morphing dari negative prompt dan cek WARNING.

## Future Improvements

- Frame-level video QC.
- Artifact detector.
- Loop seam detector.
- Reflection stability scoring.
- Channel identity checker.

## Next Module

Production

