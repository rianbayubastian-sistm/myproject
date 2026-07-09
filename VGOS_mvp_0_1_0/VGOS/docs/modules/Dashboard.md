# Dashboard

## Module Name

Dashboard

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul Dashboard menampilkan ringkasan seluruh aktivitas VGOS dalam satu layar utama. Modul ini memberikan gambaran cepat tentang pekerjaan hari ini, progres milestone, produksi, project terbaru, pertumbuhan knowledge, research, dan status QC.

Dashboard tidak mengedit data utama. Modul ini hanya membaca data dari modul lain dan menyajikannya sebagai ringkasan operasional.

## Purpose

Memberikan pusat monitoring agar user dapat melihat kondisi umum sistem dan menentukan langkah kerja berikutnya.

## Responsibilities

- Menampilkan Today's Task.
- Menampilkan Progress.
- Menampilkan Production summary.
- Menampilkan Recent Project.
- Menampilkan Knowledge Growth.
- Menampilkan Research summary.
- Menampilkan QC Status.

## Scope

- Membaca data project lokal.
- Menampilkan metrik ringkas.
- Menjadi layar awal aplikasi.

## Out of Scope

- Tidak membuat project baru.
- Tidak mengedit scene.
- Tidak melakukan Analyze.
- Tidak menjalankan QC.
- Tidak membuat laporan lengkap.

## Input

- Project list.
- Status milestone.
- Ringkasan production.
- Ringkasan QC.
- Ringkasan research.

## Process

```text
Load Project Data
↓
Read Current Milestone
↓
Calculate Summary
↓
Render Metrics
↓
Show Recent Activity
```

## Output

- Dashboard metrics.
- Progress indicator.
- Recent project list.
- Status summary.

## Dependencies

- Project Storage.
- Report Engine.
- QC Summary.
- Production Data.

## Data Structure

```json
{
  "today_task": "MVP Foundation",
  "progress": "Milestone 1",
  "project_count": 0,
  "qc_status": "MVP prompt QC rules available"
}
```

## Functions

- `render()`
- `list_projects()`

## Validation Rules

- Jika belum ada project, tampilkan empty state.
- Jika data summary belum tersedia, tampilkan status placeholder yang jelas.

## Error Handling

- Gagal membaca project tidak boleh menghentikan aplikasi.
- Data kosong harus ditampilkan sebagai informasi, bukan error.

## Performance Notes

- Dashboard harus ringan karena menjadi halaman awal.
- Hindari pemrosesan berat atau network request di halaman ini.

## UI Components

- Metric cards.
- Progress bar.
- Recent project list.
- Status panels.

## Configuration

- App version dari `config/settings.json`.
- Menu final dari `config/settings.json`.

## Test Cases

- Dashboard tampil tanpa project.
- Dashboard menampilkan jumlah project setelah project dibuat.
- Progress milestone tampil.

## Future Improvements

- Activity timeline.
- AI recommendation summary.
- Daily production heatmap.

## Next Module

Projects

