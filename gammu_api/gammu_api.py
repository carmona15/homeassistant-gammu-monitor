from fastapi import FastAPI
import subprocess
import json

app = FastAPI()

@app.get("/status")
def read_status():
    result = subprocess.run(["gammu-smsd-monitor", "-n", "1", "-d", "0"], capture_output=True, text=True)
    output = result.stdout
    data = {
        "imei": output.split("IMEI: ")[1].split("\n")[0],
        "imsi": output.split("IMSI: ")[1].split("\n")[0],
        "sent": int(output.split("Sent: ")[1].split("\n")[0]),
        "received": int(output.split("Received: ")[1].split("\n")[0]),
        "failed": int(output.split("Failed: ")[1].split("\n")[0]),
        "signal": int(output.split("NetworkSignal: ")[1].split("\n")[0]),
    }
    return data

@app.get("/ping")
def ping():
    return {"status": "ok"}
