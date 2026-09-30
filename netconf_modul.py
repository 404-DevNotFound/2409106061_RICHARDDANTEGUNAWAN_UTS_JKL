#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File    : netconf_modul.py
Tujuan  : Membuat pesan XML NETCONF untuk konfigurasi VLAN.
Pembuat : Richard Dante Gunawan
NIM     : 2409106061
"""

from identitas import kode_cabang


def buat_pesan_netconf():
    """
    Membuat pesan NETCONF <rpc><edit-config>
    untuk menambahkan VLAN berdasarkan kode cabang.
    """

    # Mengubah kode cabang menjadi integer agar VLAN ID menjadi angka
    vlan_id = int(kode_cabang)

    xml_netconf = f"""
<!-- MESSAGES LAYER -->
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"
     message-id="101">

    <!-- OPERATIONS LAYER -->
    <edit-config>
        <target>
            <running/>
        </target>

        <!-- CONTENT LAYER -->
        <config>
            <vlans xmlns="http://example.com/vlan">
                <vlan>
                    <id>{vlan_id}</id>
                    <name>VLAN_{kode_cabang}</name>
                </vlan>
            </vlans>
        </config>

    </edit-config>
</rpc>
"""

    return xml_netconf.strip()


if __name__ == "__main__":
    print("=== PESAN NETCONF ===")
    print(buat_pesan_netconf())