#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File    : snmp_modul.py
Tujuan  : Mengambil informasi sysName perangkat menggunakan SNMPv2c.
Pembuat : Richard Dante Gunawan
NIM     : 2409106061
"""

import asyncio

from pysnmp.hlapi.v3arch.asyncio import (
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    get_cmd,
)

from identitas import kode_cabang


async def _ambil_sysname():
    """
    Mengambil nilai sysName menggunakan SNMPv2c.
    """

    host = "127.0.0.1"
    port = 161

    community = f"comm_{kode_cabang}"

    snmp_engine = SnmpEngine()

    error_indication, error_status, error_index, var_binds = await get_cmd(
        snmp_engine,

        # mpModel=1 berarti SNMPv2c
        CommunityData(community, mpModel=1),

        await UdpTransportTarget.create(
            (host, port),
            timeout=3,
            retries=1
        ),

        ContextData(),

        # OID sysName
        ObjectType(
            ObjectIdentity("1.3.6.1.2.1.1.5.0")
        )
    )

    if error_indication:
        raise Exception(error_indication)

    if error_status:
        raise Exception(
            f"{error_status.prettyPrint()} pada index {error_index}"
        )

    for var_bind in var_binds:
        return var_bind[1].prettyPrint()

    return None


def cek_snmp():
    """
    Menjalankan pemeriksaan SNMP dan menampilkan nilai sysName.
    """

    print("\n=== PEMERIKSAAN SNMP ===")
    print("Host      : 127.0.0.1")
    print("Port      : 161")
    print(f"Community : comm_{kode_cabang}")
    print("OID       : 1.3.6.1.2.1.1.5.0")

    try:
        sysname = asyncio.run(_ambil_sysname())

        print("\nStatus SNMP : BERHASIL")
        print(f"sysName     : {sysname}")

        return {
            "status": "BERHASIL",
            "sysName": sysname
        }

    except Exception as error:
        print("\nStatus SNMP : GAGAL")
        print(f"Pesan Error : {error}")

        return {
            "status": "GAGAL",
            "error": str(error)
        }


if __name__ == "__main__":
    cek_snmp()