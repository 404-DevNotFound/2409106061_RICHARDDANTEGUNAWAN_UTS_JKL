#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File    : main.py
Tujuan  : Mengintegrasikan seluruh modul UTS Jaringan Komputer Lanjut.
Pembuat : Richard Dante Gunawan
NIM     : 2409106061
"""

from identitas import nim, nama, kode_cabang, buat_id_perangkat
from ssh_modul import cek_ssh
from snmp_modul import cek_snmp
from netconf_modul import buat_pesan_netconf
from telemetry_modul import klasifikasi_telemetry


class LaporanCabang:
    """
    Class untuk menampilkan laporan akhir gabungan
    dari seluruh modul project.
    """

    def tampilkan_laporan(
        self,
        hasil_ssh,
        hasil_snmp,
        pesan_netconf,
        hasil_telemetry
    ):
        print("\n")
        print("=" * 60)
        print("              LAPORAN AKHIR CABANG")
        print("=" * 60)

        print("\n=== IDENTITAS ===")
        print(f"NIM          : {nim}")
        print(f"Nama         : {nama}")
        print(f"Kode Cabang  : {kode_cabang}")
        print(f"ID Router    : {buat_id_perangkat('RTR', 1)}")

        print("\n=== HASIL SSH ===")
        print(f"Status       : {hasil_ssh.get('status')}")

        if hasil_ssh.get("status") == "BERHASIL":
            print(f"Hostname     : {hasil_ssh.get('hostname')}")
            print(f"User         : {hasil_ssh.get('user')}")
        else:
            print(f"Error        : {hasil_ssh.get('error')}")

        print("\n=== HASIL SNMP ===")
        print(f"Status       : {hasil_snmp.get('status')}")

        if hasil_snmp.get("status") == "BERHASIL":
            print(f"sysName      : {hasil_snmp.get('sysName')}")
        else:
            print(f"Error        : {hasil_snmp.get('error')}")

        print("\n=== PESAN NETCONF ===")
        print(pesan_netconf)

        print("\n=== HASIL TELEMETRY ===")

        for data in hasil_telemetry:
            print(
                f"{data['perangkat']} | "
                f"CPU Usage: {data['cpuUsage']}% | "
                f"Status: {data['status']}"
            )

        print("\n" + "=" * 60)
        print("              SELESAI")
        print("=" * 60)


def main():
    """
    Menjalankan seluruh modul project secara berurutan.
    """

    print("=" * 60)
    print("     UTS JARINGAN KOMPUTER LANJUT")
    print("=" * 60)

    # Menjalankan modul SSH
    hasil_ssh = cek_ssh()

    # Menjalankan modul SNMP
    hasil_snmp = cek_snmp()

    # Membuat pesan NETCONF
    pesan_netconf = buat_pesan_netconf()

    print("\n=== PESAN NETCONF ===")
    print(pesan_netconf)

    # Menjalankan analisis telemetry
    hasil_telemetry = klasifikasi_telemetry()

    # Membuat laporan akhir
    laporan = LaporanCabang()

    laporan.tampilkan_laporan(
        hasil_ssh,
        hasil_snmp,
        pesan_netconf,
        hasil_telemetry
    )


if __name__ == "__main__":
    main()