from flask import Flask, request, jsonify
from tool import run as run_numerology_astrology
from lasotuvi.app import lapDiaBan, lapThienBan, format_thien_ban, format_cung_data
from lasotuvi.DiaBan import diaBan

app = Flask(__name__)

@app.route('/')
def home():
    return {"status": "Mystic API running"}

@app.route('/api/profile', methods=['POST'])
def profile():
    try:
        data = request.get_json()

        required_fields = ['name', 'birth_date', 'birth_time', 'birth_place', 'gender']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        name = data['name']
        birth_date = data['birth_date']
        birth_time = data['birth_time']
        birth_place = data['birth_place']
        gender_str = data['gender'].strip().lower()
        gioiTinh = 1 if gender_str == 'nam' else 0

        # === TÍNH THẦN SỐ HỌC + CHIÊM TINH ===
        result_text = run_numerology_astrology({
            'name': name,
            'birth_date': birth_date,
            'birth_time': birth_time,
            'birth_place': birth_place
        })

        # === TÍNH TỬ VI ===
        dd, mm, yyyy = map(int, birth_date.split('/'))
        hh, mi = map(int, birth_time.split(':'))

        gio_map = {
            23: 1, 0: 1, 1: 2, 2: 2, 3: 3, 4: 3,
            5: 4, 6: 4, 7: 5, 8: 5, 9: 6, 10: 6,
            11: 7, 12: 7, 13: 8, 14: 8, 15: 9, 16: 9,
            17: 10, 18: 10, 19: 11, 20: 11, 21: 12, 22: 12
        }
        gioSinh = gio_map.get(hh, 1)

        try:
            diaban = lapDiaBan(diaBan, nn=dd, tt=mm, nnnn=yyyy, gioSinh=gioSinh, gioiTinh=gioiTinh, duongLich=1, timeZone=7)
        except Exception as e:
            return jsonify({"error": f"Lỗi khi lập Địa Bàn: {str(e)}"}), 400

        try:
            thienban = lapThienBan(nn=dd, tt=mm, nnnn=yyyy, gioSinh=gioSinh, gioiTinh=gioiTinh, ten=name, diaBan=diaban)
        except Exception as e:
            return jsonify({"error": f"Lỗi khi lập Thiên Bàn: {str(e)}"}), 400

        try:
            if not hasattr(diaban, 'thapNhiCung') or not diaban.thapNhiCung:
                return jsonify({"error": "Không tìm thấy dữ liệu 12 cung trong Địa Bàn"}), 400

            thienban_text = format_thien_ban(thienban.__dict__)
            cung_data_text = format_cung_data(diaban.thapNhiCung)
            tuvi_text = f"{thienban_text}\n{cung_data_text}"
        except Exception as e:
            return jsonify({"error": f"Lỗi khi xử lý dữ liệu Tử Vi: {str(e)}"}), 400

        return jsonify({
            "result": result_text,
            "tuvi": tuvi_text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
