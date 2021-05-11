# A simple Periodic Table written in Python
# Hope it may be useful to you

import tkinter as tk
from tkinter import tix
from tkinter import font

my_elements = {
    "Hydrogen": {"name": "Hydrogen", "row": 0, "column": 0, "acro": "H", "color": "grey", "weight": 1.008},
    "Helium": {"name": "Helium", "row": 0, "column": 17, "acro": "He", "color": "#FFF38C", "weight": 4.003},
    "Lithium": {"name": "Lithium", "row": 1, "column": 0, "acro": "Li", "color": "#F2A8F5", "weight": 6.941},
    "Beryllium": {"name": "Beryllium", "row": 1, "column": 1, "acro": "Be", "color": "#FA91BB", "weight": 9.012},
    "Boron": {"name": "Boron", "row": 1, "column": 12, "acro": "B", "color": "#5AE0AF", "weight": 10.811},
    "Carbon": {"name": "Carbon", "row": 1, "column": 13, "acro": "C", "color": "#FF7FCE", "weight": 12.011},
    "Nitrogen": {"name": "Nitrogen", "row": 1, "column": 14, "acro": "N", "color": "grey", "weight": 14.007},
    "Oxygen": {"name": "Oxygen", "row": 1, "column": 15, "acro": "O", "color": "#FFE88D", "weight": 15.999},
    "Fluorine": {"name": "Fluorine", "row": 1, "column": 16, "acro": "F", "color": "#FA8246", "weight": 18.998},
    "Neon": {"name": "Neon", "row": 1, "column": 17, "acro": "Ne", "color": "#FFF38C", "weight": 20.18},
    "Sodium": {"name": "Sodium", "row": 2, "column": 0, "acro": "Na", "color": "#F2A8F6", "weight": 22.99},
    "Magnesium": {"name": "Magnesium", "row": 2, "column": 1, "acro": "Mg", "color": "#FA91BB", "weight": 24.305},
    "Aluminum": {"name": "Aluminum", "row": 2, "column": 12, "acro": "Al", "color": "#5AE0AF", "weight": 26.982},
    "Silicon": {"name": "Silicon", "row": 2, "column": 13, "acro": "Si", "color": "#FF7FCE", "weight": 28.086},
    "Phosphorus": {"name": "Phosphorus", "row": 2, "column": 14, "acro": "P", "color": "grey", "weight": 30.974},
    "Sulfur": {"name": "Sulfur", "row": 2, "column": 15, "acro": "S", "color": "#FFE88D", "weight": 32.065},
    "Chlorine": {"name": "Chlorine", "row": 2, "column": 16, "acro": "Cl", "color": "#FA8246", "weight": 35.453},
    "Argon": {"name": "Argon", "row": 2, "column": 17, "acro": "Ar", "color": "#FFF38C", "weight": 39.948},
    "Potassium": {"name": "Potassium", "row": 3, "column": 0, "acro": "K", "color": "#F2A8F7", "weight": 39.098},
    "Calcium": {"name": "Calcium", "row": 3, "column": 1, "acro": "Ca", "color": "#FA91BB", "weight": 40.078},
    "Scandium": {"name": "Scandium", "row": 3, "column": 2, "acro": "Sc", "color": "#85B5F5", "weight": 44.956},
    "Titanium": {"name": "Titanium", "row": 3, "column": 3, "acro": "Ti", "color": "#85B5F5", "weight": 47.867},
    "Vanadium": {"name": "Vanadium", "row": 3, "column": 4, "acro": "V", "color": "#85B5F5", "weight": 50.942},
    "Chromium": {"name": "Chromium", "row": 3, "column": 5, "acro": "Cr", "color": "#85B5F5", "weight": 51.996},
    "Manganese": {"name": "Manganese", "row": 3, "column": 6, "acro": "Mn", "color": "#85B5F5", "weight": 54.938},
    "Iron": {"name": "Iron", "row": 3, "column": 7, "acro": "Fe", "color": "#85B5F5", "weight": 55.845},
    "Cobalt": {"name": "Cobalt", "row": 3, "column": 8, "acro": "Co", "color": "#85B5F5", "weight": 58.933},
    "Nickel": {"name": "Nickel", "row": 3, "column": 9, "acro": "Ni", "color": "#85B5F5", "weight": 58.693},
    "Copper": {"name": "Copper", "row": 3, "column": 10, "acro": "Cu", "color": "#85B5F5", "weight": 63.546},
    "Zinc": {"name": "Zinc", "row": 3, "column": 11, "acro": "Zn", "color": "#85B5F5", "weight": 65.39},
    "Gallium": {"name": "Gallium", "row": 3, "column": 12, "acro": "Ga", "color": "#5AE0AF", "weight": 69.723},
    "Germanium": {"name": "Germanium", "row": 3, "column": 13, "acro": "Ge", "color": "#FF7FCE", "weight": 72.64},
    "Arsenic": {"name": "Arsenic", "row": 3, "column": 14, "acro": "As", "color": "grey", "weight": 74.922},
    "Selenium": {"name": "Selenium", "row": 3, "column": 15, "acro": "Se", "color": "#FFE88D", "weight": 78.96},
    "Bromine": {"name": "Bromine", "row": 3, "column": 16, "acro": "Br", "color": "#FA8246", "weight": 79.904},
    "Krypton": {"name": "Krypton", "row": 3, "column": 17, "acro": "Kr", "color": "#FFF38C", "weight": 83.8},
    "Rubidium": {"name": "Rubidium", "row": 4, "column": 0, "acro": "Rb", "color": "#F2A8F8", "weight": 85.468},
    "Strontium": {"name": "Strontium", "row": 4, "column": 1, "acro": "Sr", "color": "#FA91BB", "weight": 87.62},
    "Yttrium": {"name": "Yttrium", "row": 4, "column": 2, "acro": "Y", "color": "#85B5F5", "weight": 88.906},
    "Zirconium": {"name": "Zirconium", "row": 4, "column": 3, "acro": "Zr", "color": "#85B5F5", "weight": 91.224},
    "Niobium": {"name": "Niobium", "row": 4, "column": 4, "acro": "Nb", "color": "#85B5F5", "weight": 92.906},
    "Molybdenum": {"name": "Molybdenum", "row": 4, "column": 5, "acro": "Mo", "color": "#85B5F5", "weight": 95.94},
    "Technetium": {"name": "Technetium", "row": 4, "column": 6, "acro": "Tc", "color": "#85B5F5", "weight": 98},
    "Ruthenium": {"name": "Ruthenium", "row": 4, "column": 7, "acro": "Ru", "color": "#85B5F5", "weight": 101.07},
    "Rhodium": {"name": "Rhodium", "row": 4, "column": 8, "acro": "Rh", "color": "#85B5F5", "weight": 102.906},
    "Palladium": {"name": "Palladium", "row": 4, "column": 9, "acro": "Pd", "color": "#85B5F5", "weight": 106.42},
    "Silver": {"name": "Silver", "row": 4, "column": 10, "acro": "Ag", "color": "#85B5F5", "weight": 107.868},
    "Cadmium": {"name": "Cadmium", "row": 4, "column": 11, "acro": "Cd", "color": "#85B5F5", "weight": 112.411},
    "Indium": {"name": "Indium", "row": 4, "column": 12, "acro": "In", "color": "#5AE0AF", "weight": 114.818},
    "Tin": {"name": "Tin", "row": 4, "column": 13, "acro": "Sn", "color": "#FF7FCE", "weight": 118.71},
    "Antimony": {"name": "Antimony", "row": 4, "column": 14, "acro": "Sb", "color": "grey", "weight": 121.76},
    "Tellurium": {"name": "Tellurium", "row": 4, "column": 15, "acro": "Te", "color": "#FFE88D", "weight": 127.6},
    "Iodine": {"name": "Iodine", "row": 4, "column": 16, "acro": "I", "color": "#FA8246", "weight": 126.905},
    "Xenon": {"name": "Xenon", "row": 4, "column": 17, "acro": "Xe", "color": "#FFF38C", "weight": 131.293},
    "Cesium": {"name": "Cesium", "row": 5, "column": 0, "acro": "Cs", "color": "#F2A8F9", "weight": 132.906},
    "Barium": {"name": "Barium", "row": 5, "column": 1, "acro": "Ba", "color": "#FA91BB", "weight": 137.327},
    "Lanthanum": {"name": "Lanthanum", "row": 5, "column": 2, "acro": "La", "color": "#7BDFD4", "weight": 138.906},
    "Cerium": {"name": "Cerium", "row": 9, "column": 2, "acro": "Ce", "color": "#7BDFD4", "weight": 140.116},
    "Praseodymium": {"name": "Praseodymium", "row": 9, "column": 3, "acro": "Pr", "color": "#7BDFD4",
                     "weight": 140.908},
    "Neodymium": {"name": "Neodymium", "row": 9, "column": 4, "acro": "Nd", "color": "#7BDFD4", "weight": 144.24},
    "Promethium": {"name": "Promethium", "row": 9, "column": 5, "acro": "Pm", "color": "#7BDFD4", "weight": 145},
    "Samarium": {"name": "Samarium", "row": 9, "column": 6, "acro": "Sm", "color": "#7BDFD4", "weight": 150.36},
    "Europium": {"name": "Europium", "row": 9, "column": 7, "acro": "Eu", "color": "#7BDFD4", "weight": 151.964},
    "Gadolinium": {"name": "Gadolinium", "row": 9, "column": 8, "acro": "Gd", "color": "#7BDFD4", "weight": 157.25},
    "Terbium": {"name": "Terbium", "row": 9, "column": 9, "acro": "Tb", "color": "#7BDFD4", "weight": 158.925},
    "Dysprosium": {"name": "Dysprosium", "row": 9, "column": 10, "acro": "Dy", "color": "#7BDFD4", "weight": 162.5},
    "Holmium": {"name": "Holmium", "row": 9, "column": 11, "acro": "Ho", "color": "#7BDFD4", "weight": 164.93},
    "Erbium": {"name": "Erbium", "row": 9, "column": 12, "acro": "Er", "color": "#7BDFD4", "weight": 167.259},
    "Thulium": {"name": "Thulium", "row": 9, "column": 13, "acro": "Tm", "color": "#7BDFD4", "weight": 168.934},
    "Ytterbium": {"name": "Ytterbium", "row": 9, "column": 14, "acro": "Yb", "color": "#7BDFD4", "weight": 173.04},
    "Lutetium": {"name": "Lutetium", "row": 9, "column": 15, "acro": "Lu", "color": "#7BDFD4", "weight": 174.967},
    "Hafnium": {"name": "Hafnium", "row": 5, "column": 3, "acro": "Hf", "color": "#85B5F5", "weight": 178.49},
    "Tantalum": {"name": "Tantalum", "row": 5, "column": 4, "acro": "Ta", "color": "#85B5F5", "weight": 180.948},
    "Tungsten": {"name": "Tungsten", "row": 5, "column": 5, "acro": "W", "color": "#85B5F5", "weight": 183.84},
    "Rhenium": {"name": "Rhenium", "row": 5, "column": 6, "acro": "Re", "color": "#85B5F5", "weight": 186.207},
    "Osmium": {"name": "Osmium", "row": 5, "column": 7, "acro": "Os", "color": "#85B5F5", "weight": 190.23},
    "Iridium": {"name": "Iridium", "row": 5, "column": 8, "acro": "Ir", "color": "#85B5F5", "weight": 192.217},
    "Platinum": {"name": "Platinum", "row": 5, "column": 9, "acro": "Pt", "color": "#85B5F5", "weight": 195.078},
    "Gold": {"name": "Gold", "row": 5, "column": 10, "acro": "Au", "color": "#85B5F5", "weight": 196.967},
    "Mercury": {"name": "Mercury", "row": 5, "column": 11, "acro": "Hg", "color": "#85B5F5", "weight": 200.59},
    "Thallium": {"name": "Thallium", "row": 5, "column": 12, "acro": "Tl", "color": "#5AE0AF", "weight": 204.383},
    "Lead": {"name": "Lead", "row": 5, "column": 13, "acro": "Pb", "color": "#FF7FCE", "weight": 207.2},
    "Bismuth": {"name": "Bismuth", "row": 5, "column": 14, "acro": "Bi", "color": "grey", "weight": 208.98},
    "Polonium": {"name": "Polonium", "row": 5, "column": 15, "acro": "Po", "color": "#FFE88D", "weight": 209},
    "Astatine": {"name": "Astatine", "row": 5, "column": 16, "acro": "At", "color": "#FA8246", "weight": 210},
    "Radon": {"name": "Radon", "row": 5, "column": 17, "acro": "Rn", "color": "#FFF38C", "weight": 222},
    "Francium": {"name": "Francium", "row": 6, "column": 0, "acro": "Fr", "color": "#F2A8F1", "weight": 223},
    "Radium": {"name": "Radium", "row": 6, "column": 1, "acro": "Ra", "color": "#FA91BB", "weight": 226},
    "Actinium": {"name": "Actinium", "row": 6, "column": 2, "acro": "Ac", "color": "#8CFF9C", "weight": 227},
    "Thorium": {"name": "Thorium", "row": 10, "column": 2, "acro": "Th", "color": "#8CFF9C", "weight": 232.038},
    "Protactinium": {"name": "Protactinium", "row": 10, "column": 3, "acro": "Pa", "color": "#8CFF9C",
                     "weight": 231.036},
    "Uranium": {"name": "Uranium", "row": 10, "column": 4, "acro": "U", "color": "#8CFF9C", "weight": 238.029},
    "Neptunium": {"name": "Neptunium", "row": 10, "column": 5, "acro": "Np", "color": "#8CFF9C", "weight": 237},
    "Plutonium": {"name": "Plutonium", "row": 10, "column": 6, "acro": "Pu", "color": "#8CFF9C", "weight": 244},
    "Americium": {"name": "Americium", "row": 10, "column": 7, "acro": "Am", "color": "#8CFF9C", "weight": 243},
    "Curium": {"name": "Curium", "row": 10, "column": 8, "acro": "Cm", "color": "#8CFF9C", "weight": 247},
    "Berkelium": {"name": "Berkelium", "row": 10, "column": 9, "acro": "Bk", "color": "#8CFF9C", "weight": 247},
    "Californium": {"name": "Californium", "row": 10, "column": 10, "acro": "Cf", "color": "#8CFF9C", "weight": 251},
    "Einsteinium": {"name": "Einsteinium", "row": 10, "column": 11, "acro": "Es", "color": "#8CFF9C", "weight": 252},
    "Fermium": {"name": "Fermium", "row": 10, "column": 12, "acro": "Fm", "color": "#8CFF9C", "weight": 257},
    "Mendelevium": {"name": "Mendelevium", "row": 10, "column": 13, "acro": "Md", "color": "#8CFF9C", "weight": 258},
    "Nobelium": {"name": "Nobelium", "row": 10, "column": 14, "acro": "No", "color": "#8CFF9C", "weight": 259},
    "Lawrencium": {"name": "Lawrencium", "row": 10, "column": 15, "acro": "Lr", "color": "#8CFF9C", "weight": 262},
    "Rutherfordium": {"name": "Rutherfordium", "row": 6, "column": 3, "acro": "Rf", "color": "#85B5F5", "weight": 261},
    "Dubnium": {"name": "Dubnium", "row": 6, "column": 4, "acro": "Db", "color": "#85B5F5", "weight": 262},
    "Seaborgium": {"name": "Seaborgium", "row": 6, "column": 5, "acro": "Sg", "color": "#85B5F5", "weight": 266},
    "Bohrium": {"name": "Bohrium", "row": 6, "column": 6, "acro": "Bh", "color": "#85B5F5", "weight": 264},
    "Hassium": {"name": "Hassium", "row": 6, "column": 7, "acro": "Hs", "color": "#85B5F5", "weight": 277},
    "Meitnerium": {"name": "Meitnerium", "row": 6, "column": 8, "acro": "Mt", "color": "#85B5F5", "weight": 278},
    "Darmstadtium": {"name": "Darmstadtium", "row": 6, "column": 9, "acro": "Ds", "color": "#85B5F5", "weight": 281},
    "Roentgenium": {"name": "Roentgenium", "row": 6, "column": 10, "acro": "Rg", "color": "#85B5F5", "weight": 280},
    "Copernicium": {"name": "Copernicium", "row": 6, "column": 11, "acro": "Cn", "color": "#85B5F5", "weight": 285},
    "Nihonium": {"name": "Nihonium", "row": 6, "column": 12, "acro": "Nh", "color": "#5AE0AF", "weight": 286},
    "Flerovium": {"name": "Flerovium", "row": 6, "column": 13, "acro": "Fl", "color": "#FF7FCE", "weight": 289},
    "Moscovium": {"name": "Moscovium", "row": 6, "column": 14, "acro": "Mc", "color": "grey", "weight": 289},
    "Livermorium": {"name": "Livermorium", "row": 6, "column": 15, "acro": "Lv", "color": "#FFE88D", "weight": 293},
    "Tennessine": {"name": "Tennessine", "row": 6, "column": 16, "acro": "Ts", "color": "#FA8246", "weight": 294},
    "Oganesson": {"name": "Oganesson", "row": 6, "column": 17, "acro": "Og", "color": "#FFF38C", "weight": 294}
}

root = tix.Tk()
root.title("PTChem")
root.configure(bg="white")
root.wm_attributes("-topmost", 0)
main_window = tk.Frame(bg="white")
main_window.grid(padx=0, pady=0, ipadx=5, ipady=5)

header = tk.LabelFrame(main_window, text=" ", bg="white", bd=0)
header.grid(row=0, column=1)
p_table = tk.LabelFrame(main_window, text=" ", bg="white", bd=0)
p_table.grid(row=1, column=1, padx=10, pady=10, ipadx=15, ipady=15)

header_style = font.Font(family="helvetica", weight="bold", size=20)
group_period_style = font.Font(family="helvetica", weight="bold", size=10)
tooltip_style = font.Font(family="helvetica", weight="normal", size=8)

for n in range(1, 19, 1):
    _ = tk.LabelFrame(p_table, bd=0, bg="white")
    _.grid(row=0, column=n)
    _ = tk.Label(_, text=str(n), bg="white", height=2, font=group_period_style)
    _.grid()

for n in range(1, 8, 1):
    _ = tk.LabelFrame(p_table, bd=0, bg="white")
    _.grid(row=n, column=0, padx=5, pady=5)
    _ = tk.Label(_, text=str(n), bg="white", width=5, font=group_period_style)
    _.grid()

for element in my_elements:
    mye = my_elements[element]
    a = tk.LabelFrame(p_table, bg=mye['color'], bd=3)
    a.grid(row=mye['row']+1, column=mye['column']+1, sticky='nsew', padx=5, pady=5)
    b = tk.Label(a, text=mye['acro'], width=5, bg=mye['color'], font=group_period_style)
    b.grid(row=1, column=1, sticky='nsew')
    b = tk.Label(a, text=round(mye['weight']), width=5, bg='white', font=1)
    b.grid(row=2, column=1, sticky='nsew')
    bal = tix.Balloon(a)
    par = my_elements[element]
    ele_description = str(par['name']) + "\n" + str(par['weight'])
    bal.bind_widget(a, balloonmsg=ele_description)


def extra_labels(row, col, span, text, bg="white", loc=p_table, font=None):
    _ = tk.LabelFrame(master=loc, bd=0, bg=bg)
    _.grid(row=row, column=col, columnspan=span)
    _ = tk.Label(_, text=text, bg=bg, justify="center", font=font)
    _.grid()


extra_labels(9, 1, 2, " ", font=group_period_style)
extra_labels(10, 1, 2, "Lanthanides", font=group_period_style)
extra_labels(11, 1, 2, "Actinides", font=group_period_style)
extra_labels(3, 6, 3, "Transition Elements", font=group_period_style)
extra_labels(0, 0, 1, "Group\n \nPeriod", font=group_period_style)
extra_labels(0, 1, 1, "Periodic Table of the Elements", loc=header, font=header_style)
extra_labels(1, 1, 1, "(Hover on element for more info)", loc=header, font=tooltip_style)


root.mainloop()
