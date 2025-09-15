import numpy as np

#SENSOR DATA
# Load only numeric columns (temperature, distance, battery, humidity)
data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(1,2,3,4))

temp = data[:,0]
dist = data[:,1]
bat  = data[:,2]
hum  = data[:,3]

print("SENSOR DATA RESULTS")
print("Temperature: mean =", np.mean(temp), ", min =", np.min(temp), ", max =", np.max(temp))
print("Distance: mean =", np.mean(dist), ", min =", np.min(dist), ", max =", np.max(dist))
print("Battery: mean =", np.mean(bat), ", min =", np.min(bat), ", max =", np.max(bat))
print("Humidity: mean =", np.mean(hum), ", min =", np.min(hum), ", max =", np.max(hum))

# Find time when temperature highest 
timestamps = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(0), dtype=str)
idx_max_temp = np.argmax(temp)
print("Time of max temperature:", timestamps[idx_max_temp])

# Count battery < 30
count_low_bat = np.sum(bat < 30)
print("Battery <30% occurred", count_low_bat, "times")


# ---------------- ROBOT PATH ---------------- #
# Load robot positions (x, y)
robot = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)

x = robot[:,0]
y = robot[:,1]

# Total distance traveled
dx = np.diff(x)
dy = np.diff(y)
step_dist = np.sqrt(dx**2 + dy**2)
total_dist = np.sum(step_dist)
print("\nROBOT DATA RESULTS")
print("Total distance traveled =", total_dist)

# Farthest point from origin
dist_origin = np.sqrt(x**2 + y**2)
idx_far = np.argmax(dist_origin)
print("Farthest point from origin =", (x[idx_far], y[idx_far]), " Distance =", dist_origin[idx_far])

# Check revisited positions 
coords = list(zip(x,y))
revisited = len(coords) != len(set(coords))
print("Revisited position?", revisited)



with open("results.txt", "w") as f:
    f.write("=== SENSOR DATA RESULTS ===\n")
    f.write(f"Temperature: mean={np.mean(temp)}, min={np.min(temp)}, max={np.max(temp)}\n")
    f.write(f"Distance: mean={np.mean(dist)}, min={np.min(dist)}, max={np.max(dist)}\n")
    f.write(f"Battery: mean={np.mean(bat)}, min={np.min(bat)}, max={np.max(bat)}\n")
    f.write(f"Humidity: mean={np.mean(hum)}, min={np.min(hum)}, max={np.max(hum)}\n")
    f.write(f"Time of max temperature: {timestamps[idx_max_temp]}\n")
    f.write(f"Battery <30% count: {count_low_bat}\n\n")

    f.write("=== ROBOT PATH RESULTS ===\n")
    f.write(f"Total distance traveled: {total_dist}\n")
    f.write(f"Farthest point from origin: (x={x[idx_far]}, y={y[idx_far]}), distance={dist_origin[idx_far]}\n")
    f.write(f"Revisited positions?: {revisited}\n")
print("Results saved in results.txt ✅")