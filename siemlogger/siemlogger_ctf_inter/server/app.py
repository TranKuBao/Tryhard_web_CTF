from flask import Flask, request, render_template, jsonify
import re
import os
import requests

app = Flask(__name__)

ALLOWED_DOMAIN = "intranet.ctf.cert.unlp.edu.ar"
domain_regex = re.compile(rf"^{re.escape(ALLOWED_DOMAIN)}")
flag = os.environ.get('FLAG', 'flag{fakeflag}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_flag', methods=['POST'])
def send_flag():
    target_domain = request.form.get('domain', '')

    if not domain_regex.match(target_domain):
        return jsonify({"error": "Invalid domain"}), 400
    try:
        siem_response = send_to_siem(target_domain)
        return jsonify({"success": "Flag sent successfully", "domain": target_domain, "siem_response": siem_response})
    except Exception as e:
        return jsonify({"error": f"Error sending flag: {e}"}), 500


def send_to_siem(domain):
    global flag
    data = {
        "domain": domain
    }                                                  # ↓ we are good people
    response = requests.post(f"https://{domain}/siem", verify=False, allow_redirects=False, json=data, headers={"Flag": flag})
    return "Log received"
    

@app.route('/siem', methods=['POST'])
def siem():
    data = request.get_json()
    print(f"[SIEM] Received: {data}")
    return jsonify({"status": "Received in SIEM", "data": data})

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
