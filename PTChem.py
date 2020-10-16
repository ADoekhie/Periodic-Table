# A simple Periodic Table written in Python
# Hope it may be useful to you

import tkinter as tk
import tkinter.font as ffont

element_name = ["Hydrogen",
                "Helium",
                "Lithium",
                "Beryllium",
                "Boron",
                "Carbon",
                "Nitrogen",
                "Oxygen",
                "Fluorine",
                "Neon",
                "Sodium",
                "Magnesium",
                "Aluminum",
                "Silicon",
                "Phosphorus",
                "Sulfur",
                "Chlorine",
                "Argon",
                "Potassium",
                "Calcium",
                "Scandium",
                "Titanium",
                "Vanadium",
                "Chromium",
                "Manganese",
                "Iron",
                "Cobalt",
                "Nickel",
                "Copper",
                "Zinc",
                "Gallium",
                "Germanium",
                "Arsenic",
                "Selenium",
                "Bromine",
                "Krypton",
                "Rubidium",
                "Strontium",
                "Yttrium",
                "Zirconium",
                "Niobium",
                "Molybdenum",
                "Technetium",
                "Ruthenium",
                "Rhodium",
                "Palladium",
                "Silver",
                "Cadmium",
                "Indium",
                "Tin",
                "Antimony",
                "Tellurium",
                "Iodine",
                "Xenon",
                "Cesium",
                "Barium",
                "Lanthanum",
                "Cerium",
                "Praseodymium",
                "Neodymium",
                "Promethium",
                "Samarium",
                "Europium",
                "Gadolinium",
                "Terbium",
                "Dysprosium",
                "Holmium",
                "Erbium",
                "Thulium",
                "Ytterbium",
                "Lutetium",
                "Hafnium",
                "Tantalum",
                "Tungsten",
                "Rhenium",
                "Osmium",
                "Iridium",
                "Platinum",
                "Gold",
                "Mercury",
                "Thallium",
                "Lead",
                "Bismuth",
                "Polonium",
                "Astatine",
                "Radon"
                "Francium",
                "Radium",
                "Actinium",
                "Thorium",
                "Protactinium",
                "Uranium",
                "Neptunium",
                "Plutonium",
                "Americium",
                "Curium",
                "Berkelium",
                "Californium",
                "Einsteinium",
                "Fermium",
                "Mendelevium",
                "Nobelium",
                "Lawrencium",
                "Rutherfordium",
                "Dubnium",
                "Seaborgium",
                "Bohrium",
                "Hassium",
                "Meitnerium",
                "Darmstadtium",
                "Roentgenium",
                "Copernicium",
                "Nihonium",
                "Flerovium",
                "Moscovium",
                "Livermorium",
                "Tennessine",
                "Oganesson", ]

element_row = [0,
               0,
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
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               3,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               4,
               5,
               5,
               5,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               8,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               5,
               6,
               6,
               6,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               9,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6,
               6]

element_column = [0,
                  17,
                  0,
                  1,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17,
                  0,
                  1,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17,
                  0,
                  1,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17,
                  0,
                  1,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17,
                  0,
                  1,
                  2,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17,
                  0,
                  1,
                  2,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17]

element_acro = ["H",
                "He",
                "Li",
                "Be",
                "B",
                "C",
                "N",
                "O",
                "F",
                "Ne",
                "Na",
                "Mg",
                "Al",
                "Si",
                "P",
                "S",
                "Cl",
                "Ar",
                "K",
                "Ca",
                "Sc",
                "Ti",
                "V",
                "Cr",
                "Mn",
                "Fe",
                "Co",
                "Ni",
                "Cu",
                "Zn",
                "Ga",
                "Ge",
                "As",
                "Se",
                "Br",
                "Kr",
                "Rb",
                "Sr",
                "Y",
                "Zr",
                "Nb",
                "Mo",
                "Tc",
                "Ru",
                "Rh",
                "Pd",
                "Ag",
                "Cd",
                "In",
                "Sn",
                "Sb",
                "Te",
                "I",
                "Xe",
                "Cs",
                "Ba",
                "La",
                "Ce",
                "Pr",
                "Nd",
                "Pm",
                "Sm",
                "Eu",
                "Gd",
                "Tb",
                "Dy",
                "Ho",
                "Er",
                "Tm",
                "Yb",
                "Lu",
                "Hf",
                "Ta",
                "W",
                "Re",
                "Os",
                "Ir",
                "Pt",
                "Au",
                "Hg",
                "Tl",
                "Pb",
                "Bi",
                "Po",
                "At",
                "Rn",
                "Fr",
                "Ra",
                "Ac",
                "Th",
                "Pa",
                "U",
                "Np",
                "Pu",
                "Am",
                "Cm",
                "Bk",
                "Cf",
                "Es",
                "Fm",
                "Md",
                "No",
                "Lr",
                "Rf",
                "Db",
                "Sg",
                "Bh",
                "Hs",
                "Mt",
                "Ds",
                "Rg",
                "Cn",
                "Nh",
                "Fl",
                "Mc",
                "Lv",
                "Ts",
                "Og"]

element_colour = ["grey",
                  "#FFF38C",
                  "#F2A8F5",
                  "#FA91BB",
                  "#5AE0AF",
                  "#FF7FCE",
                  "grey",
                  "#FFE88D",
                  "#FA8246",
                  "#FFF38C",
                  "#F2A8F6",
                  "#FA91BB",
                  "#5AE0AF",
                  "#FF7FCE",
                  "grey",
                  "#FFE88D",
                  "#FA8246",
                  "#FFF38C",
                  "#F2A8F7",
                  "#FA91BB",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#5AE0AF",
                  "#FF7FCE",
                  "grey",
                  "#FFE88D",
                  "#FA8246",
                  "#FFF38C",
                  "#F2A8F8",
                  "#FA91BB",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#5AE0AF",
                  "#FF7FCE",
                  "grey",
                  "#FFE88D",
                  "#FA8246",
                  "#FFF38C",
                  "#F2A8F9",
                  "#FA91BB",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#7BDFD4",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#5AE0AF",
                  "#FF7FCE",
                  "grey",
                  "#FFE88D",
                  "#FA8246",
                  "#FFF38C",
                  "#F2A8F1",
                  "#FA91BB",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#8CFF9C",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#85B5F5",
                  "#5AE0AF",
                  "#FF7FCE",
                  "grey",
                  "#FFE88D",
                  "#FA8246",
                  "#FFF38C"]

element_weight = ["1.008",
                  "4.003",
                  "6.941",
                  "9.012",
                  "10.811",
                  "12.011",
                  "14.007",
                  "15.999",
                  "18.998",
                  "20.18",
                  "22.99",
                  "24.305",
                  "26.982",
                  "28.086",
                  "30.974",
                  "32.065",
                  "35.453",
                  "39.948",
                  "39.098",
                  "40.078",
                  "44.956",
                  "47.867",
                  "50.942",
                  "51.996",
                  "54.938",
                  "55.845",
                  "58.933",
                  "58.693",
                  "63.546",
                  "65.39",
                  "69.723",
                  "72.64",
                  "74.922",
                  "78.96",
                  "79.904",
                  "83.8",
                  "85.468",
                  "87.62",
                  "88.906",
                  "91.224",
                  "92.906",
                  "95.94",
                  "98",
                  "101.07",
                  "102.906",
                  "106.42",
                  "107.868",
                  "112.411",
                  "114.818",
                  "118.71",
                  "121.76",
                  "127.6",
                  "126.905",
                  "131.293",
                  "132.906",
                  "137.327",
                  "138.906",
                  "140.116",
                  "140.908",
                  "144.24",
                  "145",
                  "150.36",
                  "151.964",
                  "157.25",
                  "158.925",
                  "162.5",
                  "164.93",
                  "167.259",
                  "168.934",
                  "173.04",
                  "174.967",
                  "178.49",
                  "180.948",
                  "183.84",
                  "186.207",
                  "190.23",
                  "192.217",
                  "195.078",
                  "196.967",
                  "200.59",
                  "204.383",
                  "207.2",
                  "208.98",
                  "209",
                  "210",
                  "222",
                  "223",
                  "226",
                  "227",
                  "232.038",
                  "231.036",
                  "238.029",
                  "237",
                  "244",
                  "243",
                  "247",
                  "247",
                  "251",
                  "252",
                  "257",
                  "258",
                  "259",
                  "262",
                  "261",
                  "262",
                  "266",
                  "264",
                  "277",
                  "278",
                  "281",
                  "280",
                  "285",
                  "286",
                  "289",
                  "289",
                  "293",
                  "294",
                  "294"
                  ]

root = tk.Tk()
root.geometry("1200x800")
root.title("PTChem")
root.configure(bg='white')

main_window = tk.Frame(bg='white')
main_window.pack()

p_table = tk.LabelFrame(main_window, text="Periodic Table", bg='white', bd=0)
p_table.pack(side=tk.TOP)

font_style = ffont.Font(family=' Helvetica', size='10')
font_style2 = ffont.Font(family=' Helvetica', size='8')


class Element:
    def __init__(self, elem_name, row, column, weight, colour, i):
        self.name = elem_name
        self.row = row
        self.column = column
        self.weight = weight[0:5]
        self.colour = colour
        self.ele_cell = tk.Frame(p_table, width=50, height=50)
        self.ele_cell.grid(row=self.row, column=self.column, sticky="nsew")
        self.my_frame = tk.LabelFrame(self.ele_cell, width=50, height=50, bg=self.colour, bd=2, highlightbackground='white')
        self.my_label = tk.Label(self.my_frame, width=5, height=1, text=self.name, bg=self.colour, font=font_style)
        self.my_label2 = tk.Label(self.my_frame, width=5, height=1, text=self.weight, bg=self.colour, font=font_style2)
        self.my_label3 = tk.Label(self.my_frame,  width=5, height=0, text=i+1, bg=self.colour, font=font_style2, anchor='w')
        self.my_frame.pack(side="top")
        self.my_label3.pack(side="top")
        self.my_label.pack(side="top")
        self.my_label2.pack(side="top")


def populate(r_start, r_end, r_step):
    for i in range(r_start, r_end, r_step):
        Element(element_acro[i], element_row[i], element_column[i], element_weight[i], element_colour[i], i)


tk.LabelFrame(p_table, width=50, height=25, bd=0, bg='white').grid(row=7, column=0)
populate(0, 118, 1)
root.mainloop()