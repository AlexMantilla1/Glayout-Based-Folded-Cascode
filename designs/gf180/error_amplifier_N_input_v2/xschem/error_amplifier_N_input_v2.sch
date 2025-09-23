v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 -260 -140 {}
N -50 60 -30 60 {lab=#net1}
N -370 70 -290 70 {lab=Vref}
N -20 -40 50 -40 {lab=V+}
N -20 -100 50 -100 {lab=V-}
N 250 -70 420 -70 {lab=Vout}
N -50 80 100 80 {lab=VbiasP2}
N -50 100 100 100 {lab=VbiasN2}
N -50 120 100 120 {lab=VbiasN1}
N 200 60 420 60 {lab=Vcomn}
N 100 60 200 60 {lab=Vcomn}
C {devices/lab_wire.sym} -290 90 0 0 {name=p12 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} -290 110 0 0 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 50 -100 0 0 {name=p6 sig_type=std_logic lab=V-}
C {devices/lab_wire.sym} 50 -40 0 0 {name=p7 sig_type=std_logic lab=V+}
C {devices/lab_wire.sym} 100 20 0 0 {name=p4 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 100 40 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} -20 -40 0 0 {name=p14 lab=V+}
C {devices/iopin.sym} 420 -70 0 0 {name=p18 lab=Vout}
C {devices/ipin.sym} -20 -100 0 0 {name=p19 lab=V-}
C {devices/ipin.sym} -370 70 0 0 {name=p9 lab=Vref}
C {devices/iopin.sym} -270 -190 0 0 {name=p15 lab=VDD}
C {devices/iopin.sym} -270 -160 0 0 {name=p10 lab=VSS}
C {devices/iopin.sym} 420 60 0 0 {name=p11 lab=Vcomn}
C {noconn.sym} -30 60 2 0 {name=l1}
C {devices/lab_wire.sym} 80 80 0 0 {name=p13 sig_type=std_logic lab=VbiasP2}
C {devices/lab_wire.sym} 80 100 0 0 {name=p16 sig_type=std_logic lab=VbiasN2}
C {devices/lab_wire.sym} 80 120 0 0 {name=p17 sig_type=std_logic lab=VbiasN1}
C {gf180/error_amplifier_N_input_core_v2/xschem/error_amplifier_N_input_core_v2.sym} 150 -70 0 0 {name=x1}
C {gf180/error_amplifier_N_input_bias_v2/xschem/error_amplifier_N_input_bias_v2.sym} -170 90 0 0 {name=x2}
