import matplotlib.pyplot as plt
import numpy as np

# Ensure Matplotlib backend is set appropriately
# For Jupyter notebooks, uncomment the following line if needed:
# %matplotlib inline
# For scripts, ensure you have a GUI backend or use a non-interactive backend like 'Agg' for saving plots

def find_payment(loan, monthly_rate, months):
    """Calculate the fixed monthly payment for a mortgage."""
    if monthly_rate == 0:  # Handle case with 0% interest
        return loan / months
    return loan * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

class Mortgage:
    """Base class for creating different types of mortgages"""

    def __init__(self, loan, annRate, months):
        """Initialize mortgage details."""
        self._loan = loan
        self._rate = annRate / 12.0
        self._months = months
        self._payment = find_payment(loan, self._rate, months)
        self._paid = [0.0]
        self._outstanding = [loan]
        self._total_paid = [0.0]
        self._legend = None

    def make_payment(self):
        """Simulate making a monthly payment."""
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1] * self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)
        self._total_paid.append(self._total_paid[-1] + self._payment)

    def get_total_paid(self):
        """Calculate the total amount paid so far."""
        return self._total_paid[-1]

    def __str__(self):
        """Return the description of the mortgage when printed."""
        return self._legend if self._legend else "Mortgage"

    def plot_payments(self, style, ax):
        """Plot the monthly payments over time on the given axis."""
        print(f"Plotting payments: {self._paid[1:]}")  # Debug
        ax.plot(self._paid[1:], style, label=self._legend)

    def plot_balance(self, style, ax):
        """Plot the remaining loan balance over time on the given axis."""
        print(f"Plotting balance: {self._outstanding}")  # Debug
        ax.plot(self._outstanding, style, label=self._legend)

    def plot_tot_pd(self, style, ax):
        """Plot the total payments made over time on the given axis."""
        print(f"Plotting total paid: {self._total_paid}")  # Debug
        ax.plot(self._total_paid, style, label=self._legend)

    def plot_net(self, style, ax):
        """Plot the net cost (total payments minus equity gained) on the given axis."""
        equity_acquired = np.array([self._loan] * len(self._outstanding)) - np.array(self._outstanding)
        net = np.array(self._total_paid) - equity_acquired
        print(f"Plotting net cost: {net}")  # Debug
        ax.plot(net, style, label=self._legend)

def plot_mortgages(morts, amt):
    """Helper function to create labeled plots for a list of mortgages."""
    # Create figures and axes explicitly
    fig_payments, ax_payments = plt.subplots(figsize=(8, 6))
    fig_cost, ax_cost = plt.subplots(figsize=(8, 6))
    fig_balance, ax_balance = plt.subplots(figsize=(8, 6))
    fig_net_cost, ax_net_cost = plt.subplots(figsize=(8, 6))

    # Define line styles for different mortgage types
    styles = ['k-', 'k--', 'k:']  # Solid, dashed, and dotted lines

    # Plot each mortgage on the respective axes
    for i in range(len(morts)):
        morts[i].plot_payments(styles[i], ax_payments)
        morts[i].plot_tot_pd(styles[i], ax_cost)
        morts[i].plot_balance(styles[i], ax_balance)
        morts[i].plot_net(styles[i], ax_net_cost)

    # Label each plot
    def label_plot(fig, ax, title, x_label, y_label):
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.legend(loc='best')
        ax.grid(True)
        fig.tight_layout()

    label_plot(fig_payments, ax_payments, f'Monthly Payments of ${amt:,}: Mortgages',
               'Months', 'Monthly Payments')
    label_plot(fig_cost, ax_cost, f'Cash Outlay of ${amt:,}: Mortgages',
               'Months', 'Total Payments')
    label_plot(fig_balance, ax_balance, f'Balance Remaining of ${amt:,}: Mortgages',
               'Months', 'Remaining Loan Balance')
    label_plot(fig_net_cost, ax_net_cost, f'Net Cost of ${amt:,}: Mortgages',
               'Months', 'Net Cost (Payments - Equity)')

    # Display all plots
    plt.show()

# Example usage
if __name__ == "__main__":
    # Create a sample mortgage
    mortgage1 = Mortgage(loan=200000, annRate=0.06, months=360)  # $200,000 loan, 6% annual rate, 30 years
    mortgage1._legend = "30-Year Fixed at 6%"

    # Simulate payments for 12 months
    print("Simulating 12 months of payments...")
    for _ in range(12):
        mortgage1.make_payment()

    # Print data for debugging
    print(f"Payments: {mortgage1._paid}")
    print(f"Outstanding: {mortgage1._outstanding}")
    print(f"Total Paid: {mortgage1._total_paid}")

    # Plot the mortgage
    print("Generating plots...")
    plot_mortgages([mortgage1], 200000)