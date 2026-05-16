import sqlite3
import json
import os

def get_latest_proposal():
    try:
        conn = sqlite3.connect('database_layer/shared_memory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT content FROM proposals ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        conn.close()

        if row:
            raw_content = row[0]
            return json.loads(raw_content)
        return None
    except Exception as e:
        print(f"❌ خطأ في معالجة البيانات: {e}")
        return None

def check_and_run():
    proposal = get_latest_proposal()
    if proposal:
        print(f"✅ تم تحميل المقترح بنجاح: {proposal.get('status', 'N/A')}")
    else:
        print("📭 لا توجد مقترحات جديدة في قاعدة البيانات.")

if __name__ == '__main__':
    check_and_run()
