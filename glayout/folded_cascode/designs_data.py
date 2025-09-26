# Diseno 1

def get_data_design1():
    #Biasing info
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

    arrays_biasing = [array_m1, array_m2, array_m3, array_m4, array_m5, array_m6, array_m7]
    info_biasing = [devices_info_m1, devices_info_m2, devices_info_m3, devices_info_m4, devices_info_m5, devices_info_m6, devices_info_m7]

    #core info
    array_par_bias = [
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

    array_bi_current = [[[1, 2, 1], [2, 1, 2]], [[1, 2], [2, 1]]]

    array_cascode = [
        [[1, 2], [2, 1], [2, 1], [1, 2]],
        [[1, 2, 2, 1, 1, 2, 2, 1, 1, 2], [2, 1, 1, 2, 2, 1, 1, 2, 2, 1]],
    ]

    m1_bias = {
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
    m2_bias = {
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

    m1_bi_current = {
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
    m2_bi_current = {
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

    m1_cascode = {
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
    m2_cascode = {
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

    array_core = [array_par_bias, array_bi_current, array_cascode]
    info_core = [m1_bias, m2_bias, m1_bi_current, m2_bi_current, m1_cascode, m2_cascode]

    design_info = {'arrays_bias' : arrays_biasing, 'info_bias' : info_biasing, 'arrays_core' : array_core, 'info_core' : info_core}
    return design_info

# Diseno 2

def get_data_design2():
    #Biasing info
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

    arrays_biasing = [array_m1, array_m2, array_m3, array_m4, array_m5, array_m6, array_m7]
    info_biasing = [devices_info_m1, devices_info_m2, devices_info_m3, devices_info_m4, devices_info_m5, devices_info_m6, devices_info_m7]

    #core info
    array_par_bias = [
        [
            [1, 2, 2, 1, 1, 2, 2, 1],
            [2, 1, 1, 2, 2, 1, 1, 2],
        ],
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
    ] 

    array_bi_current = [[[1, 2], [2, 1]], [[1, 2]]]

    array_cascode = [[[1, 2]], [[2, 1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]]

    m1_bias = {
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
    m2_bias = {
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

    m1_bi_current = {
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
    m2_bi_current = {
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

    m1_cascode = {
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
    m2_cascode = {
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

    array_core = [array_par_bias, array_bi_current, array_cascode]
    info_core = [m1_bias, m2_bias, m1_bi_current, m2_bi_current, m1_cascode, m2_cascode]

    design_info = {'arrays_bias' : arrays_biasing, 'info_bias' : info_biasing, 'arrays_core' : array_core, 'info_core' : info_core}
    return design_info

# Diseno 3


def get_data_design3():
    #Biasing info
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

    arrays_biasing = [array_m1, array_m2, array_m3, array_m4, array_m5, array_m6, array_m7]
    info_biasing = [devices_info_m1, devices_info_m2, devices_info_m3, devices_info_m4, devices_info_m5, devices_info_m6, devices_info_m7]

    #core info
    array_par_bias = [
        [
            [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
            [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2],
            [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
        ],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    ] 
    array_bi_current = [[[1, 2], [2, 1]], [[1, 2], [2, 1]]]

    array_cascode = [[[2, 1], [1, 2]], [[1, 2]]]

    m1_bias = {
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
    m2_bias = {
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

    m1_bi_current = {
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
    m2_bi_current = {
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

    m1_cascode = {
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
    m2_cascode = {
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

    array_core = [array_par_bias, array_bi_current, array_cascode]
    info_core = [m1_bias, m2_bias, m1_bi_current, m2_bi_current, m1_cascode, m2_cascode]

    design_info = {'arrays_bias' : arrays_biasing, 'info_bias' : info_biasing, 'arrays_core' : array_core, 'info_core' : info_core}
    return design_info

# Diseno 4

def get_data_design4():
    #Biasing info
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

    arrays_biasing = [array_m1, array_m2, array_m3, array_m4, array_m5, array_m6, array_m7]
    info_biasing = [devices_info_m1, devices_info_m2, devices_info_m3, devices_info_m4, devices_info_m5, devices_info_m6, devices_info_m7]

    #core info
    array_par_bias = [
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
    ]

    array_bi_current = [[[1, 2], [2, 1]], [[1, 2]]]

    array_cascode = [[[1, 2], [2, 1]], [[1, 2, 2, 1], [2, 1, 1, 2]]]

    m1_bias = {
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
    m2_bias = {
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

    m1_bi_current = {
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
    m2_bi_current = {
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

    m1_cascode = {
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
    m2_cascode = {
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

    array_core = [array_par_bias, array_bi_current, array_cascode]
    info_core = [m1_bias, m2_bias, m1_bi_current, m2_bi_current, m1_cascode, m2_cascode]

    design_info = {'arrays_bias' : arrays_biasing, 'info_bias' : info_biasing, 'arrays_core' : array_core, 'info_core' : info_core}
    return design_info
