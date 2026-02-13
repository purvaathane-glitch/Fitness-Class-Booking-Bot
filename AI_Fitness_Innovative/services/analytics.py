import matplotlib.pyplot as plt
import os

def generate_graph():
    attendance = [2,4,6,8,10,12,15]
    renewal_prob = [10,20,35,50,70,85,95]

    plt.figure()
    plt.plot(attendance, renewal_prob)
    plt.xlabel("Attendance")
    plt.ylabel("Renewal Probability (%)")
    plt.title("Retention Prediction Trend")

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/graph.png")
    plt.close()
