# VGOS MVP Test Cases

## Test Case 1: App Startup

Command:

```bash
streamlit run app.py
```

Expected:

- Header menampilkan VGOS v1.0.
- Sidebar menampilkan 10 menu final.
- Dashboard terbuka.

## Test Case 2: Create Project

Steps:

1. Buka Projects.
2. Klik Create Project.
3. Isi nama `Beach Cafe Rain`.

Expected:

- File project tersimpan di folder `projects/`.
- Project tampil di Project List.
- Tombol Open membawa user ke Scene Editor.

## Test Case 3: Analyze Prompt

Input:

```text
Ultra luxury penthouse in Rome at night with fireplace, glass, warm tungsten lighting, cinematic cinemagraph.
```

Expected:

- Background Detection muncul.
- DNA Summary muncul.
- Theme Mapping muncul.
- Risk Detection memberi warning temporal consistency/reflection.

## Test Case 4: Scene Editor Compile

Steps:

1. Buka Scene Editor.
2. Isi field Scene, Camera, Lighting, Material, Motion, Boundary.
3. Klik Compile.

Expected:

- Prompt terkompilasi.
- Negative prompt otomatis tersedia.
- Version `0.1.0`.

## Test Case 5: QC

Steps:

1. Compile prompt dari Scene Editor.
2. Buka QC.

Expected:

- Daftar QC tampil.
- Status minimal PASS/WARNING.

