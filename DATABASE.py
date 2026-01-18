import sqlite3

class DatabaseManager:
    def __init__(self):
        self.db_name = "tk_angkasa_db.sqlite"
        self.init_db()
    
    def init_db(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS kinerja_guru (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_guru TEXT, guru_kelas TEXT, tanggal TEXT,
                    status_kehadiran TEXT, skor_kinerja INTEGER, catatan TEXT
                )""")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS materi_pelajaran (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_guru TEXT, tanggal TEXT, judul_materi TEXT, detail_materi TEXT
                )""")
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database Error: {e}")

    def simpan_kinerja(self, nama, kelas, tgl, status, skor, catatan):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            query = "INSERT INTO kinerja_guru (nama_guru, guru_kelas, tanggal, status_kehadiran, skor_kinerja, catatan) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (nama, kelas, tgl, status, skor, catatan))
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Simpan Kinerja Error: {e}")
            return False

    def simpan_materi(self, nama, tgl, judul, detail):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            query = "INSERT INTO materi_pelajaran (nama_guru, tanggal, judul_materi, detail_materi) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (nama, tgl, judul, detail))
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Simpan Materi Error: {e}")
            return False

    def ambil_kinerja(self):
        conn = sqlite3.connect(self.db_name)
        res = conn.execute("SELECT id, nama_guru, guru_kelas, tanggal, status_kehadiran, skor_kinerja FROM kinerja_guru ORDER BY id DESC").fetchall()
        conn.close()
        return res

    def ambil_materi(self):
        conn = sqlite3.connect(self.db_name)
        res = conn.execute("SELECT id, nama_guru, tanggal, judul_materi, detail_materi FROM materi_pelajaran ORDER BY id DESC").fetchall()
        conn.close()
        return res

    def hapus_data(self, tabel, id_data):
        try:
            conn = sqlite3.connect(self.db_name)
            conn.execute(f"DELETE FROM {tabel} WHERE id = ?", (id_data,))
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Hapus Error: {e}")
            return False
