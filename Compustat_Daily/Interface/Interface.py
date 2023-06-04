from tkinter import *
from tkinter import ttk
from Interface.Tools.tools import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
from matplotlib import style
import mplfinance as mpf



class window:

    def __init__(self):
        wrdsdata()
        interface = Tk()
        interface.title("SCOUT 0.01")
        interface.state('zoomed')
        interface.configure(background='#2E3138')

        nb = ttk.Notebook(interface, height=1920, width=1920)
        nb.grid()

        page1 = Frame(nb, bg = '#2E3138', border=0, background='#2E3138', )

        page1.grid(row=0, column=3, sticky='W', padx=(0,0), pady=(0,0))

        nb.add(page1,text='Data')


        Label(page1, text='Symbol',bg="#2E3138", fg="white", font=("montserrat", 10), bd=0, highlightthickness=0).grid(row=0, column=6, padx=(0,5), pady=(0,0))
        Label(page1, text='Period',bg="#2E3138", fg="white", font=("montserrat", 10), bd=0, highlightthickness=0).grid(row=0, column=7, padx=(0,5), pady=(0,0))
        Label(page1, text='Duration',bg="#2E3138", fg="white", font=("montserrat", 10), bd=0, highlightthickness=0).grid(row=0, column=8, padx=(0,5), pady=(0,0))

        
        search_sym = Entry(page1, width=10, bg="#23252B", fg="white", font=("montserrat", 15), bd=0, highlightthickness=0, justify='center')
        search_sym.insert(END,'AAPL')
        search_sym.grid(row=1, column=6, sticky='n', padx=(0,5), pady=(0,0))

        search_per = Entry(page1, width=10, bg="#23252B", fg="white", font=("montserrat", 15), bd=0, highlightthickness=0, justify='center')
        search_per.insert(END,'months')
        search_per.grid(row=1, column=7, sticky='n', padx=(0,5), pady=(0,0))

        search_dur = Entry(page1, width=10, bg="#23252B", fg="white", font=("montserrat", 15), bd=0, highlightthickness=0, justify='center')
        search_dur.insert(END,1)
        search_dur.grid(row=1, column=8, sticky='n', padx=(0,5), pady=(0,0))

        def search(Event=None):
            nighclouds_mod = {
                "base_mpl_style": "dark_background",
                "marketcolors": {
                    'candle'  : {'up':'w', 'down':'#0095ff'},
                    'edge'    : {'up':'w', 'down':'#0095ff'},
                    'wick'    : {'up':'w', 'down':'w'},
                    'ohlc'    : {'up':'w', 'down':'w'},
                    'volume'  : {'up':'w', 'down':'#0095ff'},
                    'vcdopcod': False,
                    'alpha'   : 1.0,
                },
                "mavcolors": ('#40e0d0','#ff00ff','#ffd700','#1f77b4','#ff7f0e','#2ca02c','#e377c2'),
                "facecolor": '#0b0b0b',
                "gridcolor": '#2E3138',
                "gridstyle": "--",
                "y_on_right": False,
                "rc": {
                    'patch.linewidth': 1.0,
                    'lines.linewidth': 1.0,
                    "axes.grid": True,
                    "axes.grid.axis": "y",
                    "axes.edgecolor": "#474d56",
                    "axes.titlecolor": "red",
                    "figure.facecolor": "#2E3138",
                    "figure.titlesize": "x-large",
                    "figure.titleweight": "semibold",
                },
                "base_mpf_style": 'nightclouds',
            }
            symbol = search_sym.get()
            period = search_per.get()
            duration = int(search_dur.get())
            data = wrdsdata.get_data(symbol,period,duration)
            data = data[['datadate','Open','High','Low','Close','Volume']]
            data.index = pd.DatetimeIndex(data['datadate'])
            fig, ax1 = mpf.plot(data,type='candle',volume=True, style=nighclouds_mod,returnfig=True,figsize =(15,10))
            canvas = FigureCanvasTkAgg(fig, master=page1)
            canvas.get_tk_widget().grid(row=2, column=10)
            canvas.draw()

        style = ttk.Style(page1)
        style.theme_use("clam")
        style.configure("Treeview", background="#2E3138", fieldbackground="#2E3138", foreground="white")
        Button(page1, text="Search", command=search, height=1, fg="#2E3138", font=("montserrat", 8), bd=0, highlightthickness=0) .grid(row=1, column=9, sticky='n', padx=(0,5), pady=(2,0))

        
        interface.mainloop()