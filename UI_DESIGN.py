from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QCalendarWidget, QSpinBox, QTextEdit, QPushButton, QTableWidget, QHeaderView, QGroupBox, QStackedWidget, QRadioButton)

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve

class AppTKAngkasaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistem Manajemen TK Angkasa")
        self.setGeometry(100, 100, 1250, 850)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.init_login_ui()
        self.init_monitoring_ui()
        self.init_guru_ui()

    def init_login_ui(self):
        self.login_page = QWidget()
        layout = QVBoxLayout(self.login_page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_label = QLabel()
        pixmap = QPixmap("LOGO.png")
        if not pixmap.isNull():
            self.logo_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            self.logo_label.setText("LOGO TIDAK DITEMUKAN")
        self.logo_label.setStyleSheet("color: red; font-weight: bold;")

        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.logo_label)
    
        self.anim_logo = QPropertyAnimation(self.logo_label, b"geometry")
        self.anim_logo.setDuration(1200)
        self.anim_logo.setStartValue(QRect(625, 150, 0, 0)) 
        self.anim_logo.setEndValue(QRect(525, 50, 200, 200)) 
        self.anim_logo.setEasingCurve(QEasingCurve.Type.OutBack)

        box = QGroupBox("LOGIN SISTEM")
        box.setFixedWidth(350)
        bl = QVBoxLayout(box)
        self.user_input = QLineEdit(placeholderText="Username")
        self.pass_input = QLineEdit(placeholderText="Password", echoMode=QLineEdit.EchoMode.Password)
        self.radio_kepsek = QRadioButton("Kepala Sekolah"); self.radio_kepsek.setChecked(True)
        self.radio_guru = QRadioButton("Guru")
        self.btn_login = QPushButton("MASUK")
        self.btn_login.setStyleSheet("background-color: #27ae60; color: white; padding: 10px; font-weight: bold;")
        bl.addWidget(QLabel("Username:")); bl.addWidget(self.user_input)
        bl.addWidget(QLabel("Password:")); bl.addWidget(self.pass_input)
        bl.addWidget(self.radio_kepsek); bl.addWidget(self.radio_guru)
        bl.addWidget(self.btn_login)
        layout.addWidget(box)
        self.stacked_widget.addWidget(self.login_page)

    def init_monitoring_ui(self):
        self.monitor_page = QWidget()
        main_layout = QHBoxLayout(self.monitor_page)
        self.panel_input = QGroupBox("Form Evaluasi Kepsek")
        self.panel_input.setFixedWidth(320)
        fl = QVBoxLayout(self.panel_input)
        self.input_nama = QLineEdit(placeholderText="Nama Guru")
        self.combo_jabatan = QComboBox(); self.combo_jabatan.addItems(["Kelas A", "Kelas B", "Kelas C", "Pendamping"])
        self.kalender = QCalendarWidget(); self.kalender.setFixedHeight(180)
        self.combo_status = QComboBox(); self.combo_status.addItems(["Sangat Baik", "Baik", "Cukup", "Perlu Bimbingan"])
        self.spin_skor = QSpinBox(); self.spin_skor.setRange(0, 100)
        self.input_catatan = QTextEdit(placeholderText="Catatan..."); self.input_catatan.setMaximumHeight(80)
        self.btn_simpan = QPushButton("SIMPAN PENILAIAN")
        self.btn_simpan.setStyleSheet("background-color: #2980b9; color: white; font-weight: bold; padding: 10px;")
        fl.addWidget(self.input_nama); fl.addWidget(self.combo_jabatan); fl.addWidget(self.kalender); 
        fl.addWidget(self.combo_status); fl.addWidget(self.spin_skor); fl.addWidget(self.input_catatan); fl.addWidget(self.btn_simpan)

        right = QVBoxLayout()
        self.search_kinerja = QLineEdit(placeholderText="Cari Nama Guru...")
        self.tabel_data = QTableWidget(0, 6); self.tabel_data.setHorizontalHeaderLabels(["ID", "Nama", "Kelas", "Tgl", "Status", "Skor"])
        self.tabel_data.setColumnHidden(0, True); self.tabel_data.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.btn_hapus_kinerja = QPushButton("Hapus Kinerja Terpilih")
        self.btn_hapus_kinerja.setStyleSheet("background-color: #e74c3c; color: white;")
        
        self.search_materi = QLineEdit(placeholderText="Cari Materi Guru...")
        self.tabel_materi_guru = QTableWidget(0, 5); self.tabel_materi_guru.setHorizontalHeaderLabels(["ID", "Guru", "Tgl", "Judul", "Rencana"])
        self.tabel_materi_guru.setColumnHidden(0, True); self.tabel_materi_guru.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.btn_hapus_materi = QPushButton("Hapus Materi Terpilih")
        self.btn_hapus_materi.setStyleSheet("background-color: #e74c3c; color: white;")

        right.addWidget(QLabel("<h2>Dashboard Kepsek</h2>"))
        right.addWidget(QLabel("<b>DATA KINERJA</b>")); right.addWidget(self.search_kinerja); right.addWidget(self.tabel_data); right.addWidget(self.btn_hapus_kinerja)
        right.addWidget(QLabel("<b>LAPORAN MATERI</b>")); right.addWidget(self.search_materi); right.addWidget(self.tabel_materi_guru); right.addWidget(self.btn_hapus_materi)
        main_layout.addWidget(self.panel_input, 1); main_layout.addLayout(right, 2)
        self.stacked_widget.addWidget(self.monitor_page)

    def init_guru_ui(self):
        self.guru_page = QWidget()
        layout = QVBoxLayout(self.guru_page)
        box = QGroupBox("INPUT MATERI PEMBELAJARAN")
        box.setFixedWidth(500)
        gl = QVBoxLayout(box)
        self.input_nama_guru = QLineEdit(placeholderText="Nama Anda")
        self.tgl_materi = QCalendarWidget()
        self.judul_materi = QLineEdit(placeholderText="Tema/Judul")
        self.detail_materi = QTextEdit(placeholderText="Detail rencana...")
        self.btn_simpan_materi = QPushButton("KIRIM LAPORAN")
        self.btn_simpan_materi.setStyleSheet("background-color: #8e44ad; color: white; padding: 10px; font-weight: bold;")
        gl.addWidget(self.input_nama_guru); gl.addWidget(self.tgl_materi); gl.addWidget(self.judul_materi); gl.addWidget(self.detail_materi); gl.addWidget(self.btn_simpan_materi)
        layout.addWidget(box, alignment=Qt.AlignmentFlag.AlignCenter)
        self.stacked_widget.addWidget(self.guru_page)