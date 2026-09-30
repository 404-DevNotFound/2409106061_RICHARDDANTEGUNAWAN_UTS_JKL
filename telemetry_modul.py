#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File    : telemetry_modul.py
Tujuan  : Menganalisis data sampel telemetry CPU usage.
Pembuat : Richard Dante Gunawan
NIM     : 2409106061
"""

# ============================================================
# DATA SAMPEL TELEMETRY
# ============================================================

# Nilai CPU diturunkan dari digit-digit NIM 2409106061
data_telemetry = {
    "router_1": {
        "cpuUsage": 24
    },
    "router_2": {
        "cpuUsage": 61
    },
    "router_3": {
        "cpuUsage": 91
    }
}


# ============================================================
# FUNCTION KLASIFIKASI TELEMETRY
# ============================================================

def klasifikasi_telemetry():
    """
    Mengklasifikasikan nilai cpuUsage menjadi:
    - KRITIS  : di atas 80
    - WASPADA : 50 sampai 80
    - NORMAL  : di bawah 50
    """

    print("\n=== ANALISIS DATA TELEMETRY ===")

    hasil_klasifikasi = []

    for perangkat, data in data_telemetry.items():
        cpu_usage = data["cpuUsage"]

        if cpu_usage > 80:
            status = "KRITIS"

        elif cpu_usage >= 50:
            status = "WASPADA"

        else:
            status = "NORMAL"

        print(
            f"{perangkat} | "
            f"CPU Usage: {cpu_usage}% | "
            f"Status: {status}"
        )

        hasil_klasifikasi.append({
            "perangkat": perangkat,
            "cpuUsage": cpu_usage,
            "status": status
        })

    return hasil_klasifikasi


if __name__ == "__main__":
    klasifikasi_telemetry()