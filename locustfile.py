"""
OptiCrop Load Test Script (Locust)
----------------------------------
Tests the /predict endpoint of your deployed OptiCrop app using realistic
form values matching your actual input fields (nitrogen, phosphorus,
potassium, ph, temperature, humidity, rainfall).

SETUP:
  pip install locust

RUN (headless, 20 virtual users, spawn 5/sec, for 60 seconds):
  locust -f locustfile.py --host=https://YOUR-APP.vercel.app \
         --headless -u 20 -r 5 -t 60s --csv=results

This produces:
  results_stats.csv          -> avg/max response time, requests/sec, failures
  results_stats_history.csv  -> stats over time
  results_failures.csv       -> any failed requests

WHAT TO DO WITH THE OUTPUT:
  Open results_stats.csv and find the row for "/predict". Report to me:
    - Average Response Time (ms)
    - Max Response Time (ms)
    - Requests/s
    - Failure count / Failure %
  I'll convert these into the Performance Testing form (seconds, pass/fail
  vs targets, etc.)

OPTIONAL - Web UI instead of headless:
  locust -f locustfile.py --host=https://YOUR-APP.vercel.app
  Then open http://localhost:8089 in your browser, set users/spawn rate,
  and click Start. Charts and stats are shown live and can be screenshotted
  directly for Step 5 (Screenshots / Evidence) of the form.
"""

import random
from locust import HttpUser, task, between


class OptiCropUser(HttpUser):
    # Simulates a farmer pausing 1-3 seconds between actions, like real usage
    wait_time = between(1, 3)

    @task
    def submit_prediction(self):
        payload = {
            "nitrogen": round(random.uniform(0, 140), 1),
            "phosphorus": round(random.uniform(0, 145), 1),
            "potassium": round(random.uniform(0, 205), 1),
            "ph": round(random.uniform(3.5, 9.5), 2),
            "temperature": round(random.uniform(10, 40), 1),
            "humidity": round(random.uniform(20, 100), 1),
            "rainfall": round(random.uniform(20, 300), 1),
        }
        with self.client.post("/predict", data=payload, catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure(f"Got status code {resp.status_code}")

    @task(1)
    def load_home_page(self):
        # Also test the input form page itself, not just the API
        self.client.get("/")
