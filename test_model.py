import joblib
import pandas as pd
import time
import psutil
import os
model = joblib.load("gb_ids_model.pkl")
data = pd.read_csv("deployment_test.csv")
start = time.time()
end = time.time()
model_size = os.path.getsize("gb_ids_model.pkl") / 1024
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
predictions = model.predict(data)
print("predictions:", predictions)
print("inference Time:", end - start, "seconds")
print("model Size:", model_size, "KB")
print("CPU Usage:", cpu_usage, "%")
print("Memory Usage:", memory_usage, "%")
print(predictions)
print("model loaded sucessfully!")
