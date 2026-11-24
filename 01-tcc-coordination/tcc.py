
# sets the curve shape for the relay
curve_settings = {
    "IEEE Moderate":  {"A":0.0515, "B":0.114, "p":0.02},
    "IEEE High":      {"A":19.61, "B":0.491, "p":2},
    "IEEE Extreme":   {"A":28.2, "B":0.1217, "p":2},
    "SEL Moderate":   {"A":0.0104, "B":0.0226, "p":0.02},
    "SEL CO-8":       {"A":5.95, "B":0.18, "p":2},
    "SEL High":       {"A":3.88, "B":0.0963, "p":2},
}

def trip_time(current, pickup, td, curve):
    M = current/pickup
    if M <= 1:
        return float('inf')  # No trip if current is below pickup
    A = curve_settings[curve]["A"]
    B = curve_settings[curve]["B"]
    p = curve_settings[curve]["p"]
    t = td * (A/(M**p - 1) + B)
    return t

def main():
    print(trip_time(2000, 400, 1, "IEEE Moderate"))


if __name__ == "__main__":
    main()