v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 270 -140 270 -130 {lab=GND}
N 270 -230 270 -200 {lab=Vref}
N 110 -140 110 -130 {lab=GND}
N 110 -230 110 -200 {lab=VDD}
N 190 -140 190 -130 {lab=GND}
N 190 -230 190 -200 {lab=VSS}
N 990 -190 990 -130 {
lab=GND}
N 900 -300 990 -300 {
lab=Vout}
N 990 -300 990 -250 {
lab=Vout}
N 600 -330 700 -330 {
lab=#net1}
N 700 -330 720 -330 {lab=#net1}
N 350 -140 350 -130 {lab=GND}
N 350 -230 350 -200 {lab=Vin}
N 820 -420 820 -400 {lab=GND}
N 860 -430 860 -410 {lab=GND}
N 820 -410 860 -410 {lab=GND}
N 950 -470 950 -300 {lab=Vout}
N 860 -470 950 -470 {lab=Vout}
N 600 -480 600 -330 {lab=#net1}
N 600 -480 670 -480 {lab=#net1}
N 730 -480 820 -480 {lab=#net2}
N 600 -280 720 -280 {lab=Vin}
C {devices/vsource.sym} 270 -170 0 0 {name=V1 value=\{Vref\}}
C {devices/gnd.sym} 270 -130 0 0 {name=l2 lab=GND}
C {devices/lab_wire.sym} 270 -230 0 0 {name=p1 sig_type=std_logic lab=Vref}
C {devices/noconn.sym} 830 -240 0 1 {name=l4}
C {devices/lab_wire.sym} 790 -180 0 0 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 790 -200 0 0 {name=p8 sig_type=std_logic lab=VDD}
C {devices/vsource.sym} 110 -170 0 0 {name=V8 value=\{VDD\}}
C {devices/gnd.sym} 110 -130 0 0 {name=l5 lab=GND}
C {devices/lab_wire.sym} 110 -230 0 0 {name=p9 sig_type=std_logic lab=VDD}
C {devices/vsource.sym} 190 -170 0 0 {name=V5 value=\{VSS\}}
C {devices/gnd.sym} 190 -130 0 0 {name=l6 lab=GND}
C {devices/lab_wire.sym} 190 -230 0 0 {name=p10 sig_type=std_logic lab=VSS}
C {devices/capa.sym} 990 -220 0 0 {name=C1
m=1
value=2p
footprint=1206
device="ceramic capacitor"}
C {devices/vsource.sym} 350 -170 0 0 {name=Vin value=\{Vin\}}
C {devices/lab_wire.sym} 990 -300 0 0 {name=p12 sig_type=std_logic lab=Vout}
C {devices/gnd.sym} 820 -400 0 0 {name=l8 lab=GND}
C {devices/code_shown.sym} 70 -580 0 0 {name=MODELS only_toplevel=true
format="tcleval( @value )"
value="
.include $::180MCU_MODELS/design.ngspice
.lib $::180MCU_MODELS/sm141064.ngspice statistical
"}
C {devices/code_shown.sym} 570 -630 0 0 {name=Voltage_sources only_toplevel=true
value="
.param VDD = 3.3
.param VSS = 0
.param Vref = 1.2
.param Vin = 1.2
"}
C {devices/lab_wire.sym} 790 -220 0 0 {name=p4 sig_type=std_logic lab=Vref}
C {devices/gnd.sym} 350 -130 0 0 {name=l1 lab=GND}
C {devices/lab_wire.sym} 350 -230 0 0 {name=p2 sig_type=std_logic lab=Vin}
C {devices/lab_wire.sym} 600 -280 0 0 {name=p3 sig_type=std_logic lab=Vin}
C {simulator_commands.sym} 1010 -560 0 0 {name=COMMANDS1
simulator=ngspice
only_toplevel=false 
value="

*.param TEMPGAUSS = agauss(40, 30, 1)
*.option terror_amplifier_N_input_v3p = 'TEMPGAUSS'

.param sw_stat_global = 0
.param sw_stat_mismatch = 1

*.save all
.control
  let mc_runs = 1000
  let run = 0
  set curplot=new          $ create a new plot
  set scratch=$curplot     $ store its name to 'scratch'
  setplot $scratch         $ make 'scratch' the active plot
  let v_offset=unitvec(mc_runs) $ create a vector in plot 'scratch' to store v_offset data


  dowhile run < mc_runs

    *MC statistical

    *dc Vsweep -0.04 0.04 0.0005 
    op
    let Voffset = v(Vout) - 1.65
    *meas dc Voffset when vout_sw=1.65 rise=1
    *plot vout_sw
    print Voffset

    set run = $&run             $ create a variable from the vector
    set dt = $curplot           $ store the current plot to dt
    setplot $scratch            $ make 'scratch' the active plot

    let v_offset[run]=\{$dt\}.voffset       $ store voffset to vector v_offset in plot 'scratch'

    setplot $dt                 $ go back to the previous plot

    let run = run + 1
    *op
    write error_amplifier_N_input_v4_TB_offset_v2.raw
    reset
  end    $ loop ends here

  echo
  *print \{$scratch\}.v_offset

* Compute statistics

let mean_val_offset = avg(\{$scratch\}.v_offset)          ; Store mean in scalar variable
let mean_offset = mean_val_offset[mc_runs-1]
let diff_offset = \{$scratch\}.v_offset - mean_val_offset
let diff_sq_offset = diff_offset * diff_offset
let variance_offset = avg(diff_sq_offset)
let stddev_val_offset = sqrt(variance_offset)  ; Store stddev in scalar variable
let stddev_offset = stddev_val_offset[mc_runs-1]

* Print statistics
echo
echo '----------------------------------------'
echo 'Monte Carlo Results (n = $&mc_runs)'
echo '----------------------------------------'
echo 'Mean Voffset: $&mean_offset V'
echo 'Std Dev Voffset: $&stddev_offset V'
echo '----------------------------------------'

.endc
"}
C {devices/launcher.sym} 190 -440 0 0 {name=h3
descr="Save & Netlist & sim" 
tclcommand="xschem save; xschem netlist; xschem simulate"}
C {launcher.sym} 190 -380 0 0 {name=h2
descr="Annotate OP"
tclcommand="set show_hidden_texts 1; xschem annotate_op"}
C {vcvs.sym} 820 -450 0 1 {name=E1 value=1}
C {devices/gnd.sym} 990 -130 0 0 {name=l3 lab=GND}
C {devices/vsource.sym} 700 -480 1 0 {name=V2 value=0.45}
C {gf180/error_amplifier_N_input_v4/xschem/error_amplifier_N_input_v4.sym} 810 -300 0 0 {name=x1}
