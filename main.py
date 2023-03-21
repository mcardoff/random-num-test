"""Generating 3 Random digits vs One num 0-999."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rand_dig():
    """Return a random digit."""
    return np.random.randint(0, 10)


def main():
    """Test whether the distributions data1 and data2 are the same."""
    # Numbers to generate
    N = 1000000
    # generate a single number 0-999
    data1 = np.random.randint(low=0, high=1000, size=N)
    data2 = np.array(
        100*rand_dig() + 10*rand_dig() + 1*rand_dig() for _ in range(N))

    df = pd.DataFrame({"single": data1, "separate": data2})
    plt.hist(df['single'])
    plt.hist(df['separate'])
    m1 = df['single'].mean()
    m2 = df['separate'].mean()
    s1 = df['single'].std()
    s2 = df['separate'].std()
    plt.text(500, 1000, f"m1={m1:.2f} s1={s1:.2f}\nm2={m2:.2f} s2={s2:.2f}")
    plt.show()


if __name__ == "__main__":
    main()
