from collections import deque

portion = [int(x) for x in input().split(', ')]
stamina = deque([int(x) for x in input().split(', ')])
peaks_deque = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])

concurred_peaks = []
days = 1

peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
}

while portion and stamina and peaks_deque and days < 8:
    power = portion[-1] + stamina[0]
    first_peak = peaks_deque[0]
    first_peak_level = peaks[first_peak]
    if power >= first_peak_level:
        concurred_peaks.append(peaks_deque.popleft())
    else:
        days += 1

    portion.pop()
    stamina.popleft()

if len(concurred_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if concurred_peaks:
    print(f"Conquered peaks:")
    print("\n".join([str(x) for x in concurred_peaks]))
