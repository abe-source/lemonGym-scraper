from itemadapter import ItemAdapter
import sqlite3

class LemongymBusynessScraperPipeline:
    def __init__ (self):
        self.con = sqlite3.connect('lgymOcc.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS busyness(
        timeStamp TEXT PRIMARY KEY,
        antakalnis INTEGER,
        banginis INTEGER,
        europa INTEGER,
        fabijoniskes INTEGER,
        perkunkiemis INTEGER,
        pilaite INTEGER,
        savanoriai INTEGER,
        silainiai INTEGER,
        zalgirioArena INTEGER
        )""")    

    def process_item(self, item, spider):
        self.cur.execute("""INSERT INTO busyness VALUES (?,?,?,?,?,?,?,?,?,?)""",
                    (item['timeStamp'],
                     item['antakalnis'],
                     item['banginis'],
                     item['europa'],
                     item['fabijoniskes'],
                     item['perkunkiemis'],
                     item['pilaite'],
                     item['savanoriai'],
                     item['silainiai'],
                     item['zalgirioArena']))
        self.con.commit()
        return item