# Reports

## Module Name

Reports

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul Reports mengompilasi data dari Production, QC, Research, dan Knowledge Library menjadi laporan harian, mingguan, atau bulanan secara otomatis. Laporan digunakan untuk evaluasi performa produksi, perkembangan Knowledge, tren, dan perencanaan konten berikutnya.

Pada MVP, Reports menghasilkan struktur report dasar dari project lokal.

## Purpose

Mengubah aktivitas VGOS menjadi laporan evaluasi yang dapat digunakan untuk keputusan produksi berikutnya.

## Responsibilities

- Daily report.
- Weekly report.
- Monthly report.
- Production summary.
- QC summary.
- Research summary.
- Knowledge summary.
- Trend summary.

## Scope

- Report JSON preview.
- Daily/Weekly/Monthly selector.
- Basic project count.

## Out of Scope

- Tidak export PDF pada MVP.
- Tidak membuat chart penuh.
- Tidak membuat email automation.
- Tidak menarik data research eksternal.

## Input

- Project list.
- Production summary.
- QC result.
- Research summary.
- Knowledge summary.

## Process

```text
Select Report Type
↓
Load Project Data
↓
Load Production Summary
↓
Load QC Summary
↓
Load Research Summary
↓
Build Report Object
↓
Render Report
```

## Output

- Daily report.
- Weekly report.
- Monthly report.
- JSON report object.

## Dependencies

- Projects.
- Production.
- QC.
- Research.
- Knowledge.
- Report Engine.

## Data Structure

```json
{
  "date": "2026-07-09",
  "type": "Daily",
  "production": {
    "project_count": 3
  },
  "qc": {
    "status": "MVP manual review"
  }
}
```

## Functions

- `build_daily_report()`
- `render()`

## Validation Rules

- Report harus punya date.
- Report type harus Daily, Weekly, atau Monthly.
- Missing module data harus ditulis sebagai pending, bukan error.

## Error Handling

- Project kosong tetap menghasilkan report.
- Missing research data tampil sebagai pending.

## Performance Notes

- Report MVP harus cepat.
- Export dan chart dapat ditambahkan setelah data model stabil.

## UI Components

- Report type selector.
- JSON report viewer.

## Configuration

- Report type: Daily, Weekly, Monthly.

## Test Cases

- Generate Daily report tanpa project.
- Generate Weekly report dengan project.
- Report memiliki date dan type.

## Future Improvements

- Markdown export.
- PDF export.
- Trend charts.
- Production analytics.

## Next Module

Dashboard

