# Analyze

## Module Name

Analyze

## Version

0.1.0

## Status

Milestone 1 Foundation

## Description

Modul Analyze bertugas menerima berbagai jenis input pengguna seperti gambar, teks, URL, atau proyek kosong, kemudian melakukan analisis visual untuk mengubah input mentah menjadi Knowledge terstruktur.

Modul ini tidak menghasilkan prompt. Fokus utamanya adalah mendeteksi background, memetakan DNA, mengidentifikasi risiko, melakukan theme mapping, dan menormalisasi data agar siap digunakan oleh modul berikutnya.

## Purpose

Mengubah data mentah menjadi Knowledge yang dapat dipahami seluruh sistem.

## Responsibilities

- Background Detection.
- Scene Detection.
- DNA Detection.
- Theme Mapping.
- Risk Detection.
- Prompt Normalization.
- Knowledge Extraction.

## Scope

- Analisis prompt teks.
- Analisis URL sebagai text seed pada MVP.
- Analisis gambar berbasis metadata dan nama file pada MVP.
- Output Knowledge Result.

## Out of Scope

- Tidak membuat prompt.
- Tidak menghasilkan video.
- Tidak melakukan Quality Control.
- Tidak melakukan Research.
- Tidak mengubah Knowledge Library.
- Tidak menjalankan computer vision penuh pada MVP 0.1.0.

## Input

- Image.
- Prompt.
- URL.
- Manual Input.

## Process

```text
Receive Input
↓
Normalize Input
↓
Analyze Background
↓
Detect Visual DNA
↓
Map Theme
↓
Detect Risk
↓
Output Knowledge
```

## Output

- Background Profile.
- DNA Profile.
- DNA Summary.
- Theme Mapping.
- Risk Report.
- Normalized Data.

## Dependencies

- Knowledge Library.
- DNA Detector.
- Theme Mapper.
- Normalizer.
- Rules Engine.

## Data Structure

```json
{
  "input_type": "text",
  "normalized_input": "Luxury penthouse at night",
  "background_profile": {
    "has_interior": true,
    "has_exterior": false,
    "has_night": true
  },
  "dna_summary": {
    "world": "Luxury Interior",
    "camera": "Unknown"
  },
  "theme_mapping": {},
  "risk_detection": []
}
```

## Functions

- `analyze_text()`
- `analyze_image_metadata()`
- `detect_background()`
- `detect_risk()`
- `detect_dna()`
- `build_dna_summary()`
- `map_theme()`
- `normalize_prompt_text()`

## Validation Rules

- Empty input tetap menghasilkan output valid.
- Unknown detection harus ditulis sebagai `Unknown`.
- Risk harus selalu memiliki minimal satu status.

## Error Handling

- File gambar tanpa metadata tetap dianalisis dari nama file.
- URL yang belum bisa di-scrape diperlakukan sebagai text seed.
- Knowledge JSON kosong tidak boleh membuat Analyze gagal.

## Performance Notes

- MVP memakai rule-based keyword matching.
- Computer vision dan URL scraping harus ditambahkan bertahap agar tidak merusak fondasi.

## UI Components

- Upload Image.
- Paste Prompt.
- Paste URL.
- Start Empty.
- Knowledge Result.
- DNA Detection Detail.

## Configuration

- Knowledge source: `knowledge/*.json`.
- Current analyzer mode: rule-based MVP.

## Test Cases

- Analyze prompt luxury penthouse Rome.
- Analyze image file name `beach-cafe-rain.jpg`.
- Analyze empty input.
- Risk warning muncul untuk cinemagraph/fire/glass.

## Future Improvements

- Computer vision detection.
- URL scraping.
- OCR.
- Scene segmentation.
- Confidence scoring.

## Next Module

Scene Editor

