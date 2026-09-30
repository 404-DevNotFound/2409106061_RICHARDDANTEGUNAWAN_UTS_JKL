#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File    : identitas.py
Tujuan  : Menyimpan identitas cabang dan membuat ID perangkat.
Pembuat : Richard Dante Gunawan
NIM     : 2409106061
"""

# ============================================================
# IDENTITAS MAHASISWA DAN CABANG
# ============================================================

nim = "2409106061"
nama = "Richard Dante Gunawan"

# Mengambil 3 digit terakhir NIM sebagai kode cabang
kode_cabang = "061"


# ============================================================
# FUNCTION PEMBUAT ID PERANGKAT
# ============================================================

def buat_id_perangkat(jenis, nomor):
    """
    Membuat ID perangkat berdasarkan jenis perangkat,
    kode cabang, dan nomor perangkat.

    Contoh:
    buat_id_perangkat("RTR", 1)
    menghasilkan RTR-123-01
    """

    return f"{jenis.upper()}-{kode_cabang}-{nomor:02d}"


# ============================================================
# PENGUJIAN MODUL
# ============================================================

if __name__ == "__main__":
    print("=== IDENTITAS CABANG ===")
    print(f"NIM          : {nim}")
    print(f"Nama         : {nama}")
    print(f"Kode Cabang  : {kode_cabang}")

    print("\n=== ID PERANGKAT ===")
    print(f"Router       : {buat_id_perangkat('RTR', 1)}")
    print(f"Switch       : {buat_id_perangkat('SW', 1)}")
    print(f"Access Point : {buat_id_perangkat('AP', 1)}")