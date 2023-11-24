skip_list = [
    {'scheme': 'kyber1024', 'implementation': 'm4fspeed', 'estmemory': 15360},
    {'scheme': 'kyber1024', 'implementation': 'm4fstack', 'estmemory': 11264},
    {'scheme': 'kyber1024-90s', 'implementation': 'm4fspeed', 'estmemory': 17408},
    {'scheme': 'kyber1024-90s', 'implementation': 'm4fstack', 'estmemory': 13312},
    {'scheme': 'kyber512', 'implementation': 'm4fspeed', 'estmemory': 10240},
    {'scheme': 'kyber512', 'implementation': 'm4fstack', 'estmemory': 7168},
    {'scheme': 'kyber512-90s', 'implementation': 'm4fspeed', 'estmemory': 12288},
    {'scheme': 'kyber512-90s', 'implementation': 'm4fstack', 'estmemory': 9216},
    {'scheme': 'kyber768', 'implementation': 'm4fspeed', 'estmemory': 13312},
    {'scheme': 'kyber768', 'implementation': 'm4fstack', 'estmemory': 9216},
    {'scheme': 'kyber768-90s', 'implementation': 'm4fspeed', 'estmemory': 14336},
    {'scheme': 'kyber768-90s', 'implementation': 'm4fstack', 'estmemory': 11264},
    {'scheme': 'bikel3', 'implementation': 'opt', 'estmemory': 175104},
    {'scheme': 'bikel1', 'implementation': 'opt', 'estmemory': 90112},
    {'scheme': 'bikel3', 'implementation': 'm4f', 'estmemory': 194560},
    {'scheme': 'bikel1', 'implementation': 'm4f', 'estmemory': 103424},
    {'scheme': 'frodokem640aes', 'implementation': 'm4', 'estmemory': 124928},
    {'scheme': 'firesaber', 'implementation': 'm4f', 'estmemory': 15360},
    {'scheme': 'frodokem640shake', 'implementation': 'm4', 'estmemory': 113664},
    {'scheme': 'lightsaber', 'implementation': 'm4f', 'estmemory': 10240},
    {'scheme': 'ntruhps2048509', 'implementation': 'm4f', 'estmemory': 25600},
    {'scheme': 'ntruhps2048677', 'implementation': 'm4f', 'estmemory': 33792},
    {'scheme': 'ntruhps4096821', 'implementation': 'm4f', 'estmemory': 40960},
    {'scheme': 'ntruhrss701', 'implementation': 'm4f', 'estmemory': 32768},
    {'scheme': 'saber', 'implementation': 'm4f', 'estmemory': 12288},
    {'scheme': 'ntrulpr953', 'implementation': 'm4f', 'estmemory': 40960},
    {'scheme': 'ntrulpr857', 'implementation': 'm4f', 'estmemory': 38912},
    {'scheme': 'ntrulpr761', 'implementation': 'm4f', 'estmemory': 29696},
    {'scheme': 'ntrulpr653', 'implementation': 'm4f', 'estmemory': 24576},
    {'scheme': 'ntrulpr1277', 'implementation': 'm4f', 'estmemory': 64512},
    {'scheme': 'ntrulpr1013', 'implementation': 'm4f', 'estmemory': 41984},
    {'scheme': 'sikep434', 'implementation': 'm4', 'estmemory': 10240},
    {'scheme': 'sikep610', 'implementation': 'm4', 'estmemory': 14336},
    {'scheme': 'sikep751', 'implementation': 'm4', 'estmemory': 16384},
    {'scheme': 'sikep503', 'implementation': 'm4', 'estmemory': 11264},
    {'scheme': 'sntrup953', 'implementation': 'm4f', 'estmemory': 96256},
    {'scheme': 'sntrup857', 'implementation': 'm4f', 'estmemory': 108544},
    {'scheme': 'sntrup761', 'implementation': 'm4f', 'estmemory': 111616},
    {'scheme': 'sntrup653', 'implementation': 'm4f', 'estmemory': 97280},
    {'scheme': 'sntrup1277', 'implementation': 'm4f', 'estmemory': 99328},
    {'scheme': 'sntrup1013', 'implementation': 'm4f', 'estmemory': 110592},
    {'scheme': 'sikep434', 'implementation': 'opt', 'estmemory': 10240},
    {'scheme': 'sikep610', 'implementation': 'opt', 'estmemory': 14336},
    {'scheme': 'sikep503', 'implementation': 'opt', 'estmemory': 10240},
    {'scheme': 'sikep751', 'implementation': 'opt', 'estmemory': 16384},
    {'scheme': 'kyber1024', 'implementation': 'clean', 'estmemory': 28672},
    {'scheme': 'kyber1024-90s', 'implementation': 'clean', 'estmemory': 28672},
    {'scheme': 'kyber512', 'implementation': 'clean', 'estmemory': 14336},
    {'scheme': 'kyber512-90s', 'implementation': 'clean', 'estmemory': 15360},
    {'scheme': 'kyber768', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'kyber768-90s', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'frodokem1344aes', 'implementation': 'clean', 'estmemory': 3852288},
    {'scheme': 'frodokem1344aes', 'implementation': 'opt', 'estmemory': 305152},
    {'scheme': 'frodokem1344shake', 'implementation': 'clean', 'estmemory': 3852288},
    {'scheme': 'frodokem1344shake', 'implementation': 'opt', 'estmemory': 252928},
    {'scheme': 'firesaber', 'implementation': 'clean', 'estmemory': 28672},
    {'scheme': 'frodokem640aes', 'implementation': 'clean', 'estmemory': 932864},
    {'scheme': 'frodokem640aes', 'implementation': 'opt', 'estmemory': 144384},
    {'scheme': 'frodokem640shake', 'implementation': 'clean', 'estmemory': 932864},
    {'scheme': 'frodokem640shake', 'implementation': 'opt', 'estmemory': 119808},
    {'scheme': 'frodokem976aes', 'implementation': 'clean', 'estmemory': 2080768},
    {'scheme': 'frodokem976aes', 'implementation': 'opt', 'estmemory': 222208},
    {'scheme': 'frodokem976shake', 'implementation': 'clean', 'estmemory': 2079744},
    {'scheme': 'frodokem976shake', 'implementation': 'opt', 'estmemory': 185344},
    {'scheme': 'hqc-rmrs-128', 'implementation': 'clean', 'estmemory': 81920},
    {'scheme': 'hqc-rmrs-192', 'implementation': 'clean', 'estmemory': 161792},
    {'scheme': 'hqc-rmrs-256', 'implementation': 'clean', 'estmemory': 257024},
    {'scheme': 'lightsaber', 'implementation': 'clean', 'estmemory': 15360},
    {'scheme': 'mceliece348864', 'implementation': 'clean', 'estmemory': 833536},
    {'scheme': 'mceliece348864f', 'implementation': 'clean', 'estmemory': 833536},
    {'scheme': 'mceliece460896', 'implementation': 'clean', 'estmemory': 4733952},
    {'scheme': 'mceliece460896f', 'implementation': 'clean', 'estmemory': 4733952},
    {'scheme': 'mceliece6688128', 'implementation': 'clean', 'estmemory': 5255168},
    {'scheme': 'mceliece6688128f', 'implementation': 'clean', 'estmemory': 5255168},
    {'scheme': 'mceliece6960119', 'implementation': 'clean', 'estmemory': 5257216},
    {'scheme': 'mceliece6960119f', 'implementation': 'clean', 'estmemory': 5257216},
    {'scheme': 'mceliece8192128', 'implementation': 'clean', 'estmemory': 5568512},
    {'scheme': 'mceliece8192128f', 'implementation': 'clean', 'estmemory': 5568512},
    {'scheme': 'ntruhps2048509', 'implementation': 'clean', 'estmemory': 29696},
    {'scheme': 'ntruhps2048677', 'implementation': 'clean', 'estmemory': 38912},
    {'scheme': 'ntruhps4096821', 'implementation': 'clean', 'estmemory': 47104},
    {'scheme': 'ntruhrss701', 'implementation': 'clean', 'estmemory': 38912},
    {'scheme': 'ntrulpr953', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'ntrulpr857', 'implementation': 'clean', 'estmemory': 23552},
    {'scheme': 'ntrulpr761', 'implementation': 'clean', 'estmemory': 18432},
    {'scheme': 'ntrulpr653', 'implementation': 'clean', 'estmemory': 18432},
    {'scheme': 'ntrulpr1277', 'implementation': 'clean', 'estmemory': 28672},
    {'scheme': 'ntrulpr1013', 'implementation': 'clean', 'estmemory': 23552},
    {'scheme': 'saber', 'implementation': 'clean', 'estmemory': 20480},
    {'scheme': 'sntrup953', 'implementation': 'clean', 'estmemory': 22528},
    {'scheme': 'sntrup857', 'implementation': 'clean', 'estmemory': 20480},
    {'scheme': 'sntrup761', 'implementation': 'clean', 'estmemory': 18432},
    {'scheme': 'sntrup653', 'implementation': 'clean', 'estmemory': 16384},
    {'scheme': 'sntrup1277', 'implementation': 'clean', 'estmemory': 29696},
    {'scheme': 'sntrup1013', 'implementation': 'clean', 'estmemory': 23552},
    {'scheme': 'dilithium2', 'implementation': 'm4f', 'estmemory': 57344},
    {'scheme': 'dilithium3', 'implementation': 'm4f', 'estmemory': 79872},
    {'scheme': 'dilithium5', 'implementation': 'm4f', 'estmemory': 130048},
    {'scheme': 'dilithium2', 'implementation': 'clean', 'estmemory': 60416},
    {'scheme': 'dilithium2aes', 'implementation': 'clean', 'estmemory': 61440},
    {'scheme': 'dilithium3aes', 'implementation': 'clean', 'estmemory': 92160},
    {'scheme': 'dilithium3', 'implementation': 'clean', 'estmemory': 91136},
    {'scheme': 'dilithium5', 'implementation': 'clean', 'estmemory': 136192},
    {'scheme': 'dilithium5aes', 'implementation': 'clean', 'estmemory': 138240},
    {'scheme': 'falcon-1024', 'implementation': 'clean', 'estmemory': 90112},
    {'scheme': 'falcon-512', 'implementation': 'clean', 'estmemory': 47104},
    {'scheme': 'rainbowI-circumzenithal', 'implementation': 'clean', 'estmemory': 490496},
    {'scheme': 'rainbowI-classic', 'implementation': 'clean', 'estmemory': 445440},
    {'scheme': 'rainbowI-compressed', 'implementation': 'clean', 'estmemory': 387072},
    {'scheme': 'rainbowIII-circumzenithal', 'implementation': 'clean', 'estmemory': 2383872},
    {'scheme': 'rainbowIII-classic', 'implementation': 'clean', 'estmemory': 2046976},
    {'scheme': 'rainbowIII-compressed', 'implementation': 'clean', 'estmemory': 2032640},
    {'scheme': 'rainbowV-circumzenithal', 'implementation': 'clean', 'estmemory': 6140928},
    {'scheme': 'rainbowV-classic', 'implementation': 'clean', 'estmemory': 3587072},
    {'scheme': 'rainbowV-compressed', 'implementation': 'clean', 'estmemory': 4732928},
    {'scheme': 'sphincs-haraka-128f-robust', 'implementation': 'clean', 'estmemory': 23552},
    {'scheme': 'sphincs-haraka-128f-simple', 'implementation': 'clean', 'estmemory': 23552},
    {'scheme': 'sphincs-haraka-128s-robust', 'implementation': 'clean', 'estmemory': 13312},
    {'scheme': 'sphincs-haraka-128s-simple', 'implementation': 'clean', 'estmemory': 13312},
    {'scheme': 'sphincs-haraka-192f-robust', 'implementation': 'clean', 'estmemory': 43008},
    {'scheme': 'sphincs-haraka-192f-simple', 'implementation': 'clean', 'estmemory': 43008},
    {'scheme': 'sphincs-haraka-192s-robust', 'implementation': 'clean', 'estmemory': 23552},
    {'scheme': 'sphincs-haraka-192s-simple', 'implementation': 'clean', 'estmemory': 23552},
    {'scheme': 'sphincs-haraka-256f-robust', 'implementation': 'clean', 'estmemory': 59392},
    {'scheme': 'sphincs-haraka-256f-simple', 'implementation': 'clean', 'estmemory': 59392},
    {'scheme': 'sphincs-haraka-256s-robust', 'implementation': 'clean', 'estmemory': 38912},
    {'scheme': 'sphincs-haraka-256s-simple', 'implementation': 'clean', 'estmemory': 38912},
    {'scheme': 'sphincs-sha256-128f-robust', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'sphincs-sha256-128f-simple', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'sphincs-sha256-128s-robust', 'implementation': 'clean', 'estmemory': 12288},
    {'scheme': 'sphincs-sha256-128s-simple', 'implementation': 'clean', 'estmemory': 12288},
    {'scheme': 'sphincs-sha256-192f-robust', 'implementation': 'clean', 'estmemory': 41984},
    {'scheme': 'sphincs-sha256-192f-simple', 'implementation': 'clean', 'estmemory': 41984},
    {'scheme': 'sphincs-sha256-192s-robust', 'implementation': 'clean', 'estmemory': 22528},
    {'scheme': 'sphincs-sha256-192s-simple', 'implementation': 'clean', 'estmemory': 22528},
    {'scheme': 'sphincs-sha256-256f-robust', 'implementation': 'clean', 'estmemory': 57344},
    {'scheme': 'sphincs-sha256-256f-simple', 'implementation': 'clean', 'estmemory': 57344},
    {'scheme': 'sphincs-sha256-256s-robust', 'implementation': 'clean', 'estmemory': 37888},
    {'scheme': 'sphincs-sha256-256s-simple', 'implementation': 'clean', 'estmemory': 37888},
    {'scheme': 'sphincs-shake256-128f-robust', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'sphincs-shake256-128f-simple', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'sphincs-shake256-128s-robust', 'implementation': 'clean', 'estmemory': 12288},
    {'scheme': 'sphincs-shake256-128s-simple', 'implementation': 'clean', 'estmemory': 12288},
    {'scheme': 'sphincs-shake256-192f-robust', 'implementation': 'clean', 'estmemory': 41984},
    {'scheme': 'sphincs-shake256-192f-simple', 'implementation': 'clean', 'estmemory': 41984},
    {'scheme': 'sphincs-shake256-192s-robust', 'implementation': 'clean', 'estmemory': 22528},
    {'scheme': 'sphincs-shake256-192s-simple', 'implementation': 'clean', 'estmemory': 21504},
    {'scheme': 'sphincs-shake256-256f-robust', 'implementation': 'clean', 'estmemory': 57344},
    {'scheme': 'sphincs-shake256-256f-simple', 'implementation': 'clean', 'estmemory': 57344},
    {'scheme': 'sphincs-shake256-256s-robust', 'implementation': 'clean', 'estmemory': 37888},
    {'scheme': 'sphincs-shake256-256s-simple', 'implementation': 'clean', 'estmemory': 37888},
    {'scheme': 'falcon-1024-tree', 'implementation': 'opt-ct', 'estmemory': 186368},
    {'scheme': 'falcon-1024-tree', 'implementation': 'opt-leaktime', 'estmemory': 186368},
    {'scheme': 'falcon-1024', 'implementation': 'opt-leaktime', 'estmemory': 90112},
    {'scheme': 'falcon-1024', 'implementation': 'opt-ct', 'estmemory': 90112},
    {'scheme': 'falcon-512-tree', 'implementation': 'opt-ct', 'estmemory': 91136},
    {'scheme': 'falcon-512-tree', 'implementation': 'opt-leaktime', 'estmemory': 91136},
    {'scheme': 'falcon-512', 'implementation': 'opt-ct', 'estmemory': 47104},
    {'scheme': 'falcon-512', 'implementation': 'opt-leaktime', 'estmemory': 47104},
    {'scheme': 'falcon-1024', 'implementation': 'm4-ct', 'estmemory': 90112},
    {'scheme': 'falcon-512-tree', 'implementation': 'm4-ct', 'estmemory': 91136},
    {'scheme': 'falcon-512', 'implementation': 'm4-ct', 'estmemory': 47104},
    {'scheme': 'rainbowI-circumzenithal', 'implementation': 'm4f', 'estmemory': 308224},
    {'scheme': 'rainbowI-classic', 'implementation': 'm4f', 'estmemory': 308224},
    {'scheme': 'rainbowI-compressed', 'implementation': 'm4f', 'estmemory': 308224},
    {'scheme': 'picnicl1full', 'implementation': 'opt', 'estmemory': 40960},
    {'scheme': 'picnicl1fs', 'implementation': 'opt', 'estmemory': 43008},
    {'scheme': 'picnic3l1', 'implementation': 'opt-mem', 'estmemory': 51200},
    {'scheme': 'picnic3l1', 'implementation': 'opt', 'estmemory': 106496},
    {'scheme': 'ov-Ip', 'implementation': 'm4f', 'estmemory': 534528},
    {'scheme': 'ov-Ip-pkc', 'implementation': 'm4fstack', 'estmemory': 425984},
    {'scheme': 'ov-Ip-pkc', 'implementation': 'm4fspeed', 'estmemory': 565248},
    {'scheme': 'ov-Ip-pkc-skc', 'implementation': 'm4fstack', 'estmemory': 425984},
    {'scheme': 'ov-Ip-pkc-skc', 'implementation': 'm4fspeed', 'estmemory': 425984},
    {'scheme': 'ov-Ip', 'implementation': 'ref', 'estmemory': 534528},
    {'scheme': 'ov-Ip-pkc', 'implementation': 'ref', 'estmemory': 568320},
    {'scheme': 'ov-Ip-pkc-skc', 'implementation': 'ref', 'estmemory': 330752},
    {'scheme': 'mayo3', 'implementation': 'm4f', 'estmemory': 477184},
    {'scheme': 'mayo1', 'implementation': 'm4f', 'estmemory': 446464},
    {'scheme': 'mayo2', 'implementation': 'm4f', 'estmemory': 287744},
    {'scheme': 'mayo3', 'implementation': 'ref', 'estmemory': 1144832},
    {'scheme': 'mayo1', 'implementation': 'ref', 'estmemory': 404480},
    {'scheme': 'mayo2', 'implementation': 'ref', 'estmemory': 279552},
    {'scheme': 'hawk512', 'implementation': 'ref', 'estmemory': 17408},
    {'scheme': 'hawk1024', 'implementation': 'ref', 'estmemory': 32768},
    {'scheme': 'hawk256', 'implementation': 'ref', 'estmemory': 10240},
    {'scheme': 'perk-192-fast-3', 'implementation': 'ref', 'estmemory': 1036288},
    {'scheme': 'perk-192-fast-5', 'implementation': 'ref', 'estmemory': 1001472},
    {'scheme': 'perk-128-fast-5', 'implementation': 'ref', 'estmemory': 463872},
    {'scheme': 'perk-256-fast-5', 'implementation': 'ref', 'estmemory': 1722368},
    {'scheme': 'perk-128-fast-3', 'implementation': 'ref', 'estmemory': 475136},
    {'scheme': 'perk-128-short-5', 'implementation': 'ref', 'estmemory': 2235392},
    {'scheme': 'perk-256-fast-3', 'implementation': 'ref', 'estmemory': 1797120},
    {'scheme': 'perk-128-short-3', 'implementation': 'ref', 'estmemory': 2377728},
    {'scheme': 'ascon-sign-128s-simple', 'implementation': 'ref', 'estmemory': 12288},
    {'scheme': 'ascon-sign-128f-simple', 'implementation': 'ref', 'estmemory': 21504},
    {'scheme': 'ascon-sign-192s-simple', 'implementation': 'ref', 'estmemory': 22528},
    {'scheme': 'ascon-sign-192f-robust', 'implementation': 'ref', 'estmemory': 43008},
    {'scheme': 'ascon-sign-192f-simple', 'implementation': 'ref', 'estmemory': 41984},
    {'scheme': 'ascon-sign-192s-robust', 'implementation': 'ref', 'estmemory': 23552},
    {'scheme': 'ascon-sign-128s-robust', 'implementation': 'ref', 'estmemory': 12288},
    {'scheme': 'ascon-sign-128f-robust', 'implementation': 'ref', 'estmemory': 21504},
    {'scheme': 'cross-sha3-r-sdp-3-small', 'implementation': 'ref', 'estmemory': 1295360},
    {'scheme': 'cross-sha3-r-sdpg-1-small', 'implementation': 'ref', 'estmemory': 477184},
    {'scheme': 'cross-sha3-r-sdp-1-fast', 'implementation': 'ref', 'estmemory': 234496},
    {'scheme': 'cross-sha2-r-sdp-3-small', 'implementation': 'ref', 'estmemory': 1295360},
    {'scheme': 'cross-sha2-r-sdpg-5-small', 'implementation': 'ref', 'estmemory': 1063936},
    {'scheme': 'cross-sha2-r-sdpg-3-fast', 'implementation': 'ref', 'estmemory': 230400},
    {'scheme': 'cross-sha2-r-sdp-5-small', 'implementation': 'ref', 'estmemory': 1748992},
    {'scheme': 'cross-sha3-r-sdp-5-small', 'implementation': 'ref', 'estmemory': 1748992},
    {'scheme': 'cross-sha2-r-sdp-3-fast', 'implementation': 'ref', 'estmemory': 365568},
    {'scheme': 'cross-sha3-r-sdpg-5-fast', 'implementation': 'ref', 'estmemory': 440320},
    {'scheme': 'cross-sha2-r-sdp-1-small', 'implementation': 'ref', 'estmemory': 721920},
    {'scheme': 'cross-sha3-r-sdpg-5-small', 'implementation': 'ref', 'estmemory': 1063936},
    {'scheme': 'cross-sha3-r-sdpg-3-small', 'implementation': 'ref', 'estmemory': 776192},
    {'scheme': 'cross-sha2-r-sdpg-5-fast', 'implementation': 'ref', 'estmemory': 440320},
    {'scheme': 'cross-sha2-r-sdp-5-fast', 'implementation': 'ref', 'estmemory': 914432},
    {'scheme': 'cross-sha2-r-sdpg-3-small', 'implementation': 'ref', 'estmemory': 776192},
    {'scheme': 'cross-sha2-r-sdpg-1-small', 'implementation': 'ref', 'estmemory': 477184},
    {'scheme': 'cross-sha3-r-sdp-1-small', 'implementation': 'ref', 'estmemory': 721920},
    {'scheme': 'cross-sha3-r-sdpg-1-fast', 'implementation': 'ref', 'estmemory': 143360},
    {'scheme': 'cross-sha2-r-sdp-1-fast', 'implementation': 'ref', 'estmemory': 234496},
    {'scheme': 'cross-sha2-r-sdpg-1-fast', 'implementation': 'ref', 'estmemory': 143360},
    {'scheme': 'cross-sha3-r-sdpg-3-fast', 'implementation': 'ref', 'estmemory': 230400},
    {'scheme': 'cross-sha3-r-sdp-5-fast', 'implementation': 'ref', 'estmemory': 914432},
    {'scheme': 'cross-sha3-r-sdp-3-fast', 'implementation': 'ref', 'estmemory': 365568},
]
