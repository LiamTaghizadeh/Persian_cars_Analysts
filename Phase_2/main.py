import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform

import sqlite3
import csv
import io
import os
from datetime import datetime

# ============================================================
# کلاس مدیریت دیتابیس
# ============================================================
class Database:
    def __init__(self):
        if platform == 'android':
            from android.storage import app_storage_path
            self.db_path = os.path.join(app_storage_path(), 'cars.db')
        else:
            self.db_path = 'cars.db'
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Year INTEGER,
                Shamsi_Year INTEGER,
                Manufacturer TEXT,
                Model TEXT,
                Fuel_Type TEXT,
                Engine_Type TEXT,
                Power_hp REAL,
                Torque_Nm REAL,
                Fuel_Consumption_L100km REAL,
                Acceleration_0_100_s REAL,
                Top_Speed_kmh REAL,
                CO2_Emission_g_km REAL,
                Emission_Standard TEXT,
                Score REAL,
                Key_Options TEXT,
                Image_URL TEXT,
                UNIQUE(Year, Manufacturer, Model)
            )
        ''')
        conn.commit()
        conn.close()
    
    def get_count(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM cars')
        count = c.fetchone()[0]
        conn.close()
        return count
    
    def insert_car(self, data):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        try:
            c.execute('''
                INSERT OR REPLACE INTO cars (
                    Year, Shamsi_Year, Manufacturer, Model, Fuel_Type,
                    Engine_Type, Power_hp, Torque_Nm, Fuel_Consumption_L100km,
                    Acceleration_0_100_s, Top_Speed_kmh, CO2_Emission_g_km,
                    Emission_Standard, Score, Key_Options, Image_URL
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data.get('Year'), data.get('Shamsi_Year'), data.get('Manufacturer'),
                data.get('Model'), data.get('Fuel_Type'), data.get('Engine_Type'),
                data.get('Power_hp'), data.get('Torque_Nm'),
                data.get('Fuel_Consumption_L100km'), data.get('Acceleration_0_100_s'),
                data.get('Top_Speed_kmh'), data.get('CO2_Emission_g_km'),
                data.get('Emission_Standard'), data.get('Score'),
                data.get('Key_Options'), data.get('Image_URL')
            ))
            conn.commit()
        except Exception as e:
            print(f"Error inserting: {e}")
        finally:
            conn.close()
    
    def get_all_cars(self, filter_by=None, search_term=None):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        query = 'SELECT * FROM cars'
        params = []
        
        if filter_by and search_term:
            if filter_by == 'Manufacturer':
                query += ' WHERE Manufacturer LIKE ?'
                params.append(f'%{search_term}%')
            elif filter_by == 'Model':
                query += ' WHERE Model LIKE ?'
                params.append(f'%{search_term}%')
            elif filter_by == 'Fuel_Type':
                query += ' WHERE Fuel_Type LIKE ?'
                params.append(f'%{search_term}%')
        
        query += ' ORDER BY Year DESC, Manufacturer, Model'
        c.execute(query, params)
        rows = c.fetchall()
        conn.close()
        
        # تبدیل به لیست دیکشنری
        columns = ['id', 'Year', 'Shamsi_Year', 'Manufacturer', 'Model',
                   'Fuel_Type', 'Engine_Type', 'Power_hp', 'Torque_Nm',
                   'Fuel_Consumption_L100km', 'Acceleration_0_100_s',
                   'Top_Speed_kmh', 'CO2_Emission_g_km', 'Emission_Standard',
                   'Score', 'Key_Options', 'Image_URL']
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))
        return result
    
    def get_manufacturers(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT DISTINCT Manufacturer FROM cars ORDER BY Manufacturer')
        rows = c.fetchall()
        conn.close()
        return [r[0] for r in rows]


# ============================================================
# ویجت کارت نمایش خودرو
# ============================================================
class CarCard(BoxLayout):
    def __init__(self, car_data, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = 280
        self.padding = 10
        self.spacing = 5
        
        # کانتینر اصلی با حاشیه و پس‌زمینه
        container = BoxLayout(orientation='vertical', padding=10, spacing=5)
        container.size_hint_y = None
        container.height = 260
        
        # ردیف بالا: تصویر + اطلاعات اصلی
        top_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=140, spacing=10)
        
        # تصویر
        if car_data.get('Image_URL') and car_data['Image_URL'] != 'N/A':
            img = AsyncImage(source=car_data['Image_URL'], size_hint_x=0.35)
        else:
            img = Label(text='🚗\nNo Image', size_hint_x=0.35, font_size=30)
        top_row.add_widget(img)
        
        # اطلاعات اصلی
        info_box = BoxLayout(orientation='vertical', size_hint_x=0.65, spacing=3)
        info_box.add_widget(Label(
            text=f"[b]{car_data['Manufacturer']} - {car_data['Model']}[/b]",
            markup=True, font_size=16, size_hint_y=None, height=30, halign='left'
        ))
        info_box.add_widget(Label(
            text=f"سال: {car_data['Shamsi_Year']} ({car_data['Year']})",
            font_size=13, size_hint_y=None, height=25, halign='left'
        ))
        info_box.add_widget(Label(
            text=f"سوخت: {car_data['Fuel_Type']}",
            font_size=13, size_hint_y=None, height=25, halign='left'
        ))
        info_box.add_widget(Label(
            text=f"امتیاز: {'⭐' * int(car_data['Score'])} {car_data['Score']}/10",
            font_size=13, size_hint_y=None, height=25, halign='left'
        ))
        top_row.add_widget(info_box)
        container.add_widget(top_row)
        
        # ردیف پایین: مشخصات فنی
        specs_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=5)
        
        specs = [
            f"⚡ {car_data['Power_hp']}hp",
            f"🔧 {car_data['Torque_Nm']}Nm",
            f"⛽ {car_data['Fuel_Consumption_L100km']}L/100km",
            f"🚀 {car_data['Acceleration_0_100_s']}s",
            f"💨 {car_data['Top_Speed_kmh']}km/h"
        ]
        
        for spec in specs:
            specs_row.add_widget(Label(
                text=spec, font_size=12, size_hint_x=0.2,
                halign='center', valign='middle'
            ))
        
        container.add_widget(specs_row)
        
        # موتور
        container.add_widget(Label(
            text=f"موتور: {car_data['Engine_Type']}",
            font_size=11, size_hint_y=None, height=25,
            halign='left', color=(0.6, 0.6, 0.6, 1)
        ))
        
        # امکانات
        if car_data.get('Key_Options') and car_data['Key_Options'] != 'N/A':
            container.add_widget(Label(
                text=f"امکانات: {car_data['Key_Options'][:60]}...",
                font_size=11, size_hint_y=None, height=25,
                halign='left', color=(0.5, 0.5, 0.8, 1)
            ))
        
        self.add_widget(container)


# ============================================================
# صفحه اصلی برنامه
# ============================================================
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.db = Database()
        self.all_cars = []
        self.filtered_cars = []
        
        # هدر
        header = BoxLayout(size_hint_y=None, height=60, padding=10, spacing=10)
        header.add_widget(Label(
            text="🚗 خودروهای ایرانی ۱۳۸۰–۱۴۰۵",
            font_size=20, bold=True, size_hint_x=0.7
        ))
        
        # دکمه به‌روزرسانی
        self.update_btn = Button(text="🔄 بروزرسانی", size_hint_x=0.3, background_color=(0.2, 0.6, 0.2, 1))
        self.update_btn.bind(on_press=self.update_data)
        header.add_widget(self.update_btn)
        self.add_widget(header)
        
        # نوار جستجو و فیلتر
        filter_row = BoxLayout(size_hint_y=None, height=50, padding=10, spacing=10)
        
        self.search_input = TextInput(hint_text='جستجو...', size_hint_x=0.5, multiline=False)
        filter_row.add_widget(self.search_input)
        
        self.filter_spinner = Spinner(
            text='همه',
            values=['همه', 'Manufacturer', 'Model', 'Fuel_Type'],
            size_hint_x=0.25
        )
        filter_row.add_widget(self.filter_spinner)
        
        search_btn = Button(text='🔍', size_hint_x=0.15)
        search_btn.bind(on_press=self.do_search)
        filter_row.add_widget(search_btn)
        
        clear_btn = Button(text='✕', size_hint_x=0.1, background_color=(0.8, 0.2, 0.2, 1))
        clear_btn.bind(on_press=self.clear_search)
        filter_row.add_widget(clear_btn)
        
        self.add_widget(filter_row)
        
        # نمایش تعداد
        self.count_label = Label(text="تعداد: ۰ خودرو", size_hint_y=None, height=30, font_size=14)
        self.add_widget(self.count_label)
        
        # لیست خودروها (اسکرول‌دار)
        scroll = ScrollView()
        self.car_list = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.car_list.bind(minimum_height=self.car_list.setter('height'))
        scroll.add_widget(self.car_list)
        self.add_widget(scroll)
        
        # بارگذاری اولیه
        Clock.schedule_once(self.load_data, 0.5)
    
    def load_data(self, dt):
        count = self.db.get_count()
        if count == 0:
            self.show_loading_popup("در حال بارگذاری داده‌ها از سرور...")
            self.download_csv()
        else:
            self.all_cars = self.db.get_all_cars()
            self.filtered_cars = self.all_cars
            self.display_cars()
    
    def download_csv(self):
        url = 'https://raw.githubusercontent.com/LiamTaghizadeh/Persian_cars_Analysts/main/Phase_1/iranian_cars_final.csv'
        req = UrlRequest(url, self.on_csv_downloaded, on_failure=self.on_download_fail)
    
    def on_csv_downloaded(self, req, result):
        self.close_popup()
        try:
            # پردازش CSV
            data = result.decode('utf-8')
            reader = csv.DictReader(io.StringIO(data))
            
            count = 0
            for row in reader:
                car_data = {
                    'Year': int(row.get('Year', 0)) if row.get('Year', '').strip() else 0,
                    'Shamsi_Year': int(row.get('Shamsi_Year', 0)) if row.get('Shamsi_Year', '').strip() else 0,
                    'Manufacturer': row.get('Manufacturer', '').strip(),
                    'Model': row.get('Model', '').strip(),
                    'Fuel_Type': row.get('Fuel_Type', '').strip(),
                    'Engine_Type': row.get('Engine_Type', '').strip(),
                    'Power_hp': float(row.get('Power_hp', 0)) if row.get('Power_hp', '').strip() else 0,
                    'Torque_Nm': float(row.get('Torque_Nm', 0)) if row.get('Torque_Nm', '').strip() else 0,
                    'Fuel_Consumption_L100km': float(row.get('Fuel_Consumption_L100km', 0)) if row.get('Fuel_Consumption_L100km', '').strip() else 0,
                    'Acceleration_0_100_s': float(row.get('Acceleration_0_100_s', 0)) if row.get('Acceleration_0_100_s', '').strip() else 0,
                    'Top_Speed_kmh': float(row.get('Top_Speed_kmh', 0)) if row.get('Top_Speed_kmh', '').strip() else 0,
                    'CO2_Emission_g_km': float(row.get('CO2_Emission_g_km', 0)) if row.get('CO2_Emission_g_km', '').strip() else 0,
                    'Emission_Standard': row.get('Emission_Standard', '').strip(),
                    'Score': float(row.get('Score', 0)) if row.get('Score', '').strip() else 0,
                    'Key_Options': row.get('Key_Options', '').strip(),
                    'Image_URL': row.get('Image_URL', '').strip()
                }
                self.db.insert_car(car_data)
                count += 1
            
            self.all_cars = self.db.get_all_cars()
            self.filtered_cars = self.all_cars
            self.display_cars()
            
            # ذخیره زمان آخرین بروزرسانی
            store = JsonStore('settings.json')
            store.put('last_update', time=datetime.now().isoformat())
            
        except Exception as e:
            self.show_error_popup(f"خطا در خواندن داده‌ها: {str(e)}")
    
    def on_download_fail(self, req, error):
        self.close_popup()
        self.show_error_popup(f"خطا در دانلود داده‌ها: {error}")
    
    def update_data(self, instance):
        self.show_loading_popup("در حال بروزرسانی داده‌ها...")
        self.download_csv()
    
    def display_cars(self):
        self.car_list.clear_widgets()
        if not self.filtered_cars:
            self.car_list.add_widget(Label(
                text="هیچ خودرویی یافت نشد",
                font_size=18, color=(0.5, 0.5, 0.5, 1)
            ))
            self.count_label.text = "تعداد: ۰ خودرو"
            return
        
        for car in self.filtered_cars:
            card = CarCard(car)
            self.car_list.add_widget(card)
        
        self.count_label.text = f"تعداد: {len(self.filtered_cars)} خودرو"
    
    def do_search(self, instance):
        search_text = self.search_input.text.strip()
        filter_type = self.filter_spinner.text
        
        if not search_text:
            self.filtered_cars = self.all_cars
        else:
            if filter_type == 'همه':
                self.filtered_cars = self.db.get_all_cars()
                # جستجوی دستی در تمام فیلدها
                search_text_lower = search_text.lower()
                self.filtered_cars = [
                    c for c in self.filtered_cars
                    if search_text_lower in str(c.get('Manufacturer', '')).lower()
                    or search_text_lower in str(c.get('Model', '')).lower()
                    or search_text_lower in str(c.get('Fuel_Type', '')).lower()
                    or search_text_lower in str(c.get('Engine_Type', '')).lower()
                ]
            else:
                # fillters
              filter_map = {
                    'Manufacturer': 'Manufacturer',
                    'Model': 'Model',
                    'Fuel_Type': 'Fuel_Type'
                }
                col = filter_map.get(filter_type, 'Manufacturer')
                self.filtered_cars = self.db.get_all_cars(filter_by=col, search_term=search_text)
        
        self.display_cars()
    
    def clear_search(self, instance):
        self.search_input.text = ''
        self.filter_spinner.text = 'همه'
        self.filtered_cars = self.all_cars
        self.display_cars()
    
    # ============================================================
    # Popup
    # ============================================================
    def show_loading_popup(self, message):
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        content.add_widget(Label(text=message, font_size=14))
        pb = ProgressBar(size_hint_y=None, height=30)
        content.add_widget(pb)
        self.loading_popup = Popup(title="لطفاً صبر کنید", content=content, size_hint=(0.7, 0.3))
        self.loading_popup.open()
    
    def close_popup(self):
        if hasattr(self, 'loading_popup'):
            self.loading_popup.dismiss()
    
    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        content.add_widget(Label(text=message, font_size=14))
        btn = Button(text='باشه', size_hint_y=None, height=50)
        popup = Popup(title="خطا", content=content, size_hint=(0.8, 0.4))
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()


# ============================================================
# main class
# ============================================================
class PersianCarsApp(App):
    def build(self):
        self.title = 'خودروهای ایرانی'
        return MainScreen()
    
    def on_start(self):
        # rtlا
        from kivy.core.text import LabelBase
        LabelBase.register(name='CustomFont', fn_regular='DejaVuSans.ttf')


if __name__ == '__main__':
    PersianCarsApp().run()
