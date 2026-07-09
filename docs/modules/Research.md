# Research

## Module Name

Research

## Version

0.1.0

## Status

Milestone 1 Placeholder

## Description

Modul Research mengumpulkan dan menganalisis referensi visual, tren industri, channel kompetitor, serta menemukan DNA atau Knowledge baru yang berpotensi memperkaya Knowledge Library.

Semua rekomendasi Research bersifat usulan dan memerlukan persetujuan pengguna sebelum menjadi bagian dari sistem.

## Purpose

Menjadi pusat eksplorasi tren dan referensi agar VGOS berkembang berdasarkan data, bukan tebakan.

## Responsibilities

- Youtube research.
- Pinterest research.
- Instagram research.
- Competitor research.
- Trend extraction.
- Theme extraction.
- DNA suggestion.
- Reference collection.
- Idea generation.

## Scope

- Placeholder module pada MVP.
- Menampilkan sumber research final.
- Menjelaskan output planned.

## Out of Scope

- Tidak scraping otomatis pada MVP.
- Tidak mengubah Knowledge Library otomatis.
- Tidak mengambil data eksternal tanpa persetujuan.
- Tidak membuat competitor database penuh.

## Input

- Source URL.
- Channel name.
- Keyword.
- Manual reference.

## Process

```text
Receive Research Source
↓
Collect Reference
↓
Extract Trend
↓
Detect Theme
↓
Suggest DNA
↓
Request User Approval
↓
Send Approved Knowledge
```

## Output

- Trend.
- Theme.
- DNA.
- Reference.
- Idea.
- Knowledge proposal.

## Dependencies

- Knowledge Library.
- Reports.
- Production.

## Data Structure

```json
{
  "source": "Youtube",
  "trend": "Night jazz cafe ambience",
  "theme": "Luxury Rain Interior",
  "dna": ["warm lighting", "rain reflection"],
  "status": "proposal"
}
```

## Functions

- `render()`

## Validation Rules

- Research output harus berstatus `proposal` sebelum masuk Knowledge.
- Source harus tercatat.
- Approval user wajib untuk Knowledge update.

## Error Handling

- Source kosong tidak diproses.
- External fetch error harus menjadi warning.

## Performance Notes

- Research dapat berat dan sebaiknya asynchronous pada milestone berikutnya.

## UI Components

- Source list.
- Trend output.
- Theme output.
- DNA proposal.
- Reference list.

## Configuration

- Research sources: Youtube, Pinterest, Instagram, Competitor.

## Test Cases

- Research page tampil.
- Semua source final tampil.
- Placeholder output jelas.

## Future Improvements

- Connector per platform.
- Manual reference board.
- Trend scoring.
- Knowledge proposal approval.

## Next Module

Reports

