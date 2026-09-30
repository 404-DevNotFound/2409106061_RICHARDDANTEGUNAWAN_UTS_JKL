#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File    : ssh_modul.py
Tujuan  : Melakukan koneksi SSH dan menjalankan perintah diagnostik.
Pembuat : Richard Dante Gunawan
NIM     : 2409106061
"""

import paramiko

from identitas import kode_cabang


def cek_ssh():
    """
    Melakukan koneksi SSH ke perangkat tujuan dan menjalankan
    dua perintah diagnostik.

    Kegagalan koneksi ditangani menggunakan try/except
    agar program utama tidak berhenti.
    """

    host = "127.0.0.1"
    port = 22

    username = f"admin_{kode_cabang}"

    # Ganti dengan password user SSH yang digunakan.
    password = "dante123"

    print("\n=== PEMERIKSAAN SSH ===")
    print(f"Host     : {host}")
    print(f"Port     : {port}")
    print(f"Username : {username}")

    try:
        # Membuat SSH client
        client = paramiko.SSHClient()

        # Menerima host key yang belum dikenal secara otomatis
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Melakukan koneksi SSH
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            timeout=10
        )

        print("\nStatus SSH : BERHASIL TERHUBUNG")

        # ----------------------------------------------------
        # Perintah diagnostik 1
        # ----------------------------------------------------
        stdin, stdout, stderr = client.exec_command("hostname")

        hasil_hostname = stdout.read().decode().strip()

        print("\n[Perintah 1] hostname")
        print(hasil_hostname)

        # ----------------------------------------------------
        # Perintah diagnostik 2
        # ----------------------------------------------------
        stdin, stdout, stderr = client.exec_command("whoami")

        hasil_user = stdout.read().decode().strip()

        print("\n[Perintah 2] whoami")
        print(hasil_user)

        # Menutup koneksi SSH
        client.close()

        return {
            "status": "BERHASIL",
            "hostname": hasil_hostname,
            "user": hasil_user
        }

    except Exception as error:
        print("\nStatus SSH : GAGAL")
        print(f"Pesan Error: {error}")

        return {
            "status": "GAGAL",
            "error": str(error)
        }


if __name__ == "__main__":
    cek_ssh()