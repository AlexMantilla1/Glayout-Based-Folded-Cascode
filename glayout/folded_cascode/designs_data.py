# Diseno 4

def get_data_design4():
    return
array_m1 = [[1, 2]]
array_m2 = [[1, 2]]
array_m3 = [[2, 1, 3]]
array_m4 = [[1, 2]]
array_m5 = [[1, 2]]
array_m6 = [[1, 2, 3]]
array_m7 = [[3, 2, 1, 2, 1, 3, 1, 2, 3]]

devices_info_m1 = {
    "type": "nfet",
    "name": "M1",
    "width": 1,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m2 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.70,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m3 = {
    "type": "pfet",
    "name": "M1",
    "width": 1,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m4 = {
    "type": "pfet",
    "name": "M1",
    "width": 1,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m5 = {
    "type": "pfet",
    "name": "M1",
    "width": 1,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m6 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.60,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m7 = {
    "type": "nfet",
    "name": "M1",
    "width": 2,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}


# place_par_bias:

m1 = {
    "type": "nfet",
    "name": "M1_M2",
    "width": 2,
    "length": 1.2,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M11",
    "width": 2,
    "length": 2,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}

array = [
    [
        [1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1],
        [2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2],
        [1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
]  #

# place_bi_current:

m1 = {
    "type": "nfet",
    "name": "M9_M10",
    "width": 1.5,
    "length": 2,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M7_M8",
    "width": 2,
    "length": 1.5,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
# m1 son los que van a vss
array = array = [[[1, 2], [2, 1]], [[1, 2]]]

# place_cascode:

m1 = {
    "type": "pfet",
    "name": "M3_M4",
    "width": 2.5,
    "length": 0.5,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}
m2 = {
    "type": "pfet",
    "name": "M5_M6",
    "width": 2,
    "length": 0.5,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}

array = [[[1, 2], [2, 1]], [[1, 2, 2, 1], [2, 1, 1, 2]]]


### ------------------------------------------------------------------

# Diseño 1
array_m1 = [[1, 2]]
array_m2 = [[1, 2]]
array_m3 = [[2, 1, 3]]
array_m4 = [[1, 2, 2, 1, 1, 2]]
array_m5 = [[1, 2, 1, 2, 1]]
array_m6 = [[1, 2, 3]]
array_m7 = [[3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3]]

devices_info_m1 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.90,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m2 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.50,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m3 = {
    "type": "pfet",
    "name": "M1",
    "width": 0.67,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m4 = {
    "type": "pfet",
    "name": "M1",
    "width": 0.75,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m5 = {
    "type": "pfet",
    "name": "M1",
    "width": 0.75,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m6 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.50,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m7 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.70,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}

# Par bias
m1 = {
    "type": "nfet",
    "name": "M1_M2",
    "width": 10,
    "length": 0.5,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M11",
    "width": 0.86,
    "length": 2,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}

array = [
    [
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
]  #

# bi current
m1 = {
    "type": "nfet",
    "name": "M9_M10",
    "width": 2,
    "length": 2,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M7_M8",
    "width": 2.5,
    "length": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
# m1 son los que van a vss
array = array = [[[1, 2, 1], [2, 1, 2]], [[1, 2], [2, 1]]]

# cascode

m1 = {
    "type": "pfet",
    "name": "M3_M4",
    "width": 2.5,
    "length": 0.4,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}
m2 = {
    "type": "pfet",
    "name": "M5_M6",
    "width": 4,
    "length": 0.6,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}

array = [
    [[1, 2], [2, 1], [2, 1], [1, 2]],
    [[1, 2, 2, 1, 1, 2, 2, 1, 1, 2], [2, 1, 1, 2, 2, 1, 1, 2, 2, 1]],
]


### ------------------------------------------------------------------

# Diseño 2
array_m1 = [[1, 2]]
array_m2 = [[1, 2]]
array_m3 = [[2, 1, 3]]
array_m4 = [[1, 2, 2, 1]]
array_m5 = [[2, 1, 1, 2]]
array_m6 = [[1, 2, 3]]
array_m7 = [
    [
        3,
        3,
        3,
        3,
        3,
        2,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        2,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
    ]
]

devices_info_m1 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.75,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m2 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.60,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m3 = {
    "type": "pfet",
    "name": "M1",
    "width": 0.70,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m4 = {
    "type": "pfet",
    "name": "M1",
    "width": 1.90,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m5 = {
    "type": "pfet",
    "name": "M1",
    "width": 1.90,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m6 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.50,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m7 = {
    "type": "nfet",
    "name": "M1",
    "width": 7.00,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}

# Par bias
m1 = {
    "type": "nfet",
    "name": "M1_M2",
    "width": 6.00,
    "length": 3.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M11",
    "width": 2.00,
    "length": 2.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}

array = [
    [
        [1, 2, 2, 1, 1, 2, 2, 1],
        [2, 1, 1, 2, 2, 1, 1, 2],
    ],
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
]  #

# bi current
m1 = {
    "type": "nfet",
    "name": "M9_M10",
    "width": 2.50,
    "length": 2.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M7_M8",
    "width": 2.00,
    "length": 2.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
# m1 son los que van a vss
array = array = [[[1, 2], [2, 1]], [[1, 2]]]

# cascode

m1 = {
    "type": "pfet",
    "name": "M3_M4",
    "width": 2.00,
    "length": 2.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}
m2 = {
    "type": "pfet",
    "name": "M5_M6",
    "width": 8.00,
    "length": 0.80,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}

array = [[[1, 2]], [[2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]]


### ------------------------------------------------------------------


# Diseño 3
array_m1 = [[1, 2]]
array_m2 = [[1, 2]]
array_m3 = [[2, 1, 3]]
array_m4 = [[1, 2]]
array_m5 = [[2, 1]]
array_m6 = [[1, 2, 3]]
array_m7 = [
    [
        3,
        3,
        2,
        2,
        1,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        3,
        3,
        2,
        2,
        1,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        3,
        3,
        2,
        2,
        1,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        3,
        3,
        2,
        2,
        1,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
    ]
]

devices_info_m1 = {
    "type": "nfet",
    "name": "M1",
    "width": 1.00,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m2 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.50,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m3 = {
    "type": "pfet",
    "name": "M1",
    "width": 1.00,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m4 = {
    "type": "pfet",
    "name": "M1",
    "width": 1.00,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m5 = {
    "type": "pfet",
    "name": "M1",
    "width": 1.00,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m6 = {
    "type": "nfet",
    "name": "M1",
    "width": 0.50,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}
devices_info_m7 = {
    "type": "nfet",
    "name": "M1",
    "width": 2.00,
    "length": 2,
    "width_route_mult": 1,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "lvt": False,
}

# Par bias
m1 = {
    "type": "nfet",
    "name": "M1_M2",
    "width": 2.00,
    "length": 4.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M11",
    "width": 2.00,
    "length": 2.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}

array = [
    [
        [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
        [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2],
        [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
    ],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
]  #

# bi current
m1 = {
    "type": "nfet",
    "name": "M9_M10",
    "width": 2.00,
    "length": 2.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
m2 = {
    "type": "nfet",
    "name": "M7_M8",
    "width": 2.00,
    "length": 2.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": False,
}
# m1 son los que van a vss
array = array = [[[1, 2], [2, 1]], [[1, 2], [2, 1]]]

# cascode

m1 = {
    "type": "pfet",
    "name": "M3_M4",
    "width": 2.00,
    "length": 1.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}
m2 = {
    "type": "pfet",
    "name": "M5_M6",
    "width": 2.00,
    "length": 1.00,
    "fingers": 1,
    "with_substrate_tap": False,
    "with_tie": True,
    "with_dummy": True,
    "width_route_mult": 1,
    "lvt": True,
}

array = [[[2, 1], [1, 2]], [[1, 2]]]
