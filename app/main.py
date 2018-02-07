# -*- coding:utf-8 -*-
from tkinter import Tk, Toplevel, Button, Frame


class WeekeryApp(Tk):
    def __init__(self):
        super().__init__()
        self.canvas_show = 'frequency'  # or 'sleep'

        self.withdraw()
        splash = Splash(self)
        splash.pgb['maximum'] = 5

        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from tkinter.ttk import Progressbar, Style

        splash.pgb['value'] = 1
        splash.label.image = splash.gif1
        splash.update()

        plt.style.use('ggplot')
        matplotlib.use('TkAgg')
        matplotlib.rcParams['font.family'] = 'STSong'
        self.Set3 = plt.cm.Set3(range(10))
        self.Paired = plt.cm.Paired(range(10))

        splash.pgb['value'] = 2
        splash.label.image = splash.gif1
        splash.update()

        # +++++++++++++++
        # +  GUI_setup  +
        # +++++++++++++++
        from tkinter import Frame, Button, Text, END
        self.title('Weekery')
        Style().theme_use('vista')
        '''
        root
        |- Progressbar.bottom
        |- Frame_Left
        |  |- Frame_btn_left.top
        |  |  |- left(btn{d,w,m,y})
        |  |  |- right(btn{+,-})
        |  |  |- Frame_btn_mid
        |  |     |- <.left
        |  |     |- >.right
        |  |     |- calendar.middle
        |  |- fig_up.top
        |  |- fig_down.top
        |- Frame_Right
           |- Frame_btn_right
           |  |- btn_setting.right
           |  |- btn_reload.right
           |  |- btn_switch.left
           |- Text.bottom.top expand=both
        '''
        # ====== Frames ======
        self.frame_left = Frame(self)

        self.frame_right = Frame(self)

        self.frame_btn_left = Frame(self.frame_left)
        self.frame_btn_left.config(bg='white')
        self.frame_btn_mid = Frame(self.frame_btn_left)

        self.frame_btn_right = Frame(self.frame_right)
        self.frame_btn_right.config(bg='white')

        # ====== Buttons ======
        self.btn_days = Button(self.frame_btn_left, text='日', command=self.days)
        self.btn_days.config(bg='white')
        self.btn_weeks = Button(self.frame_btn_left, text='周', command=self.weeks)
        self.btn_weeks.config(bg='white')
        self.btn_months = Button(self.frame_btn_left, text='月', command=self.months)
        self.btn_months.config(bg='white')
        self.btn_years = Button(self.frame_btn_left, text='年', command=self.years)
        self.btn_years.config(bg='white')
        self.btn_plus = Button(self.frame_btn_left, text='十', command=self.plus)
        self.btn_plus.config(bg='white')
        self.btn_minus = Button(self.frame_btn_left, text='一', command=self.minus)
        self.btn_minus.config(bg='white')
        self.btn_switch = Button(self.frame_btn_left, text='睡眠|词频', command=self.switch)
        self.btn_switch.config(bg='white')

        self.btn_previous = Button(self.frame_btn_mid, text='《', command=self.previous)
        self.btn_previous.config(bg='white')
        self.btn_backward = Button(self.frame_btn_mid, text='》', command=self.backward)
        self.btn_backward.config(bg='white')
        self.btn_calendar = Button(self.frame_btn_mid, text="日历", command=self.ask_selected_date)
        self.btn_calendar.config(bg='white')

        self.btn_reload = Button(self.frame_btn_right, text='重载', command=self.reload)
        self.btn_reload.config(bg='white')
        self.btn_settings = Button(self.frame_btn_right, text='设置', command=self.settings)
        self.btn_settings.config(bg='white')

        # ====== Others ======
        self.fig_up = plt.figure(figsize=(7, 3))
        self.fig_down = plt.figure(figsize=(7, 3))
        self.canvas_up = FigureCanvasTkAgg(self.fig_up, master=self.frame_left)
        self.canvas_down = FigureCanvasTkAgg(self.fig_down, master=self.frame_left)

        self.pgb = Progressbar(self, orient='horizontal', length=1000, mode='determinate')

        self.notes = Text(self.frame_right, width=50)
        self.notes.config(bg='azure')
        self.notes.insert(END, '本周评价：A+ \n 【写作情况】\n 年终总结 \n ...')

        splash.pgb['value'] = 3
        splash.label.image = splash.gif1
        splash.update()

        # ++++++++++++++++++
        # +  GUI Packing   +
        # ++++++++++++++++++
        # level-1
        self.pgb.pack(side='bottom', fill='both')

        # level-1
        self.frame_left.pack(side='left', fill='both', expand='YES')
        # # level-2
        self.frame_btn_left.pack(side='top', fill='both')
        self.canvas_up.get_tk_widget().pack(side='top', fill='both', expand='YES')
        self.canvas_down.get_tk_widget().pack(side='top', fill='both', expand='YES')
        # # # level-3
        self.btn_days.pack(side='left')
        self.btn_weeks.pack(side='left')
        self.btn_months.pack(side='left')
        self.btn_years.pack(side='left')
        self.btn_switch.pack(side='right')
        self.btn_minus.pack(side='right')
        self.btn_plus.pack(side='right')
        self.frame_btn_mid.pack(side='top')
        # # # # level-4
        self.btn_previous.pack(side='left')
        self.btn_backward.pack(side='right')
        self.btn_calendar.pack(side='top')

        # level-1
        self.frame_right.pack(side='left', fill='both', expand='YES')
        # # level-2
        self.frame_btn_right.pack(side='top', fill='both')
        # # # level-3
        self.btn_settings.pack(side='right')
        self.btn_reload.pack(side='right')
        # # level-2
        self.notes.pack(side='top', fill='both', expand='YES')

        splash.pgb['value'] = 4
        splash.label.image = splash.gif1
        splash.update()

        # ++++++++++++++++++
        # +  Import class  +
        # ++++++++++++++++++
        import sqlite3
        from config import Config
        from controls import Controls
        from load_data import wiz_week_index, read_data
        splash.pgb['value'] = 5
        splash.label.image = splash.gif1
        splash.update()
        splash.destroy()
        # ============= Show Main GUI ==============
        self.protocol('WM_DELETE_WINDOW', self.close_window)
        self.wm_state('zoomed')  # maximize windows
        self.deiconify()

        self.cfg = Config(self)
        self.db_path = self.cfg.cache_dir + '/weekery.db'
        self.conn = sqlite3.connect(self.db_path)

        self.id_filenames, self.id_dates = wiz_week_index(self.cfg)

        if self.cfg.last_read == 20160000:
            read_data(self, self.cfg, self.pgb, self.id_dates, self.id_filenames, 'all')
        else:
            read_data(self, self.cfg, self.pgb, self.id_dates, self.id_filenames, dialog=False)

        self.controls = Controls(self.conn)
        self.conn.commit()

        self.colors = {v: (int(f[4:7])/255, int(f[9:12])/255, int(f[14:17])/255, 1) for f, v in self.cfg.color_kind.items()}

        self._paint()

    def ask_selected_date(self):
        select_calendar = CalendarPopup()
        self.wait_window(select_calendar)
        if select_calendar.selected_days:
            self.controls.y = int(select_calendar.selected_days.year)
            self.controls.m = int(select_calendar.selected_days.month)
            self.controls.w = int(select_calendar.selected_days.strftime("%W"))
            self.controls.d = int(select_calendar.selected_days.strftime("%d"))
            self.controls.date_range()
            self.controls.query_data()
            self._paint()

        return select_calendar.selected_days

    def days(self):
        self.controls.days()
        self._paint()

    def weeks(self):
        self.controls.weeks()
        self._paint()

    def months(self):
        self.controls.months()
        self._paint()

    def years(self):
        self.controls.years()
        self._paint()

    def previous(self):
        self.controls.previous()
        self._paint()

    def backward(self):
        self.controls.backward()
        self._paint()

    def plus(self):
        self.controls.plus()
        self._paint()

    def minus(self):
        self.controls.minus()
        self._paint()
    
    def switch(self):
        if self.canvas_show == 'frequency':
            self.canvas_show = 'sleep'
        elif self.canvas_show == 'sleep':
            self.canvas_show = 'frequency'
        else:
            pass
        self._paint()
    
    def _paint(self):
        kinds = self.controls.kinds
        sleep_condition = self.controls.sleep_condition
        frequency = self.controls.frequency
        notes = self.controls.notes

        # paint canvas_up
        axs = self.fig_up.add_subplot(111)
        axs.clear()
        ax1 = kinds.plot(kind='bar', ax=axs, legend=False, color=[self.colors['fun'],
                                                                  self.colors['rest'],
                                                                  self.colors['work'],
                                                                  self.colors['compel'],
                                                                  self.colors['useless'],
                                                                  self.colors['sleep']])
        ax1.set_ylabel('Hours')
        # ax1.set_xlabel('Month')
        ax1.xaxis.grid()
        ax1.set_xticklabels(kinds.index, rotation=0)
        # box = ax1.get_position()
        # ax1.set_position([box.x0, box.y0, box.width * 0.95, box.height])
        ax1.legend(loc='best', ncol=1, bbox_to_anchor=(1.0, 0.7))  # 0.96, 0.7
        self.fig_up.canvas.draw()

        # paint canvas_down
        if self.canvas_show == 'frequency':
            self.fig_down.clear()
            num = len(frequency)
            if num <= 4:
                row = 1
                col = num
            else:
                logging.error('number of x' + str(num) + ' axis out of range (8)')
                return
            # plot
            for i, key in enumerate(frequency):
                b = self.fig_down.add_subplot(row, col, i+1)
                week_label = key
                labels = frequency[key][0][:10]
                count = frequency[key][1][:10]
                b.set_title(week_label)

                if week_label == 'Summary':
                    b.pie(count, labels=labels, autopct=self.make_autopct(count), shadow=False, startangle=0, colors=self.Set3)
                else:
                    b.pie(count, labels=labels, autopct=self.make_autopct(count), shadow=False, startangle=0, colors=self.Paired)
                b.axis('equal')
                b.set_xlabel('(Top 10)')
                b.set_title(week_label)
            self.fig_down.canvas.draw()
        elif self.canvas_show == 'sleep':
            self.fig_down.clear()
            axes2 = self.fig_down.add_subplot(111)

            sl = len(sleep_condition.index)
            up = sleep_condition.dropna().values.max()
            down = sleep_condition.dropna().values.min()
            mean_st = sleep_condition.mean()['sleep_st']
            mean_ed = sleep_condition.mean()['sleep_ed']

            axes2.axhline(y=mean_st, linewidth=1, color='r')
            axes2.axhline(y=mean_ed, linewidth=1, color='g')

            axes2.text(0, mean_st - 0.3, '入睡：' + self._decimal_to_str(mean_st), color='r')
            axes2.text(0, mean_ed + 0.5, '起床：' + self._decimal_to_str(mean_ed), color='g')

            axes2.set_xlim(0, sl + 1)
            axes2.set_ylim(down - 1, up + 1)
            axes2.set_xticks(list(range(1, sl + 1)))
            axes2.set_xticklabels(list(sleep_condition.index))
            axes2.set_yticks(list(range(int(math.floor(down)), int(math.ceil(up + 1)))))
            ticks = axes2.get_yticks()
            axes2.set_yticklabels([str(i) + ':00' if i >= 0 else str(24 + i) + ':00' for i in ticks])

            patches = []
            for i, sid in enumerate(sleep_condition.index):
                st = sleep_condition.loc[sid]['sleep_st']
                ed = sleep_condition.loc[sid]['sleep_ed']
                div = ed - st
                if div == np.nan:
                    continue
                fancy_box = mpatches.FancyBboxPatch([i + 1, st], 0.1, div, color='yellow')
                axes2.text(i + 0.95, st + div / 2, str(round(div, 1)) + 'h')
                patches.append(fancy_box)

            collection = PatchCollection(patches, facecolors='gray', alpha=0.6)
            axes2.add_collection(collection)
            axes2.invert_yaxis()

            self.fig_down.canvas.draw()

        # refresh note board

    def reload(self):
        ans = askyesno('警告', '重新读取所有数据？')
        if ans:
            read_data(self, self.cfg, self.pgb, self.id_dates, self.id_filenames, 'all', dialog=False)
            showinfo('提示', '重新读取数据完成！')
            self.weeks()
    
    @staticmethod
    def settings():
        showinfo('提示', '开发中，敬请期待')

    @staticmethod
    def close_window():
        ans = askyesno('提示', '确认退出？')
        if ans:
            sys.exit()
        else:
            return

    @staticmethod
    def _decimal_to_str(t):
        minute, hour = math.modf(t)
        if t < 0:
            hour = int(24 + hour)
        else:
            hour = int(hour)

        minute = round(minute * 60)
        t_str = str(hour) + ':' + str(minute)
        return t_str

    @staticmethod
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            # return '{p:1.1f}%({v:1.1f}h)'.format(p=pct, v=val/2)
            return '{v:1.1f}h'.format(p=pct, v=val / 2)
        return my_autopct


class Splash(Toplevel):
    def __init__(self, parent):
        from tkinter import  Label, PhotoImage
        from tkinter.ttk import Progressbar

        Toplevel.__init__(self, parent)
        self.title("Splash")
        self.overrideredirect(True)

        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        width = round(screenwidth / 30) * 10
        height = round(screenheight / 30) * 10

        from timg import img
        self.gif1 = PhotoImage(data=img)
        self.gif1 = self.gif1.subsample(3,3)
        self.label = Label(self, image=self.gif1)
        self.label.config(width=width, height=height-20, bg='white', bd=1)

        self.pgb = Progressbar(self, orient='horizontal', length=width, mode='determinate')

        self.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2))

        self.label.pack(side='top', fill='both')
        self.pgb.pack(side='bottom', fill='both')

        # required to make window show before the program gets to the mainloop
        self.update()


class CalendarPopup(Toplevel):
    def __init__(self):
        self.selected_days = None
        super().__init__()
        self.title('选择日期')

        self.frame_cal = Frame(self)

        self.calendar = Calendar(self.frame_cal, firstweekday=calendar.MONDAY)
        self.btnselect = Button(self.frame_cal, text="选择", command=self.select_focus_days)

        self.btnselect.pack(side="bottom")
        self.calendar.pack(expand=1, fill='both')

        self.frame_cal.pack()

    def select_focus_days(self):
        back = Calendar.selection(self.calendar)
        if back:
            self.selected_days = back
        self.destroy()


if __name__ == '__main__':
    try:
        app = WeekeryApp()
        import math
        import numpy as np
        import matplotlib.patches as mpatches
        import matplotlib.pyplot as plt
        import calendar
        import sys
        from calendar4wiz import Calendar
        from matplotlib.collections import PatchCollection
        from load_data import read_data
        from tkinter.messagebox import showinfo, askyesno
        app.mainloop()
    except Exception as e:
        import sys
        import logging
        import traceback
        from tkinter.messagebox import showinfo
        logging.exception('opps', exc_info=e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        showinfo('报错', ''.join(line for line in lines))
