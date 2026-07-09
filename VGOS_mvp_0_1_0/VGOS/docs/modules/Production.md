# Production

## Module Name

Production

## Version

0.1.0

## Status

Milestone 1 Placeholder

## Description

Modul Production mengelola jadwal produksi harian, target setiap channel, progres pekerjaan, serta status penyelesaian visual. Modul ini menghubungkan project dengan QC dan Reports.

Pada MVP, Production menampilkan jadwal contoh untuk menjaga bentuk sistem tanpa membuat workflow produksi penuh sebelum fondasi selesai.

## Purpose

Mengatur ritme produksi agar project visual tidak hanya dibuat, tetapi juga dijadwalkan, dilacak, dan dievaluasi.

## Responsibilities

- Menampilkan jadwal harian.
- Menampilkan target produksi.
- Menampilkan progress harian.
- Menghubungkan project dengan QC.
- Menjadi sumber data report produksi.

## Scope

- Schedule display.
- Target display.
- Progress placeholder.

## Out of Scope

- Tidak membuat persistence schedule penuh pada MVP.
- Tidak membuat multi-channel automation.
- Tidak membuat asset approval workflow.
- Tidak membuat calendar sync.

## Input

- Production schedule.
- Target count.
- Completed count.
- QC status.

## Process

```text
Load Schedule
↓
Read Target
↓
Read Completed Count
↓
Render Progress
↓
Send Summary to Reports
```

## Output

- Daily schedule.
- Target progress.
- Production summary.

## Dependencies

- Projects.
- QC.
- Reports.

## Data Structure

```json
{
  "day": "Senin",
  "theme": "Night Jazz",
  "target": 10,
  "done": 6
}
```

## Functions

- `render()`

## Validation Rules

- `done` tidak boleh lebih besar dari `target`.
- Target harus angka positif.

## Error Handling

- Schedule kosong tampil sebagai empty state.
- Progress invalid harus ditampilkan sebagai warning pada milestone berikutnya.

## Performance Notes

- Production harus ringan dan bisa dibuka cepat setiap hari.

## UI Components

- Schedule rows.
- Progress bars.
- Target counters.

## Configuration

- MVP schedule berada di `ui/production.py`.

## Test Cases

- Production page tampil.
- Progress bar menampilkan 6/10 untuk Senin.

## Future Improvements

- Persistent schedule JSON.
- Channel-based calendar.
- Drag-and-drop production board.
- QC gate integration.

## Next Module

Research

