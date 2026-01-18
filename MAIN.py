import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from DATABASE import DatabaseManager
from UI_DESIGN import AppTKAngkasaUI

class Controller(AppTKAngkasaUI):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        
        # Hubungkan Login
        self.btn_login.clicked.connect(self.cek_login)
        # Hubungkan Simpan
        self.btn_simpan.clicked.connect(self.proses_simpan_penilaian)
        self.btn_simpan_materi.clicked.connect(self.proses_simpan_materi)
        # Hubungkan Hapus
        self.btn_hapus_kinerja.clicked.connect(lambda: self.proses_hapus("kinerja_guru", self.tabel_data))
        self.btn_hapus_materi.clicked.connect(lambda: self.proses_hapus("materi_pelajaran", self.tabel_materi_guru))
        # Hubungkan Pencarian
        self.search_kinerja.textChanged.connect(lambda t: self.filter_table(self.tabel_data, t))
        self.search_materi.textChanged.connect(lambda t: self.filter_table(self.tabel_materi_guru, t))
        
        self.anim_logo.start()
    
    def tampilkan_info(self):
        QMessageBox.about(self, "Tentang Aplikasi",
                          "Sistem Manajemen TK Angkasa\nVersi 1.0\nDikembangkan untuk UAS Praktikum Pemograman Visual.")

    def cek_login(self):
        u, p = self.user_input.text(), self.pass_input.text()
        if self.radio_kepsek.isChecked() and u == "angkasa" and p == "123":
            self.stacked_widget.setCurrentIndex(1)
            self.refresh_all_tables()
        elif self.radio_guru.isChecked() and u == "guru" and p == "guru123":
            self.stacked_widget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Gagal", "User/Pass salah!")

    def refresh_all_tables(self):
        self.tabel_data.setRowCount(0)
        for r_idx, r_data in enumerate(self.db.ambil_kinerja()):
            self.tabel_data.insertRow(r_idx)
            for c_idx, data in enumerate(r_data):
                self.tabel_data.setItem(r_idx, c_idx, QTableWidgetItem(str(data)))
        
        self.tabel_materi_guru.setRowCount(0)
        for r_idx, r_data in enumerate(self.db.ambil_materi()):
            self.tabel_materi_guru.insertRow(r_idx)
            for c_idx, data in enumerate(r_data):
                self.tabel_materi_guru.setItem(r_idx, c_idx, QTableWidgetItem(str(data)))

    def proses_simpan_penilaian(self):
        nama = self.input_nama.text()
        if not nama: return
        if self.db.simpan_kinerja(nama, self.combo_jabatan.currentText(), self.kalender.selectedDate().toString("yyyy-MM-dd"),
                                  self.combo_status.currentText(), self.spin_skor.value(), self.input_catatan.toPlainText()):
            QMessageBox.information(self, "Sukses", "Data Disimpan!")
            self.refresh_all_tables()
            self.input_nama.clear()

    def proses_simpan_materi(self):
        nama = self.input_nama_guru.text()
        if not nama: return
        if self.db.simpan_materi(nama, self.tgl_materi.selectedDate().toString("yyyy-MM-dd"), self.judul_materi.text(), self.detail_materi.toPlainText()):
            QMessageBox.information(self, "Sukses", "Materi Terkirim!")
            self.input_nama_guru.clear()

    def proses_hapus(self, table_name, table_widget):
        row = table_widget.currentRow()
        if row < 0: return
        id_data = table_widget.item(row, 0).text()
        if QMessageBox.question(self, "Hapus", "Yakin hapus?") == QMessageBox.StandardButton.Yes:
            if self.db.hapus_data(table_name, id_data):
                self.refresh_all_tables()

    def filter_table(self, table, text):
        for i in range(table.rowCount()):
            item = table.item(i, 1)
            table.setRowHidden(i, text.lower() not in item.text().lower() if item else False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec())
